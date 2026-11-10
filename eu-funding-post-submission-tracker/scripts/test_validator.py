#!/usr/bin/env python3
"""Test unitari del solo modello di tracciamento; dati e autorità sono fittizi."""
import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from validate_tracker import validate


def sample():
    return {
        "tracking": {"status": "AGGIORNATO_CON_EVIDENZE", "as_of": "2026-11-10T16:00:00+01:00",
                     "since": "2026-11-01T00:00:00+01:00", "scope": "Atto fittizio disponibile", "limitations": "Non consultato il portale"},
        "application": {"reference": "TEST-001", "call_or_notice": "CALL-TEST", "phase": "Valutazione",
                        "authority": "Ente test", "management_mode": "DA_VERIFICARE"},
        "sources": [{"id": "SRC-1", "title": "Richiesta fittizia", "authority": "Ente test",
                     "file_ref": "fixture.txt", "locator": "§2", "observed_at": "2026-11-10T16:00:00+01:00",
                     "official": True, "verified": True}],
        "events": [{"id": "EV-1", "kind": "RICHIESTA_INTEGRAZIONE", "description": "Richiesta di integrare dati",
                    "source_id": "SRC-1", "source_locator": "§2", "observed_at": "2026-11-10T16:00:00+01:00",
                    "verification": "VERIFICATO"}],
        "deadlines": [],
        "next_steps": [{"id": "NEXT-1", "description": "Valutare una risposta", "basis": "RACCOMANDAZIONE_INTERNA",
                        "state": "PROPOSTA", "event_id": "EV-1"}],
        "operations": {"messages_sent": False, "portal_writes": False,
                       "documents_uploaded": False, "background_monitoring": False},
    }


class TrackerTests(unittest.TestCase):
    def good(self, a):
        errs, _ = validate(a)
        self.assertEqual([], errs)

    def bad(self, a, contains):
        errs, _ = validate(a)
        self.assertTrue(any(contains in x for x in errs), errs)

    def test_valid_fixture(self): self.good(sample())
    def test_json_must_be_object(self): self.bad([], "manifest")
    def test_invalid_status(self):
        a=sample();a["tracking"]["status"]="CONCESSA";self.bad(a,"tracking.status")
    def test_scope_required(self):
        a=sample();a["tracking"]["scope"]="";self.bad(a,"tracking.scope")
    def test_asof_timezone_required(self):
        a=sample();a["tracking"]["as_of"]="2026-11-10T16:00:00";self.bad(a,"tracking.as_of")
    def test_since_timezone_required(self):
        a=sample();a["tracking"]["since"]="2026-11-01T00:00:00";self.bad(a,"tracking.since")
    def test_since_not_after_asof(self):
        a=sample();a["tracking"]["since"]="2026-11-11T16:00:00+01:00";self.bad(a,"tracking.since")
    def test_partial_requires_limitations(self):
        a=sample();a["tracking"].update(status="MONITORAGGIO_PARZIALE",limitations="");self.bad(a,"tracking.limitations")
    def test_blocked_requires_limitations(self):
        a=sample();a["tracking"].update(status="BLOCCATO_DA_FONTI",limitations="");self.bad(a,"tracking.limitations")
    def test_missing_application_ref(self):
        a=sample();a["application"]["reference"]="";self.bad(a,"application.reference")
    def test_bad_mode(self):
        a=sample();a["application"]["management_mode"]="HORIZON";self.bad(a,"management_mode")
    def test_missing_sources_collection(self):
        a=sample();a.pop("sources");self.bad(a,"sources: deve essere lista")
    def test_source_id_duplicates(self):
        a=sample();a["sources"].append(copy.deepcopy(a["sources"][0]));self.bad(a,"id duplicato")
    def test_source_url_or_file(self):
        a=sample();a["sources"][0].pop("file_ref");self.bad(a,"URL o riferimento file")
    def test_source_verified_must_be_bool(self):
        a=sample();a["sources"][0]["verified"]="true";self.bad(a,"deve essere booleano")
    def test_source_observed_aware(self):
        a=sample();a["sources"][0]["observed_at"]="2026-11-10";self.bad(a,"sources.SRC-1.observed_at")
    def test_source_future(self):
        a=sample();a["sources"][0]["observed_at"]="2026-11-11T16:00:00+01:00";self.bad(a,"futuro rispetto")
    def test_event_kind(self):
        a=sample();a["events"][0]["kind"]="FONDI_PAGATI_AUTOMATICAMENTE";self.bad(a,"events.EV-1.kind")
    def test_event_unknown_source(self):
        a=sample();a["events"][0]["source_id"]="SRC-99";self.bad(a,"events.EV-1.source_id")
    def test_formal_event_needs_official_source(self):
        a=sample();a["sources"][0]["official"]=False;self.bad(a,"atto formale VERIFICATO")
    def test_verified_needs_verified_source(self):
        a=sample();a["sources"][0]["verified"]=False;self.bad(a,"VERIFICATO richiede fonte verificata")
    def test_event_unverified_needs_reason(self):
        a=sample();a["events"][0]["verification"]="DA_VERIFICARE";self.bad(a,"events.EV-1.uncertainty")
    def test_event_unverified_with_reason(self):
        a=sample();a["tracking"]["status"]="MONITORAGGIO_PARZIALE";a["events"][0].update(verification="DA_VERIFICARE",uncertainty="Mittente non verificato");self.good(a)
    def test_event_received_timestamp(self):
        a=sample();a["events"][0]["received_at"]="2026-11-08";self.bad(a,"received_at")
    def test_event_future(self):
        a=sample();a["events"][0]["observed_at"]="2026-11-11T00:00:00+01:00";self.bad(a,"futuro rispetto")
    def test_deadline_verified_date_only_without_timezone(self):
        a=sample();a["deadlines"]=[{"id":"DL-1","literal":"30 novembre 2026", "phase":"valutazione", "source_id":"SRC-1","source_locator":"§2","status":"VERIFICATO","timezone_verified":False,"event_id":"EV-1"}];self.good(a)
    def test_deadline_with_clock_requires_timezone(self):
        a=sample();a["deadlines"]=[{"id":"DL-1","literal":"30 novembre ore 17:00","phase":"valutazione","source_id":"SRC-1","source_locator":"§2","status":"VERIFICATO","timezone_verified":False}];self.bad(a,"fuso non verificato")
    def test_deadline_instant_no_zone(self):
        a=sample();a["deadlines"]=[{"id":"DL-1","literal":"30 novembre 17:00","phase":"valutazione","source_id":"SRC-1","source_locator":"§2","status":"DA_VERIFICARE","timezone_verified":False,"uncertainty":"Fuso ignoto","instant":"2026-11-30T17:00:00+01:00"}];self.bad(a,"conversione non autorizzata")
    def test_deadline_instant_aware(self):
        a=sample();a["deadlines"]=[{"id":"DL-1","literal":"30 novembre 17:00 CET","phase":"valutazione","source_id":"SRC-1","source_locator":"§2","status":"VERIFICATO","timezone_verified":True,"instant":"2026-11-30T17:00:00"}];self.bad(a,"instant: ISO")
    def test_deadline_instant_valid(self):
        a=sample();a["deadlines"]=[{"id":"DL-1","literal":"30 novembre 17:00 CET","phase":"valutazione","source_id":"SRC-1","source_locator":"§2","status":"VERIFICATO","timezone_verified":True,"instant":"2026-11-30T17:00:00+01:00"}];self.good(a)
    def test_deadline_unknown_event(self):
        a=sample();a["deadlines"]=[{"id":"DL-1","literal":"30 novembre 2026","phase":"valutazione","source_id":"SRC-1","source_locator":"§2","status":"VERIFICATO","timezone_verified":False,"event_id":"EV-99"}];self.bad(a,"deadlines.DL-1.event_id")
    def test_deadline_uncertain_needs_reason(self):
        a=sample();a["deadlines"]=[{"id":"DL-1","literal":"30 novembre 17:00","phase":"valutazione","source_id":"SRC-1","source_locator":"§2","status":"DA_VERIFICARE","timezone_verified":False}];self.bad(a,"deadlines.DL-1.uncertainty")
    def test_deadline_not_official(self):
        a=sample();a["sources"][0]["official"]=False;a["deadlines"]=[{"id":"DL-1","literal":"30 novembre 2026","phase":"valutazione","source_id":"SRC-1","source_locator":"§2","status":"VERIFICATO","timezone_verified":False}];self.bad(a,"deadlines.DL-1: VERIFICATO")
    def test_action_obligation_needs_official_source(self):
        a=sample();a["next_steps"][0]["basis"]="OBBLIGO_DOCUMENTATO";self.bad(a,"obbligo documentato richiede fonte ufficiale")
    def test_action_obligation_valid(self):
        a=sample();a["next_steps"][0].update(basis="OBBLIGO_DOCUMENTATO",source_id="SRC-1",source_locator="§2");self.good(a)
    def test_action_unknown_deadline(self):
        a=sample();a["next_steps"][0]["deadline_id"]="DL-9";self.bad(a,"next_steps.NEXT-1.deadline_id")
    def test_action_approved_needs_proof(self):
        a=sample();a["next_steps"][0]["state"]="APPROVATA";self.bad(a,"approvazione non documentata")
    def test_action_approved_with_proof(self):
        a=sample();a["next_steps"][0].update(state="APPROVATA",approval_source_id="SRC-1");self.good(a)
    def test_action_performed_needs_event(self):
        a=sample();a["next_steps"][0]["state"]="ESEGUITA";self.bad(a,"esecuzione non documentata")
    def test_action_performed_valid(self):
        a=sample();a["events"].append({"id":"EV-2","kind":"RISPOSTA_PRESENTATA","description":"Ricevuta da pratica di test", "source_id":"SRC-1","source_locator":"§3","observed_at":"2026-11-10T16:00:00+01:00","verification":"VERIFICATO"});a["next_steps"][0].update(state="ESEGUITA",execution_event_id="EV-2");self.good(a)
    def test_action_uncertain_needs_reason(self):
        a=sample();a["next_steps"][0]["basis"]="DA_VERIFICARE";self.bad(a,"next_steps.NEXT-1.uncertainty")
    def test_observed_state_must_reference_event(self):
        a=sample();a["observed_state"]={"external_label":"valutazione","verification":"VERIFICATO","event_id":"EV-9"};self.bad(a,"observed_state.event_id")
    def test_observed_state_valid(self):
        a=sample();a["observed_state"]={"external_label":"Richiesta documentale","verification":"VERIFICATO","event_id":"EV-1"};self.good(a)
    def test_observed_state_weak_source(self):
        a=sample();a["sources"][0]["official"]=False;a["observed_state"]={"external_label":"esito","verification":"VERIFICATO","event_id":"EV-1"};self.bad(a,"stato verificato")
    def test_no_updates_missing_channels(self):
        a=sample();a["tracking"]["status"]="NESSUN_NUOVO_EVENTO_DOCUMENTATO";self.bad(a,"tracking.checked_channels")
    def test_no_updates_with_recent_event(self):
        a=sample();a["tracking"].update(status="NESSUN_NUOVO_EVENTO_DOCUMENTATO",checked_channels="Fascicolo");self.bad(a,"incompatibile con eventi recenti")
    def test_no_updates_without_new_event(self):
        a=sample();a["tracking"].update(status="NESSUN_NUOVO_EVENTO_DOCUMENTATO",checked_channels="Fascicolo");a["events"]=[];a["next_steps"]=[];self.good(a)
    def test_no_updates_without_sources(self):
        a=sample();a["tracking"].update(status="NESSUN_NUOVO_EVENTO_DOCUMENTATO",checked_channels="Fascicolo");a["events"]=[];a["next_steps"]=[];a["sources"]=[];self.bad(a,"senza fonti consultate")
    def test_updated_without_event(self):
        a=sample();a["events"]=[];a["next_steps"]=[];self.bad(a,"aggiornato senza nuovi eventi")
    def test_not_applicable_with_event(self):
        a=sample();a["tracking"]["status"]="NON_APPLICABILE";self.bad(a,"NON_APPLICABILE con eventi")
    def test_writes_forbidden(self):
        a=sample();a["operations"]["portal_writes"]=True;self.bad(a,"operations.portal_writes")
    def test_emails_forbidden(self):
        a=sample();a["operations"]["messages_sent"]=True;self.bad(a,"operations.messages_sent")
    def test_upload_forbidden(self):
        a=sample();a["operations"]["documents_uploaded"]=True;self.bad(a,"operations.documents_uploaded")
    def test_background_forbidden(self):
        a=sample();a["operations"]["background_monitoring"]=True;self.bad(a,"operations.background_monitoring")
    def test_forbidden_probability(self):
        a=sample();a["approval_probability"]=0.9;self.bad(a,"campo di pretesa")
    def test_unverified_state_reason(self):
        a=sample();a["observed_state"]={"external_label":"In attesa","verification":"DA_VERIFICARE","event_id":"EV-1"};self.bad(a,"observed_state.uncertainty")


if __name__ == "__main__":
    unittest.main(verbosity=2)
