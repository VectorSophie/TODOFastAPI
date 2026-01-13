from fastapi import HTTPException
from repositories.todo_repository import TodoRepository

class TodoService:
    def __init__(self):
        self.repo = TodoRepository()

    def create_todo(self, content: str):
        return self.repo.create(content)

    def get_todos(self):
        return self.repo.find_all()

    def get_todo(self, todo_id: int):
        todo = self.repo.find_by_id(todo_id)
        if not todo:
            raise HTTPException(status_code=404, detail="Todo not found")
        return todo

    def update_todo(self, todo_id: int, content: str):
        if not self.repo.update(todo_id, content):
            raise HTTPException(status_code=404, detail="Todo not found")
        return self.repo.find_by_id(todo_id)

    def delete_todo(self, todo_id: int):
        if not self.repo.delete(todo_id):
            raise HTTPException(status_code=404, detail="Todo not found")
