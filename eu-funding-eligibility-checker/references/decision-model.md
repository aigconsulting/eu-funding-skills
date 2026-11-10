# Modello di valutazione dell'ammissibilità (preliminare)

## Unità della verifica

Una valutazione è riferita a una tupla:
`(opportunity_id, versione_atti, fase/cutoff, data_verifica, soggetto, ruolo, progetto, partenariato)`.
Se cambiano ruolo, fase o fonte, **rifare il controllo**, senza ereditare automaticamente l'esito precedente.

## Record di ogni requisito

| Campo | Descrizione |
|---|---|
| id_requisito | Identificativo locale stabile `R01`, `R02` ... |
| dimensione | `PARTECIPAZIONE`, `FINANZIABILITA`, `PROGETTO`, `AMMISSIBILITA_FORMALE`, `CAPACITY_EXCLUSION` o `MERITO` |
| obbligatorieta | `OBBLIGATORIO`, `VALUTATIVO`, `RACCOMANDATO`, `DA_CHIARIRE` |
| applica_a | Beneficiario, coordinatore, partner, progetto, consorzio, richiedente ecc. |
| regola | Requisito sintetizzato fedelmente, senza estensioni |
| termine | Presentazione, prima fase, seconda fase, grant agreement, durante esecuzione, non determinato |
| fonte | URL primario, titolo/versione/data, sezione, data verifica |
| evidenza | Fatto dichiarato dall'utente o documento verificato, distinguendo la provenienza |
| stato | `SODDISFATTO`, `NON_SODDISFATTO`, `NON_VERIFICATO`, `NON_APPLICABILE` |
| rimediabilita | Solo se supportata da fonte + data; altrimenti `NON_DETERMINATA` |
| impatto | Blocco, condizione, lacuna documentale o informazione |

## Regola di decisione

1. Filtrare le condizioni `OBBLIGATORIO` applicabili al ruolo, alla data e alla fase. Non trasformare i criteri `MERITO` in veto.
2. Se un requisito obbligatorio è documentalmente **non soddisfatto e non rimediabile nei termini**, dichiarare `INCOMPATIBILE_DOCUMENTATO` per la dimensione interessata; continuare a elencare i restanti non verificati senza occultarli.
3. Se non vi sono incompatibilità documentate ma fonti decisive, profilo o condizioni temporali sono insufficienti, assegnare `DATI_INSUFFICIENTI` alla relativa dimensione. Non usare `CONDIZIONATO` come sinonimo di sconosciuto.
4. Solo se l'insieme dei requisiti è coperto e l'unico ostacolo è una o più condizioni **esplicitamente rimediabili** entro una data documentata, assegnare `CONDIZIONATO`, elencando l'azione necessaria senza eseguirla.
5. Se tutti i requisiti obbligatori di una dimensione sono soddisfatti e verificati, usare `COERENTE_PRELIMINARE` con la precisazione che l'autorità svolge la decisione formale.
6. Non creare una decisione unica quando partecipazione, finanziabilità, progetto o ammissibilità formale differiscono. Un partner può essere ammesso a partecipare **senza** ricevere finanziamento.
7. I requisiti di capacity/exclusion possono essere oggetto di verifica successiva; non stimare l'esito senza documenti, né ritardare artificialmente una conclusione già supportata per un altro blocco documentato.

## Checklist antifalsi positivi

- Il titolo della call non basta a dimostrare compatibilità con scope del topic.
- Una società «costituenda» non equivale a un'entità legalmente costituita.
- Almeno tre partner è una regola **frequente**, non universale: verificare la singola action.
- `eligible to participate` ≠ `eligible to receive EU funding`.
- `topic budget` ≠ `contribution per project` ≠ `costi ammissibili`.
- `award criteria` ≠ `eligibility`; nessuna previsione di successo.
- `closing date` e *cutoff* devono riferirsi alla fase corretta e alla fonte attuale.
- Una FAQ informale o un sito terzo non modifica il bando ufficiale.
- Una regola senza URL diretto applicabile non è `SODDISFATTO` o `NON_SODDISFATTO` in modo conclusivo.
