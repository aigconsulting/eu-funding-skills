# Dossier progettuale condiviso — schema minimo e scambio fra skill

Il dossier è un **formato di scambio proposto** fra le skill del repository, non un servizio né un database obbligatorio: funziona come insieme di file locali (tipicamente `dossier.json` più allegati), senza persistenza remota. Le skill possono operare anche **senza** un dossier preesistente.

## Componenti

| File | Contenuto |
| --- | --- |
| `dossier.schema.json` | proposta di **schema minimo versionato** (`eu-funding-skills/dossier@v1`), autodescrittivo |
| `example-dossier.json` | **esempio interamente sintetico** (nessun dato reale di bandi o soggetti) |
| `check_dossier.py` | validatore deterministico senza dipendenze: struttura, stati, riferimenti, date, stale-check |
| `test_dossier.py` | test unitari del validatore (11 casi) |

## Stati distinti (mai mescolati)

`VERIFICATO` (fatto, con fonte e data di verifica) · `DA_CONFERMARE` (dato fornito in attesa di riscontro) · `IPOTESI` · `PROPOSTA` · `DECISIONE_APPROVATA` (con `approvato_il`) · `MANCANTE` · `NON_APPLICABILE`.

Una proposta non diventa mai decisione, e un'ipotesi mai fatto: le trasformazioni richiedono un intervento esplicito dell'utente (o di una skill con le evidenze), registrato in `revisioni`.

## Rettifiche del bando: nessuna auto-conferma

`opportunita.ultima_verifica` rappresenta la data dell'ultimo riscontro sulle fonti. Quando avanza (per esempio dopo una rettifica rilevata dalla Skill 03), il validatore segnala come **da riesaminare** ogni evidenza consultata prima di quella data e ogni elemento `VERIFICATO` verificato prima di quella data: i dati precedenti **restano salvati e invariati**, senza auto-conferma né riscrittura (test `test_rettifica_does_not_confirm_previous_data`).

## Scambio fra skill

- **Skill 01–03** (hierarchy, programme finder, call finder): popolano `opportunita`, `evidenze` (URL, versione, data di consultazione) e scadenze; la Skill 03 aggiorna `ultima_verifica` quando rileva rettifiche/aggiornamenti.
- **Skill 04–05** (eligibility, financial): aggiornano `requisiti` (con ID `REQ-*`) e tassi/cofinanziamento in `finanza`, sempre con `fonte_regole`.
- **Skill 06–07** (planner, drafter): consumano requisiti e fonti, aggiornano `progetto` (contesto, obiettivi, attività, output, outcome, impatti, indicatori solo se fondati) e `revisioni`.
- **Skill 08–10** (review, pre-check, post-submission): leggono la versione corrente e le evidenze, producono rapporto o esiti; possono aggiornare `requisiti.stato` mantenendo le versioni precedenti negli output.
- **Skill suggerite #5/#8** (project designer e partnership designer, se installate): aggiornano rispettivamente `progetto` e `partenariato`.
- Ogni **trasformazione di stato** richiede una nuova evidenza o una decisione approvata: niente sovrascritture silenziose, ogni cambiamento è registrato in `revisioni`.

## Compatibilità con l'esecuzione autonoma

Il dossier è una **risorsa opzionale**: nessuna skill lo richiede come precondizione. Un agente può: (a) procedere senza dossier; (b) usare un dossier esistente indicato dall'utente; (c) crearne uno nuovo a partire dai propri output seguendo lo schema. L'assenza del dossier non blocca alcuna skill.

## Cosa NON è

- Non un archivio di dati personali: minimizzare informazioni personali e riservate.
- Non un servizio, non un database, non un meccanismo automatico: è un file che le skill e l'utente leggono/aggiornano.
- Non un attestato di validità legale o di correttezza sostanziale: il validatore attesta solo coerenza formale e tracciabilità interna.
