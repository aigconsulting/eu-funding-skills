#!/usr/bin/env python3
"""Controlli statici di integrità. Non esegue analisi legale o browsing di call."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
expected = [
    "SKILL.md", "references/official-sources.md", "references/decision-model.md",
    "references/output-template.md", "references/test-cases.md", "scripts/check_skill.py",
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
    for local in re.findall(r"\]\((references/[^)]+\.md)\)", content):
        if not (root / local).is_file():
            errors.append(f"Riferimento non risolvibile: {local}")
    for token in (
        "PARTECIPAZIONE", "FINANZIABILITA", "AMMISSIBILITA", "COERENTE_PRELIMINARE",
        "CONDIZIONATO", "INCOMPATIBILE_DOCUMENTATO", "DATI_INSUFFICIENTI",
        "NON_VERIFICATO", "NON_APPLICABILE", "due fasi", "costituzione",
    ):
        if token.casefold() not in content.casefold():
            errors.append(f"Guardrail testuale mancante: {token}")
for rel in expected:
    file = root / rel
    if file.is_file() and file.stat().st_size == 0:
        errors.append(f"File vuoto: {rel}")
if errors:
    print("FAIL\n" + "\n".join(f"- {err}" for err in errors))
    sys.exit(1)
print("PASS: file, metadata, link interni, guardrail testuali; test funzionali NON eseguiti")
