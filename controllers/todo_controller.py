from fastapi import APIRouter, Request, HTTPException
from services.todo_service import TodoService

router = APIRouter()
service = TodoService()


@router.post("/todos")
async def create_todo(request: Request):
    body = await request.json()
    content = body.get("content")

    if not content:
        raise HTTPException(status_code=400, detail="content is required")

    todo = service.create_todo(content)

    return {
        "id": todo.id,
        "content": todo.content,
        "created_at": str(todo.created_at)
    }


@router.get("/todos")
def get_todos():
    todos = service.get_todos()

    return [
        {
            "id": t.id,
            "content": t.content,
            "created_at": str(t.created_at)
        }
        for t in todos
    ]


@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    todo = service.get_todo(todo_id)

    return {
        "id": todo.id,
        "content": todo.content,
        "created_at": str(todo.created_at)
    }


@router.put("/todos/{todo_id}")
async def update_todo(todo_id: int, request: Request):
    body = await request.json()
    content = body.get("content")

    if not content:
        raise HTTPException(status_code=400, detail="content is required")

    todo = service.update_todo(todo_id, content)

    return {
        "id": todo.id,
        "content": todo.content,
        "created_at": str(todo.created_at)
    }


@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    service.delete_todo(todo_id)
    return {"message": "Todo deleted"}
