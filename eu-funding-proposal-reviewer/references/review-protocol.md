# Protocollo di revisione — Skill 08

## Baseline e indipendenza

Conservare identificativo di avviso/fase, elenco e versione dei documenti ufficiali consultati, titolo e versione o hash della proposta, elenco degli allegati letti, data della verifica e natura del riesame (`AUTO_REVISIONE`, `REVISIONE_SEPARATA`, `REVISIONE_ESTERNA`). Se esiste una revisione precedente, confrontare esattamente la revisione della stessa versione e non dichiarare chiusi i rilievi senza rilettura del testo corretto.

## Matrice requisito — prova — esito

| Campo | Contenuto minimo |
|---|---|
| `REQ-*` | Descrizione del requisito, categoria e condizionalità/fase |
| `SRC-*` | Emittente, titolo, versione, URL o file, pagina/sezione, data consultazione, status verificato |
| `proposal_locator` | File, sezione, pagina, paragrafo o campo del formulario esaminato |
| `proposal_excerpt` | Breve estratto fedele, se disponibile, oppure esito documentato della ricerca dell'elemento |
| `review_status` | `SODDISFATTO_DOCUMENTALMENTE`, `CARENZA_ACCERTATA`, `DA_VERIFICARE`, `NON_APPLICABILE` motivato |

Distinguere una **carenza certa** (testo e criterio controllati) da una **mancanza di documenti** (non è possibile concludere). Un campo obbligatorio non trovato in un documento *parziale* non è automaticamente assente nella candidatura completa.

## Rilievi

Ogni rilievo `FND-*` comprende categoria, gravità interna, stato della prova, descrizione, conseguenza, requisito e source_id (se attribuito all'avviso), localizzatore ufficiale, passaggio della proposta, elemento mancante/contraddittorio e raccomandazione. Per un'osservazione redazionale pura indicare `OSSERVAZIONE_REDAZIONALE`, senza fingere che esista un obbligo ufficiale.

La priorità di remediation può essere proposta, ma **non rappresenta** il voto dell'autorità e non determina automaticamente se candidarsi.

### Gravità interne

- `CRITICO`: possibile incompatibilità sostanziale con obbligo documentato o elemento che rende non affidabile la bozza (descrivere prova e limiti, non predire l'esclusione).
- `MAGGIORE`: difetto importante nella copertura del criterio, nell'evidenza o nella coerenza.
- `MINORE`: problema circoscritto non dimostrato come bloccante.
- `OSSERVAZIONE`: proposta migliorativa redazionale o questione a bassa materialità.

### Stati di prova

- `ACCERTATO`: fonte e testo entrambi controllati e circostanza comprovata nell'ambito dichiarato.
- `POTENZIALE`: indizi, dipendenze o ambiguità da verificare; non chiamare "violazione".
- `NON_VERIFICABILE`: fonte, testo o prova decisivi mancanti, con richiesta specifica.
- `RISOLTO_VERIFICATO`: rilievo precedente ricontrollato contro una nuova versione identificata, con prova della chiusura.

## Fonti e istruzioni in conflitto

Trattare i documenti ufficiali e le rettifiche in modo specifico: data, ambito, fase e valore attribuito dall'autorità. Se un criterio non è localizzabile o due testi incompatibili non risultano riconciliati, non usare conoscenze di altri programmi per risolvere il conflitto. Segnalare `CONFLITTO_FONTI` e il relativo impatto.

## Niente valutazione simulata

Non assegnare punteggi, rating di finanziabilità, soglie di successo ipotetiche, percentuali di probabilità né formule di ranking simulando la commissione. Riportare eventuali **soglie ufficiali** solo con la loro fonte, distinguendole da risultati della bozza. Evitare espressioni “verosimilmente finanziata” o “approvata”.

## Manifest opzionale

`validate_review.py` si aspetta:

- `opportunity`: `{identifier, official_url, phase, as_of}`;
- `proposal`: `{reference, version, review_scope}` (stringhe; `sha256` opzionale);
- `review`: `{mode, status, reviewer_note}` con modalità `AUTO_REVISIONE` / `REVISIONE_SEPARATA` / `REVISIONE_ESTERNA` e stato interno;
- `sources`: `[{id,title,locator,official,verified}]`;
- `requirements`: `[{id,description,category,source_id,locator,review_status,proposal_locator}]` (con `justification` se non applicabile);
- `findings`: `[{id,kind,severity,evidence_status,description,recommendation,source_id?,requirement_id?,official_locator?,proposal_locator?,proposal_excerpt?,missing_evidence?,resolved_in_version?}]`;
- `submission`: `{performed:false}`.

`kind` è `REQUISITO_UFFICIALE`, `COERENZA_INTERNA` o `OSSERVAZIONE_REDAZIONALE`; il controllo statico verifica che i rilievi normativi accertati citino una fonte ufficiale dichiarata e un passaggio della proposta. **Non controlla che il contenuto delle fonti sia reale**: `verified:true` è una dichiarazione dell'estensore che deve essere controllata con accesso alle fonti.
