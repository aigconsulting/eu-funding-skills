---
name: eu-funding-project-designer
description: Supporta la costruzione sostanziale del progetto per una opportunita' di finanziamento UE - contesto e bisogni, obiettivi, logica d'intervento, attivita', risultati, impatti e indicatori verificabili - con separazione esplicita fra fatti verificati, dichiarazioni dell'utente, ipotesi e proposte; produce un dossier tracciabile per compilare il formulario della call o del avviso, senza dati inventati.
---

# EU Funding Project Designer — Skill 11

## Scopo

Supportare la **progettazione sostanziale del progetto** candidato a finanziamento UE: analisi del contesto e dei bisogni, definizione degli obiettivi, logica d'intervento, attività, risorse, risultati, impatti, indicatori e modalità di verifica. La skill si colloca logicamente **tra la pianificazione della candidatura (Skill 06) e la redazione nel formulario ufficiale (Skill 07)**, senza rinumerare le skill esistenti.

Non è una seconda `eu-funding-proposal-drafter`: la progettazione dell'intervento è **distinta dalla compilazione** del modello di domanda. Non redige il formulario, non valuta ammissibilità (Skill 04) e non costruisce i calcoli economici (Skill 05); non presenta candidature e non effettua azioni esterne.

## Input

- **Opportunità (consigliata)**: identificativo call/topic/avviso e link ufficiale, programma e ciclo QFP, per adattare il lessico della progettazione.
- **Materiali del proponente**: idea, contesto, destinatari, dati e fonti disponibili, risorse, partner, vincoli; ogni informazione riporta provenienza e stato di conferma.
- **Eventuali output** della pianificazione (Skill 06) o un dossier condiviso esistente, con fonti e versioni.

Se non è noto l'avviso applicabile, dichiararlo con `NON_VERIFICATO` e proseguire la progettazione senza regole del bando; non applicare una regola per analogia.

## Procedure

1. **Analisi di contesto e bisogni.** Territorio o settore di riferimento, destinatari finali e intermediari, stakeholder, problema affrontato, cause ed effetti, dati di base con fonti (ufficiali, statistiche, studi) oppure dichiarazioni da confermare, vincoli e fabbisogni. Ogni dato con il proprio stato: `VERIFICATO` (con fonte e data), `DICHIARAZIONE_UTENTE_DA_CONFERMARE`, `IPOTESI`.
2. **Obiettivi e logica d'intervento.** Definire obiettivo generale, obiettivi specifici, output, outcome e impatti secondo il lessico pertinente al programma (senza assumere che valga ovunque): costruire una teoria del cambiamento comprensibile e falsificabile nella forma `problema → intervento → attività → output → outcome → impatto`, con assunzioni e condizioni esterne esplicite.
3. **Soluzione e attività.** Approccio proposto, attività con sequenza logica e dipendenze, risorse, risultati attesi, rischi e condizioni esterne. Work package, milestone e deliverable solo se utili o prescritti dall'opportunità specifica, con la fonte che li prescrive.
4. **Indicatori verificabili.** Per ciascun risultato o obiettivo significativo: indicatore, definizione, unità di misura, baseline, target, periodo, fonte o metodo di rilevazione; la responsabilità di rilevazione è assegnata **solo se realmente determinata**. Non inventare baseline, target e valori; le stime restano `STIMA_NON_VALIDATA`, non dati.
5. **Coerenza e test di qualità.** Verificare la continuità problema → intervento → attività → output → outcome → impatto, la proporzionalità fra risorse e obiettivi, la copertura dei rischi e la verificabilità dei risultati. Esporre alternative, lacune e decisioni ancora da approvare; un progetto plausibile non equivale a una candidatura ammissibile o finanziabile.
6. **Dossier di progetto.** Produrre una scheda conforme al [modello](references/output-template.md) con `progetto`, `evidenze` e `requisiti` compatibile col [dossier condiviso](../dossier/README.md) e con gli stati `VERIFICATO`, `DA_CONFERMARE`, `IPOTESI`, `PROPOSTA`, `DECISIONE_APPROVATA`, `MANCANTE`, `NON_APPLICABILE`; una fonte per ogni fatto documentato.
7. **Passaggio alla Skill 07.** Consegnare il dossier per la redazione: la Skill 07 adatta i contenuti al formulario ufficiale della call/topic/avviso **senza** importare obblighi inesistenti; l'appropriazione delle fonti, versioni e assenze resta a carico del dossier.

## Guardrail inderogabili

- **Non inventare**: nessun bisogno, dato statistico, risultato pregresso, valore baseline/target, indicatore normativamente imposto, partner, risorsa o impegno. Le partenze rimaste senza base sono etichettate `IPOTESI` o `PROPOSTA`.
- **Il singolo avviso prevale**: consultare le fonti ufficiali correnti per regole e criteri del bando specifico; le linee del [metodo](references/design-method.md) non sostituiscono mai l'atto applicabile.
- **Se manca la fonte**, segnalarlo chiaramente; se mancano dati progettuali, mantenere segnaposto `[DA INTEGRARE: ...]` e alternative esplicite. Un progetto plausibile **non equivale** a una candidatura ammissibile o finanziabile.
- **Nessuna azione esterna**: nessun contatto con terzi, tutti partenariati o impegno risorse senza autorizzazione specifica.

## Programmi e cicli

Il metodo si adatta a programmi e cicli diversi (Horizon Europe, Digital Europe, Erasmus+, LIFE, Creative Europe, Interreg e avvisi FESR/FSE+), **senza presupporre una struttura unica dei progetti o che tutti gli indicatori siano obbligatori**: la struttura richieste segue sempre la fonte della specifica opportunità. Le distinzioni fra cicli restano compito delle skill 06 e 07, non qui duplicate.

## Esiti

- `DOSSIER_COMPLETO`: elementi minimi impostati con stati e fonti; non attesta la qualità del progetto né l'ammissibilità.
- `DOSSIER_PARZIALE`: dati o fonti ancora mancanti; segnaposto e alternative conservati.
- `BLOCCATA_DA_FONTI`: assenza di base documentale verificabile o conflitto decisivo segnalato, senza fine progettazione affidabile.

## Verifiche e limiti

- `python3 eu-funding-project-designer/scripts/check_skill.py`: controlli statici di struttura e guardrail.
- [design-method.md](references/design-method.md) elenca le fonti di metodo; [test-cases.md](references/test-cases.md) racchiude gli scenari da provare con un agente. Nessuna verifica automatica attesta la qualità sostanziale del progetto o l'ammissibilità.
