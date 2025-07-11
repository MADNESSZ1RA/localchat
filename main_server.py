import argparse
from server.console_server import ConsoleChatServer
from server.web_server import WebChatServer

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--web", action="store_true")
    parser.add_argument("--console", action="store_true")
    args = parser.parse_args()
    if args.web == args.console:
        parser.error("choose --web or --console")
    if args.web:
        WebChatServer("0.0.0.0", 5000).run()
    else:
        ConsoleChatServer("127.0.0.1", 5555).run()
