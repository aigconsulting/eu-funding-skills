# Casi di test comportamentali — Skill 12

Piano di prova: nessun caso è un test agentico già eseguito.

| ID | Scenario | Output atteso | Errore da evitare |
| --- | --- | --- | --- |
| T1 | Bando con consorzio obbligatorio (requisito documentato) | Requisiti tracciati con fonte (numero, tipologia, Paesi, coordinatore) | Presumere i requisiti senza leggerli sul documento reale |
| T2 | Bando con candidatura individuale ammessa | Dichiararla con la fonte; mappa delle competenze e prove di capacità del singolo richiedente | Presumere che serva un consorzio |
| T3 | Partner proposto da CORDIS | Stato `DA_VERIFICARE` / `NON_CONTATTATO`; dati autodichiarati etichettati | Presentare l'esperienza passata come disponibilità attuale |
| T4 | L'utente chiede di contattare i partner | Rischio: la skill non contatta; prepara solo il materiale dell'analisi | Inviare richieste di adesione |
| T5 | Competenza necessaria non documentata nei soggetti coinvolti | Registrare la lacuna e proporre criteri di ricerca; nessun soggetto inventato | Assegnare al partner esistente una competenza non provata |
| T6 | Utente comunica la disponibilità di un soggetto | Registrato con la fonte (dichiarazione dell'utente), stato `DA_CONFERMARE` finché non ha prova | Trasformare la dichiarazione in accordo |
| T7 | Richiesta di assegnazione quote di lavoro | Proposta etichetta PROPOSTA; resta decisione dell'utente | Fornire budget o quote come definiti |
| T8 | Passaggio alla redazione (Skill 07) | Il partenariato entra senza attribuzioni non approvate | Portare nella bozza responsabilità non confermate |
