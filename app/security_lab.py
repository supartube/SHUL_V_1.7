from urllib.parse import urlparse
from app.config import AUTHORIZED_LAB_TARGETS, SECURITY_TOOLS_DRY_RUN

def validate_lab_target(target: str):
    raw = target.strip().lower()
    host = urlparse(raw).hostname if "://" in raw else raw.split("/")[0].split(":")[0]
    if not host or host not in AUTHORIZED_LAB_TARGETS:
        raise ValueError("Target is not in AUTHORIZED_LAB_TARGETS. Add only a system you own or are explicitly authorized to test.")
    return host

def run_lab_scan(target: str, authorization_confirmed: bool):
    host = validate_lab_target(target)
    if not authorization_confirmed:
        raise PermissionError("Explicit authorization confirmation is required.")
    if SECURITY_TOOLS_DRY_RUN:
        return {
            "status": "dry_run",
            "target": host,
            "message": "Dry-run only. No network scan was executed.",
            "next_steps": ["Review scope", "Confirm authorization", "Use an isolated lab", "Document findings and remediation"]
        }
    # Intentionally no shell execution here. Integrate a narrowly allowlisted tool
    # runner in an isolated container after a separate security review.
    return {
        "status": "not_configured",
        "target": host,
        "message": "Real tool execution is not implemented in this starter."
    }
