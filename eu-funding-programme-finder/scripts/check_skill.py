#!/usr/bin/env python3
"""Validazione locale, senza dipendenze, di struttura e riferimenti della skill.
Non valida contenuto giuridico, portali, bandi correnti o runtime degli agenti.
"""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "SKILL.md",
    "references/programme-map.md",
    "references/official-sources.md",
    "references/output-template.md",
    "scripts/check_skill.py",
]
errors = [f"File mancante: {name}" for name in required if not (root / name).is_file()]
skill = root / "SKILL.md"
if skill.is_file():
    body = skill.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", body, re.S)
    if not match:
        errors.append("Frontmatter YAML mancante")
    else:
        header = match.group(1)
        found_name = re.search(r"(?m)^name:\s*(\S+)\s*$", header)
        found_description = re.search(r"(?m)^description:\s*(.+?)\s*$", header)
        if not found_name or found_name.group(1) != root.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", found_name.group(1)) or len(found_name.group(1)) > 64:
            errors.append("Campo name assente, non valido o diverso dalla directory")
        if not found_description or not 1 <= len(found_description.group(1)) <= 1024:
            errors.append("Campo description assente o troppo lungo")
    for link in re.findall(r"\]\((references/[^)]+\.md)\)", body):
        if not (root / link).is_file():
            errors.append(f"Riferimento locale mancante: {link}")
if errors:
    print("FAIL\n" + "\n".join(f"- {problem}" for problem in errors))
    sys.exit(1)
print("PASS: file, metadati e riferimenti locali; nessuna validazione di contenuto o esecuzione")
