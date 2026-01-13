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

    row = service.create_todo(content)
    return {
        "id": row[0],
        "content": row[1],
        "created_at": str(row[2])
    }

@router.get("/todos")
def get_todos():
    rows = service.get_todos()
    return [
        {
            "id": r[0],
            "content": r[1],
            "created_at": str(r[2])
        }
        for r in rows
    ]

@router.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    r = service.get_todo(todo_id)
    return {
        "id": r[0],
        "content": r[1],
        "created_at": str(r[2])
    }

@router.put("/todos/{todo_id}")
async def update_todo(todo_id: int, request: Request):
    body = await request.json()
    content = body.get("content")
    if not content:
        raise HTTPException(status_code=400, detail="content is required")

    r = service.update_todo(todo_id, content)
    return {
        "id": r[0],
        "content": r[1],
        "created_at": str(r[2])
    }

@router.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    service.delete_todo(todo_id)
    return {"message": "Todo deleted"}
