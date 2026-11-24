---
name: eu-funding-project-intelligence
description: Ricerca e confronto di progetti UE finanziati per progetti finanziati dall'UE; produce evidenze tracciabili e risultati adattati alla call senza inventare dati.
---

# EU Funding Project Intelligence

## Scopo
Ricerca e confronto di progetti UE finanziati. Specializzazione autonoma a supporto delle skill di progettazione, redazione e gestione esistenti; non sostituisce verifica di ammissibilità, budget ammissibile o formulario ufficiale.

## Input
Call, settore, paesi, periodo, criteri di confronto. Identificare versione e fonte del materiale; se manca la call dichiarare NON_VERIFICATO.

## Procedura
1. Definire query riproducibili e criteri inclusione/esclusione.
2. Cercare CORDIS, Funding & Tenders e KEEP.
3. Registrare ID progetto, programma, date, contributo UE distinto dal costo totale, coordinatore e risultati pubblici.
4. Deduplicare per ID e distinguere dati mancanti da zero.
5. Confrontare progetti per topic, maturità e contesto.
6. Estrarre gap e lezioni senza dedurre fattori causali di successo da soli vincitori.

## Output
Registro progetti con ID, URL, data, criteri, dati comparabili, limiti del campione e implicazioni progettuali.
Per ogni elemento indicare ID, fonte, data, stato e motivazione; registrare lacune e decisioni pendenti. Usare il dossier condiviso solo per campi compatibili, mantenendo l'output specialistico separato.

## Fonti
- https://cordis.europa.eu/projects
- https://keep.eu/
Punti di accesso da verificare al momento dell'uso; individuare il documento preciso e la versione. Le regole della call e del contratto prevalgono sulle guide metodologiche.

## Guardrail
Non inventare dati, fonti, risultati, punteggi, partner o obblighi. Stati: VERIFICATO, DA_CONFERMARE, IPOTESI, PROPOSTA, DECISIONE_APPROVATA, MANCANTE, NON_APPLICABILE. Nessuna azione esterna o invio di candidature. Non elevare stati per inferenza.

## Esiti
COMPLETO per output documentato, PARZIALE per lacune, BLOCCATO_DA_FONTI per conflitti decisivi. Nessuna certificazione di finanziabilità.

## Scenari da verificare (non eseguiti)
- Campione di soli vincitori: non stimare probabilità di finanziamento
- importi assenti: non imputare zero.
- Call non identificata: fornire solo metodologia, senza obblighi inventati.
