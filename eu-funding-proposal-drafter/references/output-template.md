# Modello di consegna — Proposal Drafter

> Questo è un **formato di rendicontazione della skill**, non il formulario ufficiale del finanziamento. Le sezioni narrative della proposta si chiamano come nel modello autentico dell'avviso.

## A. Identità e tracciabilità

| Campo | Valore |
|---|---|
| Identificativo dell'avviso | [DA IDENTIFICARE] |
| Autorità competente / modalità di gestione | [DA VERIFICARE] |
| Fase / versione / rettifiche | [DA VERIFICARE] |
| Fonte ufficiale del formulario | [URL/documento e locator] |
| Lingua e formato richiesti | [DA VERIFICARE] |
| Data consultazione | [AAAA-MM-GG] |
| Stato della redazione | BOZZA_DOCUMENTATA / BOZZA_PARZIALE / BLOCCATA_DA_FONTI / NON_APPLICABILE |

## B. Registro delle fonti

| Source ID | Documento | URL/riferimento | Versione/fase | Punto | Consultato/verificato |
|---|---|---|---|---|---|
| SRC-001 | [titolo ufficiale] | [link] | [versione] | [pagina/§] | [stato] |

## C. Mappa del modulo **effettivo**

| SEC ID | Intestazione/identificativo ufficiale | Fonte | Limite e lingua verificati | REQ collegate | Stato |
|---|---|---|---|---|---|
| SEC-001 | [campo autentico] | SRC-001 §... | [solo se documentati] | REQ-001 | [COPERTO_DA_TESTO / DA_INTEGRARE / DA_CONFERMARE] |

## D. Testo della proposta

**Solo intestazioni del modulo effettivo, nell'ordine previsto.**

### [Titolo esatto sezione/campo dal formulario]

[Testo ricavato da informazioni documentate]

`[DA CONFERMARE: informazione mancante, chi la può documentare se noto]`

*Nota redazionale*: evidenze usate, ipotesi e incoerenze; se necessarie, tenerle fuori dal testo da presentare.

## E. Matrice di copertura

| REQ ID | Classe | Fonte ufficiale con locator | SEC di risposta | Evidenza effettiva | Esito | Blocco |
|---|---|---|---|---|---|---|
| REQ-001 | OBBLIGATORIO | SRC-001 §... | SEC-001 | [documento/claim/assente] | DA_CONFERMARE | [dato mancante] |

## F. Registro claim

| CLM ID | Testo della dichiarazione | Sezione | Stato di prova | Evidenza / ipotesi / origine | Criticità |
|---|---|---|---|---|---|

## G. Coerenza e questioni aperte

- Contraddizioni tra importi, tempi, attività, partner, condizioni e testi ufficiali.
- Elementi obbligatori privi di prova e segnaposto da completare.
- Proposte redazionali **non approvate**, separate dai requisiti normativi.
- Distinzione esplicita: `BOZZA` ≠ `CANDIDATURA_PRESENTATA`.

## H. Manifest opzionale per validazione statica

Il formato JSON è descritto nel [protocollo delle evidenze](evidence-protocol.md) e nei test del validatore. Il controllo automatico segnala inconsistenze **formali**, non sostituisce la lettura dei documenti né la valutazione della proposta.
