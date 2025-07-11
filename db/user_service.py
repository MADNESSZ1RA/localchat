from db.models import User
from db.database import SessionLocal
import hashlib


class UserService:
    def __init__(self):
        self.db = SessionLocal()

    def _hash(self, value: str) -> str:
        return hashlib.sha256(value.encode()).hexdigest()

    def register(self, username: str, password: str) -> bool:
        if self.db.query(User).filter_by(username=username).first():
            return False
        self.db.add(User(username=username, password_hash=self._hash(password)))
        self.db.commit()
        return True

    def login(self, username: str, password: str) -> bool:
        user = self.db.query(User).filter_by(username=username).first()
        if not user:
            return False
        return user.password_hash == self._hash(password)
