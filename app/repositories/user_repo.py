from app.core.db import get_conn, release_conn
from app.models.entities.users import User

class UserRepository:
    def __init__(self):
        pass

    def create_user(self, name: str, email: str):
        conn = get_conn()
        try:
            user = User(name=name, email=email)
            conn.add(user)
            conn.commit()
            conn.refresh(user)
            return user
        finally:
            release_conn(conn)