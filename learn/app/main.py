import logging
import os

from api.routes.router import api_router
from core.config import API_PREFIX
from core.config import APP_NAME
from core.config import APP_VERSION
from core.config import IS_DEBUG
from core.event_handlers import start_app_handler
from core.event_handlers import stop_app_handler
from fastapi import FastAPI

# configure logging with filename, function name and line numbers
logging.basicConfig(
    level=os.environ.get("LOGLEVEL", "DEBUG"),
    datefmt='%I:%M:%S %p %Z',
    format='%(levelname)s [%(asctime)s - %(filename)s:%(lineno)s::%(funcName)s]\t%(message)s',
)


def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION, debug=IS_DEBUG)
    fast_app.include_router(api_router, prefix=API_PREFIX)

    fast_app.add_event_handler("startup", start_app_handler(fast_app))
    fast_app.add_event_handler("shutdown", stop_app_handler(fast_app))

    return fast_app


app = get_app()
