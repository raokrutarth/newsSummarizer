import logging
import os

from config.tool_config_parser import ConfigParser
from commands.commands import CommandsHelper
from replace.replace import Replace
from runner.runner import Runner

# configure logging with filename, function name and line numbers
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "DEBUG"),
    datefmt='%I:%M:%S %p %Z',
    format='%(levelname)s [%(asctime)s - %(filename)s:%(lineno)s::%(funcName)s]\t%(message)s',
)
log = logging.getLogger()


def main():
    log.info("Central Lite Developer Utility")
    config = ConfigParser.get_config("./config.yml")
    command_helper = CommandsHelper(config)
    replacer = Replace(command_helper, config)
    runner = Runner(command_helper, config)

    replacer.replace_pods()
    runner.execute_commands()

    # DO NOT TOUCH
    command_helper.clean_up_sessions()

    log.info("Finished")


if __name__ == "__main__":
    main()
