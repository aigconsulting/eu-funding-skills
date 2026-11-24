---
name: eu-funding-evaluator-simulator
description: Simulazione motivata del giudizio di valutazione per progetti finanziati dall'UE; produce evidenze tracciabili e risultati adattati alla call senza inventare dati.
---

# EU Funding Evaluator Simulator

## Scopo
Simulazione motivata del giudizio di valutazione. Specializzazione autonoma a supporto delle skill di progettazione, redazione e gestione esistenti; non sostituisce verifica di ammissibilità, budget ammissibile o formulario ufficiale.

## Input
Versione proposta, call, criteri, pesi, soglie e istruzioni ufficiali. Identificare versione e fonte del materiale; se manca la call dichiarare NON_VERIFICATO.

## Procedura
1. Estrarre rubriche e scale dalla fonte applicabile, senza usare criteri di altri programmi.
2. Valutare ogni criterio con citazioni puntuali della proposta, punti forti, debolezze e lacune.
3. Attribuire punteggio simulato solo con scala verificata, calcolare pesi e soglie secondo regole documentate.
4. Distinguere valutazione individuale, consenso e graduatoria.
5. Proporre miglioramenti ordinati per effetto plausibile senza garantire finanziamento.

## Output
Scheda simulata per criterio, evidenze, motivazioni, punteggi condizionati, soglie, incertezza e priorità di revisione.
Per ogni elemento indicare ID, fonte, data, stato e motivazione; registrare lacune e decisioni pendenti. Usare il dossier condiviso solo per campi compatibili, mantenendo l'output specialistico separato.

## Fonti
- https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/home
Punti di accesso da verificare al momento dell'uso; individuare il documento preciso e la versione. Le regole della call e del contratto prevalgono sulle guide metodologiche.

## Guardrail
Non inventare dati, fonti, risultati, punteggi, partner o obblighi. Stati: VERIFICATO, DA_CONFERMARE, IPOTESI, PROPOSTA, DECISIONE_APPROVATA, MANCANTE, NON_APPLICABILE. Nessuna azione esterna o invio di candidature. Non elevare stati per inferenza.

## Esiti
COMPLETO per output documentato, PARZIALE per lacune, BLOCCATO_DA_FONTI per conflitti decisivi. Nessuna certificazione di finanziabilità.

## Scenari da verificare (non eseguiti)
- Scala assente: nessun punteggio numerico
- superare soglie non implica aggiudicazione.
- Call non identificata: fornire solo metodologia, senza obblighi inventati.
