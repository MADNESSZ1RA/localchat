from threading import Thread
from core.interfaces import IMessageTransport, IMessageHandler

class ChatClient:
    def __init__(self, transport: IMessageTransport, handler: IMessageHandler, username: str):
        self.transport = transport
        self.handler = handler
        self.username = username

    def start(self) -> None:
        Thread(target=self._receive_loop, daemon=True).start()
        self.transport.send(f"{self.username} вошёл в чат.")

        while True:
            msg = input("> ")
            self.transport.send(f"{self.username}: {msg}")

    def _receive_loop(self) -> None:
        while True:
            msg = self.transport.receive()
            self.handler.handle(msg)
