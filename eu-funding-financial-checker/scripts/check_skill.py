#!/usr/bin/env python3
"""Controlli statici: struttura, link interni e guardrail testuali, NON verifica giuridica."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
expected = [
    "SKILL.md", "references/official-sources.md", "references/calculation-model.md",
    "references/output-template.md", "references/test-cases.md",
    "scripts/check_skill.py", "scripts/estimate_grant.py", "scripts/test_calculations.py",
]
errors = [f"File mancante: {p}" for p in expected if not (root / p).is_file()]
main = root / "SKILL.md"
if main.is_file():
    content = main.read_text(encoding="utf-8")
    front = re.match(r"\A---\n(.*?)\n---\n", content, flags=re.S)
    if not front:
        errors.append("Frontmatter YAML mancante")
    else:
        metadata = front.group(1)
        name = re.search(r"(?m)^name:\s*(\S+)\s*$", metadata)
        desc = re.search(r"(?m)^description:\s*(.+?)\s*$", metadata)
        if not name or name.group(1) != root.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)) or len(name.group(1)) > 64:
            errors.append("name assente o incoerente")
        if not desc or not 1 <= len(desc.group(1)) <= 1024:
            errors.append("description mancante o fuori limiti")
    for link in re.findall(r"\]\((references/[^)]+\.md)\)", content):
        if not (root / link).is_file():
            errors.append(f"Riferimento non risolvibile: {link}")
    for token in ("GRANT_ACTUAL_COST", "GRANT_LUMP_SUM", "NON_VERIFICATO", "CALCOLATO_SU_INPUT",
                  "non ammissibili", "fabbisogno", "prefinancing", "MIM", "grant_cap", "costs", "equity"):
        if token.casefold() not in content.casefold():
            errors.append(f"Guardrail mancante: {token}")
for rel in expected:
    path = root / rel
    if path.is_file() and not path.stat().st_size:
        errors.append(f"File vuoto: {rel}")
if errors:
    print("FAIL\n" + "\n".join(f"- {e}" for e in errors))
    sys.exit(1)
print("PASS: file, metadati, link, guardrail; conformità bando NON verificata")
