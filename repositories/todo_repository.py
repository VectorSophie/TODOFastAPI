from database import get_db

class TodoRepository:

    def create(self, content: str):
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
        return row

    def find_all(self):
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, content, created_at FROM todo ORDER BY id DESC"
        )
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows

    def find_by_id(self, todo_id: int):
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT id, content, created_at FROM todo WHERE id = %s",
            (todo_id,)
        )
        row = cursor.fetchone()

        cursor.close()
        conn.close()
        return row

    def update(self, todo_id: int, content: str):
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE todo SET content = %s WHERE id = %s",
            (content, todo_id)
        )
        conn.commit()

        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected

    def delete(self, todo_id: int):
        conn = get_db()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM todo WHERE id = %s",
            (todo_id,)
        )
        conn.commit()

        affected = cursor.rowcount
        cursor.close()
        conn.close()
        return affected
