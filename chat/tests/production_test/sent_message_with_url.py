message_event_with_link = {
    "token": "",
    "team_id": "TLU46BXNC",
    "api_app_id": "ALGMSQCF4",
    "event": {
        "client_msg_id": "fecbcf9d-3fa7-4828-9e86-94c23649eb1a",
        "type": "message",
        "text": "<https://www.bbc.com/sport/horse-racing/54695641>",
        "user": "ULW8RBLKY",
        "ts": "1605097921.004500",
        "team": "TLU46BXNC",
        "blocks": [
            {
                "type": "rich_text",
                "block_id": "PV1",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "link",
                                "url": "https://www.bbc.com/sport/horse-racing/54695641",
                                "text": "https://www.bbc.com/sport/horse-racing/54695641",
                            }
                        ],
                    }
                ],
            }
        ],
        "channel": "#test",
        "event_ts": "1605097921.004500",
        "channel_type": "channel",
    },
    "type": "event_callback",
    "event_id": "Ev01EHF02Y1Z",
    "event_time": 1605097921,
    "authorizations": [
        {
            "enterprise_id": None,
            "team_id": "TLU46BXNC",
            "user_id": "ULTL1UF5J",
            "is_bot": True,
            "is_enterprise_install": False,
        }
    ],
    "is_ext_shared_channel": False,
    "event_context": "1-message-TLU46BXNC-CLW8RBNLE",
}

multi_link_link_event = {
    "token": "",
    "team_id": "TLU46BXNC",
    "api_app_id": "ALGMSQCF4",
    "event": {
        "client_msg_id": "a4bf50b2-0214-44c8-acff-a4c74c6e8a9f",
        "type": "message",
        "text": "<https://www.nationalgeographic.com/>\n<https://www.nytimes.com/section/todayspaper>",
        "user": "ULW8RBLKY",
        "ts": "1605255956.001600",
        "team": "TLU46BXNC",
        "blocks": [
            {
                "type": "rich_text",
                "block_id": "4t1",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "link",
                                "url": "https://www.nationalgeographic.com/",
                            },
                            {"type": "text", "text": "\n"},
                            {
                                "type": "link",
                                "url": "https://www.nytimes.com/section/todayspaper",
                            },
                        ],
                    }
                ],
            }
        ],
        "channel": "C01FCNRATPA",
        "event_ts": "1605255956.001600",
        "channel_type": "channel",
    },
    "type": "event_callback",
    "event_id": "Ev01EP717RT5",
    "event_time": 1605255956,
    "authorizations": [
        {
            "enterprise_id": None,
            "team_id": "TLU46BXNC",
            "user_id": "ULTL1UF5J",
            "is_bot": True,
            "is_enterprise_install": False,
        }
    ],
    "is_ext_shared_channel": False,
    "event_context": "1-message-TLU46BXNC-C01FCNRATPA",
}

multi_link_event_change_notification = {
    "token": "",
    "team_id": "TLU46BXNC",
    "api_app_id": "ALGMSQCF4",
    "event": {
        "type": "message",
        "subtype": "message_changed",
        "hidden": True,
        "message": {
            "client_msg_id": "a4bf50b2-0214-44c8-acff-a4c74c6e8a9f",
            "type": "message",
            "text": "<https://www.nationalgeographic.com/>\n<https://www.nytimes.com/section/todayspaper>",
            "user": "ULW8RBLKY",
            "team": "TLU46BXNC",
            "attachments": [
                {
                    "service_name": "National Geographic",
                    "title": "National Geographic: Stories of Animals, Nature, and Culture",
                    "title_link": "https://www.nationalgeographic.com/",
                    "text": "Explore National Geographic. A world leader in geography, cartography and exploration.",
                    "fallback": "National Geographic: National Geographic: Stories of Animals, Nature, and Culture",
                    "thumb_url": "https://www.nationalgeographic.com/content/dam/ngdotcom/rights-exempt/homepage/nationalgeographicog.ngsversion.1530540626597.adapt.1900.1.jpg",
                    "from_url": "https://www.nationalgeographic.com/",
                    "thumb_width": 1900,
                    "thumb_height": 1266,
                    "service_icon": "https://www.nationalgeographic.com/etc.clientlibs/ui/clientlibs/resources/platform/refresh/images/apple-touch-icon.ngsversion.20201008121756.png",
                    "id": 1,
                    "original_url": "https://www.nationalgeographic.com/",
                }
            ],
            "blocks": [
                {
                    "type": "rich_text",
                    "block_id": "4t1",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "link",
                                    "url": "https://www.nationalgeographic.com/",
                                },
                                {"type": "text", "text": "\n"},
                                {
                                    "type": "link",
                                    "url": "https://www.nytimes.com/section/todayspaper",
                                },
                            ],
                        }
                    ],
                }
            ],
            "ts": "1605255956.001600",
        },
        "channel": "C01FCNRATPA",
        "previous_message": {
            "client_msg_id": "a4bf50b2-0214-44c8-acff-a4c74c6e8a9f",
            "type": "message",
            "text": "<https://www.nationalgeographic.com/>\n<https://www.nytimes.com/section/todayspaper>",
            "user": "ULW8RBLKY",
            "ts": "1605255956.001600",
            "team": "TLU46BXNC",
            "blocks": [
                {
                    "type": "rich_text",
                    "block_id": "4t1",
                    "elements": [
                        {
                            "type": "rich_text_section",
                            "elements": [
                                {
                                    "type": "link",
                                    "url": "https://www.nationalgeographic.com/",
                                },
                                {"type": "text", "text": "\n"},
                                {
                                    "type": "link",
                                    "url": "https://www.nytimes.com/section/todayspaper",
                                },
                            ],
                        }
                    ],
                }
            ],
        },
        "event_ts": "1605255957.001700",
        "ts": "1605255957.001700",
        "channel_type": "channel",
    },
    "type": "event_callback",
    "event_id": "Ev01FCRR0B8Q",
    "event_time": 1605255957,
    "authorizations": [
        {
            "enterprise_id": None,
            "team_id": "TLU46BXNC",
            "user_id": "ULTL1UF5J",
            "is_bot": True,
            "is_enterprise_install": False,
        }
    ],
    "is_ext_shared_channel": False,
    "event_context": "1-message-TLU46BXNC-C01FCNRATPA",
}

single_url_message = {
    "token": "",
    "team_id": "TLU46BXNC",
    "api_app_id": "ALGMSQCF4",
    "event": {
        "client_msg_id": "1597b9f4-b758-4a9c-ab40-a1edb2b09121",
        "type": "message",
        "text": "<https://pypi.org/project/schedule/>",
        "user": "ULW8RBLKY",
        "ts": "1605259391.001600",
        "team": "TLU46BXNC",
        "blocks": [
            {
                "type": "rich_text",
                "block_id": "rj2T",
                "elements": [
                    {
                        "type": "rich_text_section",
                        "elements": [
                            {
                                "type": "link",
                                "url": "https://pypi.org/project/schedule/",
                            }
                        ],
                    }
                ],
            }
        ],
        "channel": "DLGN96J3D",
        "event_ts": "1605259391.001600",
        "channel_type": "im",
    },
    "type": "event_callback",
    "event_id": "Ev01EV9B4C68",
    "event_time": 1605259391,
    "authorizations": [
        {
            "enterprise_id": None,
            "team_id": "TLU46BXNC",
            "user_id": "ULTL1UF5J",
            "is_bot": True,
            "is_enterprise_install": False,
        }
    ],
    "is_ext_shared_channel": False,
    "event_context": "1-message-TLU46BXNC-DLGN96J3D",
}

import requests
from yaml import safe_load

url = "https://data-proxy-1.azurewebsites.net/slack_poxy/event"
headers = {"Content-Type": "application/json"}

with open("./secrets.yaml", "r") as f:
    secrets = safe_load(f)
    message_event_with_link["token"] = secrets["slack"]["verification_token"]
response = requests.request("POST", url, headers=headers, json=message_event_with_link)
print(response.text)
