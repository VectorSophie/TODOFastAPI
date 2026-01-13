from fastapi import FastAPI, Request, HTTPException
import mysql.connector

app = FastAPI()

def get_db():
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="my-secret-pw",
        database="mydb"
    )

# ---------------------------
# CREATE
# ---------------------------
@app.post("/todos")
async def create_todo(request: Request):
    body_bytes = await request.body()
    if not body_bytes:
        raise HTTPException(status_code=400, detail="Missing JSON body")

    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    content = body.get("content")
    if not content:
        raise HTTPException(status_code=400, detail="content is required")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO todo (content) VALUES (%s)",
        (content,)
    )
    conn.commit()

    todo_id = cursor.lastrowid

    cursor.execute(
        "SELECT id, content, created_at FROM todo WHERE id = %s",
        (todo_id,)
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "id": row[0],
        "content": row[1],
        "created_at": str(row[2])
    }

# ---------------------------
# READ (ALL)
# ---------------------------
@app.get("/todos")
def get_todos():
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, content, created_at FROM todo ORDER BY id DESC"
    )
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
        {
            "id": r[0],
            "content": r[1],
            "created_at": str(r[2])
        }
        for r in rows
    ]

# ---------------------------
# READ (ONE)
# ---------------------------
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id, content, created_at FROM todo WHERE id = %s",
        (todo_id,)
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if not row:
        raise HTTPException(status_code=404, detail="Todo not found")

    return {
        "id": row[0],
        "content": row[1],
        "created_at": str(row[2])
    }

# ---------------------------
# UPDATE
# ---------------------------
@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, request: Request):
    body_bytes = await request.body()
    if not body_bytes:
        raise HTTPException(status_code=400, detail="Missing JSON body")

    try:
        body = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    content = body.get("content")
    if not content:
        raise HTTPException(status_code=400, detail="content is required")

    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE todo SET content = %s WHERE id = %s",
        (content, todo_id)
    )
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Todo not found")

    cursor.execute(
        "SELECT id, content, created_at FROM todo WHERE id = %s",
        (todo_id,)
    )
    row = cursor.fetchone()

    cursor.close()
    conn.close()

    return {
        "id": row[0],
        "content": row[1],
        "created_at": str(row[2])
    }

# ---------------------------
# DELETE
# ---------------------------
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    conn = get_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM todo WHERE id = %s",
        (todo_id,)
    )
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Todo not found")

    cursor.close()
    conn.close()

    return {"message": "Todo deleted"}
