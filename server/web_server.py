from flask import Flask, request, jsonify, render_template
from db.database import Base, engine
from db.user_service import UserService


class WebChatServer:
    def __init__(self, host: str, port: int):
        self.app = Flask(__name__, template_folder="../templates")
        self.messages = []
        self.user_service = UserService()
        self._register_routes()
        self.host = host
        self.port = port

    def run(self) -> None:
        Base.metadata.create_all(bind=engine)
        self.app.run(host=self.host, port=self.port, threaded=True)

    def _register_routes(self) -> None:
        @self.app.route("/")
        def index():
            return render_template("index.html")

        @self.app.route("/register", methods=["POST"])
        def register():
            data = request.get_json()
            ok = self.user_service.register(data["username"], data["password"])
            return ("", 204) if ok else ("", 409)

        @self.app.route("/login", methods=["POST"])
        def login():
            data = request.get_json()
            ok = self.user_service.login(data["username"], data["password"])
            return ("", 204) if ok else ("", 401)

        @self.app.route("/messages", methods=["GET"])
        def get_messages():
            last_id = int(request.args.get("last_id", -1))
            return jsonify([m for m in self.messages if m["id"] > last_id])

        @self.app.route("/messages", methods=["POST"])
        def post_message():
            data = request.get_json()
            msg_id = self.messages[-1]["id"] + 1 if self.messages else 0
            self.messages.append(
                {"id": msg_id, "user": data["user"], "text": data["text"]})
            return ("", 204)
