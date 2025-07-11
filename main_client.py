from core.transport_tcp import TCPTransport
from core.handler import ChatMessageHandler
from core.client import ChatClient
from db.database import Base, engine
from db.user_service import UserService

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    service = UserService()

    print("1. Регистрация\n2. Вход")
    choice = input("Выбор: ").strip()
    username = input("Имя: ").strip()
    password = input("Пароль: ").strip()

    if choice == "1":
        if service.register(username, password):
            print("Регистрация успешна.")
        else:
            print("Пользователь уже существует.")
            exit()
    elif choice == "2":
        if not service.login(username, password):
            print("Неверные данные.")
            exit()
    else:
        print("Ошибка ввода.")
        exit()

    transport = TCPTransport("127.0.0.1", 5555)
    handler = ChatMessageHandler()
    client = ChatClient(transport, handler, username)
    client.start()
