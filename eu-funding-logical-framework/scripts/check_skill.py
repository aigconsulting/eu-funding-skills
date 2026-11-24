#!/usr/bin/env python3
"""Controllo statico locale, non verifica metodologica o agentica."""
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = ("SKILL.md", "references/official-sources.md", "references/output-template.md", "references/test-cases.md")
for rel in required:
    assert (root / rel).is_file(), f"File mancante: {rel}"
skill = (root / "SKILL.md").read_text(encoding="utf-8")
assert skill.startswith("---\nname: eu-funding-logical-framework\ndescription: ")
assert skill.count("\n---\n") >= 1
for term in ("baseline", "target", "assunzioni", "MANCANTE", "Guardrail"):
    assert term in skill, f"Elemento mancante: {term}"
print("PASS: struttura e guardrail testuali")
