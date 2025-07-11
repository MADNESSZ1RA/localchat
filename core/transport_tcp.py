import socket


class TCPTransport:
    def __init__(self, host: str, port: int):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

    def send(self, data: str) -> None:
        self.sock.sendall(data.encode())

    def receive(self) -> str:
        return self.sock.recv(4096).decode()
