import logging
import sys
from os import environ
from os.path import abspath, exists, isfile

from yaml import YAMLError, safe_load

log = logging.getLogger()
"""
    Application configurations and secrets.
"""


class Settings:
    def __init__(self, secrets_file_path: str):
        secrets = Settings._get_secrets(secrets_file_path)
        dynamic_config = Settings._get_dynamic_config()

        self.config = dict()
        self.config.update(secrets)
        self.config.update(dynamic_config)

    @property
    def slack_workspace_token(self) -> str:
        return self.config["slack"]["workspace_oauth_access_token"]

    @property
    def slack_bot_user_token(self) -> str:
        return self.config["slack"]["bot_user_oauth_access_token"]

    @property
    def data_proxy_url(self) -> str:
        return self.config["data-proxy"]["url"]

    @property
    def data_proxy_username(self) -> str:
        return self.config["data-proxy"]["username"]

    @property
    def data_proxy_password(self) -> str:
        return self.config["data-proxy"]["password"]

    @staticmethod
    def _invalid_config_exit(message: str):
        log.error(
            "Unable to start due to error %s while parsing secretsuration file. Exiting...",
            message,
        )
        sys.exit(1)

    @staticmethod
    def _get_dynamic_config() -> dict:
        """
        returns non-secret secretsuration that depends on runtime.
        """
        config = dict()
        # Adopt the more secure mode by default.
        config["runtime_mode"] = environ.get("RUNTIME_MODE", "production")

        if config["runtime_mode"] == "production":
            config["learn-url"] = "http://learn:5000"
            config["scrape-url"] = "http://scrape:5000"

        return config

    @staticmethod
    def _get_secrets(secrets_file_path: str) -> dict:  # type: ignore

        secrets_file_path = abspath(secrets_file_path)
        if not exists(secrets_file_path) or not isfile(secrets_file_path):
            Settings._invalid_config_exit(
                "Missing secrets file %s" % (secrets_file_path)
            )

        try:
            with open(secrets_file_path, "r") as f:
                secrets = safe_load(f)
                log.info(
                    f"secrets read from file {secrets_file_path} with secrets: {secrets.keys()}"
                )
                return secrets

        except YAMLError as err:
            Settings._invalid_config_exit(
                f"Got exception when reading invalid YAML in {secrets_file_path} {err}"
            )
        except Exception as e:
            Settings._invalid_config_exit(
                f"Unknown error {e} reading secrets file {secrets_file_path}"
            )


settings = Settings("./secrets.yaml")
