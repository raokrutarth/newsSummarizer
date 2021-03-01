import logging
import sys

from api.router import api_router
from api import heartbeat

# from fastapi.logger import logger as log
from core.config import settings
from fastapi import FastAPI

app = FastAPI(title="News Project Scrape")

# configure logging with filename, function name and line numbers
logging.basicConfig(
    datefmt="%I:%M:%S %p %Z",
    format="%(levelname)s [%(asctime)s - %(filename)s:%(lineno)s::%(funcName)s]\t%(message)s",
    stream=sys.stdout,
    level=logging.INFO,
)
log = logging.getLogger(__name__)


@app.on_event("startup")
async def app_bootstrap():
    log.info("Scrape bootstrap handler running.")
    log.info(settings.RUNTIME_MODE)


@app.on_event("shutdown")
def shutdown_event():
    log.warning("Scrape shutdown handler running.")


# add the router from the implemented endpoints
app.include_router(
    router=api_router,
    prefix="/api",
)

app.include_router(
    heartbeat.router,
    tags=["health"],
    prefix="/health",
)


@app.get(path="/")
async def home_page():
    return "Project N Scrape Home Page"
