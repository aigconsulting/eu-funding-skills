#!/usr/bin/env python3
"""Verifica strutturale locale; non certifica contenuti o conformità."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
skill = (root / "SKILL.md").read_text(encoding="utf-8")
assert skill.startswith("---\nname: eu-funding-state-aid-checker\ndescription: ")
assert root.name == "eu-funding-state-aid-checker"
for heading in ("## Scopo", "## Input", "## Procedura", "## Output", "## Fonti istituzionali", "## Guardrail", "## Esiti", "## Scenari da verificare"):
    assert heading in skill, f"Sezione mancante: {heading}"
assert "| --- |" in skill
assert "MANCANTE" in skill and "NON_APPLICABILE" in skill
print("PASS: struttura testuale eu-funding-state-aid-checker")
