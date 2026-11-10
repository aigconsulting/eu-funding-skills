---
name: eu-institutional-framework
description: Spiega e ricostruisce il quadro istituzionale dell'Unione europea - istituzioni, organi consultivi, articolazione della Commissione, direzioni generali, agenzie esecutive e decentralizzate e i processi decisionali e di bilancio (QFP) - per capire chi decide, chi amministra e chi gestisce i finanziamenti, senza inventare competenze o mandati.
---

# EU Institutional Framework — Skill 00

## Obiettivo

Spiegare e ricostruire **come funziona l'Unione europea** e quali soggetti intervengono nell'indirizzo politico, nella produzione normativa, nel bilancio e nell'attuazione di politiche e programmi. Rispondere in italiano, mantenendo la denominazione ufficiale in inglese quando utile.

La skill è **istituzionale e conoscitiva**: non cerca bandi (vedi Skill 01–03), non valuta ammissibilità né propone candidature. Rimanda alla Skill 01 (`eu-funding-hierarchy`) la ricostruzione della gerarchia programma → work programme → call → topic e degli avvisi in gestione concorrente o indiretta.

## Input

Accettare come punto di partenza uno dei seguenti: nome di un'istituzione, organo, direzione generale o agenzia; un processo (legislativo, di bilancio, adozione del QFP, gestione di un programma); un nesso del tipo «chi gestisce cosa»; una domanda generica («Chi decide il bilancio UE?»). Se il soggetto non è presente nella [mappa statica](references/institutional-map.md), procedere con la ricerca dinamica usando le fonti primarie.

## Procedure

### A — Spiegazione e ricostruzione dalla mappa statica

1. **Classificare il soggetto** con la [mappa](references/institutional-map.md): istituzione, organo consultivo, altro organismo, direzione generale (DG), agenzia esecutiva, agenzia decentralizzata/organismo di Unione. Non qualificare impropriamente come «istituzioni» gli organi consultivi o le agenzie.
2. **Separare gli assi**: stabili (ruoli previsti dai Trattati), variabili (portafogli del collegio dei commissari, commissari in carica, organigrammi, deleghe, mandati) e interpretazioni o collegamenti strategici. Dagli assi variabili sempre i periodi di riferimento e le fonti.
3. **Reperire le fonti primarie** indicate in [official-sources.md](references/official-sources.md): portali istituzionali, EUR-Lex (atti istitutivi e mandati), EU Whoiswho, organigrammi ufficiali. Non usare una fonte generica come prova di un mandato specifico.
4. **Costruire la risposta** secondo [output-template.md](references/output-template.md) con stati `VERIFICATO`, `PARZIALE`, `NON_VERIFICATO`, `NON_APPLICABILE`. Rendere visibili i nessi non documentati, senza riempirli per analogia.

### B — Ricerca istituzionale dinamica (su richiesta, per soggetti non nella mappa)

1. **Identificare il soggetto**: denominazione ufficiale, sigle, omonimie, tipologia e stato attuale o storico. Le sigle cambiano nel tempo: verificare sempre la denominazione in uso all'anno di interesse.
2. **Consultare le fonti primarie pertinenti**: repertorio ufficiale delle istituzioni e degli organismi UE, EU Whoiswho, sito del soggetto, pagine istituzionali della Commissione (per DG e agenzie esecutive), EUR-Lex per atti di istituzione e mandati, documentazione ufficiale sui programmi gestiti.
3. **Restituire una scheda verificabile** con: denominazione; natura giuridico-istituzionale; missione e mandato; competenze; struttura e rapporto con le istituzioni; eventuali programmi di finanziamento di cui è **effettivamente** responsabile, con una fonte per ciascuno; data di consultazione; periodo o versione delle informazioni.
4. **Separare** fatti documentati, dati non reperiti, informazioni storiche e inferenze. Non attribuire competenze o programmi per analogia. Se il client non ha accesso al web o le fonti non sono accessibili, **dichiarare il limite**: non simulare una consultazione aggiornata e non rispondere solo dalla conoscenza pregressa presentandola come verifica.

### C — Ricostruzione dei processi decisionali e finanziari

Su richiesta, ricostruire: orientamenti politici; iniziativa normativa della Commissione per la legislazione ordinaria; procedure legislative (ordinaria e speciali) con Parlamento e Consiglio; adozione del bilancio annuale; accordo e revisione del QFP; attuazione dei programmi e controllo (Corte dei conti, contenzioso). Distinguere sempre i procedimenti: non esiste una catena gerarchica universale. Verificare il procedimento applicabile dalla fonte ufficiale, con versione e periodo.

## Regole di classificazione essenziali

- **Consiglio europeo ≠ Consiglio dell'Unione europea**: il primo riunisce i Capi di stato o di governo e dà indirizzi politici; il secondo riunisce i ministri e legisla con il Parlamento. Non spostare i ruoli.
- **Commissione ≠ Parlamento**: la Commissione propone e attua; il Parlamento co-decide, adotta il bilancio con il Consiglio e esercita funzione di controllo. Le competenze vanno verificate sul testo applicabile.
- **Gestione diretta ≠ concorrente ≠ indiretta**: non ogni DG o agenzia ha potere di approvare o concedere finanziamenti. In gestione concorrente le autorità nazionali e regionali gestiscono gli avvisi; in gestione indiretta interviene un organismo incaricato. Ricostruire il nesso reale istituzione → responsabilità → DG/autorità/agenzia → programma, senza generalizzarlo.
- **Agenzia esecutiva ≠ agenzia decentralizzata/organismo di Unione**: natura, base giuridica e rapporto con le istituzioni differiscono. Descrivere la tipologia con fonte, non per somiglianza.
- **Un programma può seguire percorsi istituzionali diversi**: non presumere che ogni opportunità sia pubblicata sul Funding & Tenders Portal; per la specificità dei bandi rimandare a Skill 01–03.
- **Nessun azione esterna**: la skill si limita al reperimento e all'analisi di informazioni; nessun contatto, registrazione o invio.

## Criteri di qualità dell'output

- Ogni soggetto classificato correttamente (istituzione, organo, DG, agenzia), con fonte primaria per ogni asserzione materiale.
- Ruoli legislativi ed esecutivi tenuti distinti; nessi documentati con URL diretto, data di verifica e periodo.
- Le informazioni organizzative variabili (portafogli, organigrammi, mandati) riportano sempre fonte e periodo; quelle non verificabili restano `PARZIALE` o `NON_VERIFICATO`, mai presentate come fatti.
- Nessun rapporto inventato fra soggetti non collegati da fonte documentata.

## Verifiche e limiti

- `python3 eu-institutional-framework/scripts/check_skill.py`: controllo statico di struttura, metadati e guardrail.
- I test in [test-cases.md](references/test-cases.md) sono piani comportamentali, non test agentici eseguiti. Il controllo statico non certifica la correttezza dei contenuti istituzionali né il comportamento di un agente.

## Esempio di invocazione

> «Che cos'è EISMEA, da chi dipende, quali funzioni svolge e quali programmi UE gestisce? Verifica dalle fonti ufficiali.»

Un agente con accesso al web raccoglie la risposta da pagine e atti specifici (sito del soggetto, EUR-Lex, EU Whoiswho) con link diretti e data di verifica; senza accesso al web dichiarerebbe il limite invece di rispondere solo dalla conoscenza pregressa.
