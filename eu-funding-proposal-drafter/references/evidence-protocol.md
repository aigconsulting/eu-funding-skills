# Protocollo fonti ed evidenze — Skill 07

## Distinguere cinque livelli informativi

| Classe | Definizione | Impiego nella bozza |
|---|---|---|
| Fonte ufficiale dell'avviso | Condizioni, modelli, istruzioni e rettifiche pertinenti e vigenti | Definisce l'obbligo o la richiesta del campo, **non** prova che il beneficiario possieda i requisiti |
| Evidenza fornita | Documenti del proponente, dati verificabili, materiali approvati o altri documenti disponibili | Supporta affermazioni circoscritte, indicando documento/versione, senza inventare attestazioni |
| Dichiarazione utente | Informazione fornita dall'utente senza documento probatorio | Usare come dato dichiarato, evidenziando `DA_CONFERMARE` quando servono riscontri |
| Proposta/stima | Scelta progettuale non ancora approvata oppure previsione non verificata | Presentare in modo condizionale; non spacciarla per decisione presa o risultato ottenuto |
| Mancanza | Il dato non è noto, la fonte non è disponibile o il campo non è stato coperto | Inserire `[DA CONFERMARE: ...]`, senza sintesi creativa |

## Registro fonti minime

Per ogni fonte: `source_id`, titolo, tipo, emittente, URL o riferimento al documento fornito, `versione`, `data_consultazione`, `fase`, `ambito`, `stato_verifica`. Un riferimento ufficiale generale sulla procedura **non sostituisce** la fonte primaria relativa alla specifica call.

Una rettifica deve essere applicata solo nel proprio ambito temporale e procedurale. Se l'autorità non chiarisce quale documento prevalga, indicare `CONFLITTO` e bloccare l'asserzione corrispondente. Non inventare ordini di prevalenza.

## Requisiti e struttura

Per ogni requisito del bando, utilizzare ID stabile `REQ-001` ecc. e conservare testo/descrizione breve, classe, source_id, locator (articolo, pagina o campo), fase, eventuale condizione, elemento del formulario `SEC-001` ecc. e prova. Separare **obbligatorietà del campo** da **qualità del contenuto**. Un campo compilato può essere sostanzialmente non dimostrato.

## Claim e prova

Le affermazioni sostanziali `CLM-*` devono citare origine concreta o essere marcate `PROPOSTA`, `STIMA_NON_VALIDATA`, `SEGNAPOSTO`. Una dichiarazione ricevuta oralmente non deve essere presentata come attestazione ufficiale. Per una metrica citare definizione, base temporale, unità, origine e, se stimata, metodo; senza questi elementi preferire segnaposto.

## Separazione dall'esecuzione

La bozza può utilizzare una struttura di output modificabile ma non compila o invia automaticamente moduli ufficiali; non crea documenti firmati, lettere di adesione, dichiarazioni fiscali, registrazioni su portali o accordi di partenariato.

## Manifest JSON opzionale: campi per il validatore

Il validatore `scripts/validate_draft.py` accetta un oggetto JSON con campi obbligatori:

- `opportunity`: `identifier`, `official_url`, `phase`, `as_of` (stringhe).
- `sources`: array di `{id,title,locator,official:boolean,verified:boolean}`.
- `sections`: array di `{id,official_label,source_id,coverage,text}`.
- `requirements`: array di `{id,kind,source_id,locator,section_ids:[...],coverage,justification?}`.
- `claims`: array di `{id,section_id,state,text,evidence_ref?}`.
- `submission`: `{performed:false}` per registrare che la skill non attesta invii.

Gli stati sono quelli indicati nella Skill. `verified:true` e `official:true` nel manifest sono **asserzioni fornite dall'estensore**, non verificate da questo script consultando il portale. È responsabilità dell'analisi umana/agentica verificarle sulle fonti autentiche. Lo script non assegna status `PRONTA`, non certifica la validità di una rettifica e non valuta la qualità del testo.
