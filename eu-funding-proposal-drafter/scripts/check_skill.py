#!/usr/bin/env python3
"""Controllo statico locale Skill 07; non valuta documenti reali o output agentici."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
files = ["SKILL.md", "references/evidence-protocol.md", "references/official-sources.md",
         "references/output-template.md", "references/test-cases.md",
         "scripts/check_skill.py", "scripts/validate_draft.py", "scripts/test_validator.py"]
errors = [f"File mancante o vuoto: {p}" for p in files if not (root/p).is_file() or not (root/p).stat().st_size]
if (root/"SKILL.md").is_file():
    body = (root/"SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", body, re.S)
    if not m:
        errors.append("Frontmatter YAML assente")
    else:
        n = re.search(r"(?m)^name:\s*(\S+)\s*$", m[1])
        d = re.search(r"(?m)^description:\s*(.+)\s*$", m[1])
        if not n or n[1] != root.name:
            errors.append("Campo name incoerente")
        if not d or not 1 <= len(d[1]) <= 1024:
            errors.append("Campo description assente/non valido")
    for target in re.findall(r"\]\((references/[^)]+\.md)\)", body):
        if not (root/target).is_file():
            errors.append(f"Link locale non valido: {target}")
    checks = ["indipendente dal programma", "fonte", "OBBLIGATORIO", "CONDIZIONALE",
              "BLOCCATA_DA_FONTI", "PROPOSTA", "STIMA_NON_VALIDATA", "SEGNAPOSTO",
              "matrice", "non effettuare la submission", "non inventare", "fase"]
    for check in checks:
        if check.casefold() not in body.casefold():
            errors.append(f"Guardrail non trovato: {check}")
if errors:
    print("FAIL:\n- " + "\n- ".join(errors))
    sys.exit(1)
print("PASS: struttura/metadati/link/guardrail locali; nessun controllo normativo o agentico")
