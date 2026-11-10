---
name: eu-funding-partnership-designer
description: "Assiste nella definizione del partenariato per una specifica candidatura UE: recupera i requisiti di partenariato del bando da fonti ufficiali, costruisce la mappa delle competenze necessarie e disponibili, ricerca soggetti potenzialmente pertinenti su fonti ufficiali e produce una valutazione comparativa con stati e link; nessun contatto, accordo o quota inventata."
---

# EU Funding Partnership Designer — Skill 12

## Scopo

Assistere nella definizione del **partenariato necessario o opportuno** per una specifica candidatura europea: recuperare i requisiti di partenariato del bando dalla fonte ufficiale, valutare la composizione del consorzio e proporre candidati pertinenti con evidenze documentate. Distinguere sempre i requisiti **obbligatori del bando** dai criteri di composizione **suggeriti**; nessun contatto con soggetti e nessun impegno.

Non duplica le skill adiacenti: usa la progettazione (Skill 11 od i dati del proponente) per la mappa delle competenze e consegna agli output compatibili con pianificazione (06), redazione (07) e dossier condiviso.

## Input

- **Opportunità**: identificativo della call/topic/avviso e documenti ufficiali correnti (requisiti di partecipazione, composizione del consorzio, ruoli).
- **Progettazione corrente**: obiettivi, attività, risultati (Skill 11 o dati del proponente) da cui derivare le competenze necessarie.
- **Soggetti già coinvolti**: con la fonte della relazione (dichiarazione dell'utente o documenti condivisi); senza conferma, restano `DA_VERIFICARE`.

## Procedure

1. **Recuperare i requisiti di partenariato dal bando** sulla fonte ufficiale della specifica call/topic/avviso: numero e tipologia di partecipanti, Paesi eleggibili, ruolo del coordinatore, ammissibilità della candidatura individuale, partner associati, entità terze e vincoli eventuali. **Non presumere** che tutti i bandi richiedano un consorzio: dove la candidatura individuale è ammessa, dichiararlo con la fonte.
2. **Mappa delle competenze**: partire da obiettivi, attività e risultati del progetto; distinguere le competenze documentate dei soggetti già coinvolti (con evidenza) dalle competenze mancanti o **da verificare**; ogni lacuna porta a un requisito di ricerca, non a un soggetto inventato.
3. **Ricerca dei soggetti potenzialmente pertinenti** (su richiesta): usare le fonti ufficiali pertinenti ([official-sources.md](references/official-sources.md)), fra cui **CORDIS** e il partner search ufficiale dove disponibile; separare la **partecipazione a progetti passati** (evidenza documentata) dalla **disponibilità reale a collaborare**, che richiede conferma del soggetto e non si deduce da un database.
4. **Valutazione comparativa**: per ogni candidato registrare denominazione verificata, ambito, evidenze ufficiali, pertinenza proposta, lacune e stato `NON_CONTATTATO` o `DA_VERIFICARE`, salvo dati effettivamente comunicati dall'utente (che restano dichiarati come provenienti dall'utente).
5. **Proposta di copertura dei ruoli**: senza assegnare responsabilità, budget o quote di lavoro come decisioni già adottate; l'adesione di ogni soggetto resta una decisione dell'utente in attesa di conferma.
6. **Integrazione**: consegna compatibile con la sezione `partenariato` del [dossier condiviso](../dossier/README.md) e con gli input di pianificazione (06), redazione (07) e review (08).

## Guardrail

- **Nessun contatto**: non inviare messaggi, richieste di adesione, inviti; non registrare organizzazioni sui portali; non creare accordi o contratti.
- **Non inventare** accordi, adesioni, disponibilità, quote di lavoro o impegni, nemmeno in esempi: gli impegni scaturiscono solo da conferma documentata dell'utente o del soggetto.
- **Distinzione esplicita** fra obblighi del bando (fonte citata con documento ufficiale e localizzatore) e suggerimento di composizione (etichetta `PROPOSTA`).
- **Minimizzare i dati personali** e non trattare l'elenco dei partner come materiale pubblicabile senza autorizzazione.

## Verifiche e limiti

- `python3 eu-funding-partnership-designer/scripts/check_skill.py`: guardrail statici di struttura.
- [official-sources.md](references/official-sources.md): fonti per ricerca partner; [partnership-map.md](references/partnership-map.md): tipologie di requisiti; [test-cases.md](references/test-cases.md): scenari (consorzio obbligatorio vs candidatura individuale, ecc.).

## Esempio di invocazione

> «Per questo topic verifica cosa richiede il bando in termini di consorzio; poi dimmi quali competenze mancano e cerca soggetti pertinenti con fonti ufficiali.»

La skill risponde con: requisiti tracciati alla fonte, mappa delle competenze, candidati con evidenze e stati (`NON_CONTATTATO`), senza contatti e senza assegnare quote.
