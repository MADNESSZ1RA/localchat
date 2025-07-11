import socket
from threading import Thread
from server.interfaces import IChatServer

class ConsoleChatServer:
    def __init__(self, host: str, port: int):
        self.clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen()
    def run(self) -> None:
        print("Console chat server started")
        while True:
            client_sock, _ = self.sock.accept()
            self.clients.append(client_sock)
            Thread(target=self._handle_client, args=(client_sock,), daemon=True).start()
    def _handle_client(self, client_sock):
        while True:
            try:
                data = client_sock.recv(4096)
                if not data:
                    break
                self._broadcast(data, client_sock)
            except:
                break
        self.clients.remove(client_sock)
        client_sock.close()
    def _broadcast(self, message, sender):
        for c in self.clients:
            if c != sender:
                c.sendall(message)
