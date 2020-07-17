from threading import Lock

STATE_LOCK = Lock()
STATE = "init"

ID_LOCK = Lock()
BOT_ID = 'BLU4X4KL5'

STATE_INIT = 'init'
STATE_SHARED = 'shared'
STATE_COMPLETE = 'complete'

def get_state() -> str:
    with STATE_LOCK:
        return STATE

def set_state(new_state: str):
    with STATE_LOCK:
        global STATE
        STATE = new_state


def get_id() -> str:
    with ID_LOCK:
        return BOT_ID

def set_id(new_id: str):
    with ID_LOCK:
        global BOT_ID
        BOT_ID = new_id