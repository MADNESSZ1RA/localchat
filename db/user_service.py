from db.models import User
from db.database import SessionLocal
import hashlib

class UserService:
    def __init__(self):
        self.db = SessionLocal()

    def hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def register(self, username: str, password: str) -> bool:
        if self.db.query(User).filter_by(username=username).first():
            return False
        user = User(username=username, password_hash=self.hash_password(password))
        self.db.add(user)
        self.db.commit()
        return True

    def login(self, username: str, password: str) -> bool:
        user = self.db.query(User).filter_by(username=username).first()
        if not user:
            return False
        return user.password_hash == self.hash_password(password)
