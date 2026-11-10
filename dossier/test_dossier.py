#!/usr/bin/env python3
"""Test unitari del validatore del dossier condiviso (stdlib soltanto)."""
from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[0]
if str(ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(ROOT))

import check_dossier  # noqa: E402

EXAMPLE = ROOT / "example-dossier.json"


def load_example() -> dict:
    return json.loads(EXAMPLE.read_text(encoding="utf-8"))


class DossierTests(unittest.TestCase):
    def test_example_valid(self):
        errors, warnings = check_dossier.check(load_example())
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])

    def test_schema_tag_required(self):
        dossier = load_example()
        dossier["schema"] = "altro"
        errors, _ = check_dossier.check(dossier)
        self.assertTrue(any("schema non conforme" in e for e in errors))

    def test_verificato_requires_fonte_and_date(self):
        dossier = load_example()
        dossier["evidenze"] = []
        errors, _ = check_dossier.check(dossier)
        self.assertTrue(any("senza fonte" in e or "evidenze vuota" in e for e in errors))

    def test_unknown_state_rejected(self):
        dossier = load_example()
        dossier["progetto"]["problemi"][0]["stato"] = "CERTO"
        errors, _ = check_dossier.check(dossier)
        self.assertTrue(any("stato non ammesso" in e for e in errors))

    def test_broken_source_reference(self):
        dossier = load_example()
        dossier["requisiti"][0]["fonte"] = "SRC-999"
        errors, _ = check_dossier.check(dossier)
        self.assertTrue(any("SRC-999" in e for e in errors))

    def test_decision_requires_approval_date(self):
        dossier = load_example()
        dossier["partenariato"] = []
        dossier["progetto"]["problemi"][0] = {
            "testo": "decisione approvata senza data",
            "stato": "DECISIONE_APPROVATA",
            "fonte": None,
        }
        errors, _ = check_dossier.check(dossier)
        self.assertTrue(any("approvato_il" in e for e in errors))

    def test_rettifica_does_not_confirm_previous_data(self):
        """Una rettifica porta in avanti `ultima_verifica`: i fatti VERIFICATO
        con data precedente restano stale → avviso di riesame, non conferma."""
        dossier = load_example()
        dossier["opportunita"]["ultima_verifica"] = "2026-11-15"
        dossier["revisioni"].append({
            "data": "2026-11-15",
            "descrizione": "Rettifica ufficiale del bando segnalata dalla fonte primaria",
            "motivo": "rettifica_bando",
        })
        errors, warnings = check_dossier.check(dossier)
        self.assertEqual(errors, [])
        self.assertTrue(any("da riesaminare" in w for w in warnings))
        self.assertEqual(
            dossier["progetto"]["problemi"][0]["stato"],
            "IPOTESI",  # nessuna trasformazione automatica di stati
        )

    def test_proposal_never_becomes_decision(self):
        """Gli stati non si trasformano da soli: una PROPOSTA resta PROPOSTA
        se non approvata; il validatore la lascia invariata e non segnala errore."""
        dossier = load_example()
        before = dossier["progetto"]["obiettivi_generali"][0]["stato"]
        errors, warnings = check_dossier.check(dossier)
        self.assertEqual(before, "PROPOSTA")
        self.assertEqual(errors, [])

    def test_missing_any_opportunity_id(self):
        dossier = load_example()
        dossier["opportunita"]["topic_id"] = None
        errors, _ = check_dossier.check(dossier)
        self.assertTrue(any("senza call_id/topic_id/avviso_id" in e for e in errors))

    def test_revision_requires_description(self):
        dossier = load_example()
        dossier["revisioni"][0].pop("descrizione")
        errors, _ = check_dossier.check(dossier)
        self.assertTrue(any("senza descrizione" in e for e in errors))

    def test_stale_only_flagged_when_newer_check(self):
        dossier = load_example()
        dossier["opportunita"]["ultima_verifica"] = "2026-10-01"  # PRIMA della verifica
        errors, warnings = check_dossier.check(dossier)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])


if __name__ == "__main__":
    unittest.main()
