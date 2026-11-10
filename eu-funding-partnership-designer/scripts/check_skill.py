#!/usr/bin/env python3
"""Controllo statico locale Skill 12; NON valida i contenuti, le fonti live né l'output agentico."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md", "references/official-sources.md", "references/partnership-map.md",
    "references/output-template.md", "references/test-cases.md", "scripts/check_skill.py",
]
errors = []
for rel in required:
    if not (root / rel).is_file():
        errors.append(f"File mancante: {rel}")

skill = root / "SKILL.md"
if skill.exists():
    body = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", body, re.S)
    if not match:
        errors.append("Frontmatter YAML mancante")
    else:
        hdr = match.group(1)
        name = re.search(r"(?m)^name:\s*(\S+)\s*$", hdr)
        desc = re.search(r"(?m)^description:\s*(.+?)\s*$", hdr)
        if not name or name.group(1) != root.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)) or len(name.group(1)) > 64:
            errors.append("Campo name assente, non valido o incoerente")
        if not desc or not 1 <= len(desc.group(1)) <= 1024:
            errors.append("Campo description assente o troppo lungo")
    for rel in re.findall(r"\]\((references/[^)]+\.md)\)", body):
        if not (root / rel).is_file():
            errors.append(f"Link locale non risolvibile: {rel}")
    for token in (
        "NON_CONTATTATO", "DA_VERIFICARE", "PROPOSTA", "CORDIS",
        "candidatura individuale", "consorzio", "coordinatore", "partner associati",
        "nessun contatto", "dossier condiviso",
    ):
        if token.casefold() not in body.casefold():
            errors.append(f"Garanzia descrittiva mancante: {token}")

if errors:
    print("FAIL\n- " + "\n- ".join(errors))
    sys.exit(1)
print("PASS: struttura, frontmatter, riferimenti e garanzie testuali; NON verifica fonti live né esecuzione agentica")
