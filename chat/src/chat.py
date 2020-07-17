from yaml import safe_load
from slack import WebClient, RTMClient
from os.path import abspath
from time import sleep
from random import choice
from threading import Thread
from mock_db import get_state, set_state, get_id, set_id
from pprint import pprint

config = safe_load(open(abspath("./config.yaml"), 'r'))
token = config["chat"]["token"]

client = RTMClient(token=token)
web_client = WebClient(token, timeout=30)


def initiator():
    while True:
        if get_state() == 'init' or get_state() == 'complete':
            print("Invoking initiator")

            r = web_client.api_call('chat.postMessage', json={
                'channel': 'news',
                'text': 'Do you like {}'.format(choice(['color', 'liquid', 'rock', 'school'])),
                }
            )
            set_id(r['message']['bot_id'])
            set_state('asked')
        sleep(3)

def do_thread(payload):
    channel_id = payload['data']['channel']
    message = payload['data']['message']

    if get_id() in message['reply_users']:
        return

    wc = payload['web_client']
    thread_ts = message['ts']
    wc.chat_postMessage(
        text="Tread replies not supported. Use main channel message board",
        thread_ts=thread_ts,
        channel=channel_id,
    )

@RTMClient.run_on(event='message')
def record_reply(**payload):
    print('[+] Event=message, payload=')
    pprint(payload)
    print('[+] State:', get_state(), '\n')


    if 'subtype' in payload['data'] and payload['data']['subtype'] == 'message_replied':
        do_thread(payload)
        return

    data = payload['data']
    if 'bot_id' in data:
        if data['bot_id'] == get_id():
            return

    if 'thread_ts' not in payload['data'] and get_state() == 'asked':
        channel_id = data['channel']

        webclient = payload['web_client']
        webclient.chat_postMessage(
            channel=channel_id,
            text="you said: {}. saving answer to database".format(data['text'])
            # text="Hi <@{}>!".format(user),
            # thread_ts=thread_ts
        )
        set_state('complete')

def main():
    # daemon mode to terminate with main program
    Thread(target=initiator, daemon=True).start()
    client.start()



if __name__ == "__main__":
    main()