# Casi limite per verificare l'uso della skill

Gli scenari sono **sintetici**, non call reali. Non devono comparire nel report come opportunità attive.

| Caso | Input sintetico | Output atteso | Errore da evitare |
| --- | --- | --- | --- |
| 1. Call con più topic | Una call contiene 8 topic, uno solo coerente | Risultato riferito al topic coerente, con call padre e topic ID | Attribuire alla singola proposta budget complessivo della call |
| 2. Due fasi | Topic con prima e seconda scadenza | Indicare stage 1 e stage 2 e condizioni di invito | Dire che ci si può candidare direttamente allo stage 2 |
| 3. Multi-cut-off | Un topic resta attivo con cut-off successivi | Stato riferito alla finestra utilizzabile al momento della verifica | Confondere cut-off scaduto con chiusura definitiva dell'intero topic |
| 4. Costituzione non ancora avvenuta | Il beneficiario è una startup da costituire | `CONDIZIONATO` o `NON_VERIFICATO` finché non si verifica la disciplina specifica | Affermare ammissibilità per analogia con altri programmi |
| 5. Importi di livello diverso | La call ha €100m, il topic €10m, il contributo indicativo è €2m | Tre campi separati più tasso e spese se documentati | Presentare €100m come finanziamento ottenibile per singolo progetto |
| 6. Avviso regionale | Il progetto cerca FESR Lazio | Trovare l'avviso nell'autorità competente, con ID/link/budget se esistenti | Inventare un identificativo Horizon o limitarsi al Funding & Tenders Portal |
| 7. Appalto | Search restituisce `call for tenders` | Scartare se il mandato riguarda sovvenzioni e motivare | Equiparare appalto a grant |
| 8. Fonte inaccessibile | Snippet suggerisce data e importi ma il record non è apribile | `STATO_NON_VERIFICATO` e dati non verificati | Dichiarare aperto senza consultare la fonte primaria |
| 9. Programma noto, topic inesistente | Work programme parla di un'azione ma non vi è record di topic pubblicato | Evidenziare «azione programmata», non una call aperta | Inventare ID e deadline |
| 10. Modifica successiva | Corrigendum aggiorna un termine | Riferire versione corretta con link e data | Riutilizzare la scadenza del documento superato |
| 11. Rettifica scadenze | Nuova versione della call proroga di 30 giorni i termini (fonte primaria) | Scheda di differenze prima/dopo con URL, documento e sezione; avviso di riesame per le skill successive | Dichiarare in assoluto che «non esistono modifiche» o riscrivere decisioni senza conferma |
| 12. Nessuna variazione | Il record ufficiale è invariato rispetto alla verifica precedente | «Nessuna variazione ufficiale rilevata nelle fonti controllate alla data X», con elenco fonti | Affermare genericamente che il bando «non è mai cambiato» |
| 13. Fonte indisponibile | Il portale dell'autorità non risponde durante il controllo | «Non verificabile alla data X»; indisponibilità non equivale a assenza di rettifiche | Riportare «nessuna variazione» per sola indisponibilità |
| 14. Monitoraggio richiesto | L'utente chiede «tieni d'occhio il topic» eseguito in background | Preparare la lista di fonti da monitorare e la scheda vuota; chiarire che l'esecuzione ricorrente richiede uno strumento esterno attivato a parte | Attivare verifiche ricorrenti o notifiche di propria iniziativa |

Il solo script `check_skill.py` non esegue questi scenari su un agente: vanno usati come checklist per prove funzionali future.
