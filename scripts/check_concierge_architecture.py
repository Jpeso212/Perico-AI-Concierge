#!/usr/bin/env python3
"""Static contract checks for Perico Concierge architecture documents."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "business" / "concierge"
REQUIRED = {
    "orchestrator.md": ("transaction-context-contract.md", "atomically register or serialize"),
    "payment-router.md": ("transaction-context-contract.md", "coordinate the intended operation across channels"),
    "integration-registry.md": ("provider callback may directly set Perico", "Booking Engine"),
    "identity-permissions-engine.md": ("validate authorization against the specific resource", "recheck current permissions after channel or agent handoff"),
    "virtual-reseller-agent-layer.md": ("authorize the specific receiving staff identity", "Revalidate access at acceptance"),
    "channel-layer.md": ("Before granting human control or exposing protected conversation context", "does not confer broader record access"),
}
ERRORS = []
for name, clauses in REQUIRED.items():
    path = DOCS / name
    if not path.is_file():
        ERRORS.append(f"Missing required document: {path.relative_to(ROOT)}")
        continue
    text = path.read_text(encoding="utf-8")
    for clause in clauses:
        if clause not in text:
            ERRORS.append(f"{name}: missing architecture guardrail: {clause}")
    for target in re.findall(r"\]\(([^)#]+\.md)(?:#[^)]*)?\)", text):
        if "://" in target:
            continue
        if not (path.parent / target).is_file():
            ERRORS.append(f"{name}: broken relative document link: {target}")

for error in ERRORS:
    print(f"FAIL: {error}", file=sys.stderr)
if ERRORS:
    sys.exit(1)
print(f"PASS: {len(REQUIRED)} architecture documents; required guardrails and local Markdown links verified.")
