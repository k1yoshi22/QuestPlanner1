import os
import sys
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

sys.stdout.reconfigure(encoding="utf-8")

app = FastAPI(title="QuestPlanner API")


class UserCreate(BaseModel):
    name: str
    email: str


class UserUpdate(BaseModel):
    name: str
    email: str


class AIRequest(BaseModel):
    message: str


def get_conn():
    return psycopg2.connect(
        host="postgres",
        database="quest_db",
        user="quest_user",
        password="quest_pass",
        port=5432
    )


def init_db():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()


@app.get("/")
def root():
    return {"message": "QuestPlanner API работает"}


@app.get("/users")
def get_users():
    init_db()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return [{"id": r[0], "name": r[1], "email": r[2]} for r in rows]


@app.get("/users/{user_id}")
def get_user(user_id: int):
    init_db()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name, email FROM users WHERE id = %s;", (user_id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"id": row[0], "name": row[1], "email": row[2]}


@app.post("/users")
def create_user(user: UserCreate):
    init_db()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id;",
        (user.name, user.email)
    )
    user_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()

    return {"id": user_id, "name": user.name, "email": user.email}


@app.put("/users/{user_id}")
def update_user(user_id: int, user: UserUpdate):
    init_db()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET name = %s, email = %s WHERE id = %s RETURNING id;",
        (user.name, user.email, user_id)
    )
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"id": user_id, "name": user.name, "email": user.email}


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    init_db()
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("DELETE FROM users WHERE id = %s RETURNING id;", (user_id,))
    row = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="User not found")

    return {"message": "User deleted", "id": user_id}


@app.post("/ai")
def ask_ai(request: AIRequest):
    try:
        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            return {"response": "Ошибка: OPENAI_API_KEY не найден"}

        response = requests.post(
            "https://api.openai.com/v1/responses",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json"
            },
            json={
                "model": "gpt-4.1-mini",
                "input": request.message
            },
            timeout=30
        )

        data = response.json()
        print("OPENAI RESPONSE:", data)

        if "output" in data:
            text = data["output"][0]["content"][0]["text"]
            return {"response": text}

        if "error" in data:
            return {"response": f"Ошибка OpenAI: {data['error'].get('message')}"}

        return {"response": str(data)}

    except Exception as e:
        return {"response": f"Ошибка AI: {str(e)}"}
