import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

log = logging.getLogger()


class Runner():

    '''
        Runner runs commands or pre-defined actions on the CL
    '''

    def __init__(self, command_helper, config):
        self.cmd_h = command_helper
        self.to_run = config.get('post_replace', {})

        if not self.to_run:
            log.info("No post-replace configuration found")

    def execute_commands(self):
        commands = self.to_run.get("commands", [])

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = set()

            for command_info in commands:
                cmd = command_info["command"]
                mode = command_info["mode"].lower().strip()
                delay = command_info.get("delay", 0)
                log.debug("Waiting %d seconds before executing %s command %s", delay, mode, cmd)

                if mode == 'local':
                    futures.add(
                        executor.submit(self._execute_local_command, cmd, delay)
                    )
                elif mode == 'remote':
                    futures.add(
                        executor.submit(self._execute_remote_command, cmd, delay)
                    )
                else:
                    log.error("Unknown command mode '%s' for command %s", mode, cmd)

            for _ in as_completed(futures):
                # HACK to wait for commands to finish
                pass

    def _execute_local_command(self, command, delay):
        sleep(delay)
        response = self.cmd_h.run_local_command(
            command,
            directory=None,
            allow_fail=True
        )
        log.info(f"\nLocal Command: {command}\nReply: \n{response}")

    def _execute_remote_command(self, command, delay):
        sleep(delay)
        response = self.cmd_h.run_remote_command(command)
        log.info(f"\nRemote Command: {command}\nReply: \n{response}")
