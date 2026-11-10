#!/usr/bin/env python3
"""Controllo statico di struttura e guardrail della Skill 06, NON test agentico/normativo."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
expected = [
    "SKILL.md", "references/source-protocol.md", "references/official-sources.md",
    "references/output-template.md", "references/test-cases.md", "scripts/check_skill.py",
]
errors = [f"File mancante: {p}" for p in expected if not (root / p).is_file()]
main = root / "SKILL.md"
if main.is_file():
    content = main.read_text(encoding="utf-8")
    m = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not m:
        errors.append("Frontmatter YAML mancante")
    else:
        name = re.search(r"(?m)^name:\s*(\S+)\s*$", m[1])
        desc = re.search(r"(?m)^description:\s*(.+?)\s*$", m[1])
        if not name or name[1] != root.name:
            errors.append("name non coerente con cartella")
        if not desc or not (1 <= len(desc[1]) <= 1024):
            errors.append("description mancante o fuori limiti")
    for link in re.findall(r"\]\((references/[^)]+\.md)\)", content):
        if not (root / link).is_file():
            errors.append(f"Link interno non risolto: {link}")
    required = [
        "nessun programma", "gestione", "OBBLIGATORIO", "CONDIZIONALE",
        "NON_VERIFICATO", "BLOCCATO_DA_FONTI", "scadenze", "rettifiche",
        "responsabili", "non presentare una domanda", "fonte", "fase",
    ]
    for term in required:
        if term.casefold() not in content.casefold():
            errors.append(f"Guardrail assente: {term}")
for p in expected:
    f = root / p
    if f.is_file() and not f.stat().st_size:
        errors.append(f"File vuoto: {p}")
if errors:
    print("FAIL\n" + "\n".join("- " + e for e in errors))
    sys.exit(1)
print("PASS: struttura, metadati, link e guardrail testuali. Nessun test agente/giuridico eseguito.")
