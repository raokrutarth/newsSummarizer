import logging
import sys
from typing import List

from chat_client.slack_chat import SlackClient
from fastapi import FastAPI, HTTPException, Path

# from fastapi.logger import logger as log
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Extra, Field, validator

app = FastAPI()

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
    SlackClient.bootstrap()


@app.on_event("shutdown")
def shutdown_event():
    log.warning("chat shutting down.")


class IMMessage(BaseModel):
    class Config:
        extra = Extra.forbid

    content: str = Field(
        ...,
        title="Message content",
    )
    via: str = Field(
        ...,
        title="Messaging platform",
    )

    @validator("via")
    def via_is_valid(cls, value):
        valid_platforms: List[str] = ["slack"]
        assert value in valid_platforms, f"via has to be one of {valid_platforms}"
        return value


@app.post("/send_message/{user_id}", description="Send a message to a user")
async def send_message(
    im_message: IMMessage,
    user_id: str = Path(..., title="User ID", description="Project N user id"),
):
    log.info(f"Sending message {im_message} to {user_id}")

    if im_message.via == "slack":
        user_preffered_channel = "#general"  # TODO fix to get from DB
        await SlackClient.send_message(
            destination=user_preffered_channel,
            message=im_message.content,
        )
        return JSONResponse(
            status_code=200,
            content=dict(
                status="sent",
            ),
        )
    else:
        raise HTTPException(status_code=401, detail="Invalid request to send message.")
