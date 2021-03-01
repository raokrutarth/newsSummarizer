import logging
import sys
from os.path import abspath, isfile, dirname
from os import makedirs

from commands.commands import CommandsHelper

log = logging.getLogger()


class Build():
    '''
        TODO
        Class to build the docker images for CL using the build_any
        script
    '''
    # location to the build_any shell script. relative to the
    # cl-dev-tool/ directory
    BUILD_ANY_SCRIPT_PATH = abspath("../build_any_container.sh")

    # constants needed when building and transferring docker images
    TEMP_IMAGE_NAME_PREFIX = "quay.io/arubadevops/devcontainers"

    def __init__(self, command_helper: CommandsHelper):
        self.cmd_h = command_helper

    def _create_file_for_flag(self, items, file_path):
        '''
            Create a new file containing each item
            on a new line. Needed to pass multi-value
            flags to build_any script. Returns the filename.
        '''
        temp_file_path = abspath(file_path)
        makedirs(dirname(temp_file_path), exist_ok=True)

        with open(temp_file_path, "w+") as f:
            f.writelines([item + "\n" for item in items])
            log.debug("Successfully created build_any flag file %s with %d lines", temp_file_path, len(items))
            return temp_file_path

    def _build_image(self, pod_image, target_repo, in_container_path, updated_libs, py_deps, image_tag):
        '''
            Build image using script and return temp files that need to be cleaned up.
        '''
        assert isfile(self.BUILD_ANY_SCRIPT_PATH), "missing build script %s" % (self.BUILD_ANY_SCRIPT_PATH)

        log.info(
            "Build script building with base image %s, in-container path %s, libraries changed %s, with source code in %s to image %s:%s",
            pod_image,
            in_container_path,
            updated_libs,
            target_repo,
            self.TEMP_IMAGE_NAME_PREFIX,
            image_tag,
        )

        build_cmd = "time %s --base_image %s --app_docker_path %s --app_path %s --image_name %s --tag_name %s" % (
            self.BUILD_ANY_SCRIPT_PATH,
            pod_image,
            in_container_path,
            target_repo,
            self.TEMP_IMAGE_NAME_PREFIX,
            image_tag,
        )

        # identify any library changes and build the flag
        if updated_libs:
            file_with_lib_paths = self._create_file_for_flag(updated_libs, "./temp/build/internal-libs.txt")
            build_cmd += f" --libraries {file_with_lib_paths}"

        if py_deps:
            deps_temp_file = "cl-dev-tool-python-requirements.txt"
            deps_file_fullpath = f"{target_repo}/{deps_temp_file}"
            if not self._create_file_for_flag(py_deps, deps_file_fullpath):
                log.error("Unable to create deps flag file in location %s. Will not call build_any", deps_file_fullpath)
                sys.exit(1)
            # NOTE the path below has to be relative to the repo's path. Not absolute to avoid
            # issues with dockerfile "COPY" commands
            build_cmd += f" --deps {deps_temp_file}"

        build_cmd += " --copyall 1"  # HACK to avoid identifying base branch of repo

        reply = self.cmd_h.run_local_command(build_cmd, log_reply=True, allow_fail=True, directory=target_repo).lower()

        if "successfully built" not in reply or 'successfully tagged' not in reply:
            log.error("Build failed when using %s", self.BUILD_ANY_SCRIPT_PATH)

            if "not authorized" in reply:
                # docker pull of an image probably failed
                log.error("Unable to pull docker images during build. Verify docker login credentials are valid and docker pull works")
            sys.exit(1)

    def build_image(self, pod_image, target_repo, in_container_path, updated_libs, py_deps, image_tag):
        '''
            Use the build_any_container script described in
            https://confluence.arubanetworks.com/pages/viewpage.action?pageId=342892811
            to build the container.
        '''
        self._build_image(pod_image, target_repo, in_container_path, updated_libs, py_deps, image_tag)
        # TODO perform cleanup of temp files (files might be needed for debugging)
