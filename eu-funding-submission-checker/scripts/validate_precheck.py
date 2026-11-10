#!/usr/bin/env python3
"""Valida SOLO la struttura del report pre-invio; non verifica né invia candidature."""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

STATUSES = {
    "PRECHECK_COMPLETO_SENZA_BLOCCHI_DOCUMENTATI", "PRECHECK_CON_BLOCCHI",
    "PRECHECK_PARZIALE", "BLOCCATO_DA_FONTI", "NON_APPLICABILE",
}
CHECK_STATUSES = {"VERIFICATO", "BLOCCO_ACCERTATO", "DA_VERIFICARE", "NON_APPLICABILE"}
CATEGORIES = {
    "SCADENZA_FASE", "CANALE_MODALITA", "FORMULARIO_ALLEGATI", "FORMATO_LIMITI",
    "DICHIARAZIONI_FIRME", "SOGGETTI_RUOLI", "COERENZA_VERSIONI",
    "VALIDAZIONE_SISTEMA", "ALTRO",
}
MODES = {"DIRETTA", "CONCORRENTE", "INDIRETTA", "DA_VERIFICARE"}
FORBIDDEN_CERTIFICATIONS = {"approval_probability", "predicted_score", "official_score", "success_probability", "submission_confirmation"}
SHA256 = re.compile(r"^[0-9a-fA-F]{64}$")


def present(value):
    return isinstance(value, str) and bool(value.strip())


def objects(data, key, errors):
    items = data.get(key)
    if not isinstance(items, list):
        errors.append(f"{key}: deve essere una lista")
        return {}
    by_id = {}
    for i, item in enumerate(items):
        if not isinstance(item, dict):
            errors.append(f"{key}[{i}]: atteso oggetto")
            continue
        ident = item.get("id")
        if not present(ident):
            errors.append(f"{key}[{i}]: id mancante")
        elif ident in by_id:
            errors.append(f"{key}[{i}]: id duplicato: {ident}")
        else:
            by_id[ident] = item
    return by_id


def forbidden_keys(node, path, errors):
    if isinstance(node, dict):
        for key, value in node.items():
            if key.lower() in FORBIDDEN_CERTIFICATIONS:
                errors.append(f"{path}.{key}: campo di falsa certificazione/esito non ammesso")
            forbidden_keys(value, f"{path}.{key}", errors)
    elif isinstance(node, list):
        for i, value in enumerate(node):
            forbidden_keys(value, f"{path}[{i}]", errors)


def aware_timestamp(value):
    if not present(value):
        return False
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return dt.tzinfo is not None and dt.utcoffset() is not None
    except ValueError:
        return False


def validate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["manifest: atteso oggetto JSON"], warnings
    forbidden_keys(data, "manifest", errors)

    summary = data.get("precheck")
    if not isinstance(summary, dict):
        errors.append("precheck: oggetto mancante")
        summary = {}
    status = summary.get("status")
    if status not in STATUSES:
        errors.append("precheck.status: valore non valido")
    if not present(summary.get("scope")):
        errors.append("precheck.scope: perimetro reale mancante")
    if not aware_timestamp(summary.get("as_of")):
        errors.append("precheck.as_of: richiesta data/ora ISO 8601 con fuso")

    opportunity = data.get("opportunity")
    if not isinstance(opportunity, dict):
        errors.append("opportunity: oggetto mancante")
        opportunity = {}
    for key in ("identifier", "phase"):
        if not present(opportunity.get(key)):
            errors.append(f"opportunity.{key}: mancante")
    mode = opportunity.get("management_mode")
    if mode not in MODES:
        errors.append("opportunity.management_mode: valore non valido")
    url = opportunity.get("official_url")
    if not present(url) and status not in {"BLOCCATO_DA_FONTI", "NON_APPLICABILE"}:
        errors.append("opportunity.official_url: mancante")
    elif present(url) and not url.startswith("https://"):
        warnings.append("opportunity.official_url: usare preferibilmente URL HTTPS ufficiale")
    if mode == "DA_VERIFICARE" and status == "PRECHECK_COMPLETO_SENZA_BLOCCHI_DOCUMENTATI":
        warnings.append("opportunity.management_mode: non verificata; documentare se incide sul canale")

    package = data.get("package")
    if not isinstance(package, dict):
        errors.append("package: oggetto mancante")
        package = {}
    if status != "NON_APPLICABILE":
        for key in ("reference", "version"):
            if not present(package.get(key)):
                errors.append(f"package.{key}: mancante")
    files = objects(package, "files", errors) if "files" in package else {}
    if "files" not in package:
        errors.append("package.files: elenco mancante")
    for fid, f in files.items():
        if not present(f.get("name")) or not present(f.get("version")):
            errors.append(f"package.files.{fid}: name e version obbligatori")
        sha = f.get("sha256")
        if sha is not None and (not isinstance(sha, str) or not SHA256.fullmatch(sha)):
            errors.append(f"package.files.{fid}: sha256 non valido")

    sources = objects(data, "sources", errors)
    checks = objects(data, "checks", errors)
    for sid, source in sources.items():
        for key in ("title", "locator", "version"):
            if not present(source.get(key)):
                errors.append(f"sources.{sid}: {key} mancante")
        for key in ("official", "verified"):
            if type(source.get(key)) is not bool:
                errors.append(f"sources.{sid}: {key} deve essere booleano")
        if source.get("verified") is True and not present(source.get("url")):
            errors.append(f"sources.{sid}: fonte verificata senza URL/file identificabile")
        if source.get("verified") is False:
            warnings.append(f"sources.{sid}: fonte non verificata")

    for cid, check in checks.items():
        cstatus = check.get("status")
        if cstatus not in CHECK_STATUSES:
            errors.append(f"checks.{cid}: status non valido")
        if check.get("category") not in CATEGORIES:
            errors.append(f"checks.{cid}: category non valida")
        if not present(check.get("description")):
            errors.append(f"checks.{cid}: description mancante")
        sid = check.get("source_id")
        if sid is not None and sid not in sources:
            errors.append(f"checks.{cid}: source_id inesistente")
        if cstatus in {"VERIFICATO", "BLOCCO_ACCERTATO"}:
            if sid not in sources or sources[sid].get("official") is not True or sources[sid].get("verified") is not True:
                errors.append(f"checks.{cid}: {cstatus} richiede fonte ufficiale verificata")
            if not present(check.get("source_locator")):
                errors.append(f"checks.{cid}: source_locator mancante")
            if not present(check.get("item_ref")):
                errors.append(f"checks.{cid}: item_ref mancante")
            if not present(check.get("evidence")):
                errors.append(f"checks.{cid}: {cstatus} senza evidenza osservata")
        if cstatus == "BLOCCO_ACCERTATO" and not present(check.get("recommended_fix")):
            errors.append(f"checks.{cid}: recommended_fix mancante; indicare correzione proposta")
        if cstatus == "DA_VERIFICARE" and not present(check.get("reason")):
            errors.append(f"checks.{cid}: DA_VERIFICARE senza motivazione")
        if cstatus == "NON_APPLICABILE" and not present(check.get("justification")):
            errors.append(f"checks.{cid}: NON_APPLICABILE senza giustificazione")
        if isinstance(check.get("item_ref"), str) and check["item_ref"].startswith("FILE-") and check["item_ref"] not in files:
            errors.append(f"checks.{cid}: file {check['item_ref']} non trovato nel pacchetto")

    deadline = data.get("deadline")
    if deadline is not None:
        if not isinstance(deadline, dict):
            errors.append("deadline: deve essere oggetto")
        else:
            if not present(deadline.get("literal")):
                errors.append("deadline.literal: testo originale mancante")
            if deadline.get("source_id") not in sources:
                errors.append("deadline.source_id: fonte inesistente")
            if not present(deadline.get("source_locator")):
                errors.append("deadline.source_locator: indicare punto della fonte")
            if not present(deadline.get("phase")):
                errors.append("deadline.phase: mancante")
            if type(deadline.get("timezone_verified")) is not bool:
                errors.append("deadline.timezone_verified: deve essere booleano")
            if deadline.get("timezone_verified") is False:
                warnings.append("deadline: fuso non verificato; vietato dedurre scadenza superata")
                if (status == "PRECHECK_COMPLETO_SENZA_BLOCCHI_DOCUMENTATI"
                    and re.search(r"\b[0-2]?\d:[0-5]\d\b", str(deadline.get("literal", "")))):
                    errors.append("precheck.status: completo con ora di scadenza e fuso non verificato")
            if deadline.get("timezone_verified") is True:
                source = sources.get(deadline.get("source_id"), {})
                if source.get("official") is not True or source.get("verified") is not True:
                    errors.append("deadline.timezone_verified: richiede fonte ufficiale verificata")
            if deadline.get("calculated_instant") is not None:
                if deadline.get("timezone_verified") is not True:
                    errors.append("deadline.calculated_instant: conversione vietata senza fuso verificato")
                if not aware_timestamp(deadline.get("calculated_instant")):
                    errors.append("deadline.calculated_instant: formato ISO 8601 con fuso richiesto")

    submission = data.get("submission")
    if not isinstance(submission, dict):
        errors.append("submission: oggetto mancante")
    else:
        for key in ("performed", "receipt_verified", "portal_mutations_performed"):
            if submission.get(key) is not False:
                errors.append(f"submission.{key}: deve essere esplicitamente false")

    if status == "PRECHECK_COMPLETO_SENZA_BLOCCHI_DOCUMENTATI":
        if not checks:
            errors.append("precheck.status: completo ma senza controlli")
        if any(c.get("status") in {"BLOCCO_ACCERTATO", "DA_VERIFICARE"} for c in checks.values()):
            errors.append("precheck.status: completo incompatibile con blocchi o controlli aperti")
        if not any(s.get("official") is True and s.get("verified") is True for s in sources.values()):
            errors.append("precheck.status: completo senza fonti ufficiali verificate")
        if present(summary.get("limitations")):
            warnings.append("precheck.status: completo con limitazioni; verificare che il perimetro sia davvero sufficiente")
    if status == "PRECHECK_CON_BLOCCHI" and not any(c.get("status") == "BLOCCO_ACCERTATO" for c in checks.values()):
        errors.append("precheck.status: blocchi dichiarati ma non documentati nei checks")
    if status == "PRECHECK_PARZIALE" and any(c.get("status") == "BLOCCO_ACCERTATO" for c in checks.values()):
        errors.append("precheck.status: parziale con blocco accertato; usare PRECHECK_CON_BLOCCHI e segnalare le altre lacune")
    if status == "PRECHECK_PARZIALE" and not (present(summary.get("limitations")) or any(c.get("status") == "DA_VERIFICARE" for c in checks.values())):
        errors.append("precheck.status: parziale senza lacune o limiti dichiarati")
    if status in {"BLOCCATO_DA_FONTI", "NON_APPLICABILE"} and not present(summary.get("limitations")):
        errors.append(f"precheck.limitations: richiesto per {status}")
    if status == "BLOCCATO_DA_FONTI" and any(c.get("status") in {"VERIFICATO", "BLOCCO_ACCERTATO"} for c in checks.values()):
        warnings.append("precheck.status: blocco fonti con controlli conclusi; definire perimetro verificato")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Controllo formale del pre-check: non presenta candidature")
    parser.add_argument("manifest_json", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    errors, warnings = validate(data)
    print(json.dumps({"status": "FORMAL_ERRORS" if errors else "FORMAL_CHECK_PASSED", "errors": errors,
                      "warnings": warnings, "note": "Solo struttura e rinvii: non verifica reale compliance, scadenze, portale o ricevute."}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
