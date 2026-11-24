---
name: eu-funding-procurement-checker
description: Controllo documentale di acquisti, subappalti e conflitti di interesse per progetti UE; produce analisi e output tracciabili, verificando fonti e regole applicabili senza inventare dati.
---

# EU Funding Procurement Checker

## Scopo
Controllo documentale di acquisti, subappalti e conflitti di interesse. Metodo specialistico autonomo, complementare alle skill di ricerca, progettazione, redazione e attuazione. Non sostituisce decisioni del beneficiario o dell'autorità competente.

## Input
Call, GA, tipo beneficiario, giurisdizione, acquisti, valori, contratti e evidenze. Identificare call, versione, giurisdizione e documenti applicabili. Se mancanti, dichiarare le lacune e limitare l'analisi alla metodologia.

## Procedura
1. Distinguere acquisto, subappalto, contributo in natura e task del beneficiario secondo GA.
2. Verificare natura di stazione appaltante e disciplina nazionale/UE applicabile, soglie e date.
3. Controllare stima aggregata, divieto di frazionamento, scelta procedura, trasparenza e conflitti.
4. Verificare best value o lowest price quando richiesto, documentazione e autorizzazioni.
5. Distinguere ammissibilità del costo da legittimità della procedura.
6. Non selezionare fornitori o avviare procedure.

## Output
Intestazione: progetto, call, versione, data, perimetro, fonti e limiti.

| Acquisto | Categoria GA | Regime/soglia | Valore aggregato | Procedura | Evidenza | Conflitti | Esito |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE | DA INTEGRARE |

Per ogni conclusione registrare evidenza, fonte precisa, data, motivazione e stato; produrre elenco dei gap e decisioni pendenti. Conservare l'output specialistico separato e trasferire solo campi compatibili al dossier condiviso, senza modificarne lo schema.

## Fonti istituzionali
- https://eur-lex.europa.eu/eli/dir/2014/24/oj
- https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home
- https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home

I link sono punti di partenza: verificare accessibilità, documento, versione, data di applicazione, eventuali modifiche e pertinenza alla call. Le guide generali non introducono obblighi automaticamente.

## Guardrail
Distinguere VERIFICATO (fonte e data), DA_CONFERMARE, IPOTESI, PROPOSTA, DECISIONE_APPROVATA, MANCANTE, NON_APPLICABILE. Non inventare dati, autorizzazioni, impegni, fonti o obblighi; non elevare stati per inferenza. Nessuna azione esterna, modifica di documenti ufficiali o certificazione di ammissibilità/conformità.

## Esiti
COMPLETO quando gli elementi applicabili sono documentati; PARZIALE se mancano evidenze; BLOCCATO_DA_FONTI se un conflitto decisivo impedisce conclusioni affidabili. Nessun esito garantisce finanziamento.

## Scenari da verificare (non eseguiti)
- Beneficiario privato non automaticamente soggetto alla direttiva
- più lotti non eludono stima aggregata.
- Call o fonte applicabile assente: nessun esito definitivo, evidenziare lacune.
