# Security and authorization model

SHUL_V_1.7 is for defensive learning and authorized lab work.

## Kali Linux
Run Kali as a separate VM (VirtualBox/VMware) or dedicated lab machine. Keep it on a host-only or isolated lab network. Do not mount personal folders or expose privileged Docker sockets to agents. The app should call only a small, audited wrapper for explicitly allowed tools.

## Allowed first integrations
- Nmap: inventory of explicitly authorized lab targets
- OWASP ZAP: passive/baseline testing against local demo applications
- Trivy: scan container images and dependencies
- Semgrep: static analysis of project source
- Bandit: Python security linting
- pip-audit: Python dependency audit

This starter does not execute these tools. Add one integration at a time after reviewing its official documentation and creating an isolated test environment.

## Forbidden automation
No arbitrary third-party target scanning, exploitation, credential attacks, stealth, persistence, exfiltration, destructive actions, or bypassing access controls.

## Before real deployments
Add authentication and authorization, per-user isolation, request limits, encrypted secret storage, backups, monitoring, dependency pinning, security tests, and an incident-response plan.
