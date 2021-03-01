from starlette.config import Config

APP_VERSION = "0.0.1"
APP_NAME = "learn"
API_PREFIX = "/api"

config = Config(".env")

IS_DEBUG: bool = config("IS_DEBUG", cast=bool, default=False)

"""
    TODO clean this up to make the Settings class the source of truth
"""


class Settings:
    @property
    def app_name(self):
        return "derive"

    @property
    def app_version(self):
        return "v0.1"

    @property
    def cockroachdb_url(self):
        return ""

    @property
    def execution_mode(self):
        return "development"
