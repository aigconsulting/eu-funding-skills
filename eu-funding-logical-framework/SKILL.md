---
name: eu-funding-logical-framework
description: Costruisce e revisiona il Logical Framework (LFA, logframe, quadro logico) di un progetto UE, con analisi causale, catena dei risultati, indicatori, baseline, target, fonti di verifica e assunzioni, adattando il formato alla call e senza inventare evidenze.
---

# EU Funding Logical Framework

## Scopo
Specializzare la logica d'intervento prodotta da eu-funding-project-designer in una matrice verificabile, utilizzabile anche autonomamente per progettazione, revisione e monitoraggio. Il Logical Framework Approach è un metodo analitico; la matrice è uno dei suoi prodotti. Non presumere che sia obbligatoria per ogni programma UE.

## Input
Idea o dossier progettuale, call/topic e versione del formulario, analisi dei bisogni, stakeholder, risorse, dati e fonti disponibili. Se manca la call, dichiarare NON_VERIFICATO e produrre soltanto un modello metodologico.

## Procedura
1. Identificare fonte applicabile e formato richiesto; distinguere requisiti del bando da suggerimenti metodologici. Consultare [fonti](references/official-sources.md).
2. Analizzare stakeholder, beneficiari, problema centrale, cause ed effetti. Costruire albero dei problemi e albero degli obiettivi; verificare relazioni causali e selezionare la strategia motivando alternative e limiti.
3. Formalizzare la catena attività → output → outcome → impatto; attribuire identificativi stabili e collegare ogni elemento al livello superiore. Distinguere prodotti direttamente controllabili da cambiamenti attesi e contributi a impatti di lungo periodo. Non confondere deliverable, milestone e indicatori.
4. Costruire la matrice secondo il [modello](references/output-template.md), adattandola alle colonne e ai livelli del formulario ufficiale. Per ogni risultato definire indicatori pertinenti, unità, formula e popolazione, baseline con data, target con scadenza, fonte di verifica, metodo e frequenza di rilevazione; disaggregazioni quando pertinenti. Responsabili solo se confermati. Non usare zero al posto di una baseline ignota.
5. Esplicitare assunzioni esterne per ciascun nesso causale, precondizioni, rischi, probabilità e impatto qualitativi motivati, mitigazioni proposte e rischi residui. Se un'assunzione critica non è plausibile, rivedere la strategia.
6. Verificare logica verticale (risultati e assunzioni rendono plausibile il livello superiore) e orizzontale (indicatori misurano effettivamente il risultato e sono verificabili con fonti accessibili). Controllare coerenza con attività, risorse, tempi, budget, criteri e indicatori obbligatori documentati. Segnalare conflitti e lacune senza correggerli implicitamente.
7. Consegnare matrice, schede indicatori, mappa causale, assunzioni/rischi e rapporto di qualità. Trasmettere i soli campi compatibili al dossier condiviso senza estenderne lo schema; mantenere la matrice come allegato separato. Riutilizzare identificativi e fonti con eu-funding-proposal-drafter, eu-funding-proposal-reviewer, eu-funding-project-manager e eu-funding-reporting-manager. In monitoraggio distinguere target approvati, valori rilevati e variazioni proposte; non riscrivere retroattivamente le baseline.

## Guardrail
Nessun dato inventato: distinguere VERIFICATO (fonte e data), DA_CONFERMARE, IPOTESI, PROPOSTA, DECISIONE_APPROVATA, MANCANTE, NON_APPLICABILE. Non elevare stati per inferenza; non dichiarare attribuzione causale dimostrata sulla sola base della matrice. Il bando e il contratto applicabili prevalgono. Nessuna azione esterna, presentazione di domanda o modifica di sistemi.

## Esiti
MATRICE_COMPLETA se tutti gli elementi applicabili sono documentati; MATRICE_PARZIALE se vi sono lacune; BLOCCATA_DA_FONTI se un conflitto decisivo impedisce una conclusione affidabile. Nessun esito certifica finanziabilità. Eseguire i controlli statici con scripts/check_skill.py; gli scenari in [test-cases.md](references/test-cases.md) sono prove agentiche da svolgere, non già eseguite.
