#!/usr/bin/env python3
"""Controllo statico Skill 08; NON revisione agentica o giuridica."""
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
required = ["SKILL.md", "references/review-protocol.md", "references/qualitative-review.md",
            "references/official-sources.md", "references/output-template.md", "references/test-cases.md",
            "scripts/check_skill.py", "scripts/validate_review.py", "scripts/test_validator.py"]
errors = [f"File mancante o vuoto: {p}" for p in required if not (root/p).is_file() or not (root/p).stat().st_size]
if (root/"SKILL.md").is_file():
    content = (root/"SKILL.md").read_text(encoding="utf-8")
    fm = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
    if not fm:
        errors.append("Frontmatter YAML mancante")
    else:
        name = re.search(r"(?m)^name:\s*(\S+)\s*$", fm[1])
        desc = re.search(r"(?m)^description:\s*(.+)$", fm[1])
        if not name or name[1] != root.name:
            errors.append("name diverso dalla directory")
        if not desc or not 1 <= len(desc[1]) <= 1024:
            errors.append("description mancante/non valida")
    for link in re.findall(r"\]\((references/[^)]+\.md)\)", content):
        if not (root/link).is_file():
            errors.append(f"Link locale mancante: {link}")
    guardrails = ["indipendente dal programma", "AUTO_REVISIONE", "fonte", "BLOCCATA_DA_FONTI",
                  "ACCERTATO", "NON_VERIFICABILE", "REVIEW_PARZIALE", "non invia",
                  "punteggi", "proposta", "criteri", "submission", "autorizzazione",
                  "qualitative-review", "valutazione simulata", "CRITERI_NON_DISPONIBIL"]
    for word in guardrails:
        if word.casefold() not in content.casefold():
            errors.append(f"Guardrail mancante: {word}")
if errors:
    print("FAIL:\n- " + "\n- ".join(errors))
    sys.exit(1)
print("PASS: struttura/frontmatter/collegamenti/guardrail; NON verifica sostanziale")
