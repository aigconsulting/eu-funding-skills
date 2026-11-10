---
name: eu-funding-application-planner
description: Pianifica la preparazione di candidature a bandi finanziati dall'UE in modo indipendente dal programma: acquisisce avviso, istruzioni e allegati ufficiali, distingue obblighi da suggerimenti, ricostruisce requisiti documentali, fasi e criteri e produce una checklist verificabile senza inventare procedure né presentare la domanda.
---

# EU Funding Application Planner — Skill 06

## Scopo e perimetro

Produrre, per **una specifica opportunità di finanziamento**, un piano documentato per preparare la candidatura. La skill è trasversale: **nessun programma** o fondo europeo costituisce il modello predefinito per gli altri e non utilizza un template universale di proposta. Le strutture (fasi, moduli, documenti, requisiti di firme o registrazione, ruoli, portali, criteri) vengono sempre estratte dalle **istruzioni effettivamente applicabili all'avviso**.

L'attività è **analisi e pianificazione**, non esecuzione della candidatura. Non presentare una domanda, non compilare un portale, non registrare organizzazioni, non impegnare partner, non inviare comunicazioni e non dichiarare requisiti soddisfatti senza riscontro.

La skill non sostituisce le skill 03–05: può usare le schede di ricerca, ammissibilità e analisi finanziaria già disponibili, ma riconferma i dati determinanti sulla documentazione vigente e indica le discrepanze.

## Input

- Identificativo e URL ufficiale dell'**avviso/call/topic** o informazioni sufficienti a individuarlo univocamente; **versione/fase** e data di consultazione.
- Profilo sintetico del candidato/progetto, se disponibile: natura del soggetto, ruolo, idea, consorzio, risorse e informazioni già documentate. I dati mancanti restano sconosciuti.
- Vincoli espressi dall'utente, se presenti: periodo, budget, partner, formato desiderato; non trasformarli in regole del bando.

Se manca una fonte primaria identificabile, produrre solo una **scheda di documenti da recuperare** e classificare il piano `BLOCCATO_DA_FONTI`, senza inventare modulistica o requisiti. Se la fase non è nota, identificarla dal bando e dalle sue modifiche ufficiali o segnalare il dato mancante.

## Principio fondamentale: regole contestuali, nessun travaso

1. **Identificare prima** programma/fondo, autorità competente, modalità di gestione (diretta, concorrente, indiretta), procedura, fase, identificativo dell'opportunità e canale ufficiale.
2. Consultare **la documentazione del singolo avviso**: testo, documenti allegati, application guidance, schemi di domanda, moduli economici, criteri, addenda, rettifiche/corrigenda e FAQ ufficiali quando applicabili. Verificare la versione e l'ambito di efficacia di ogni documento.
3. Non imporre **parti A/B, PIC, consorzi, work package, Gantt, budget per categoria, limiti di pagina, criteri o pesi, lettere di impegno, firme digitali o regole di lingua**: registrarli solo se richiesti o ammessi dalla fonte del caso.
4. Distinguere con precisione `OBBLIGATORIO`, `CONDIZIONALE`, `FACOLTATIVO`, `SUGGERIMENTO` e `NON_VERIFICATO`. Una buona pratica redazionale **non diventa** obbligo del bando.
5. Ogni requisito, allegato, fase e scadenza determinante ha **citazione diretta** a fonte ufficiale, sezione/pagina, data di consultazione e ambito; in mancanza, stato `NON_VERIFICATO`.
6. Le scadenze delle **diverse fasi** possono essere differenti; registrare data, ora, fuso, cut-off e regole di caricamento soltanto se verificati, senza fissare scadenze interne inventate.
7. Se una fonte ufficiale è contraddittoria o non è chiara la versione applicabile, riportare il conflitto, classificare `BLOCCATO_DA_FONTI` per i passaggi coinvolti e indicare la richiesta di chiarimento come **proposta**, non azione eseguita.

Vedi [protocollo delle fonti](references/source-protocol.md) e [fonti istituzionali](references/official-sources.md).

## Procedura operativa

### 1. Identità della candidatura e set documentale

Registrare: ID, titolo, programma/fondo, autorità/organismo attuatore, canale di candidatura, modalità di gestione, fase attuale, stato dell'apertura e scadenza verificati, URL diretto. Costruire un **registro fonti** con tipo documento, link, versione, data, lingua, ruolo nel procedimento e stato di verifica. Un sito informativo terzo serve solo a individuare la fonte primaria.

### 2. Separazione fra condizioni di accesso e preparazione

Dalla documentazione estrarre: requisiti di ammissibilità e di finanziabilità (rinviando alla Skill 04 per approfondimenti), condizioni formali di domanda, obblighi delle specifiche sezioni progettuali, criteri di selezione/valutazione e relative soglie quando presenti. Non confondere il punteggio di merito con un documento obbligatorio; non attribuire il merito all'autorità prima della valutazione.

### 3. Struttura *reale* della proposta

Rilevare i campi e moduli di domanda **esattamente come previsti nella fase applicabile**: contenuti narrativi, form on-line, modelli, allegati, bilancio, dichiarazioni, documenti sulla capacità del soggetto o del partenariato, eventuali prove richieste a candidatura/contrattualizzazione. Conservare la **denominazione ufficiale** del documento e l'eventuale lingua/formato/limite. Se l'avviso non richiede una categoria, non inserirla nella checklist come obbligatoria.

### 4. Piano di preparazione, senza workflow presunto

Per ogni deliverable documentato, associare: `id_requisito`, titolo ufficiale, soggetto/ruolo cui compete **secondo la fonte**, contenuto atteso, precondizione documentata, fonte, fase, termine esterno, disponibilità della prova (`DISPONIBILE`, `DA_ACQUISIRE`, `DA_REDARE`, `DA_CONFERMARE`), eventuale dipendenza. **Non assegnare responsabili, tempistiche interne, automazioni o strumenti non richiesti**. Se utile, indicare separatamente *una proposta organizzativa* e richiedere decisione prima di trasformarla in impegno.

### 5. Criteri di valutazione e coerenza narrativa

Per ogni criterio effettivamente previsto, riportare denominazione, eventuale punteggio/peso/soglia, evidenze o contenuti che devono rispondere al criterio e relativo riferimento documentale. Quando non è disponibile una griglia ufficiale, non inventarne una. Suggerimenti per chiarezza, coerenza e completezza devono essere **esplicitamente etichettati come suggerimenti**, non come obblighi.

### 6. Controlli preliminari di completezza

Preparare una matrice controllabile delle condizioni formali e dei documenti richiesti dalla **fase attuale**: `VERIFICATO_PRESENTE`, `MANCANTE`, `NON_VERIFICATO`, `NON_APPLICABILE`, motivazione e link. Controllare coerenza con requisiti soggettivi e costi già esaminati, segnalando eventuali discrepanze senza risolverle automaticamente. Non dichiarare una candidatura `PRONTA` se mancano prove obbligatorie oppure il sistema di presentazione non è stato verificato.

### 7. Sintesi e prossimo passo

Restituire: fonte e versione, fase e scadenza verificate, checklist **obbligatoria** e condizioni, sezioni/criteri previsti, lacune, eventuali conflitti e **prossima verifica informativa**. Non dichiarare attività esterne eseguite. Seguono i [campi di output](references/output-template.md) e gli [scenari di verifica](references/test-cases.md).

## Classificazione dei risultati

- `PIANO_DOCUMENTATO`: documentazione vigente e requisiti determinanti identificati, senza presumere che i materiali del beneficiario siano pronti.
- `PIANO_PARZIALE`: parte della disciplina è documentata, parte ancora `NON_VERIFICATO`; specificare impatto e documenti necessari.
- `BLOCCATO_DA_FONTI`: mancano le fonti decisive, esiste una contraddizione non risolta oppure non è identificabile l'avviso esatto.
- `SCADENZA_TRASCORSA`: termine della fase verificato nel passato; descrivere solo l'eventuale fase successiva se ufficialmente accessibile, altrimenti non prospettare candidature tardive.

Questi sono **stati informativi**, non giudizi ufficiali di ammissibilità o successo. La conclusione non implica diritto al finanziamento, superamento dei controlli del portale né candidatura depositata.

## Regole di prudenza

- Nessun elenco universale di documenti: i campi della tabella d'output si riempiono **solo dopo** la lettura dell'avviso.
- Un portale unificato può ospitare procedure di programmi differenti; ciò non autorizza a considerarle identiche.
- Le istruzioni su deleghe, firme, riservatezza, documenti finanziari e dichiarazioni possono mutare per fase e per soggetto; non attribuirle senza fonte.
- Per avvisi territoriali/cofinanziati usare **l'autorità responsabile dell'avviso** e la relativa documentazione, non regole di un programma diverso.
- In presenza di pagine o PDF non accessibili, indicare esplicitamente la mancata lettura, senza inventare contenuto.
- Evitare la raccolta di informazioni personali e riservate non necessarie alla preparazione del piano.

## Test e limiti

Eseguire dalla radice del pacchetto `python3 eu-funding-application-planner/scripts/check_skill.py`. Il controllo verifica **solo** struttura e guardrail testuali, non l'adeguatezza giuridica né la capacità dell'agente di interpretare una call. I casi in [references/test-cases.md](references/test-cases.md) sono scenari di prova **non eseguiti**. La skill non crea submission, account, dossier né invia candidature.
