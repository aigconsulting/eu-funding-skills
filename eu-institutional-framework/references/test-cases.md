# Casi di test comportamentali — Skill 00

Piano di prova: **nessuno dei casi è un test agentico già eseguito**. Ogni verifica va condotta su fonti autentiche, giudicando la risposta effettiva del modello, non la presenza di parole chiave.

| ID | Scenario | Output atteso | Errore da evitare |
| --- | --- | --- | --- |
| T1 | «Consiglio europeo o Consiglio dell'UE: come legislano?» | Distingue i due soggetti con ruoli corretti e fonti | Confondere indirizzo strategico e co-legislazione |
| T2 | «Chi amministra il bilancio UE?» | Distingue chi adotta il bilancio (PE + Consiglio), chi lo gestisce (per programmi), chi controlla (Corte dei conti) | Attribuire tutto alla sola Commissione |
| T3 | «Quale DG gestisce il programma X?» | Risponde solo con fonte primaria aggiornata, con periodo; se non riscontrabile, `NON_VERIFICATO` | Deducere la DG per analogia o dai nomi dei programmi |
| T4 | «Che differenza c'è tra agenzia esecutiva e agenzia decentralizzata?» | Espone la distinzione con atti istitutivi: agenzia esecutiva (delega della Commissione) vs agenzia decentralizzata (base giuridica propria) | Equiparare tutte le agenzie o inventare la base giuridica |
| T5 | «Chi gestisce le call di Programma Y?» | Ricostruisce il nesso istituzione → DG/autorità/agenzia → programma, e rimanda le call a Skill 01-03 | Affermare che tutte le call si trovano su Funding & Tenders Portal |
| T6 | Organo non precompilato nella mappa (es. EISMEA) | Scheda dinamica: denominazione, mandato, rapporto istituzionale e programmi gestiti, con fonti e data di verifica; se non verifica, dichiarare il limite | Rispondere solo dalla conoscenza pregressa senza fonti |
| T7 | «Ricostruisci la catena di adozione del QFP» | Descrive fasi con atti e attori, distinguendo QFP da annuario | Presentare una catena universale senza fonte |
| T8 | Client senza accesso web | Dichiarare che la verifica dinamica non è eseguibile; usare soltanto la mappa statica, ben interpretata, e dichiarare il limite | Simulare una consultazione aggiornata |
