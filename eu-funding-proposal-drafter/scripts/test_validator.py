#!/usr/bin/env python3
"""Test unitari del validatore, senza file di avviso reali o controlli normativi."""
from copy import deepcopy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_draft import validate


def fixture():
    """Record fittizi di verifica software: NON sono un avviso vero."""
    return {
        "opportunity": {"identifier": "EXAMPLE-NOT-REAL", "official_url": "https://example.invalid/call", "phase": "fase-esempio", "as_of": "2026-11-10"},
        "sources": [{"id": "SRC-1", "title": "modello di esempio", "locator": "campo 1", "official": True, "verified": True}],
        "sections": [{"id": "SEC-1", "official_label": "campo esemplificativo", "source_id": "SRC-1", "coverage": "COPERTO_DA_TESTO", "text": "testo dimostrativo"}],
        "requirements": [{"id": "REQ-1", "kind": "OBBLIGATORIO", "source_id": "SRC-1", "locator": "campo 1", "section_ids": ["SEC-1"], "coverage": "COPERTO_DA_TESTO"}],
        "claims": [{"id": "CLM-1", "section_id": "SEC-1", "state": "VERIFICATA_DA_DOCUMENTO", "text": "dato dimostrativo", "evidence_ref": "documento dimostrativo"}],
        "submission": {"performed": False},
    }


class ManifestTests(unittest.TestCase):
    def test_valid_structure(self):
        self.assertFalse(validate(fixture())[0])

    def test_missing_source(self):
        d = fixture(); d["requirements"][0]["source_id"] = "SRC-X"
        self.assertTrue(validate(d)[0])

    def test_unverified_source_for_requirement(self):
        d = fixture(); d["sources"][0]["verified"] = False
        self.assertTrue(validate(d)[0])

    def test_unofficial_source_for_section(self):
        d = fixture(); d["sources"][0]["official"] = False
        self.assertTrue(validate(d)[0])

    def test_verified_claim_without_evidence(self):
        d = fixture(); d["claims"][0].pop("evidence_ref")
        self.assertTrue(validate(d)[0])

    def test_unlinked_section(self):
        d = fixture(); d["requirements"][0]["section_ids"] = ["SEC-X"]
        self.assertTrue(validate(d)[0])

    def test_missing_mandatory_is_warning(self):
        d = fixture(); d["requirements"][0]["coverage"] = "DA_INTEGRARE"
        errors, warnings = validate(d)
        self.assertFalse(errors)
        self.assertTrue(any("obbligo non coperto" in w for w in warnings))

    def test_unjustified_not_applicable_is_error(self):
        d = fixture(); d["requirements"][0]["coverage"] = "NON_APPLICABILE"
        self.assertTrue(validate(d)[0])

    def test_justified_not_applicable_warns(self):
        d = fixture(); d["requirements"][0].update(coverage="NON_APPLICABILE", justification="decisione da verificare")
        errors, warnings = validate(d)
        self.assertFalse(errors)
        self.assertTrue(warnings)

    def test_proposed_claim_warning(self):
        d = fixture(); d["claims"][0]["state"] = "PROPOSTA"; d["claims"][0]["evidence_ref"] = ""
        errors, warnings = validate(d)
        self.assertFalse(errors)
        self.assertTrue(any("non verificata" in w for w in warnings))

    def test_duplicate_ids(self):
        d = fixture(); d["requirements"].append(deepcopy(d["requirements"][0]))
        self.assertTrue(validate(d)[0])

    def test_submission_true_rejected(self):
        d = fixture(); d["submission"]["performed"] = True
        self.assertTrue(validate(d)[0])

    def test_missing_submission_rejected(self):
        d = fixture(); d.pop("submission")
        self.assertTrue(validate(d)[0])

    def test_covered_section_without_text(self):
        d = fixture(); d["sections"][0]["text"] = ""
        self.assertTrue(validate(d)[0])

    def test_missing_required_metadata(self):
        d = fixture(); d["opportunity"].pop("phase")
        self.assertTrue(validate(d)[0])

    def test_non_dict_input(self):
        self.assertTrue(validate(["wrong"])[0])


if __name__ == "__main__":
    unittest.main(verbosity=2)
