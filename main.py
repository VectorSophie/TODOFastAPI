from fastapi import FastAPI
from controllers.todo_controller import router as todo_router

app = FastAPI()
app.include_router(todo_router)
