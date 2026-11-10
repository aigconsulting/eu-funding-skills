#!/usr/bin/env python3
"""Check the distribution catalog `index.json` against the actual skill folders.

Verifies (deterministic, dependency-free):
1. every `eu-funding-*` directory in the repository root has an entry in index.json,
   and every entry in index.json has a matching directory;
2. for each entry, the listed files exist in the directory, and every
   `SKILL.md`, `references/*.md` and `scripts/*` file present in the directory is
   listed (the HTTP catalog must ship the whole package);
3. each version is a 12-character lowercase hex string.

Version recipe used for NEW or CHANGED entries (legacy values are grandfathered):
sha256 over UTF-8 of  `name + "\\n"` + for each file in listing order
`filename + " " + sha256(filebytes) + "\\n"`, plus a final `"\\n"`,
first 12 hex chars. With `--print-recipe` the script prints the recipe-derived
version for every skill so future bumps are mechanical.

This script does NOT validate the accuracy of EU-funding facts, of translations
or of runtime behavior.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.json"
HEX12 = re.compile(r"[0-9a-f]{12}")
PACKAGE_SUBDIRS = ("references", "scripts")


def recipe_version(name: str, files: list[str]) -> str:
    h = hashlib.sha256()
    h.update((name + "\n").encode("utf-8"))
    for rel in files:
        digest = hashlib.sha256((ROOT / name / rel).read_bytes()).hexdigest()
        h.update((rel + " " + digest + "\n").encode("utf-8"))
    h.update(b"\n")
    return h.hexdigest()[:12]


def package_files(directory: Path) -> set[str]:
    found: set[str] = set()
    for sub in PACKAGE_SUBDIRS:
        subpath = directory / sub
        if subpath.is_dir():
            for child in sorted(subpath.iterdir()):
                if child.is_file() and not child.name.startswith("."):
                    found.add(f"{sub}/{child.name}")
    if (directory / "SKILL.md").is_file():
        found.add("SKILL.md")
    return found


def main() -> int:
    if not INDEX.is_file():
        print("FAIL\n- index.json mancante")
        return 1
    try:
        catalog = json.loads(INDEX.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        print(f"FAIL\n- index.json non è JSON valido: {exc}")
        return 1
    entries = catalog.get("skills")
    if not isinstance(entries, list):
        print("FAIL\n- index.json non contiene una lista 'skills'")
        return 1

    errors: list[str] = []
    notes: list[str] = []

    directories = sorted(
        p.name for p in ROOT.iterdir()
        if p.is_dir() and p.name.startswith("eu-funding-")
    )
    listed = [entry.get("name") for entry in entries]

    for name in directories:
        if name not in listed:
            errors.append(f"Directory '{name}' assente da index.json")
    for name in listed:
        if name not in directories:
            errors.append(f"Voce index.json '{name}' senza directory corrispondente")

    for entry in entries:
        name = entry.get("name")
        files = entry.get("files")
        version = entry.get("version")
        location = f"'{name}'"
        if not isinstance(name, str) or name not in directories:
            notes.append("voce non validabile (name o directory mancante)")
            continue
        if not isinstance(files, list) or not files:
            errors.append(f"{location}: campo 'files' mancante o vuoto")
        else:
            present = package_files(ROOT / name)
            listed_files: set[str] = set()
            for rel in files:
                if isinstance(rel, str) and rel and not rel.startswith("/") \
                        and ".." not in Path(rel).parts:
                    listed_files.add(rel)
                    if not (ROOT / name / rel).is_file():
                        errors.append(f"{location}: file elencato ma inesistente '{rel}'")
                else:
                    errors.append(f"{location}: percorso non valido {rel!r}")
            for extra in sorted(present - listed_files):
                errors.append(f"{location}: file presente ma assente dal catalogo '{extra}'")
        if not isinstance(version, str) or not HEX12.fullmatch(version):
            errors.append(f"{location}: versione non conforme (12 esadecimali): {version!r}")
        elif isinstance(files, list) and files and recipe_version(name, files) != version:
            notes.append(
                f"{location}: versione legacy (anteriore alla ricetta di check_index.py); "
                "aggiornare alla prossima modifica della skill"
            )

    if "--print-recipe" in sys.argv:
        for entry in entries:
            name, files = entry.get("name"), entry.get("files")
            if isinstance(name, str) and isinstance(files, list) and (ROOT / name).is_dir():
                print(f"{name}: {recipe_version(name, files)}")
        return 0

    if errors:
        print("FAIL\n" + "\n".join(f"- {x}" for x in errors))
        for note in notes:
            print(f"  (nota) {note}")
        return 1
    for note in notes:
        print(f"(nota) {note}")
    print(f"PASS: catalogo congruente con {len(directories)} skill (file e formati verificate, non contenuti)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
