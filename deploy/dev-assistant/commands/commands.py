import logging
from os import getcwd
import sys

from .remote import RemoteSession
from .local import run_local_cmd

log = logging.getLogger()


class CommandsHelper():

    def __init__(self, config):
        instance = config["instance"]

        self.remote_host = instance["hostname"]
        self.remote_ssh_port = instance["ssh_port"]

        password = instance.get("password", None)
        ssh_key_path = instance.get("local_ssh_key_path", None)

        if not password and not ssh_key_path:
            log.critical("No password or SSH key passed in central lite instance configuration. Exiting.")
            sys.exit(1)

        if password:
            ssh_key_path = None

        self.remote_sesh = RemoteSession(
            hostname=self.remote_host,
            username=instance["username"],
            password=password,
            ssh_port=instance["ssh_port"],
            ssh_key_path=ssh_key_path,
        )

    def run_remote_command(self, cmd: str, log_reply=False, timeout=30) -> str:
        log.info('Running remote command %s on instance %s', cmd, self.remote_host)

        reply = self.remote_sesh.send_bash_cmd(cmd, timeout)
        if log_reply:
            log.info("\nReply:\n%s\n", reply)

        return reply

    def run_local_command(self, cmd: str, log_reply=False, directory=None, allow_fail=True) -> str:
        '''
            Runs the shell command cmd. If a full folder path is passed
            as directory, the commands are executed in that folder.

            directory (string): full path to working directory for the command.
            allow_fail (bool): exits program if stderr is not empty.
        '''
        if not directory:
            directory = getcwd()

        log.info('Running local command %s in directory %s', cmd, directory)

        stdout, stderr = run_local_cmd(cmd, directory)
        full_reply = stdout + "\n" + stderr
        if stderr:
            if not allow_fail:
                log.error("%s failed with result\n%s", cmd, full_reply)
                exit(-1)
            log.warning('Local command STDERR: \n%s' % (stderr))

        if log_reply:
            log.info("\nReply:\n%s", full_reply)

        return full_reply

    def clean_up_sessions(self):
        log.debug("Terminating remote terminal session")
        self.remote_sesh.terminate_sessions()
