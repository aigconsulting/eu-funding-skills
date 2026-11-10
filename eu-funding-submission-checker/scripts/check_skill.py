#!/usr/bin/env python3
"""Test struttura e guardrail di Skill 09, non conformità del bando."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
files = ["SKILL.md", "references/precheck-protocol.md", "references/official-sources.md",
         "references/output-template.md", "references/test-cases.md", "scripts/check_skill.py",
         "scripts/validate_precheck.py", "scripts/test_validator.py"]
errors = [f"file mancante/vuoto: {p}" for p in files if not (root / p).is_file() or not (root / p).stat().st_size]
skill = (root / "SKILL.md").read_text(encoding="utf-8") if (root / "SKILL.md").exists() else ""
frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill, re.S)
if not frontmatter:
    errors.append("frontmatter mancante")
else:
    nm = re.search(r"(?m)^name:\s*(\S+)\s*$", frontmatter[1])
    ds = re.search(r"(?m)^description:\s*(.+)$", frontmatter[1])
    if not nm or nm[1] != root.name:
        errors.append("name frontmatter non coincide")
    if not ds or not 1 <= len(ds[1]) <= 1024:
        errors.append("description frontmatter mancante/invalida")
for link in re.findall(r"\]\((references/[^)]+\.md)\)", skill):
    if not (root/link).is_file():
        errors.append(f"riferimento locale inesistente: {link}")
for item in ["indipendente dal programma", "BLOCCATO_DA_FONTI", "PRECHECK_PARZIALE",
             "BLOCCO_ACCERTATO", "DA_VERIFICARE", "submission.performed", "autorizzazione",
             "fuso", "non invia", "non certifica", "fonte", "fase"]:
    if item.casefold() not in skill.casefold():
        errors.append(f"guardrail mancante: {item}")
if errors:
    print("FAIL\n- " + "\n- ".join(errors))
    sys.exit(1)
print("PASS: struttura/frontmatter/link/guardrail; NON verifica sostanziale")
