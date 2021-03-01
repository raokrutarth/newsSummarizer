from abc import ABCMeta, abstractstaticmethod


class ChatClient(metaclass=ABCMeta):
    """
    Abstract class the determins the interface chat clients
    need to follow.
    """

    @abstractstaticmethod
    def bootstrap(self):
        pass

    @abstractstaticmethod
    def send_message(self, destination: str, message: str, **kwargs) -> bool:
        pass
