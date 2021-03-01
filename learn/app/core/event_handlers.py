import logging
from typing import Callable

from fastapi import FastAPI

log = logging.getLogger(__name__)


def _startup_models(app: FastAPI) -> None:
    log.info("Starting model initialization at app startup")


def _shutdown_models(app: FastAPI) -> None:
    app.state.model = None


def start_app_handler(app: FastAPI) -> Callable:
    def startup() -> None:
        log.info("Running app start handler.")
        _startup_models(app)

    return startup


def stop_app_handler(app: FastAPI) -> Callable:
    def shutdown() -> None:
        log.info("Running app shutdown handler.")
        _shutdown_models(app)

    return shutdown
