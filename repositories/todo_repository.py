from sqlalchemy.orm import Session
from database import SessionLocal
from models.todo import Todo

class TodoRepository:

    def _get_session(self) -> Session:
        return SessionLocal()

    def create(self, content: str) -> Todo:
        session = self._get_session()
        todo = Todo(content=content)

        session.add(todo)
        session.commit()
        session.refresh(todo)

        session.close()
        return todo

    def find_all(self):
        session = self._get_session()
        todos = session.query(Todo).order_by(Todo.id.desc()).all()
        session.close()
        return todos

    def find_by_id(self, todo_id: int):
        session = self._get_session()
        todo = session.query(Todo).filter(Todo.id == todo_id).first()
        session.close()
        return todo

    def update(self, todo_id: int, content: str) -> bool:
        session = self._get_session()
        todo = session.query(Todo).filter(Todo.id == todo_id).first()

        if not todo:
            session.close()
            return False

        todo.content = content
        session.commit()
        session.close()
        return True

    def delete(self, todo_id: int) -> bool:
        session = self._get_session()
        todo = session.query(Todo).filter(Todo.id == todo_id).first()

        if not todo:
            session.close()
            return False

        session.delete(todo)
        session.commit()
        session.close()
        return True
