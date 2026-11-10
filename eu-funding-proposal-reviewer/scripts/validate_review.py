#!/usr/bin/env python3
"""Controllo puramente formale manifest review EU; non verifica contenuti esterni."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REVIEW_MODES = {"AUTO_REVISIONE", "REVISIONE_SEPARATA", "REVISIONE_ESTERNA"}
REVIEW_STATUSES = {"REVIEW_COMPLETA_CON_RILIEVI", "REVIEW_SENZA_RILIEVI_DOCUMENTATI", "REVIEW_PARZIALE", "BLOCCATA_DA_FONTI", "NON_APPLICABILE"}
FINDING_KINDS = {"REQUISITO_UFFICIALE", "COERENZA_INTERNA", "OSSERVAZIONE_REDAZIONALE"}
SEVERITIES = {"CRITICO", "MAGGIORE", "MINORE", "OSSERVAZIONE"}
EVIDENCE_STATUSES = {"ACCERTATO", "POTENZIALE", "NON_VERIFICABILE", "RISOLTO_VERIFICATO"}
CATEGORIES = {"FORMALITA", "AMMISSIBILITA", "ESCLUSIONE_CAPACITA", "VALUTAZIONE", "FINANZIARIO", "ALTRO"}
REQUIREMENT_STATUSES = {"SODDISFATTO_DOCUMENTALMENTE", "CARENZA_ACCERTATA", "DA_VERIFICARE", "NON_APPLICABILE"}
FORBIDDEN_SCORE_KEYS = {"score", "scores", "official_score", "predicted_score", "funding_probability", "approval_probability", "success_rate", "rank", "ranking"}


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def records(data, name, errors):
    result = {}
    if not isinstance(data, list):
        errors.append(f"{name}: atteso array")
        return result
    for idx, item in enumerate(data):
        if not isinstance(item, dict):
            errors.append(f"{name}[{idx}]: atteso oggetto")
            continue
        key = item.get("id")
        if not nonempty(key):
            errors.append(f"{name}[{idx}]: id mancante")
        elif key in result:
            errors.append(f"{name}[{idx}]: id duplicato: {key}")
        else:
            result[key] = item
    return result


def find_forbidden_keys(node, path, errors):
    if isinstance(node, dict):
        for key, value in node.items():
            if key.lower() in FORBIDDEN_SCORE_KEYS:
                errors.append(f"{path}.{key}: score/ranking/predizione non supportati dal manifest")
            find_forbidden_keys(value, f"{path}.{key}", errors)
    elif isinstance(node, list):
        for idx, value in enumerate(node):
            find_forbidden_keys(value, f"{path}[{idx}]", errors)


def validate(data):
    errors, warnings = [], []
    if not isinstance(data, dict):
        return ["manifest: atteso oggetto"], warnings
    find_forbidden_keys(data, "manifest", errors)
    review = data.get("review")
    if not isinstance(review, dict):
        errors.append("review: oggetto assente")
        review = {}
    mode = review.get("mode")
    status = review.get("status")
    if mode not in REVIEW_MODES:
        errors.append("review.mode: valore non valido")
    if status not in REVIEW_STATUSES:
        errors.append("review.status: valore non valido")
    if not nonempty(review.get("reviewer_note")):
        errors.append("review.reviewer_note: mancante; dichiarare il perimetro reale della review")
    if mode == "REVISIONE_ESTERNA" and not nonempty(review.get("external_reviewer_evidence")):
        errors.append("review.external_reviewer_evidence: fonte dell'indipendenza esterna mancante")

    opportunity = data.get("opportunity")
    if not isinstance(opportunity, dict):
        errors.append("opportunity: oggetto assente")
        opportunity = {}
    for key in ("identifier", "phase", "as_of"):
        if not nonempty(opportunity.get(key)):
            errors.append(f"opportunity.{key}: mancante")
    if not nonempty(opportunity.get("official_url")):
        if status not in {"BLOCCATA_DA_FONTI", "NON_APPLICABILE"}:
            errors.append("opportunity.official_url: mancante")
        else:
            warnings.append("opportunity.official_url: URL non disponibile, documentare il blocco")
    elif not opportunity["official_url"].startswith("https://"):
        warnings.append("opportunity.official_url: usare URL primario HTTPS ove disponibile")

    proposal = data.get("proposal")
    if not isinstance(proposal, dict):
        errors.append("proposal: oggetto assente")
        proposal = {}
    for key in ("reference", "version", "review_scope"):
        if not nonempty(proposal.get(key)):
            errors.append(f"proposal.{key}: mancante")
    sha = proposal.get("sha256")
    if sha is not None and not re.fullmatch(r"[0-9a-fA-F]{64}", str(sha)):
        errors.append("proposal.sha256: deve essere SHA-256 esadecimale di 64 caratteri")

    sources = records(data.get("sources", []), "sources", errors)
    requirements = records(data.get("requirements", []), "requirements", errors)
    findings = records(data.get("findings", []), "findings", errors)
    for ident, src in sources.items():
        if not nonempty(src.get("title")) or not nonempty(src.get("locator")):
            errors.append(f"sources.{ident}: title e locator obbligatori")
        if type(src.get("official")) is not bool or type(src.get("verified")) is not bool:
            errors.append(f"sources.{ident}: official e verified devono essere booleani")
        if src.get("verified") is False:
            warnings.append(f"sources.{ident}: fonte dichiarata non verificata")

    for ident, req in requirements.items():
        if not nonempty(req.get("description")):
            errors.append(f"requirements.{ident}: description mancante")
        if req.get("category") not in CATEGORIES:
            errors.append(f"requirements.{ident}: category non valida")
        if req.get("review_status") not in REQUIREMENT_STATUSES:
            errors.append(f"requirements.{ident}: review_status non valido")
        source_id = req.get("source_id")
        if source_id not in sources:
            errors.append(f"requirements.{ident}: source_id non trovato")
        elif sources[source_id].get("official") is not True or sources[source_id].get("verified") is not True:
            errors.append(f"requirements.{ident}: requisito senza fonte ufficiale dichiarata verificata")
        if not nonempty(req.get("locator")):
            errors.append(f"requirements.{ident}: locator della fonte mancante")
        if req.get("review_status") == "CARENZA_ACCERTATA" and not nonempty(req.get("proposal_locator")):
            errors.append(f"requirements.{ident}: carenza accertata senza perimetro della proposta")
        if req.get("review_status") == "NON_APPLICABILE" and not nonempty(req.get("justification")):
            errors.append(f"requirements.{ident}: non applicabilità senza motivazione")

    for ident, finding in findings.items():
        kind = finding.get("kind")
        evidence = finding.get("evidence_status")
        if kind not in FINDING_KINDS:
            errors.append(f"findings.{ident}: kind non valido")
        if finding.get("severity") not in SEVERITIES:
            errors.append(f"findings.{ident}: severity non valida")
        if evidence not in EVIDENCE_STATUSES:
            errors.append(f"findings.{ident}: evidence_status non valido")
        if not nonempty(finding.get("description")) or not nonempty(finding.get("recommendation")):
            errors.append(f"findings.{ident}: description/recommendation mancanti")
        req_id = finding.get("requirement_id")
        src_id = finding.get("source_id")
        if req_id is not None and req_id not in requirements:
            errors.append(f"findings.{ident}: requirement_id non trovato")
        if src_id is not None and src_id not in sources:
            errors.append(f"findings.{ident}: source_id non trovato")
        if kind == "REQUISITO_UFFICIALE":
            if not nonempty(req_id):
                errors.append(f"findings.{ident}: requisito ufficiale senza requirement_id")
            if src_id not in sources:
                errors.append(f"findings.{ident}: requisito ufficiale senza source_id")
            elif sources[src_id].get("official") is not True or sources[src_id].get("verified") is not True:
                if evidence == "ACCERTATO":
                    errors.append(f"findings.{ident}: ACCERTATO senza fonte ufficiale verificata")
                else:
                    warnings.append(f"findings.{ident}: fonte ufficiale non verificata, tenere aperto")
            if req_id in requirements and src_id in sources and requirements[req_id].get("source_id") != src_id:
                errors.append(f"findings.{ident}: source_id non coerente con il requisito")
            if evidence == "ACCERTATO" and not nonempty(finding.get("official_locator")):
                errors.append(f"findings.{ident}: rilievo normativo ACCERTATO senza official_locator")
        if evidence in {"ACCERTATO", "RISOLTO_VERIFICATO"}:
            if not nonempty(finding.get("proposal_locator")):
                errors.append(f"findings.{ident}: stato {evidence} senza proposal_locator")
            if not nonempty(finding.get("proposal_excerpt")) and not nonempty(finding.get("checked_absence_scope")):
                errors.append(f"findings.{ident}: stato {evidence} senza estratto o controllo documentato di assenza")
        if evidence == "NON_VERIFICABILE" and not nonempty(finding.get("missing_evidence")):
            errors.append(f"findings.{ident}: NON_VERIFICABILE senza missing_evidence")
        if evidence == "RISOLTO_VERIFICATO" and not nonempty(finding.get("resolved_in_version")):
            errors.append(f"findings.{ident}: resolved_in_version mancante; risoluzione senza versione riletta")
        if kind == "OSSERVAZIONE_REDAZIONALE" and req_id is not None:
            warnings.append(f"findings.{ident}: osservazione redazionale collegata a requisito; distinguere l'obbligo dal suggerimento")

    submission = data.get("submission")
    if not isinstance(submission, dict) or submission.get("performed") is not False:
        errors.append("submission.performed: deve essere esplicitamente false")

    active = [f for f in findings.values() if f.get("evidence_status") != "RISOLTO_VERIFICATO"]
    if status == "REVIEW_COMPLETA_CON_RILIEVI" and not active:
        errors.append("review.status: dichiarati rilievi senza findings attivi")
    if status == "REVIEW_SENZA_RILIEVI_DOCUMENTATI" and active:
        errors.append("review.status: senza rilievi ma findings attivi presenti")
    if status in {"BLOCCATA_DA_FONTI", "REVIEW_PARZIALE", "NON_APPLICABILE"}:
        if not nonempty(review.get("limitations")):
            errors.append(f"review.limitations: obbligatorio per {status}")
    if status == "BLOCCATA_DA_FONTI" and active:
        warnings.append("review.status: relazione bloccata ma rilievi attivi; verificare la portata")
    if status in {"REVIEW_COMPLETA_CON_RILIEVI", "REVIEW_SENZA_RILIEVI_DOCUMENTATI"} and not sources:
        errors.append("sources: review dichiarata completa senza fonti")
    return errors, warnings


def main():
    parser = argparse.ArgumentParser(description="Validazione strutturale del manifest di review; non assegna giudizi ufficiali")
    parser.add_argument("review_json", type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.review_json.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"status": "ERROR", "errors": [str(exc)]}, ensure_ascii=False))
        return 2
    errors, warnings = validate(data)
    print(json.dumps({"status": "FORMAL_ERRORS" if errors else "FORMAL_CHECK_PASSED", "errors": errors,
                      "warnings": warnings, "note": "Controllo formale: NON verifica fonte, eleggibilità, ammissibilità, gravità o qualità reale."},
                     ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
