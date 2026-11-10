#!/usr/bin/env python3
"""Installa le EU Funding Skills in una directory di skill per agenti.

Ogni skill è una cartella con `SKILL.md` (standard Agent Skills), quindi la
stessa installazione funziona con Claude Code, OpenCode e gli altri client
compatibili. Lo script copia o collega le cartelle `eu-funding-*`, non tocca la
configurazione dei client e non richiede dipendenze esterne.

Esempi:
    python3 install.py --list
    python3 install.py claude
    python3 install.py opencode --link
    python3 install.py ~/.agents/skills --dry-run
    python3 install.py claude --uninstall
"""
from __future__ import annotations

import argparse
import filecmp
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IGNORE = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def skill_dirs() -> list[Path]:
    """Cartelle di primo livello che contengono una SKILL.md."""
    return sorted(
        p for p in ROOT.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()
    )


def presets() -> dict[str, Path]:
    """Destinazioni note, con i percorsi documentati dai rispettivi client."""
    config = Path(os.environ.get("XDG_CONFIG_HOME") or Path.home() / ".config")
    return {
        "claude": Path.home() / ".claude" / "skills",
        "claude-project": Path.cwd() / ".claude" / "skills",
        "opencode": config / "opencode" / "skills",
        "opencode-project": Path.cwd() / ".opencode" / "skills",
        "agents": Path.home() / ".agents" / "skills",
        "agents-project": Path.cwd() / ".agents" / "skills",
    }


def _files(root: Path) -> dict[str, Path]:
    """File della cartella, esclusi artefatti locali (cache, .DS_Store)."""
    found: dict[str, Path] = {}
    for path in root.rglob("*"):
        rel = path.relative_to(root)
        if any(part in {"__pycache__", ".DS_Store"} for part in rel.parts):
            continue
        if path.suffix == ".pyc" or not path.is_file():
            continue
        found[str(rel)] = path
    return found


def same_tree(left: Path, right: Path) -> bool:
    """True se le due cartelle hanno lo stesso contenuto (confronto byte a byte)."""
    a, b = _files(left), _files(right)
    if a.keys() != b.keys():
        return False
    return all(filecmp.cmp(a[name], b[name], shallow=False) for name in a)


def remove(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    else:
        shutil.rmtree(path)


def install_one(
    src: Path, target: Path, link: bool, force: bool, dry_run: bool = False
) -> str:
    dest = target / src.name
    if dest.is_symlink():
        if dest.resolve() == src.resolve():
            return "già installata (collegamento)"
        if not force:
            return "saltata: collegamento diverso già presente (usa --force)"
        if dry_run:
            return "sostituirebbe il collegamento"
        remove(dest)
    elif dest.exists():
        if dest.is_dir() and same_tree(src, dest):
            return "già installata (identica)"
        if not force:
            return "saltata: versione diversa già presente (usa --force)"
        if dry_run:
            return "sovrascriverebbe la versione presente"
        remove(dest)

    if dry_run:
        return "collegherebbe" if link else "copierebbe"

    target.mkdir(parents=True, exist_ok=True)
    if link:
        try:
            dest.symlink_to(src, target_is_directory=True)
            return "collegata"
        except OSError as exc:
            print(f"  avviso: symlink non disponibile ({exc}); copio i file")
    shutil.copytree(src, dest, ignore=IGNORE)
    return "copiata"


def uninstall_one(src: Path, target: Path) -> str:
    dest = target / src.name
    if not (dest.exists() or dest.is_symlink()):
        return "non presente"
    if dest.is_symlink():
        remove(dest)
        return "rimossa (collegamento)"
    if not (dest / "SKILL.md").is_file():
        return "saltata: non sembra una skill installata"
    remove(dest)
    return "rimossa"


def verify() -> bool:
    """Esegue i controlli statici locali delle skill."""
    ok = True
    for src in skill_dirs():
        script = src / "scripts" / "check_skill.py"
        if not script.is_file():
            continue
        result = subprocess.run(
            [sys.executable, str(script)], capture_output=True, text=True
        )
        status = "OK" if result.returncode == 0 else "FAIL"
        print(f"  {status}  {src.name}")
        ok = ok and result.returncode == 0
    return ok


def print_list() -> None:
    print("Skill disponibili:")
    for src in skill_dirs():
        print(f"  {src.name}")
    print("\nDestinazioni predefinite:")
    for name, path in presets().items():
        print(f"  {name:<18} {path}")
    print("\nQualsiasi altro percorso può essere passato al posto del nome.")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="install.py",
        description="Installa le EU Funding Skills in una directory di skill.",
    )
    parser.add_argument("target", nargs="?", help="nome predefinito o percorso")
    parser.add_argument("--link", action="store_true", help="collega invece di copiare")
    parser.add_argument("--force", action="store_true", help="sovrascrive versioni diverse")
    parser.add_argument("--dry-run", action="store_true", help="mostra senza modificare")
    parser.add_argument("--uninstall", action="store_true", help="rimuove le skill installate")
    parser.add_argument("--list", action="store_true", help="elenca skill e destinazioni")
    parser.add_argument("--verify", action="store_true", help="esegue i controlli statici")
    args = parser.parse_args(argv)

    if args.list:
        print_list()
        return 0

    if not args.target:
        parser.print_help()
        print("\nDestinazioni predefinite:")
        for name, path in presets().items():
            print(f"  {name:<18} {path}")
        return 2

    known = presets()
    target = known.get(args.target)
    if target is None:
        target = Path(args.target).expanduser().resolve()
        if target.exists() and not target.is_dir():
            print(f"Errore: {target} non è una directory", file=sys.stderr)
            return 2

    skills = skill_dirs()
    if not skills:
        print("Errore: nessuna skill trovata accanto a install.py", file=sys.stderr)
        return 2

    if args.verify and not verify():
        print("Controlli statici falliti: installazione interrotta", file=sys.stderr)
        return 1

    if args.uninstall:
        print(f"Disinstallazione da {target}")
        results = [uninstall_one(src, target) for src in skills]
    else:
        action = "Collegamento" if args.link else "Copia"
        suffix = " (dry-run, nessuna modifica)" if args.dry_run else ""
        print(f"{action} di {len(skills)} skill in {target}{suffix}")
        if not args.dry_run:
            target.mkdir(parents=True, exist_ok=True)
        results = [
            install_one(src, target, args.link, args.force, args.dry_run)
            for src in skills
        ]

    failed = False
    for src, result in zip(skills, results):
        print(f"  {src.name:<38} {result}")
        failed = failed or result.startswith("saltata")

    if args.dry_run:
        print("\nNessuna modifica effettuata.")
    elif not args.uninstall:
        print(
            "\nFatto. Claude Code: le skill compaiono in /skills e si invocano con "
            "/<nome>. OpenCode: si caricano con @<nome>. Se non appaiono, ricarica "
            "la sessione (/reload in OpenCode, /reload-skills in Claude Code quando "
            "la directory di skill è stata creata a sessione avviata)."
        )
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
