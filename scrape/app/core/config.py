import logging

from dynaconf import settings as dyna_settings

log = logging.getLogger(__name__)

# https://www.dynaconf.com/
settings = Dynaconf(
    envvar_prefix="SCRAPECONF",  # export envvars with `export DYNACONF_FOO=bar` and access with settings.FOO.
    settings_files=["settings.yaml", "secrets.yaml"],  # Load files in the given order.
)

if settings.RUNTIME_MODE == "development":
    settings.se
