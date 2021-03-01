import logging
import sys
from time import sleep
from secrets import token_hex
from collections import defaultdict
from pprint import pformat
from hashlib import blake2b
from os.path import abspath, expanduser, isfile, getsize, dirname
from os import makedirs
from kubernetes import \
    client as k8s_client, \
    config as k8s_config

from commands.commands import CommandsHelper
from replace.build_image import Build

log = logging.getLogger()

# restrict k8s library logging
logging.getLogger("kubernetes").setLevel(logging.WARNING)


class Replace():
    '''
        Replace Module builds the relevant images/artificats locally
        and replaces them in the CL instance.
    '''

    def __init__(self, command_helper: CommandsHelper, config: dict):
        self.cmd_h = command_helper
        self.config = config
        self.remote_host = config["instance"]["hostname"]

        # k8s config
        # TODO get the kubeconfig from the CL instance directly
        self._kubeconfig_path = config["instance"].get("kubeconfig_path", "")
        if self._kubeconfig_path:
            self._kubeconfig_path = abspath(expanduser(self._kubeconfig_path))
        else:
            self._kubeconfig_path = self._get_kubeconfg_file()

        log.info("Initializing k8s client to cluster specified in %s kubeconfig", self._kubeconfig_path)
        k8s_config.load_kube_config(config_file=self._kubeconfig_path)

        for _ in range(5):
            try:
                self.k8s = k8s_client.CoreV1Api()
                break
            except Exception:
                sleep(0.5)

        # dict of namespace -> set(<pod names>) that stores the
        # pods to be deleted. Optimization allows faster execution since
        # kubectl delete is slow and should be run less frequently.
        self._pods_to_delete = defaultdict(set)

    def _get_kubeconfg_file(self, remote_kc_path="~/.kube/config"):
        '''
            Obtain the kubeconfig file for the k8s cluster in the CL
            instance if the file is not already present.
        '''
        hashed_hostname = blake2b(self.remote_host.encode("utf-8"), digest_size=8).hexdigest()
        kubeconfig_file = abspath(f"./temp/k8s/kubeconfig.{hashed_hostname}.yml")
        if isfile(kubeconfig_file) and getsize(kubeconfig_file) > 0:
            # a non-empty kubeconfig file for the host already exists. reuse existing file
            log.info("kubeconfig file for host %s found in %s. Re-using file.", self.remote_host, kubeconfig_file)
            return kubeconfig_file

        makedirs(dirname(kubeconfig_file), exist_ok=True)
        with open(kubeconfig_file, "w+") as f:
            config = self.cmd_h.run_remote_command(f"cat {remote_kc_path}")
            if not config:
                log.error("Unable to fetch remote kubeconfig from %s on %s. Exiting...", remote_kc_path, self.remote_host)
                sys.exit(1)

            f.write(config.strip())
            log.debug("Sucessfully obtained remote kubeconfig file %s and stored locally in %s", remote_kc_path, kubeconfig_file)
            return kubeconfig_file

    def _get_pod_details(self, pod_name_substring, namespace):
        '''
            Returns the list of pods that contain the substring
            in the name.
        '''
        try:
            log.debug("Fetching pod list for cluster using a k8s client that uses kubeconfig %s", self._kubeconfig_path)
            ret = self.k8s.list_pod_for_all_namespaces(watch=False, timeout_seconds=5)
        except Exception:
            log.exception("Unable to obtain k8s pod list. Verify kubeconfig %s is correct", self._kubeconfig_path)
            sys.exit(1)

        pods = []
        assert isinstance(ret.items, list), "Unknown payload received from k8s cluster for pod details"
        for pod_i in ret.items:
            pod_name = pod_i.metadata.name
            pod_namespace = pod_i.metadata.namespace

            if pod_name_substring in pod_name:
                if namespace and namespace != pod_namespace:
                    log.debug("Skipping pod %s in namespace %s because it is not in namespace %s",
                              pod_name, pod_namespace, namespace)
                    continue
                pods.append(pod_i)

        if len(pods) > 1:
            log.warning("Detected multiple pods with %s in pod.metadata.name", pod_name_substring)
            existing_pod_names = [p.metadata.name for p in pods]
            log.warning("Selected %d pods:\n%s", len(existing_pod_names), pformat(existing_pod_names))

        return pods

    def _reset_pod_to_original(self, pod_name, pod_image, namespace):
        '''
            Set the pod/image to the version the CL instance was started
            with. i.e. remove all custom/private code changes.

            :param string pod_image: quay.io image of the original container image used in CL
        '''
        log.info("Resetting pod %s to use original image %s in namespace %s", pod_name, pod_image, namespace)
        self._pull_image_into_cl(pod_image)
        self._replace_image(pod_image, pod_image)
        self._schedule_pod_for_deletion(pod_name, namespace)

    def _pull_image_into_cl(self, image):
        local_cmds = [
            f"docker push {image}",
        ]
        cmds = ' && '.join(local_cmds)
        self.cmd_h.run_local_command(cmds, log_reply=True)

        remote_cmds = [
            # TODO verify there is no overwrite
            f"docker pull {image}",
        ]
        cmds = ' && '.join(remote_cmds)
        self.cmd_h.run_remote_command(cmds, log_reply=True)

    def _replace_image(self, temp_image, target_image):
        '''
            tag a newly added image as target_image in the CL docker.
            Effectively replacing the original target_image image.
        '''
        cmd = 'docker tag %s %s' % (temp_image, target_image)
        self.cmd_h.run_remote_command(cmd, log_reply=True)
        log.info("Tagged image %s as %s", temp_image, target_image)

    def _schedule_pod_for_deletion(self, pod_name, namespace):
        '''
            Add pod to a collection that is used to batch delete
            pods at the end of the replacement process to reduce
            the number of time kubectl delete is called
        '''
        log.debug(f"Pod {pod_name} in namespace {namespace} scheduled for deletion")
        self._pods_to_delete[namespace].add(pod_name)

    def _replace_pod(self, target_repo, in_container_path, pod_name,
                     pod_image, namespace, updated_libs, py_deps, image_tag, custom_build_cmd):
        '''
            Replace the image used by the pod pod_name with an
            image built from the target_repo directory.

            All build commands will be run in the context of the target_repo directory.

            TODO
            - support custom_build_cmd
        '''
        if not target_repo:
            log.error("Path to target repositiry soruce code not passed")
            sys.exit(1)
        elif not in_container_path:
            log.error("In-container path to source code not passed. May be available in a circus .conf file")
            sys.exit(1)

        log.info("Replacing pod %s with source code located in %s",
                 pod_name, target_repo)
        if custom_build_cmd:
            log.error("custom_build_cmd flag not yet supported")
            sys.exit(1)

        temp_image = f"{Build.TEMP_IMAGE_NAME_PREFIX}:{image_tag}"

        Build(self.cmd_h).build_image(pod_image, target_repo, in_container_path, updated_libs, py_deps, image_tag)
        self._pull_image_into_cl(temp_image)
        self._replace_image(temp_image, pod_image)
        self._schedule_pod_for_deletion(pod_name, namespace)  # assume pod will start with new image

    def _batch_delete_enqueued_pods(self):
        '''
            Delete all the pods that were scheduled to be deleted during the
            prior replacement process steps
        '''
        for namespace, pods in self._pods_to_delete.items():
            if pods:
                pods = ' '.join(list(pods))
                # cmd = "kubectl -n %s delete pod %s --grace-period=0 --force" % (namespace, pod_name)  # HACK force del
                cmd = "kubectl -n %s delete pod %s" % (namespace, pods)
                timeout = 120
                try:
                    self.cmd_h.run_remote_command(cmd, log_reply=True, timeout=timeout)
                    log.info("Deleted pod(s) %s in namespace %s", pods, namespace)
                except Exception:
                    log.error("Unable to delete pod %s because the kubectl delete took over %d sec(s) to finish. "
                              "Verify %s isn't running too slow.", pods, timeout, self.remote_host, exc_info=True)

    def replace_pods(self):
        try:
            replacements = self.config["replacements"]["pods"]
            if not replacements:
                log.warning("config.replacements is empty")
                return
            log.info("Found %d pod replacements from config.replacements", len(replacements))
        except KeyError:
            log.warning("config.replacements missing in config file")
            return

        default_image_tag = "cl-dev-tools-replacer-temp-" + token_hex(8)  # random string suffix

        for _, rep_info in replacements.items():

            # required fields
            target_pod = rep_info["target_pod"]

            # optional fields
            target_namespace = rep_info.get("target_namespace", None)
            should_reset = rep_info.get("should_reset", False)
            should_restart = rep_info.get("should_restart", False)
            libraries = rep_info.get("library_changes", [])
            py_deps = rep_info.get("py_libs", [])
            custom_build_cmd = rep_info.get("custom_build_command", None)
            target_repo = rep_info.get("repo_path", None)
            in_container_path = rep_info.get("in_container_path", None)
            image_tag = rep_info.get("image_tag", default_image_tag)

            matched_pods = self._get_pod_details(target_pod, target_namespace)

            # [OPTIMISATION] if a pod was using the same image as another pod and the replacement was set to replace the image,
            # the image is already replaced in the CL so just restart the pod instead of building, pushing, pulling and
            # tagging the image again
            replaced_images = set()

            for pod_i in matched_pods:
                pod_image = pod_i.spec.containers[0].image   # assumes there is exactly one container in k8s pod spec
                pod_name = pod_i.metadata.name
                namespace = pod_i.metadata.namespace

                if should_reset:
                    # revert pods to original CL version
                    self._reset_pod_to_original(pod_name, pod_image, namespace)
                elif should_restart:
                    self._schedule_pod_for_deletion(pod_name, namespace)
                elif pod_image in replaced_images:
                    # image is already replaced, restarting the pod will apply the changes
                    log.info("Skipping building an image for pod %s. Image(s) %s already replaced. Restarting pod.",
                             pod_name, replaced_images)
                    self._schedule_pod_for_deletion(pod_name, namespace)
                else:
                    # deploy private changes to CL
                    self._replace_pod(
                        target_repo,
                        in_container_path,
                        pod_name,
                        pod_image,
                        namespace,
                        libraries,
                        py_deps,
                        image_tag,
                        custom_build_cmd
                    )
                    replaced_images.add(pod_image)

        self._batch_delete_enqueued_pods()
