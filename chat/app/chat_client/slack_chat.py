import asyncio
import logging
from random import randint

import aiohttp
from chat_client.chat_client import ChatClient
from config import settings
from fastapi import status
from message_event_router.slack_router import SlackRouter
from slack_sdk.errors import SlackApiError
from slack_sdk.web.async_client import AsyncWebClient
import concurrent.futures

log = logging.getLogger(__name__)


class SlackClient(ChatClient):
    @staticmethod
    def _get_web_client() -> AsyncWebClient:
        token = settings.slack_workspace_token
        return AsyncWebClient(token=token)

    @staticmethod
    def _init_message_event_listener():
        """
        Start async infinite loop to listen for the events accumulating in
        data-proxy. Data proxies are used since the Slack events api needs a fixed
        endpoint to POST events to.
        """
        data_proxy_url = settings.data_proxy_url
        auth = aiohttp.BasicAuth(
            login=settings.data_proxy_username,
            password=settings.data_proxy_password,
        )

        async def listener():

            async with aiohttp.ClientSession() as session:
                while True:
                    try:
                        response = await session.get(
                            data_proxy_url, auth=auth, timeout=60
                        )

                        if response.status == status.HTTP_200_OK:
                            payload = await response.json()

                            if (message_event := payload.get("event")) is None:
                                log.error(f"Unexpected data-proxy response: {payload}")
                            else:
                                # Ignore errors about not waiting for the result.
                                asyncio.create_task(SlackRouter.route_new_message(message_event))
                        elif response.status == status.HTTP_204_NO_CONTENT:
                            log.debug(
                                f"No pending slack events in data proxy at {data_proxy_url}. Sleeping..."
                            )
                            await asyncio.sleep(
                                randint(3, 8)
                            )  # multiple workers = high volume = Azure free tier rate limit.
                    except Exception:
                        log.exception(
                            f"Failed to get slack events from {data_proxy_url} with exception."
                        )

        asyncio.create_task(listener())
        log.info(f"Started slack event listener on data proxy {data_proxy_url}")

    @staticmethod
    def bootstrap():
        log.info("Starting slack client(s) bootstrap.")
        SlackClient._init_message_event_listener()

    @staticmethod
    async def send_message(destination: str, message: str, **kwargs) -> bool:
        try:
            response = await SlackClient._get_web_client().chat_postMessage(
                channel=destination,
                text=message,
            )
            assert response["message"]["text"] == message
            return True
        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert not e.response["ok"], "Unexpected response status."
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            log.error(f"Error when sending message: {e.response['error']}")
            return False
