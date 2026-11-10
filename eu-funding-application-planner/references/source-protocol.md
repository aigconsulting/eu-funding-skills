# Protocollo di selezione e tracciabilità delle fonti

## Sequenza di verifica

1. **Identità del caso**: ID/URL avviso, ente concedente/autorità, programma, periodo, fase, regime e canale ufficiale.
2. **Documenti operativi**: pagina avviso, testo integrale, allegati e moduli applicabili alla fase; individuare la *versione effettiva*.
3. **Aggiornamenti**: corrigenda, amendment, proroghe, guide aggiornate e FAQ ufficiali pertinenti. Non applicare automaticamente al caso documenti emessi per altre annualità o programmi.
4. **Regole generali**: regolamento/programma/condizioni generali pertinenti, solo nei limiti richiamati o applicabili al bando.
5. **Registro di prova**: per ogni regola determinante conservare ID documento, URL, data/versione, titolo della sezione, pagina/paragrafo, testo breve/parafrasi e fase.

## Dati minimi del registro

| Campo | Semantica |
|---|---|
| `source_id` | ID interno univoco della fonte |
| `source_url` | URL istituzionale diretto, senza link inventati |
| `source_title` | Titolo ufficiale |
| `document_version` | Versione e data (se disponibili) |
| `retrieved_at` | Data della verifica |
| `applicability` | Programma, avviso, finestra, fase, soggetto/ruolo |
| `section` | Sezione/pagina a supporto |
| `verification_status` | `VERIFICATO`, `NON_VERIFICATO`, `CONFLITTO` |

## Regole non valide per inferenza

- Non usare automaticamente lo schema documentale di altri programmi o di un altro bando dello stesso programma.
- Non dedurre scadenza, fuso, finestre, allegati o percentuali da una brochure.
- Non assegnare un ruolo a un partner o a un coordinatore se il bando non lo definisce.
- Non confondere documenti richiesti alla **domanda** con quelli richiesti **solo dopo l'approvazione**.
- Non presumere la disponibilità di portali, apertura delle candidature, proroghe o esiti.

Se una fonte necessaria è irraggiungibile, dichiararla e sospendere il relativo elemento della checklist. Per condizioni confliggenti non scegliere arbitrariamente la fonte più recente: verificare prevalenza, efficacia e chiarimenti dell'ente competente.
