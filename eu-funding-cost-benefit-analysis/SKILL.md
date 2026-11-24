---
name: eu-funding-cost-benefit-analysis
description: Analisi costi-benefici e sensitività per progetti finanziati dall'UE; produce evidenze tracciabili e risultati adattati alla call senza inventare dati.
---

# EU Funding Cost-Benefit Analysis

## Scopo
Analisi costi-benefici e sensitività. Specializzazione autonoma a supporto delle skill di progettazione, redazione e gestione esistenti; non sostituisce verifica di ammissibilità, budget ammissibile o formulario ufficiale.

## Input
Orizzonte, flussi incrementali, alternative, prezzi, tasso e prospettiva. Identificare versione e fonte del materiale; se manca la call dichiarare NON_VERIFICATO.

## Procedura
1. Separare analisi finanziaria e socioeconomica.
2. Costruire scenario senza progetto e flussi incrementali per anno, includere valore residuo motivato.
3. Distinguere prezzi reali/nominali e tasso coerente.
4. Calcolare VAN come somma flussi netti attualizzati, rapporto benefici/costi con definizione esplicita e TIR solo se interpretabile.
5. Verificare segni, unità, trasferimenti, doppio conteggio, esternalità e sensitività.
6. Non assumere tasso UE universale.

## Output
Tabella flussi, formule e risultati riproducibili, scenari e soglie di pareggio, benefici non monetizzati.
Per ogni elemento indicare ID, fonte, data, stato e motivazione; registrare lacune e decisioni pendenti. Usare il dossier condiviso solo per campi compatibili, mantenendo l'output specialistico separato.

## Fonti
- https://commission.europa.eu/law/law-making-process/better-regulation_en
- https://ec.europa.eu/regional_policy/
Punti di accesso da verificare al momento dell'uso; individuare il documento preciso e la versione. Le regole della call e del contratto prevalgono sulle guide metodologiche.

## Guardrail
Non inventare dati, fonti, risultati, punteggi, partner o obblighi. Stati: VERIFICATO, DA_CONFERMARE, IPOTESI, PROPOSTA, DECISIONE_APPROVATA, MANCANTE, NON_APPLICABILE. Nessuna azione esterna o invio di candidature. Non elevare stati per inferenza.

## Esiti
COMPLETO per output documentato, PARZIALE per lacune, BLOCCATO_DA_FONTI per conflitti decisivi. Nessuna certificazione di finanziabilità.

## Scenari da verificare (non eseguiti)
- Flussi con più cambi di segno: segnalare TIR multipli o ambigui
- tasso mancante: nessun VAN definitivo.
- Call non identificata: fornire solo metodologia, senza obblighi inventati.
