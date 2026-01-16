from sqlalchemy.orm import Session
from app.models.entities.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_user(self, name: str, email: str):
        try:
            user = User(name=name, email=email)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except Exception:
            self.db.rollback()
            raise

    def get_user_by_id(self, id: int):
        return self.db.query(User).filter(User.id == id).first()

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def update_user_name(self, user_id: int, new_name: str):
        try:
            user = self.db.query(User).filter(User.id == user_id).first()
            if not user:
                return None
            user.name = new_name
            self.db.commit()
            return user
        except Exception:
            self.db.rollback()
            raise

    def delete_user_by_email(self, email: str):
        try:
            user = self.db.query(User).filter(User.email == email).first()
            if not user:
                return None
            self.db.delete(user)
            self.db.commit()
            return user
        except Exception:
            self.db.rollback()
            raise