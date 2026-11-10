# Protocollo di controllo pre-invio — Skill 09

## Ambito

Questo protocollo è una metodologia interna **indipendente dal programma**. Le categorie non sono requisiti universali. Un controllo obbligatorio deve avere una fonte specifica della singola opportunità, versione, fase e localizzatore. La fonte di metodo UE orienta la ricerca, non attribuisce obblighi alla singola call.

## Provenienza dei requisiti

- `SRC-*`: documento o pagina, soggetto responsabile, URL o file, versione/data, data consultazione, sezione/pagina, `official` e `verified` espliciti. `verified=true` è un'affermazione dell'analista, **non** verificata dal codice.
- `CHK-*`: descrizione esatta della condizione, categoria, `source_id`, `source_locator`, fase e caso d'applicazione. Per `NON_APPLICABILE` indicare `justification` e fonte/condizione quando verificabile.
- `item_ref` ed `evidence`: file/identificativo/versione o area verificata e osservazione concreta. Gli estratti non devono contenere segreti.
- Rilievi accertati: requisito documentato + fonte verificata + prova del difetto nel pacchetto identificato. Informazioni mancanti: `DA_VERIFICARE` con motivazione, non non-conformità automatica.
- `CONFLITTO_FONTI` è una limitazione che impedisce di chiudere positivamente il controllo; non inventare prevalenza o cronologia giuridica.

## Tempo, cut-off e scadenze

Annotare stringa originale della scadenza e **il fuso come pubblicati**. Se il portale riporta un'ora locale, non attribuire automaticamente UTC. Non equiparare termine di invio, deadline di manifestazione di interesse, cut-off, proroga e data di successivo step. Convertire soltanto con fuso verificato e indicare il risultato come conversione calcolata, non come testo del bando. La data di consultazione non prova l'attuale apertura futura.

## Verifica del pacchetto

1. Distinguere **presenza materiale**, **compilazione**, **firma**, **validazione applicativa** e **trasmissione**.
2. Registrare file/versioni e, se disponibile, hash calcolato dei byte; non inventare un hash.
3. Se il documento è richiesto condizionatamente, riportare la condizione e quale evidenza ne determina l'applicabilità.
4. Se l'ente prevede invio cartaceo, PEC, portale diverso o intermediazione, seguire soltanto la fonte competente.
5. Correzioni suggerite e integrazioni restano proposte finché non sono applicate e nuovamente verificate.

## Non-equivalenze da rispettare

- Esito valido del controllo statico ≠ ammissibilità ufficiale.
- File presente ≠ allegato correttamente caricato.
- Conferma di upload ≠ invio completato.
- Validazione formale di un portale ≠ giudizio sul merito.
- Invio dichiarato dall'utente ≠ ricevuta verificata.
- Ricevuta per versione precedente ≠ ricevuta della versione attuale.
- Una checklist positiva ≠ autorizzazione a presentare.

## Stop e ripresa

Fermarsi quando manca identificazione affidabile, si trova un conflitto sostanziale tra documenti, il termine/fuso è ambiguo o il pacchetto cambia durante il controllo. Concludere `PRECHECK_PARZIALE` o `BLOCCATO_DA_FONTI` come appropriato. Riprendere soltanto sulla fonte/versione chiarita e registrare cosa è stato riletto. Non usare questa skill per aprire sessioni di portale o aggirare limitazioni.
