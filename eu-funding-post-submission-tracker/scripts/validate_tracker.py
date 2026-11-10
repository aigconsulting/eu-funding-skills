#!/usr/bin/env python3
"""Valida solo il manifest locale della Skill 10. Non accede a portali, inbox o autorità."""
from __future__ import annotations

import argparse
import json
import re
from datetime import datetime
from pathlib import Path

STATUSES = {"AGGIORNATO_CON_EVIDENZE", "NESSUN_NUOVO_EVENTO_DOCUMENTATO", "MONITORAGGIO_PARZIALE", "BLOCCATO_DA_FONTI", "NON_APPLICABILE"}
MODES = {"DIRETTA", "CONCORRENTE", "INDIRETTA", "DA_VERIFICARE"}
VERIFICATIONS = {"VERIFICATO", "DA_VERIFICARE", "CONFLITTO_FONTI"}
KINDS = {
    "PRESENTAZIONE_CONFERMATA", "CAMBIO_STATO_PORTALE", "RICHIESTA_CHIARIMENTI",
    "RICHIESTA_INTEGRAZIONE", "INVITO_COLLOQUIO", "NOTIFICA_ESITO",
    "INVITO_ACCORDO", "ACCORDO_FIRMATO", "RISPOSTA_PRESENTATA",
    "ALTRO_ATTO_ESEGUITO", "COMUNICAZIONE_GENERICA", "RIESAME_O_RICORSO",
    "PAGAMENTO_DOCUMENTATO",
}
FORMAL_KINDS = {"PRESENTAZIONE_CONFERMATA", "RICHIESTA_CHIARIMENTI", "RICHIESTA_INTEGRAZIONE", "NOTIFICA_ESITO", "INVITO_ACCORDO", "ACCORDO_FIRMATO", "PAGAMENTO_DOCUMENTATO"}
ACTION_BASES = {"OBBLIGO_DOCUMENTATO", "RACCOMANDAZIONE_INTERNA", "DA_VERIFICARE"}
ACTION_STATES = {"PROPOSTA", "APPROVATA", "ESEGUITA", "DA_VERIFICARE"}
FORBIDDEN_KEYS = {"approval_probability", "success_probability", "automatic_submission", "official_certification", "auto_submission", "auto_monitoring"}
_TIME = re.compile(r"\b(?:[01]?\d|2[0-3]):[0-5]\d\b")


def nonempty(v):
    return isinstance(v, str) and bool(v.strip())


def parsed_time(v):
    if not nonempty(v):
        return None
    try:
        d = datetime.fromisoformat(v.replace("Z", "+00:00"))
        return d if d.tzinfo is not None and d.utcoffset() is not None else None
    except ValueError:
        return None


def group(data, field, errs):
    xs = data.get(field)
    if not isinstance(xs, list):
        errs.append(f"{field}: deve essere lista")
        return {}
    mapping = {}
    for i, item in enumerate(xs):
        if not isinstance(item, dict):
            errs.append(f"{field}[{i}]: atteso oggetto")
        elif not nonempty(item.get("id")):
            errs.append(f"{field}[{i}]: id mancante")
        elif item["id"] in mapping:
            errs.append(f"{field}[{i}]: id duplicato {item['id']}")
        else:
            mapping[item["id"]] = item
    return mapping


def no_claims(node, path, errors):
    if isinstance(node, dict):
        for k, v in node.items():
            if k.casefold() in FORBIDDEN_KEYS:
                errors.append(f"{path}.{k}: campo di pretesa o automatismo non ammesso")
            no_claims(v, f"{path}.{k}", errors)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            no_claims(v, f"{path}[{i}]", errors)


def validate(data):
    errs, warnings = [], []
    if not isinstance(data, dict):
        return ["manifest: atteso oggetto JSON"], warnings
    no_claims(data, "manifest", errs)
    tracking = data.get("tracking")
    if not isinstance(tracking, dict):
        errs.append("tracking: oggetto mancante")
        tracking = {}
    status = tracking.get("status")
    if status not in STATUSES:
        errs.append("tracking.status: valore non valido")
    if not nonempty(tracking.get("scope")):
        errs.append("tracking.scope: perimetro consultato mancante")
    asof = parsed_time(tracking.get("as_of"))
    since = parsed_time(tracking.get("since"))
    if asof is None:
        errs.append("tracking.as_of: ISO 8601 con fuso obbligatorio")
    if since is None:
        errs.append("tracking.since: ISO 8601 con fuso obbligatorio")
    if asof and since and since > asof:
        errs.append("tracking.since: successivo ad as_of")
    if status in {"MONITORAGGIO_PARZIALE", "BLOCCATO_DA_FONTI", "NON_APPLICABILE"} and not nonempty(tracking.get("limitations")):
        errs.append("tracking.limitations: motivazione necessaria")

    app = data.get("application")
    if not isinstance(app, dict):
        errs.append("application: oggetto mancante")
        app = {}
    if status != "NON_APPLICABILE":
        for key in ("reference", "call_or_notice", "authority", "phase"):
            if not nonempty(app.get(key)):
                errs.append(f"application.{key}: mancante")
    if app.get("management_mode") not in MODES:
        errs.append("application.management_mode: modalità non valida")

    sources = group(data, "sources", errs)
    events = group(data, "events", errs)
    deadlines = group(data, "deadlines", errs)
    actions = group(data, "next_steps", errs)

    for sid, src in sources.items():
        for field in ("title", "authority", "locator"):
            if not nonempty(src.get(field)):
                errs.append(f"sources.{sid}.{field}: mancante")
        if not (nonempty(src.get("url")) or nonempty(src.get("file_ref"))):
            errs.append(f"sources.{sid}: URL o riferimento file mancante")
        for b in ("official", "verified"):
            if type(src.get(b)) is not bool:
                errs.append(f"sources.{sid}.{b}: deve essere booleano")
        d = parsed_time(src.get("observed_at"))
        if d is None:
            errs.append(f"sources.{sid}.observed_at: ISO con fuso richiesto")
        elif asof and d > asof:
            errs.append(f"sources.{sid}.observed_at: futuro rispetto a tracking.as_of")
        if src.get("verified") is False:
            warnings.append(f"sources.{sid}: provenienza non verificata")

    for eid, ev in events.items():
        if ev.get("kind") not in KINDS:
            errs.append(f"events.{eid}.kind: non valido")
        if ev.get("verification") not in VERIFICATIONS:
            errs.append(f"events.{eid}.verification: non valida")
        if not nonempty(ev.get("description")):
            errs.append(f"events.{eid}.description: mancante")
        sid = ev.get("source_id")
        src = sources.get(sid)
        if not src:
            errs.append(f"events.{eid}.source_id: inesistente")
        if not nonempty(ev.get("source_locator")):
            errs.append(f"events.{eid}.source_locator: mancante")
        d = parsed_time(ev.get("observed_at"))
        if d is None:
            errs.append(f"events.{eid}.observed_at: ISO con fuso richiesto")
        elif asof and d > asof:
            errs.append(f"events.{eid}.observed_at: futuro rispetto a tracking.as_of")
        for opt in ("issued_at", "received_at", "effective_at"):
            if ev.get(opt) is not None and parsed_time(ev.get(opt)) is None:
                errs.append(f"events.{eid}.{opt}: ISO con fuso richiesto se presente")
        if ev.get("verification") == "VERIFICATO":
            if not src or src.get("verified") is not True:
                errs.append(f"events.{eid}: VERIFICATO richiede fonte verificata")
            if ev.get("kind") in FORMAL_KINDS and (not src or src.get("official") is not True):
                errs.append(f"events.{eid}: atto formale VERIFICATO richiede fonte ufficiale")
        else:
            if not nonempty(ev.get("uncertainty")):
                errs.append(f"events.{eid}.uncertainty: motivazione necessaria")

    for did, d in deadlines.items():
        if not nonempty(d.get("literal")) or not nonempty(d.get("phase")):
            errs.append(f"deadlines.{did}: literal e phase obbligatori")
        if d.get("status") not in VERIFICATIONS:
            errs.append(f"deadlines.{did}.status: non valido")
        if d.get("source_id") not in sources:
            errs.append(f"deadlines.{did}.source_id: inesistente")
        if not nonempty(d.get("source_locator")):
            errs.append(f"deadlines.{did}.source_locator: mancante")
        if d.get("event_id") is not None and d["event_id"] not in events:
            errs.append(f"deadlines.{did}.event_id: inesistente")
        if type(d.get("timezone_verified")) is not bool:
            errs.append(f"deadlines.{did}.timezone_verified: booleano obbligatorio")
        if d.get("instant") is not None:
            if not d.get("timezone_verified") or d.get("status") != "VERIFICATO":
                errs.append(f"deadlines.{did}.instant: conversione non autorizzata senza fuso e verifica")
            if parsed_time(d.get("instant")) is None:
                errs.append(f"deadlines.{did}.instant: ISO con fuso richiesto")
        if d.get("status") == "VERIFICATO":
            src = sources.get(d.get("source_id"), {})
            if src.get("verified") is not True or src.get("official") is not True:
                errs.append(f"deadlines.{did}: VERIFICATO richiede fonte ufficiale verificata")
            if _TIME.search(str(d.get("literal", ""))) and d.get("timezone_verified") is not True:
                errs.append(f"deadlines.{did}: ora presente, fuso non verificato")
        elif not nonempty(d.get("uncertainty")):
            errs.append(f"deadlines.{did}.uncertainty: motivazione necessaria")

    for aid, act in actions.items():
        if not nonempty(act.get("description")):
            errs.append(f"next_steps.{aid}.description: mancante")
        if act.get("basis") not in ACTION_BASES:
            errs.append(f"next_steps.{aid}.basis: non valida")
        if act.get("state") not in ACTION_STATES:
            errs.append(f"next_steps.{aid}.state: non valido")
        if act.get("event_id") is not None and act["event_id"] not in events:
            errs.append(f"next_steps.{aid}.event_id: inesistente")
        if act.get("deadline_id") is not None and act["deadline_id"] not in deadlines:
            errs.append(f"next_steps.{aid}.deadline_id: inesistente")
        if act.get("basis") == "OBBLIGO_DOCUMENTATO":
            src = sources.get(act.get("source_id"), {})
            if src.get("verified") is not True or src.get("official") is not True:
                errs.append(f"next_steps.{aid}: obbligo documentato richiede fonte ufficiale verificata")
            if not nonempty(act.get("source_locator")):
                errs.append(f"next_steps.{aid}.source_locator: mancante")
        if act.get("state") == "APPROVATA":
            if sources.get(act.get("approval_source_id"), {}).get("verified") is not True:
                errs.append(f"next_steps.{aid}: approvazione non documentata")
        if act.get("state") == "ESEGUITA":
            ev = events.get(act.get("execution_event_id"), {})
            src = sources.get(ev.get("source_id"), {})
            if ev.get("kind") not in {"RISPOSTA_PRESENTATA", "ALTRO_ATTO_ESEGUITO"} or ev.get("verification") != "VERIFICATO" or src.get("verified") is not True:
                errs.append(f"next_steps.{aid}: esecuzione non documentata da evento verificato")
        if act.get("basis") == "DA_VERIFICARE" and not nonempty(act.get("uncertainty")):
            errs.append(f"next_steps.{aid}.uncertainty: motivazione necessaria")

    state = data.get("observed_state")
    if state is not None:
        if not isinstance(state, dict):
            errs.append("observed_state: atteso oggetto")
        else:
            if not nonempty(state.get("external_label")):
                errs.append("observed_state.external_label: etichetta originale necessaria")
            if state.get("verification") not in VERIFICATIONS:
                errs.append("observed_state.verification: valore non valido")
            ev = events.get(state.get("event_id"), {})
            if not ev:
                errs.append("observed_state.event_id: inesistente")
            if state.get("verification") == "VERIFICATO":
                src = sources.get(ev.get("source_id"), {})
                if ev.get("verification") != "VERIFICATO" or src.get("official") is not True or src.get("verified") is not True:
                    errs.append("observed_state: stato verificato senza atto/portale ufficiale verificato")
            elif not nonempty(state.get("uncertainty")):
                errs.append("observed_state.uncertainty: motivazione necessaria")

    ops = data.get("operations")
    if not isinstance(ops, dict):
        errs.append("operations: oggetto mancante")
    else:
        for key in ("messages_sent", "portal_writes", "documents_uploaded", "background_monitoring"):
            if ops.get(key) is not False:
                errs.append(f"operations.{key}: deve essere esplicitamente false")

    verified_events = [e for e in events.values() if e.get("verification") == "VERIFICATO" and e.get("source_id") in sources and sources[e["source_id"]].get("verified") is True]
    if status == "AGGIORNATO_CON_EVIDENZE":
        fresh = [e for e in verified_events if parsed_time(e.get("observed_at")) is not None and (since is None or parsed_time(e["observed_at"]) >= since)]
        if not fresh:
            errs.append("tracking.status: aggiornato senza nuovi eventi verificati nel periodo")
    if status == "NESSUN_NUOVO_EVENTO_DOCUMENTATO":
        if not any(s.get("verified") is True for s in sources.values()):
            errs.append("tracking.status: assenza aggiornamenti senza fonti consultate e verificate")
        if any(parsed_time(e.get("observed_at")) is not None and (since is None or parsed_time(e["observed_at"]) >= since) for e in verified_events):
            errs.append("tracking.status: nessun nuovo evento incompatibile con eventi recenti verificati")
        if not nonempty(tracking.get("checked_channels")):
            errs.append("tracking.checked_channels: descrivere i canali effettivamente consultati")
    if status == "NON_APPLICABILE" and events:
        errs.append("tracking.status: NON_APPLICABILE con eventi presenti")
    if status == "BLOCCATO_DA_FONTI" and verified_events:
        warnings.append("tracking.status: fonti bloccanti pur con eventi verificati; motivare con precisione")
    return errs, warnings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest_json", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.manifest_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    errors, warnings = validate(data)
    print(json.dumps({"status": "FORMAL_ERRORS" if errors else "FORMAL_CHECK_PASSED", "errors": errors,
                      "warnings": warnings, "note": "Solo coerenza del manifest: non verifica l'autenticità degli atti o lo stato reale sui portali."}, indent=2, ensure_ascii=False))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
