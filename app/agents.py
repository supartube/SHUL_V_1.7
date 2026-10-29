from dataclasses import dataclass, asdict
from typing import Dict, List
import re

@dataclass
class AgentResult:
    agent: str
    status: str
    summary: str
    artifacts: list

AGENTS = [
    ("planner", "Planning & task decomposition"),
    ("researcher", "Source-based research and evidence"),
    ("architect", "System architecture and interfaces"),
    ("coder", "Code and project scaffolding"),
    ("tester", "Test strategy and validation"),
    ("reviewer", "Quality, correctness, and risk review"),
    ("security", "Defensive security and threat modeling"),
    ("data_ml", "Data pipelines and ML experiment design"),
    ("reporter", "Progress summaries and final reporting"),
    ("learning", "Feedback evaluation and reusable skill proposals"),
]

def run_agent(name: str, role: str, command: str) -> AgentResult:
    # Deterministic demo responses keep the project runnable without paid APIs.
    # Replace with provider-backed calls only after implementing rate limits,
    # prompt-injection defenses, secret filtering, and evaluation.
    low = command.lower()
    if name == "planner":
        summary = "Break the request into requirements, plan, implementation, tests, and review."
    elif name == "researcher":
        summary = "Research mode is a connector point. Add approved search APIs and require citations for factual claims."
    elif name == "architect":
        summary = "Use modular services, typed API contracts, persistent task records, audit logs, and isolated workers."
    elif name == "coder":
        summary = "Code generation is scaffolded as a workflow; generated files must be tested in a sandbox before use."
    elif name == "tester":
        summary = "Proposed checks: input validation, happy path, invalid input, permission checks, and failure recovery."
    elif name == "reviewer":
        summary = "Review for correctness, maintainability, dependency risk, secrets exposure, and test coverage."
    elif name == "security":
        summary = "Use threat modeling, least privilege, dependency checks, and authorized lab-only security testing."
    elif name == "data_ml":
        summary = "Track dataset provenance, train/validation splits, metrics, reproducibility, and human review."
    elif name == "reporter":
        summary = "Report completed work, limitations, open risks, artifacts, and recommended next actions."
    else:
        summary = "Convert reviewed feedback into versioned evaluation cases and reusable skills; do not self-modify production code."
    artifacts = []
    if any(word in low for word in ("website", "web app", "website", "application", "software")) and name == "coder":
        artifacts.append("Suggested artifact: generated project README + implementation plan")
    return AgentResult(name, "completed", summary, artifacts)

def orchestrate(command: str, mode: str = "standard") -> Dict:
    results: List[AgentResult] = []
    for name, role in AGENTS:
        results.append(run_agent(name, role, command))
    plan = [
        "Clarify requirements and acceptance criteria",
        "Research trustworthy sources if online research is required",
        "Create architecture and task breakdown",
        "Implement in an isolated workspace",
        "Run tests and security review",
        "Present report and request approval for external actions",
    ]
    return {
        "command": command,
        "mode": mode,
        "master_plan": plan,
        "agents": [asdict(r) for r in results],
        "overall_status": "completed_with_scaffold",
        "limitations": [
            "Demo agent responses are deterministic placeholders until an LLM provider is connected.",
            "No unrestricted shell, arbitrary network access, or automatic exploitation is provided.",
            "Self-training means evaluation/feedback updates, not uncontrolled model-weight modification."
        ]
    }
