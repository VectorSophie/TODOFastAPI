from fastapi import FastAPI

from controllers.todo_controller import router as todo_router
from database import engine
from models.todo import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(todo_router)
