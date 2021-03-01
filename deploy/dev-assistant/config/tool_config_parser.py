import logging
from os.path import abspath, isfile, exists
from yaml import safe_load, YAMLError
from json import dumps
import sys

log = logging.getLogger()
'''
    configuration used by tool to identify CL instance, pods to replace,
    location of source code, etc.
'''


class ConfigParser:

    @staticmethod
    def get_config(config_file_path: str):

        config_file_path = abspath(config_file_path)
        if not exists(config_file_path) or not isfile(config_file_path):
            ConfigParser._invalid_config_exit("Missing configuration file %s" % (config_file_path))

        try:
            with open(config_file_path, 'r') as f:
                config = safe_load(f)
                config_pretty = dumps(config, indent=4)
                log.info("Configuration read from file %s: \n%s", config_file_path, config_pretty)
                ConfigParser._validate_config(config)
                log.info("Successfully read configuration file")
                return config

        except YAMLError as err:
            log.error("Invalid YAML in config file with error %s", err)
        except Exception as e:
            ConfigParser._invalid_config_exit("Unknown error %s reading configuration file %s" % (e, config_file_path))
        return None

    @staticmethod
    def _validate_config(config):
        '''
            TODO
            warn about missing information in config
        '''
        pass

    @staticmethod
    def _invalid_config_exit(message: str):
        log.error('Unable to start due to error %s while parsing configuration file. '
                  'See benchmark_config_template.yaml for an example configuration.\nExiting...', message)
        sys.exit(1)
