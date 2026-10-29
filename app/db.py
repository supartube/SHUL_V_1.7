import sqlite3
from pathlib import Path
from datetime import datetime, timezone
DB_PATH = Path("shul.db")

def connect():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with connect() as c:
        c.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            command TEXT NOT NULL,
            status TEXT NOT NULL,
            created_at TEXT NOT NULL,
            result_json TEXT
        )''')
        c.execute('''CREATE TABLE IF NOT EXISTS audit (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_id INTEGER,
            event TEXT NOT NULL,
            details TEXT NOT NULL,
            created_at TEXT NOT NULL
        )''')

def add_task(command):
    now = datetime.now(timezone.utc).isoformat()
    with connect() as c:
        cur = c.execute("INSERT INTO tasks(command,status,created_at) VALUES(?,?,?)", (command, "queued", now))
        return cur.lastrowid

def update_task(task_id, status, result_json):
    with connect() as c:
        c.execute("UPDATE tasks SET status=?, result_json=? WHERE id=?", (status, result_json, task_id))

def get_task(task_id):
    with connect() as c:
        row = c.execute("SELECT * FROM tasks WHERE id=?", (task_id,)).fetchone()
        return dict(row) if row else None

def list_tasks(limit=50):
    with connect() as c:
        return [dict(r) for r in c.execute("SELECT * FROM tasks ORDER BY id DESC LIMIT ?", (limit,)).fetchall()]

def audit(task_id, event, details):
    now = datetime.now(timezone.utc).isoformat()
    with connect() as c:
        c.execute("INSERT INTO audit(task_id,event,details,created_at) VALUES(?,?,?,?)", (task_id, event, details, now))
