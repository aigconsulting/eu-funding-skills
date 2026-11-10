#!/usr/bin/env python3
"""Validazione deterministica di un dossier condiviso (senza dipendenze).

Controlla le invarianti del formato `eu-funding-skills/dossier@v1`:
- campi obbligatori di primo livello e date ISO;
- stati ammessi per ogni elemento e completezza di `fonte`/`verificato_il`
  quando lo stato è VERIFICATO (o di `approvato_il` per DECISIONE_APPROVATA);
- integrità dei riferimenti: ogni `fonte` deve puntare a un id `SRC-*`
  esistente in `evidenze`;
- stale-check: elementi `VERIFICATO` con `verificato_il` anteriore alla
  `ultima_verifica` dell'opportunità sono AVVISI "da riesaminare" —
  una rettifica del bando NON conferma automaticamente i dati precedenti;
- esistenza dell'identificativo dell'opportunità (call/topic/avviso).

Uso: python3 dossier/check_dossier.py <dossier.json> [--warn-as-error]
Uscita: PASS/WARN/FAIL con righe dettagliate. NON valida la veridicità
dei dati di bando né il comportamento agentico.
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path

SCHEMA_TAG = "eu-funding-skills/dossier@v1"
STATI = {
    "VERIFICATO", "DA_CONFERMARE", "IPOTESI", "PROPOSTA",
    "DECISIONE_APPROVATA", "MANCANTE", "NON_APPLICABILE",
}
DATE_FMT = re.compile(r"\A\d{4}-\d{2}-\d{2}\Z")


def is_iso_date(value: str) -> bool:
    if not DATE_FMT.fullmatch(value or ""):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def check(dossier: dict) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []

    for f in ("schema", "dossier_id", "created", "updated", "opportunita", "evidenze", "requisiti", "revisioni"):
        if f not in dossier:
            errors.append(f"Campo obbligatorio mancante: {f}")
    if dossier.get("schema") != SCHEMA_TAG:
        errors.append(f"schema non conforme: atteso {SCHEMA_TAG}, trovato {dossier.get('schema')!r}")
    for f in ("created", "updated"):
        v = dossier.get(f)
        if v and not is_iso_date(v):
            errors.append(f"{f} non è una data ISO: {v!r}")

    opp = dossier.get("opportunita", {})
    if not any(opp.get(x) for x in ("call_id", "topic_id", "avviso_id")):
        errors.append("opportunita senza call_id/topic_id/avviso_id")
    if opp.get("ciclo_QFP") is None:
        warnings.append("ciclo_QFP assente: indicarlo quando noto")
    if not is_iso_date(opp.get("ultima_verifica", "")):
        errors.append("opportunita.ultima_verifica mancante o non ISO")

    src_ids = {e.get("id") for e in dossier.get("evidenze", [])}
    if not src_ids:
        errors.append("evidenze vuota: requisiti e fatti VERIFICATO stabiliscono fonte obbligatoria")

    def walk_items(container, prefix):
        if isinstance(container, dict):
            for key, value in container.items():
                if key == "indicatori":
                    yield from walk_items(value, f"{prefix}.indicatori")
                elif isinstance(value, (dict, list)):
                    yield from walk_items(value, f"{prefix}.{key}")
                elif key == "testo":
                    yield prefix, container
        elif isinstance(container, list):
            for i, element in enumerate(container):
                if isinstance(element, dict) and "testo" in element:
                    yield f"{prefix}[{i}]", element

    for location, item in walk_items(dossier.get("progetto", {}), "progetto"):
        _check_item(item, location, errors, warnings, src_ids, opp)
    decls = (dossier.get("proponente", {}).get("dichiarazioni") or [])
    for i, item in enumerate(decls):
        _check_item(item, f"proponente.dichiarazioni[{i}]", errors, warnings, src_ids, opp)
    partners = (dossier.get("partenariato") or [])
    for i, partner in enumerate(partners):
        st = partner.get("stato")
        if st and st not in STATI:
            errors.append(f"partenariato[{i}].stato non ammesso: {st!r}")

    reqs = dossier.get("requisiti", [])
    for i, req in enumerate(reqs):
        if not req.get("id"):
            errors.append(f"requisiti[{i}] senza id")
        src = req.get("fonte")
        if src and src not in src_ids:
            errors.append(f"requisiti[{i}] riferimento fonte inesistente: {src}")
        st = req.get("stato")
        if st and st not in STATI:
            errors.append(f"requisiti[{i}].stato non ammesso: {st!r}")

    for i, rev in enumerate(dossier.get("revisioni", [])):
        if not is_iso_date(rev.get("data", "")):
            errors.append(f"revisioni[{i}].data mancante o non ISO")
        if not rev.get("descrizione"):
            errors.append(f"revisioni[{i}] senza descrizione")

    finanza = dossier.get("finanza") or {}
    if finanza and not finanza.get("valuta"):
        errors.append("finanza.valuta mancante")

    ultima = opp.get("ultima_verifica")
    if is_iso_date(ultima):
        for i, ev in enumerate(dossier.get("evidenze", [])):
            cons = ev.get("data_consultazione", "")
            if is_iso_date(cons) and cons < ultima:
                warnings.append(
                    f"evidenze[{i}] ({ev.get('id')}) consultata il {cons} ma ultima_verifica "
                    f"{ultima}: da riesaminare — la rettifica NON conferma i dati che si appoggiano a questa fonte"
                )

    return errors, warnings


def _check_item(item, location, errors, warnings, src_ids, opp):
    st = item.get("stato")
    if st not in STATI:
        errors.append(f"{location}.stato non ammesso: {st!r}")
        return
    fonte = item.get("fonte")
    if fonte and fonte not in src_ids:
        errors.append(f"{location} riferimento fonte inesistente: {fonte}")
    if st == "VERIFICATO":
        if not fonte:
            errors.append(f"{location} VERIFICATO senza fonte")
        if not is_iso_date(item.get("verificato_il", "")):
            errors.append(f"{location} VERIFICATO senza verificato_il ISO")
        else:
            ultima = opp.get("ultima_verifica")
            if is_iso_date(ultima) and item["verificato_il"] < ultima:
                warnings.append(
                    f"{location} verificato il {item['verificato_il']} ma ultima_verifica opportun."
                    f" {ultima}: da riesaminare (nessuna conferma automatica dopo rettifiche)"
                )
    if st == "DECISIONE_APPROVATA" and not is_iso_date(item.get("approvato_il", "")):
        errors.append(f"{location} DECISIONE_APPROVATA senza approvato_il ISO")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"FAIL\n- file non trovato: {path}")
        return 1
    try:
        dossier = load(path)
    except json.JSONDecodeError as exc:
        print(f"FAIL\n- JSON non valido: {exc}")
        return 1

    errors, warnings = check(dossier)
    warn_as_error = "--warn-as-error" in sys.argv

    if errors:
        print("FAIL\n" + "\n".join(f"- {e}" for e in errors))
        for w in warnings:
            print(f"  (warn) {w}")
        return 1
    if warnings and warn_as_error:
        print("FAIL\n" + "\n".join(f"- {w}" for w in warnings))
        return 1
    if warnings:
        print("WARN")
        for w in warnings:
            print(f"- {w}")
        return 0
    print(f"PASS: dossier coerente con {SCHEMA_TAG} (nessuna verifica di veridicità dei dati)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
