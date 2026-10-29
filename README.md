# SHUL_V_1.7 — Autonomous Multi-Agent AI Platform (Starter MVP)

A modular, safety-bounded starter project for multi-agent planning, research, software generation, quality review, reporting, and authorized security-lab workflows.

## Important scope
This is a runnable starter scaffold, not a production-ready superintelligence. It does **not** break into arbitrary networks, bypass authentication, or run unrestricted commands. Security tools are only exposed through an allowlisted adapter intended for systems you own or are explicitly authorized to test. Real tool execution is disabled by default.

## Features
- Master orchestrator + 10 specialist agents
- FastAPI backend and web API
- Local task history using SQLite
- Task plans, agent reports, review results, and audit events
- Text commands; voice/image/video processing are documented integration points
- Project-generation workspace with a safe file allowlist
- Security-lab adapter with dry-run default
- Local setup, Docker, and Render deployment files

## Quick start (Windows / Linux)
1. Install Python 3.11 or 3.12 (recommended).
2. Extract this ZIP.
3. Copy `.env.example` to `.env`.
4. In a terminal in this folder:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # Linux/macOS: source .venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
5. Open `http://127.0.0.1:8000/docs`.

The default demo mode works without an LLM API key. To enable an OpenRouter-compatible model, set `OPENROUTER_API_KEY` in `.env` and configure `MODEL_NAME`. Never commit `.env` to GitHub.

## API
- `GET /health`
- `GET /api/agents`
- `POST /api/tasks` with `{"command":"Create a small portfolio website"}`
- `GET /api/tasks/{task_id}`
- `GET /api/reports/{task_id}`
- `POST /api/security/lab-scan` (dry-run unless explicitly enabled; target must be a configured lab target)

## Safety model
- Security testing is limited to configured lab targets and authorized environments.
- No credential theft, persistence, stealth, destructive actions, public-target scanning, or automatic exploitation.
- Shell execution is not exposed as a general-purpose agent tool.
- Generated code is written only inside `workspace/generated/`.
- Human approval is required before deployment or real security-tool execution.

## Next production steps
Add authentication/RBAC, encrypted secrets, job queue (Redis/Celery), proper frontend, persistent production database, provider retry/rate limits, unit/integration tests, container isolation, monitoring, backups, and a security review before public deployment.
