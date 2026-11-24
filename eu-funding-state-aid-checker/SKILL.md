---
name: eu-funding-state-aid-checker
description: Screening aiuti di Stato, de minimis, GBER e cumulo per progetti UE; produce analisi e output tracciabili, verificando fonti e regole applicabili senza inventare dati.
---

# EU Funding State Aid Checker

## Scopo
Screening aiuti di Stato, de minimis, GBER e cumulo. Metodo specialistico autonomo, complementare alle skill di ricerca, progettazione, redazione e attuazione. Non sostituisce decisioni del beneficiario o dell'autorità competente.

## Input
Misura, beneficiario, attività economica, gruppo, costi, aiuti pregressi, date e settore. Identificare call, versione, giurisdizione e documenti applicabili. Se mancanti, dichiarare le lacune e limitare l'analisi alla metodologia.

## Procedura
1. Identificare disciplina e atto applicabile, distinguendo finanziamento UE diretto e risorse sotto controllo statale.
2. Esaminare criteri dell'articolo 107(1) TFUE senza automatismi.
3. Verificare base di compatibilità o esenzione, settore, impresa unica e condizioni pertinenti.
4. Per de minimis usare regolamento, periodo e plafond effettivamente applicabili alla data, registrando concessioni e equivalente sovvenzione lordo.
5. Analizzare cumulo per stessi costi e intensità, senza confondere con doppio finanziamento.
6. Segnalare dati incompleti e necessità di verifica autoritativa.

## Output
Intestazione: progetto, call, versione, data, perimetro, fonti e limiti.

| Misura | Base giuridica/versione | Impresa/perimetro | Costi | Aiuti/data/ESL | Cumulo | Gap | Esito preliminare |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE |

Per ogni conclusione registrare evidenza, fonte precisa, data, motivazione e stato; produrre elenco dei gap e decisioni pendenti. Conservare l'output specialistico separato e trasferire solo campi compatibili al dossier condiviso, senza modificarne lo schema.

## Fonti istituzionali
- https://eur-lex.europa.eu/eli/reg/2023/2831/oj
- https://eur-lex.europa.eu/eli/reg/2014/651/oj
- https://competition-policy.ec.europa.eu/state-aid_en
- https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home

I link sono punti di partenza: verificare accessibilità, documento, versione, data di applicazione, eventuali modifiche e pertinenza alla call. Le guide generali non introducono obblighi automaticamente.

## Guardrail
Distinguere VERIFICATO (fonte e data), DA_CONFERMARE, IPOTESI, PROPOSTA, DECISIONE_APPROVATA, MANCANTE, NON_APPLICABILE. Non inventare dati, autorizzazioni, impegni, fonti o obblighi; non elevare stati per inferenza. Nessuna azione esterna, modifica di documenti ufficiali o certificazione di ammissibilità/conformità.

## Esiti
COMPLETO quando gli elementi applicabili sono documentati; PARZIALE se mancano evidenze; BLOCCATO_DA_FONTI se un conflitto decisivo impedisce conclusioni affidabili. Nessun esito garantisce finanziamento.

## Scenari da verificare (non eseguiti)
- Aiuti pregressi ignoti: non dichiarare plafond disponibile
- non applicare regime generale a settori speciali senza verifica.
- Call o fonte applicabile assente: nessun esito definitivo, evidenziare lacune.
