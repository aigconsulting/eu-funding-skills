#!/usr/bin/env python3
"""Lightweight, dependency-free validation of the local Agent Skills package.

Does NOT validate the accuracy of EU-funding facts or runtime compatibility.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "SKILL.md"
REQUIRED = [
    ROOT / "references/taxonomy.md",
    ROOT / "references/official-sources.md",
    ROOT / "references/output-template.md",
]
errors = []

if not DOC.exists():
    errors.append("SKILL.md mancante")
else:
    data = DOC.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", data, re.S)
    if not m:
        errors.append("Frontmatter YAML non trovato")
    else:
        front = m.group(1)
        name = re.search(r"(?m)^name:\s*(.+?)\s*$", front)
        desc = re.search(r"(?m)^description:\s*(.+?)\s*$", front)
        if not name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)):
            errors.append("name non valido")
        elif name.group(1) != ROOT.name or len(name.group(1)) > 64:
            errors.append("name non corrisponde alla directory o supera 64 caratteri")
        if not desc or not (1 <= len(desc.group(1)) <= 1024):
            errors.append("description assente o troppo lunga")
    for rel in re.findall(r"\]\((references/[^)]+\.md)\)", data):
        if not (ROOT / rel).is_file():
            errors.append(f"Riferimento mancante: {rel}")
for item in REQUIRED:
    if not item.is_file():
        errors.append(f"File richiesto mancante: {item}")

if errors:
    print("FAIL\n" + "\n".join(f"- {x}" for x in errors))
    sys.exit(1)
print("PASS: struttura e metadati locali verificati (non valida contenuti o integrazioni)")
