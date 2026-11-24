---
name: eu-funding-ethics-assessment
description: Pre-screening etico e piano di evidenze per progetti UE; produce analisi e output tracciabili, verificando fonti e regole applicabili senza inventare dati.
---

# EU Funding Ethics Assessment

## Scopo
Pre-screening etico e piano di evidenze. Metodo specialistico autonomo, complementare alle skill di ricerca, progettazione, redazione e attuazione. Non sostituisce decisioni del beneficiario o dell'autorità competente.

## Input
Call, metodologia, partecipanti, dati, tecnologie, paesi, rischi e autorizzazioni. Identificare call, versione, giurisdizione e documenti applicabili. Se mancanti, dichiarare le lacune e limitare l'analisi alla metodologia.

## Procedura
1. Recuperare il questionario etico e le istruzioni della call.
2. Identificare categorie pertinenti, inclusi soggetti umani, minori, dati, animali, paesi terzi, ambiente, AI e uso improprio se applicabili.
3. Distinguere dichiarazioni, rischi, misure e autorizzazioni.
4. Valutare consenso, proporzionalità e tutele senza sostituire comitati o DPO.
5. Mappare evidenze, scadenze e responsabili confermati.
6. Segnalare elementi non determinabili, non dichiarare assenza di rischio per omissione.

## Output
Intestazione: progetto, call, versione, data, perimetro, fonti e limiti.
 
| Categoria | Applicabilità | Fonte/requisito | Rischio | Misura | Evidenza/autorizzazione | Stato |
| --- | --- | --- | --- | --- | --- | --- |
| DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE |

Per ogni conclusione registrare evidenza, fonte precisa, data, motivazione e stato; produrre elenco dei gap e decisioni pendenti. Conservare l'output specialistico separato e trasferire solo campi compatibili al dossier condiviso, senza modificarne lo schema.

## Fonti istituzionali
- https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home
- https://eur-lex.europa.eu/
- https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home

I link sono punti di partenza: verificare accessibilità, documento, versione, data di applicazione, eventuali modifiche e pertinenza alla call. Le guide generali non introducono obblighi automaticamente.

## Guardrail
Distinguere VERIFICATO (fonte e data), DA_CONFERMARE, IPOTESI, PROPOSTA, DECISIONE_APPROVATA, MANCANTE, NON_APPLICABILE. Non inventare dati, autorizzazioni, impegni, fonti o obblighi; non elevare stati per inferenza. Nessuna azione esterna, modifica di documenti ufficiali o certificazione di ammissibilità/conformità.

## Esiti
COMPLETO quando gli elementi applicabili sono documentati; PARZIALE se mancano evidenze; BLOCCATO_DA_FONTI se un conflitto decisivo impedisce conclusioni affidabili. Nessun esito garantisce finanziamento.

## Scenari da verificare (non eseguiti)
- Consenso alla ricerca non equivale automaticamente a base giuridica GDPR
- approvazione non documentata: MANCANTE.
- Call o fonte applicabile assente: nessun esito definitivo, evidenziare lacune.
