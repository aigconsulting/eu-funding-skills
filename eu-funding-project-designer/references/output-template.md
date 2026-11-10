# Modello di consegna — Skill 11

La consegna della skill è un **dossier di progetto** tracciabile, con stato e fonti per ogni elemento. Le sezioni non pertinenti del caso specifico restano `NON_APPLICABILE`, mai eliminate.

## Struttura del dossier

```
progetto
├─ stato_consulenza: data, versione della fonte corrente, programma, ciclo QFP, call/topic/avviso
├─ contesto_e_bisogni: [{testo, stato: VERIFICATO | DA_CONFERMARE | IPOTESI, fonte?}]
├─ destinatari_e_stakeholder: [{soggetto, ruolo, stato}]
├─ obiettivo_generale: testo, stato
├─ obiettivi_specifici: [{testo, stato}]
├─ logica_intervento: problema → intervento → attività → output → outcome → impatto, con assunzioni
├─ attivita: [{descrizione, sequenza, dipendenze, risorse?, stato}]
├─ output_outcome_impatti: [{tipo, testo, stato, fonte?}]
├─ indicatori: [{nome, definizione, unita, baseline?, target?, periodo?, fonte_metodo, stato}]
├─ rischi_e_assunzioni: [{elemento, effetto_potenziale, mitigazione($('<stato')}]
├─ lacune_e_decisioni: segnaposto e proposte in attesa di decisione dell'utente
└─ evidenze: [{id SRC-*, url, versione, data_consultazione}] + requisiti [{id REQ-*, testo, fonte}]
```

La struttura è compatibile col dossier condiviso del repository (vedi `dossier/README.md`): gli stati ammessi sono gli stessi e la trasformazione `PROPOSTA → DECISIONE_APPROVATA` richiede una decisione effettiva dell'utente, con data e autore.

## Criteri di qualità dell'output

- Ogni fatto documentato (dati statistici, vincoli del bando, normativa) ha una fonte primaria con link diretto, versione e data di consultazione.
- Ogni dato del proponente è distinto per stato (`DA_CONFERMARE` finché non confermato), mai presentato come accertato.
- I valori di indicatore senza base documentale restano `STIMA_NON_VALIDATA` con segnaposto esplicito; nessun valore si presenta come dato.
- La verifica della coerenza è descritta sotto own presunte assunzioni; il dossier non prospetta l'esito della valutazione dell'autorità.
- Un progetto plausibile non equivale a una candidatura ammissibile o finanziabile: la segnalazione resta nel dossier.

## Consegna

- Il dossier completo con stato, fonti e limiti dichiarati.
- La lista esplicita dei segnaposto rimasti e delle decisioni che attendono l'utente.
- `NON_APPLICABILE` per le sezioni non richieste dalla specifica opportunità (es. opportunità senza indicatori documentati); con la motivazione.
