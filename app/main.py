import json
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.config import APP_NAME
from app.db import init_db, add_task, update_task, get_task, list_tasks, audit
from app.schemas import TaskRequest, SecurityScanRequest, TaskResponse
from app.agents import AGENTS, orchestrate
from app.security_lab import run_lab_scan

app = FastAPI(title=APP_NAME, version="1.7.0", description="Bounded autonomous multi-agent AI starter")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type", "Authorization"],
)

@app.on_event("startup")
def startup():
    init_db()

@app.get("/")
def root():
    return {"name": APP_NAME, "status": "running", "docs": "/docs", "health": "/health"}

@app.get("/health")
def health():
    return {"ok": True, "app": APP_NAME, "version": "1.7.0"}

@app.get("/api/agents")
def agents():
    return [{"name": n, "role": r} for n, r in AGENTS]

@app.get("/api/tasks")
def tasks():
    return list_tasks()

@app.post("/api/tasks", response_model=TaskResponse)
def create_task(req: TaskRequest):
    task_id = add_task(req.command)
    audit(task_id, "task_created", f"mode={req.mode}")
    try:
        result = orchestrate(req.command, req.mode)
        result_json = json.dumps(result, ensure_ascii=False)
        update_task(task_id, "completed", result_json)
        audit(task_id, "task_completed", "Agent orchestration completed")
        return TaskResponse(task_id=task_id, status="completed", message="Task processed; see report endpoint.")
    except Exception as exc:
        update_task(task_id, "failed", json.dumps({"error": str(exc)}))
        audit(task_id, "task_failed", type(exc).__name__)
        raise HTTPException(status_code=500, detail="Task failed. See server logs.")

@app.get("/api/tasks/{task_id}")
def task_detail(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.get("result_json"):
        try: task["result"] = json.loads(task["result_json"])
        except json.JSONDecodeError: pass
        task.pop("result_json", None)
    return task

@app.get("/api/reports/{task_id}")
def report(task_id: int):
    task = get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    result = json.loads(task["result_json"]) if task.get("result_json") else {}
    return {
        "task_id": task_id,
        "command": task["command"],
        "status": task["status"],
        "created_at": task["created_at"],
        "report": result
    }

@app.post("/api/security/lab-scan")
def security_scan(req: SecurityScanRequest):
    try:
        return run_lab_scan(req.target, req.authorization_confirmed)
    except (ValueError, PermissionError) as exc:
        raise HTTPException(status_code=403, detail=str(exc))
