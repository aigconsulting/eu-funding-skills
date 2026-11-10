#!/usr/bin/env python3
"""Test unitari del SOLO validatore formale Skill 09."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_precheck import validate


def sample():
    return {
        "precheck": {"status": "PRECHECK_COMPLETO_SENZA_BLOCCHI_DOCUMENTATI", "scope": "Versione del pacchetto letta integralmente", "as_of": "2026-11-10T15:00:00+01:00"},
        "opportunity": {"identifier": "OPP-TEST", "phase": "Fase unica", "management_mode": "CONCORRENTE", "official_url": "https://example.eu/avviso"},
        "package": {"reference": "PACCHETTO-1", "version": "v1", "files": [{"id": "FILE-1", "name": "domanda.pdf", "version": "v1"}]},
        "sources": [{"id": "SRC-1", "title": "Avviso ufficiale (fixture)", "url": "https://example.eu/avviso", "locator": "§3", "version": "v1", "official": True, "verified": True}],
        "checks": [{"id": "CHK-1", "category": "FORMULARIO_ALLEGATI", "description": "Presenza documento richiesto (fixture)", "status": "VERIFICATO", "source_id": "SRC-1", "source_locator": "§3", "item_ref": "FILE-1", "evidence": "Il documento è presente e identificato come v1"}],
        "submission": {"performed": False, "receipt_verified": False, "portal_mutations_performed": False},
    }


class ValidatorTests(unittest.TestCase):
    def bad(self, obj, contains):
        errors, _ = validate(obj)
        self.assertTrue(any(contains in err for err in errors), errors)

    def good(self, obj):
        errors, _ = validate(obj)
        self.assertEqual([], errors)

    def test_valid(self): self.good(sample())
    def test_manifest_must_be_object(self): self.bad([], "manifest")
    def test_status_unknown(self):
        a=sample(); a["precheck"]["status"]="READY_TO_SEND"; self.bad(a,"precheck.status")
    def test_scope_mandatory(self):
        a=sample(); a["precheck"]["scope"]=""; self.bad(a,"precheck.scope")
    def test_asof_must_include_tz(self):
        a=sample(); a["precheck"]["as_of"]="2026-11-10T15:00:00"; self.bad(a,"precheck.as_of")
    def test_management_mode(self):
        a=sample(); a["opportunity"]["management_mode"]="MISTO"; self.bad(a,"management_mode")
    def test_official_url_missing(self):
        a=sample(); a["opportunity"]["official_url"]=""; self.bad(a,"opportunity.official_url")
    def test_version_missing(self):
        a=sample(); a["package"]["version"]=""; self.bad(a,"package.version")
    def test_files_missing(self):
        a=sample(); del a["package"]["files"]; self.bad(a,"package.files")
    def test_file_duplicates(self):
        a=sample(); a["package"]["files"].append(copy.deepcopy(a["package"]["files"][0])); self.bad(a,"id duplicato")
    def test_wrong_sha(self):
        a=sample(); a["package"]["files"][0]["sha256"]="123"; self.bad(a,"sha256")
    def test_correct_sha(self):
        a=sample(); a["package"]["files"][0]["sha256"]="f"*64; self.good(a)
    def test_source_missing(self):
        a=sample(); a["sources"]=[]; self.bad(a,"fonte ufficiale verificata")
    def test_source_not_verified(self):
        a=sample(); a["sources"][0]["verified"]=False; self.bad(a,"fonte ufficiale verificata")
    def test_source_not_official(self):
        a=sample(); a["sources"][0]["official"]=False; self.bad(a,"fonte ufficiale verificata")
    def test_source_boolean_str(self):
        a=sample(); a["sources"][0]["official"]="true"; self.bad(a,"deve essere booleano")
    def test_no_check_id(self):
        a=sample(); a["checks"][0].pop("id"); self.bad(a,"id mancante")
    def test_duplicated_checks(self):
        a=sample(); a["checks"].append(copy.deepcopy(a["checks"][0])); self.bad(a,"id duplicato")
    def test_category(self):
        a=sample(); a["checks"][0]["category"]="PORTALE_UNIVERSALE"; self.bad(a,"category")
    def test_check_source_unknown(self):
        a=sample(); a["checks"][0]["source_id"]="SRC-99"; self.bad(a,"source_id")
    def test_check_item_unknown(self):
        a=sample(); a["checks"][0]["item_ref"]="FILE-99"; self.bad(a,"file FILE-99")
    def test_check_missing_evidence(self):
        a=sample(); a["checks"][0]["evidence"]=""; self.bad(a,"senza evidenza")
    def test_check_missing_locator(self):
        a=sample(); a["checks"][0]["source_locator"]=""; self.bad(a,"source_locator")
    def test_complete_no_checks(self):
        a=sample(); a["checks"]=[]; self.bad(a,"completo ma senza controlli")
    def test_block_valid(self):
        a=sample(); a["precheck"]["status"]="PRECHECK_CON_BLOCCHI"; a["checks"][0].update(status="BLOCCO_ACCERTATO", recommended_fix="Aggiungere documento mancante"); self.good(a)
    def test_block_requires_fix(self):
        a=sample(); a["precheck"]["status"]="PRECHECK_CON_BLOCCHI"; a["checks"][0]["status"]="BLOCCO_ACCERTATO"; self.bad(a,"recommended_fix")
    def test_false_block_status(self):
        a=sample(); a["precheck"]["status"]="PRECHECK_CON_BLOCCHI"; self.bad(a,"blocchi dichiarati")
    def test_complete_with_block(self):
        a=sample(); a["checks"][0].update(status="BLOCCO_ACCERTATO", recommended_fix="Correggere"); self.bad(a,"incompatibile")
    def test_partial_with_gap(self):
        a=sample(); a["precheck"]["status"]="PRECHECK_PARZIALE"; a["checks"][0].update(status="DA_VERIFICARE",reason="Allegato non accessibile"); self.good(a)
    def test_gap_reason_required(self):
        a=sample(); a["checks"][0]["status"]="DA_VERIFICARE"; self.bad(a,"senza motivazione")
    def test_complete_with_gap(self):
        a=sample(); a["checks"][0].update(status="DA_VERIFICARE",reason="Da leggere"); self.bad(a,"incompatibile")
    def test_partial_without_gap(self):
        a=sample(); a["precheck"]["status"]="PRECHECK_PARZIALE"; self.bad(a,"senza lacune")
    def test_not_applicable_requires_justification(self):
        a=sample(); a["checks"][0]["status"]="NON_APPLICABILE"; self.bad(a,"senza giustificazione")
    def test_not_applicable_valid(self):
        a=sample(); a["checks"][0].update(status="NON_APPLICABILE",justification="Condizione specifica non ricorre"); self.good(a)
    def test_blocked_without_limitation(self):
        a=sample(); a["precheck"]["status"]="BLOCCATO_DA_FONTI"; self.bad(a,"precheck.limitations")
    def test_blocked_valid(self):
        a=sample(); a["precheck"].update(status="BLOCCATO_DA_FONTI", limitations="Manca avviso"); a["checks"]=[]; a["sources"]=[]; a["opportunity"]["official_url"]=""; self.good(a)
    def test_no_application_valid(self):
        a=sample(); a["precheck"].update(status="NON_APPLICABILE",limitations="Nessuna candidatura"); a["package"]={"files":[]}; a["checks"]=[]; self.good(a)
    def test_submission_prohibited(self):
        a=sample(); a["submission"]["performed"]=True; self.bad(a,"submission.performed")
    def test_receipt_prohibited(self):
        a=sample(); a["submission"]["receipt_verified"]=True; self.bad(a,"submission.receipt_verified")
    def test_portal_operation_prohibited(self):
        a=sample(); a["submission"]["portal_mutations_performed"]=True; self.bad(a,"submission.portal_mutations_performed")
    def test_deadline_unknown_source(self):
        a=sample(); a["deadline"]={"literal":"11 Nov", "phase":"F1", "timezone_verified":False,"source_id":"SRC-XXX","source_locator":"§3"}; self.bad(a,"deadline.source_id")
    def test_deadline_without_timezone_no_conversion(self):
        a=sample(); a["deadline"]={"literal":"11 novembre 17:00", "phase":"F1", "timezone_verified":False,"source_id":"SRC-1","source_locator":"§3","calculated_instant":"2026-11-11T17:00:00+01:00"}; self.bad(a,"conversione vietata")
    def test_deadline_timezone_without_official_source(self):
        a=sample(); a["sources"][0]["verified"]=False; a["deadline"]={"literal":"11 novembre 17:00 CET", "phase":"F1", "timezone_verified":True,"source_id":"SRC-1","source_locator":"§3"}; self.bad(a,"deadline.timezone_verified")
    def test_complete_time_without_zone(self):
        a=sample(); a["deadline"]={"literal":"11 novembre 17:00", "phase":"F1", "timezone_verified":False,"source_id":"SRC-1","source_locator":"§3"}; self.bad(a,"completo con ora di scadenza")
    def test_partial_with_documented_block_invalid(self):
        a=sample(); a["precheck"].update(status="PRECHECK_PARZIALE",limitations="Altri controlli incompleti"); a["checks"][0].update(status="BLOCCO_ACCERTATO",recommended_fix="Integrare"); self.bad(a,"parziale con blocco")
    def test_deadline_missing_locator(self):
        a=sample(); a["deadline"]={"literal":"11 novembre", "phase":"F1", "timezone_verified":False,"source_id":"SRC-1"}; self.bad(a,"deadline.source_locator")
    def test_deadline_conversion_valid(self):
        a=sample(); a["deadline"]={"literal":"11 novembre 17:00 CET", "phase":"F1", "timezone_verified":True,"source_id":"SRC-1","source_locator":"§3","calculated_instant":"2026-11-11T17:00:00+01:00"}; self.good(a)
    def test_forbidden_probability(self):
        a=sample(); a["approval_probability"]=0.9; self.assertTrue(validate(a)[0])
    def test_forbidden_submission_claim(self):
        a=sample(); a["submission_confirmation"]="done"; self.bad(a,"falsa certificazione")


if __name__ == "__main__":
    unittest.main(verbosity=2)
