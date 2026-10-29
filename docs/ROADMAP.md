# SHUL_V_1.7 Roadmap

## MVP delivered in this package
- FastAPI API
- Master orchestration workflow
- Ten specialist agent roles
- SQLite task history and audit events
- Reports endpoint
- Dry-run security lab target validation
- Docker and Render starter deployment files

## Milestone 2: real LLM orchestration
- Provider adapter (OpenRouter or another OpenAI-compatible endpoint)
- Per-agent model settings, timeouts, retry/backoff, token budgets
- Structured JSON output and schema validation
- Prompt injection defenses for retrieved web content
- Redaction of secrets and private data
- Evaluation suite comparing expected outputs

## Milestone 3: worker and tools
- Redis + Celery/RQ background queue
- Sandboxed code execution with CPU/RAM/time quotas
- Git worktrees or temporary project folders
- Unit tests, type checks, dependency scanning, SBOM
- Browser/search connector with source citations
- Approval gate before deployment or external side effects

## Milestone 4: frontend and multimodal
- React/Next.js dashboard or PWA
- WebSocket task streaming
- Voice-to-text and text-to-speech provider adapter
- Image/video upload with strict size/type checks and malware scanning
- Admin authentication, roles, MFA, session expiry

## Milestone 5: security lab
- Kali Linux in a dedicated VM, not privileged inside the main app
- Separate isolated Docker network / host-only VM network
- Allowlisted lab targets only
- Tool wrapper with fixed argument schemas; no arbitrary shell strings
- Manual approval and immutable audit log for each scan
- Results mapped to severity and remediation guidance

## Milestone 6: self-improvement
- Collect user ratings and test failures
- Create versioned test cases and skills proposals
- Evaluate proposals offline against a benchmark
- Human approves changes before merge/deploy
- Never allow an agent to rewrite its own safety policy or deploy itself without review
