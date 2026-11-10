#!/usr/bin/env python3
"""Controlla la coerenza documentale di un manifest di bozza. NON valuta il bando."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REQUIREMENT_KINDS = {"OBBLIGATORIO", "CONDIZIONALE", "FACOLTATIVO", "NON_VERIFICATO"}
COVERAGE = {"COPERTO_DA_TESTO", "DA_INTEGRARE", "DA_CONFERMARE", "NON_APPLICABILE"}
CLAIM_STATES = {"VERIFICATA_DA_DOCUMENTO", "DICHIARAZIONE_UTENTE_DA_CONFERMARE", "PROPOSTA", "STIMA_NON_VALIDATA", "SEGNAPOSTO"}


def _nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def _table(rows, prefix, errors):
    if not isinstance(rows, list):
        errors.append(f"{prefix}: deve essere un elenco")
        return {}
    found = {}
    for i, row in enumerate(rows):
        if not isinstance(row, dict):
            errors.append(f"{prefix}[{i}]: elemento non oggetto")
            continue
        ident = row.get("id")
        if not _nonempty(ident):
            errors.append(f"{prefix}[{i}]: id mancante")
        elif ident in found:
            errors.append(f"{prefix}[{i}]: id duplicato {ident}")
        else:
            found[ident] = row
    return found


def validate(data):
    """Return (errors, warnings) without making any legal judgement."""
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["manifest: deve essere un oggetto JSON"], warnings
    opportunity = data.get("opportunity")
    if not isinstance(opportunity, dict):
        errors.append("opportunity: oggetto mancante")
        opportunity = {}
    for field in ("identifier", "official_url", "phase", "as_of"):
        if not _nonempty(opportunity.get(field)):
            errors.append(f"opportunity.{field}: mancante")
    if _nonempty(opportunity.get("official_url")) and not opportunity["official_url"].startswith("https://"):
        warnings.append("opportunity.official_url: verificare URL primario HTTPS")

    srcs = _table(data.get("sources"), "sources", errors)
    secs = _table(data.get("sections"), "sections", errors)
    reqs = _table(data.get("requirements"), "requirements", errors)
    claims = _table(data.get("claims", []), "claims", errors)
    if not srcs:
        errors.append("sources: nessuna fonte registrata")
    if not reqs:
        errors.append("requirements: nessun requisito mappato")

    for sid, src in srcs.items():
        if not _nonempty(src.get("title")) or not _nonempty(src.get("locator")):
            errors.append(f"sources.{sid}: title/locator mancanti")
        if src.get("official") not in (True, False) or src.get("verified") not in (True, False):
            errors.append(f"sources.{sid}: official/verified devono essere booleani")
        if src.get("verified") is False:
            warnings.append(f"sources.{sid}: fonte non verificata")

    for sec_id, sec in secs.items():
        if not _nonempty(sec.get("official_label")):
            errors.append(f"sections.{sec_id}: denominazione ufficiale mancante")
        src_id = sec.get("source_id")
        if src_id not in srcs:
            errors.append(f"sections.{sec_id}: source_id inesistente")
        elif srcs[src_id].get("official") is not True or srcs[src_id].get("verified") is not True:
            errors.append(f"sections.{sec_id}: formulario non sostenuto da fonte ufficiale verificata")
        if sec.get("coverage") not in COVERAGE:
            errors.append(f"sections.{sec_id}: coverage non valido")
        if sec.get("coverage") == "COPERTO_DA_TESTO" and not _nonempty(sec.get("text")):
            errors.append(f"sections.{sec_id}: coverage coperto senza testo")

    for req_id, req in reqs.items():
        kind = req.get("kind")
        if kind not in REQUIREMENT_KINDS:
            errors.append(f"requirements.{req_id}: kind non valido")
        if req.get("coverage") not in COVERAGE:
            errors.append(f"requirements.{req_id}: coverage non valido")
        src_id = req.get("source_id")
        if src_id not in srcs:
            errors.append(f"requirements.{req_id}: source_id inesistente")
        elif kind != "NON_VERIFICATO" and (srcs[src_id].get("official") is not True or srcs[src_id].get("verified") is not True):
            errors.append(f"requirements.{req_id}: requisito senza fonte ufficiale verificata")
        if not _nonempty(req.get("locator")):
            errors.append(f"requirements.{req_id}: locator mancante")
        linked = req.get("section_ids")
        if not isinstance(linked, list):
            errors.append(f"requirements.{req_id}: section_ids deve essere un elenco")
        else:
            for section_id in linked:
                if section_id not in secs:
                    errors.append(f"requirements.{req_id}: sezione inesistente {section_id}")
            if not linked and kind == "OBBLIGATORIO":
                warnings.append(f"requirements.{req_id}: obbligo senza sezione collegata")
        if kind == "OBBLIGATORIO" and req.get("coverage") != "COPERTO_DA_TESTO":
            warnings.append(f"requirements.{req_id}: obbligo non coperto da testo")
        if kind == "OBBLIGATORIO" and req.get("coverage") == "NON_APPLICABILE" and not _nonempty(req.get("justification")):
            errors.append(f"requirements.{req_id}: non applicabilità senza motivazione")

    for claim_id, claim in claims.items():
        section_id = claim.get("section_id")
        if section_id not in secs:
            errors.append(f"claims.{claim_id}: section_id inesistente")
        state = claim.get("state")
        if state not in CLAIM_STATES:
            errors.append(f"claims.{claim_id}: state non valido")
        if not _nonempty(claim.get("text")):
            errors.append(f"claims.{claim_id}: testo mancante")
        if state == "VERIFICATA_DA_DOCUMENTO" and not _nonempty(claim.get("evidence_ref")):
            errors.append(f"claims.{claim_id}: affermazione verificata senza evidenza")
        if state in {"PROPOSTA", "STIMA_NON_VALIDATA", "SEGNAPOSTO", "DICHIARAZIONE_UTENTE_DA_CONFERMARE"}:
            warnings.append(f"claims.{claim_id}: affermazione non verificata come fatto")

    submission = data.get("submission", {})
    if not isinstance(submission, dict):
        errors.append("submission: deve essere un oggetto")
    elif submission.get("performed") is not False:
        errors.append("submission.performed: deve essere esplicitamente false; invio non attestabile da questa skill")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validatore statico del manifest di una bozza UE")
    parser.add_argument("manifest", type=Path)
    args = parser.parse_args()
    try:
        payload = json.loads(args.manifest.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    errors, warnings = validate(payload)
    print(json.dumps({"status": "FORMAL_ERRORS" if errors else "FORMAL_CHECK_PASSED", "errors": errors, "warnings": warnings,
        "note": "Solo coerenza formale, NON controllo giuridico, non revisione di merito, non invio."}, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
