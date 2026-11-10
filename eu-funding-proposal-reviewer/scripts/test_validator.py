#!/usr/bin/env python3
"""Test sintetici della validazione formale: nessun bando reale usato."""
from __future__ import annotations

import copy
import unittest
from validate_review import validate


def fixture():
    return {
        "opportunity": {"identifier": "EXAMPLE-01", "official_url": "https://example.eu/call", "phase": "fase-1", "as_of": "2026-11-10"},
        "proposal": {"reference": "bozza.md", "version": "1", "review_scope": "testo integrale e allegati elencati"},
        "review": {"mode": "AUTO_REVISIONE", "status": "REVIEW_COMPLETA_CON_RILIEVI", "reviewer_note": "revisione interna distinta dal processo di compilazione"},
        "sources": [{"id": "SRC-001", "title": "Bando esempio", "locator": "https://example.eu/call#section1", "official": True, "verified": True}],
        "requirements": [{"id": "REQ-001", "description": "Campo X richiesto", "category": "FORMALITA", "source_id": "SRC-001", "locator": "sez. 1", "review_status": "CARENZA_ACCERTATA", "proposal_locator": "sez. X"}],
        "findings": [{"id": "FND-001", "kind": "REQUISITO_UFFICIALE", "severity": "MAGGIORE", "evidence_status": "ACCERTATO", "description": "Campo X vuoto", "recommendation": "Compilare sulla base di evidenze", "source_id": "SRC-001", "requirement_id": "REQ-001", "official_locator": "sez. 1", "proposal_locator": "sez. X", "checked_absence_scope": "sezione X letta integralmente"}],
        "submission": {"performed": False},
    }


class TestReviewValidator(unittest.TestCase):
    def check_fail(self, modifier, fragment):
        data = fixture()
        modifier(data)
        errors, _ = validate(data)
        self.assertTrue(any(fragment in e for e in errors), errors)

    def test_valid(self):
        self.assertEqual(validate(fixture())[0], [])

    def test_not_object(self):
        self.assertTrue(validate([])[0])

    def test_missing_source(self):
        self.check_fail(lambda x: x.update(sources=[]), "source_id non trovato")

    def test_false_official_source(self):
        self.check_fail(lambda x: x["sources"][0].update(official=False), "senza fonte ufficiale")

    def test_false_verified_source(self):
        self.check_fail(lambda x: x["sources"][0].update(verified=False), "senza fonte ufficiale")

    def test_missing_req(self):
        self.check_fail(lambda x: x["findings"][0].update(requirement_id="REQ-999"), "requirement_id non trovato")

    def test_missing_locator_official(self):
        self.check_fail(lambda x: x["findings"][0].pop("official_locator"), "official_locator")

    def test_missing_locator_proposal(self):
        self.check_fail(lambda x: x["findings"][0].pop("proposal_locator"), "proposal_locator")

    def test_missing_excerpt_or_absence(self):
        self.check_fail(lambda x: x["findings"][0].pop("checked_absence_scope"), "estratto o controllo documentato")

    def test_missing_evidence_for_unverifiable(self):
        def mod(x):
            x["findings"][0]["evidence_status"] = "NON_VERIFICABILE"
            x["findings"][0].pop("checked_absence_scope")
        self.check_fail(mod, "missing_evidence")

    def test_unverified_can_be_unverifiable_with_req_blocked(self):
        # For an official req in the rule table, provenance must remain verified.
        data = fixture()
        data["findings"][0]["evidence_status"] = "NON_VERIFICABILE"
        data["findings"][0]["missing_evidence"] = "allegato non disponibile"
        self.assertEqual(validate(data)[0], [])

    def test_resolution_requires_version(self):
        self.check_fail(lambda x: x["findings"][0].update(evidence_status="RISOLTO_VERIFICATO"), "resolved_in_version")

    def test_no_scores(self):
        self.check_fail(lambda x: x["review"].update(score=85), "score/ranking")

    def test_no_submission(self):
        self.check_fail(lambda x: x["submission"].update(performed=True), "submission.performed")

    def test_missing_review_scope(self):
        self.check_fail(lambda x: x["proposal"].pop("review_scope"), "proposal.review_scope")

    def test_conflicting_no_findings_status(self):
        self.check_fail(lambda x: x["review"].update(status="REVIEW_SENZA_RILIEVI_DOCUMENTATI"), "findings attivi")

    def test_no_findings_valid(self):
        data = fixture()
        data["review"]["status"] = "REVIEW_SENZA_RILIEVI_DOCUMENTATI"
        data["findings"] = []
        self.assertEqual(validate(data)[0], [])

    def test_partial_requires_limitations(self):
        self.check_fail(lambda x: x["review"].update(status="REVIEW_PARZIALE"), "review.limitations")

    def test_blocked_allows_missing_url(self):
        data = fixture()
        data["review"]["status"] = "BLOCCATA_DA_FONTI"
        data["review"]["limitations"] = "avviso non recuperabile"
        del data["opportunity"]["official_url"]
        self.assertEqual(validate(data)[0], [])

    def test_external_review_needs_evidence(self):
        self.check_fail(lambda x: x["review"].update(mode="REVISIONE_ESTERNA"), "external_reviewer_evidence")

    def test_duplicate_finding_id(self):
        self.check_fail(lambda x: x["findings"].append(copy.deepcopy(x["findings"][0])), "id duplicato")

    def test_na_requires_justification(self):
        self.check_fail(lambda x: x["requirements"][0].update(review_status="NON_APPLICABILE"), "non applicabilità")

    def test_sha256_invalid(self):
        self.check_fail(lambda x: x["proposal"].update(sha256="1234"), "SHA-256")

    def test_source_mismatch(self):
        def mod(x):
            x["sources"].append({"id": "SRC-002", "title": "Bando 2", "locator": "https://example.eu/other", "official": True, "verified": True})
            x["findings"][0]["source_id"] = "SRC-002"
        self.check_fail(mod, "non coerente con il requisito")

    def test_redaction_observation_no_legal_requirement(self):
        data = fixture()
        data["findings"] = [{"id": "FND-R", "kind": "OSSERVAZIONE_REDAZIONALE", "severity": "OSSERVAZIONE",
                             "evidence_status": "POTENZIALE", "description": "Frase ambigua", "recommendation": "Chiarire"}]
        self.assertEqual(validate(data)[0], [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
