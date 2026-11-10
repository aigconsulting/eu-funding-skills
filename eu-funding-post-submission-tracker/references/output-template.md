# Modello di rapporto — Skill 10

## Rapporto di post-presentazione (non è una certificazione)

- Candidatura / avviso / autorità / fase / gestione: `[...; non verificato dove necessario]`
- Data e ora dell'analisi, con fuso: `[...]`
- Periodo analizzato e canali consultati: `[...]`
- Canali/documenti non consultati: `[...]`
- Prova di presentazione: `[riferimento e data verificati | DA_VERIFICARE]`
- **Stato osservato nel canale** (testo letterale + data + fonte): `[...]` — non dedurre la fase successiva.
- **Esito del rapporto**: `AGGIORNATO_CON_EVIDENZE | NESSUN_NUOVO_EVENTO_DOCUMENTATO | MONITORAGGIO_PARZIALE | BLOCCATO_DA_FONTI | NON_APPLICABILE`.

| Event ID | Evento osservato | Data atto/ricezione/consultazione | Fonte e localizzatore | Evidenza e incertezza |
|---|---|---|---|---|
| EV-1 | ... | ... | SRC-1, §... | ... |

| Termine | Testo letterale | Fonte/fase | Esito di verifica | Condizioni/non verificato |
|---|---|---|---|---|
| DL-1 | ... | SRC-1, §... | VERIFICATA/DA_VERIFICARE/CONFLITTO_FONTI | ... |

| Next step | Motivazione | Base | Stato reale | Riscontro |
|---|---|---|---|---|
| NEXT-1 | ... | OBBLIGO_DOCUMENTATO / RACCOMANDAZIONE_INTERNA / DA_VERIFICARE | PROPOSTA/APPROVATA/ESEGUITA/DA_VERIFICARE | ... |

**Limiti:** specificare che un evento verificato riguarda il documento letto, non una certificazione dell'intero stato della procedura; indicare periodi o canali privi di accesso. Non includere un punteggio di successo o una previsione inventata. Non inviare comunicazioni né creare monitoraggi automatici.

## Manifest JSON illustrativo (dati fittizi, non esito reale)

```json
{
  "tracking": {
    "status": "AGGIORNATO_CON_EVIDENZE",
    "as_of": "2026-11-10T16:00:00+01:00",
    "since": "2026-11-01T00:00:00+01:00",
    "scope": "Solo comunicazione ufficiale disponibile nel fascicolo di prova",
    "limitations": "Portale autenticato non consultato"
  },
  "application": {
    "reference": "DOMANDA-TEST-001",
    "call_or_notice": "AVVISO-FITTIZIO",
    "phase": "valutazione",
    "authority": "Autorita dimostrativa",
    "management_mode": "DA_VERIFICARE"
  },
  "sources": [
    {
      "id": "SRC-1", "title": "Comunicazione fittizia", "authority": "Autorita dimostrativa",
      "file_ref": "documento-prova.txt", "locator": "paragrafo 2",
      "observed_at": "2026-11-10T16:00:00+01:00", "official": true, "verified": true
    }
  ],
  "events": [
    {
      "id": "EV-1", "kind": "RICHIESTA_INTEGRAZIONE",
      "description": "Richiesta di integrazione riportata nel documento fittizio",
      "source_id": "SRC-1", "source_locator": "paragrafo 2",
      "observed_at": "2026-11-10T16:00:00+01:00"
    }
  ],
  "deadlines": [],
  "next_steps": [
    {
      "id": "NEXT-1", "description": "Valutare una risposta alla richiesta",
      "basis": "RACCOMANDAZIONE_INTERNA", "state": "PROPOSTA", "event_id": "EV-1"
    }
  ],
  "operations": {
    "messages_sent": false, "portal_writes": false,
    "documents_uploaded": false, "background_monitoring": false
  }
}
```

Tutti i campi `verified` richiedono una **verifica umana/documentale reale**; il validatore controlla che siano presenti e coerenti ma non può provarne la veridicità.
