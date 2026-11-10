#!/usr/bin/env python3
"""Controllo di struttura locale della skill; non valida fonti o comportamento dell'agente."""
from pathlib import Path
import re
import sys

skill = Path(__file__).resolve().parents[1]
text = (skill / "SKILL.md").read_text(encoding="utf-8")
expected = "eu-funding-grant-agreement-manager"
front = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
if not front or not re.search(rf"(?m)^name:\s*{re.escape(expected)}\s*$", front.group(1)):
    print(f"FAIL: name/frontmatter non conforme per {expected}", file=sys.stderr)
    raise SystemExit(1)
if not re.search(r"(?m)^description:\s*\S+", front.group(1)) or not text[front.end():].strip().startswith("# "):
    print(f"FAIL: description/titolo mancante per {expected}", file=sys.stderr)
    raise SystemExit(1)
print(f"PASS: struttura {expected}")
