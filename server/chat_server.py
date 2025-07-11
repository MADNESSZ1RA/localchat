import socket
from threading import Thread

class ChatServer:
    def __init__(self, host: str, port: int):
        self.clients = []
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((host, port))
        self.sock.listen()

    def run(self):
        print("Сервер запущен. Ожидаем подключения...")
        while True:
            client_sock, addr = self.sock.accept()
            print(f"Подключился {addr}")
            self.clients.append(client_sock)
            Thread(target=self._handle_client, args=(client_sock,), daemon=True).start()

    def _handle_client(self, client_sock):
        while True:
            try:
                data = client_sock.recv(4096)
                if not data:
                    break
                self._broadcast(data, sender=client_sock)
            except:
                break
        self.clients.remove(client_sock)
        client_sock.close()

    def _broadcast(self, message, sender):
        for client in self.clients:
            if client != sender:
                client.sendall(message)
