#!/usr/bin/env python3
"""Controlli locali di struttura e guardrail: non verifica una candidatura reale."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = ["SKILL.md", "references/evidence-protocol.md", "references/official-sources.md",
            "references/output-template.md", "references/test-cases.md", "scripts/check_skill.py",
            "scripts/validate_tracker.py", "scripts/test_validator.py"]
errors = [f"file mancante o vuoto: {p}" for p in required if not (root/p).is_file() or (root/p).stat().st_size == 0]
text = (root/"SKILL.md").read_text(encoding="utf-8") if (root/"SKILL.md").is_file() else ""
fm = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
if not fm:
    errors.append("frontmatter YAML mancante")
else:
    name = re.search(r"(?m)^name:\s*(\S+)\s*$", fm[1])
    desc = re.search(r"(?m)^description:\s*(.+)$", fm[1])
    if not name or name[1] != root.name:
        errors.append("frontmatter name non corrisponde")
    if not desc or not (1 <= len(desc[1]) <= 1024):
        errors.append("frontmatter description mancante o invalida")
for ref in re.findall(r"\]\((references/[^)]+\.md)\)", text):
    if not (root/ref).is_file():
        errors.append(f"riferimento non trovato: {ref}")
for needle in ("indipendente dal programma", "BLOCCATO_DA_FONTI", "MONITORAGGIO_PARZIALE",
               "NESSUN_NUOVO_EVENTO_DOCUMENTATO", "AZIONE_PROPOSTA", "fonte", "fuso",
               "non è un monitor autonomo", "non inviare", "non dichiarare", "autorizzazione"):
    if needle.casefold() not in text.casefold():
        errors.append(f"guardrail non trovato: {needle}")
if errors:
    print("FAIL:\n- " + "\n- ".join(errors))
    sys.exit(1)
print("PASS: struttura/frontmatter/riferimenti/guardrail; NON verifica conformità")
