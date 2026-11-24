---
name: eu-funding-risk-manager
description: Analisi e trattamento dei rischi progettuali per progetti UE; produce analisi e output tracciabili, verificando fonti e regole applicabili senza inventare dati.
---

# EU Funding Risk Manager

## Scopo
Analisi e trattamento dei rischi progettuali. Metodo specialistico autonomo, complementare alle skill di ricerca, progettazione, redazione e attuazione. Non sostituisce decisioni del beneficiario o dell'autorità competente.

## Input
Obiettivi, WBS, contesto, risorse, vincoli, assunzioni e rischi noti. Identificare call, versione, giurisdizione e documenti applicabili. Se mancanti, dichiarare le lacune e limitare l'analisi alla metodologia.

## Procedura
1. Definire scale di probabilità e impatto con orizzonte e soglie esplicite.
2. Descrivere rischio come causa-evento-conseguenza e collegarlo a obiettivi/WP.
3. Valutare rischio inerente e residuo senza falsa precisione.
4. Proporre evitare, ridurre, trasferire o accettare con trigger e contingenze.
5. Distinguere rischio futuro da problema attuale e assunzione esterna.
6. Assegnare owner solo se confermato e versionare monitoraggio.
7. Segnalare rischi critici senza mitigazione credibile.

## Output
Intestazione: progetto, call, versione, data, perimetro, fonti e limiti.
 
| ID | Causa-evento-effetto | WP | Probabilità | Impatto | Inerente | Mitigazione | Residuo | Trigger | Owner/stato |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE |

Per ogni conclusione registrare evidenza, fonte precisa, data, motivazione e stato; produrre elenco dei gap e decisioni pendenti. Conservare l'output specialistico separato e trasferire solo campi compatibili al dossier condiviso, senza modificarne lo schema.

## Fonti istituzionali
- https://pm2.europa.eu/
- https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home

I link sono punti di partenza: verificare accessibilità, documento, versione, data di applicazione, eventuali modifiche e pertinenza alla call. Le guide generali non introducono obblighi automaticamente.

## Guardrail
Distinguere VERIFICATO (fonte e data), DA_CONFERMARE, IPOTESI, PROPOSTA, DECISIONE_APPROVATA, MANCANTE, NON_APPLICABILE. Non inventare dati, autorizzazioni, impegni, fonti o obblighi; non elevare stati per inferenza. Nessuna azione esterna, modifica di documenti ufficiali o certificazione di ammissibilità/conformità.

## Esiti
COMPLETO quando gli elementi applicabili sono documentati; PARZIALE se mancano evidenze; BLOCCATO_DA_FONTI se un conflitto decisivo impedisce conclusioni affidabili. Nessun esito garantisce finanziamento.

## Scenari da verificare (non eseguiti)
- Rischio già avvenuto: registrare anche issue
- scala ordinale: non spacciare prodotto dei punteggi per perdita monetaria attesa.
- Call o fonte applicabile assente: nessun esito definitivo, evidenziare lacune.
