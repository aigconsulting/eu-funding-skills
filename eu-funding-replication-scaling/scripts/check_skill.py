#!/usr/bin/env python3
"""Verifica strutturale locale; non certifica contenuti o conformità."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
skill = (root / "SKILL.md").read_text(encoding="utf-8")
assert skill.startswith("---\nname: eu-funding-replication-scaling\ndescription: ")
assert root.name == "eu-funding-replication-scaling"
for heading in ("## Scopo", "## Input", "## Procedura", "## Output", "## Fonti istituzionali", "## Guardrail", "## Esiti", "## Scenari da verificare"):
    assert heading in skill, f"Sezione mancante: {heading}"
assert "| --- |" in skill
assert "MANCANTE" in skill and "NON_APPLICABILE" in skill
print("PASS: struttura testuale eu-funding-replication-scaling")
