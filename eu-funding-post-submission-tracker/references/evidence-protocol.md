# Protocollo degli eventi e delle evidenze — Skill 10

## Oggetto del controllo

Ogni ricostruzione identifica `application.reference` e `application.phase` (se nota), periodo `tracking.since/as_of` e fonti effettivamente consultate. Distinguere sempre: `issued_at` (data dell'atto), `received_at` (ricezione), `observed_at` (effettiva lettura), `effective_at` (se documentata). Il modello JSON base richiede **solo observed_at**: gli altri timestamp sono facoltativi, e non vanno dedotti. Per tutti i timestamp machine-readable utilizzare ISO 8601 con offset; conservare anche testo originale se incompleto.

## Gerarchia delle evidenze, senza presunzione di prevalenza normativa

- `OFFICIAL_NOTICE`: avviso e rettifiche, provvedimenti firmati, comunicazioni formali dell'autorità competente, estratti autentici del portale. **Non** significa che il documento prevalga automaticamente su altri: la gerarchia e la decorrenza si verificano nel caso.
- `AUTHORITY_MESSAGE`: email o messaggio con mittente identificato, contenuto e data, da verificare nell'account di destinazione o con riferimenti ufficiali. Un testo inoltrato non dimostra da solo autenticità ed effetti.
- `INTERNAL_RECORD`: ricevuta conservata, log/nota interni, deleghe, conferme di azioni eseguite, non sempre certificazioni dell'ente.
- `THIRD_PARTY`: segnalazioni e articoli; mai base unica per un esito formale.

Ogni fonte ha `official` e `verified` booleani, provenienza e localizzatore; tali campi registrano una **dichiarazione motivata del ricercatore**, non una firma crittografica né validazione automatica. Allegare una breve descrizione della verifica eseguita, o segnalare `verified: false`.

## Stato e cronologia

Non ridurre il post-invio a un'unica macchina a stati europea. Registrare eventi datati e una `observed_state` che riporti l'etichetta originale del sistema e l'evento di riferimento. In caso di contraddizione, usare `CONFLITTO_FONTI`, conservando entrambi gli atti. Distinguere esito della valutazione, ammissione a graduatoria, prenotazione di fondi, concessione, invito a firma, firma dell'accordo, liquidazione ed effettivo pagamento.

Le scadenze devono contenere testo originale, fonte, localizzatore, fase e stato: `VERIFICATA`, `DA_VERIFICARE` o `CONFLITTO_FONTI`. Se la scadenza contiene un'ora ma il fuso è indeterminato, l'istante ISO UTC è vietato e lo stato è `DA_VERIFICARE`. Una scadenza scritta solo come data può essere documentata senza un istante di fine preciso. I termini condizionati a notifiche o ricevute richiedono la prova della data iniziale.

## Azioni senza automatismi

Una richiesta di chiarimenti può giustificare una **proposta di risposta**; non autorizza invio né stabilisce da sé un obbligo universale. `OBBLIGO_DOCUMENTATO` solo da fonte ufficiale verificata; `RACCOMANDAZIONE_INTERNA` è facoltativa; `DA_VERIFICARE` per condizioni incomplete. Gli stati delle azioni: `PROPOSTA`, `APPROVATA`, `ESEGUITA`, `DA_VERIFICARE`. Per affermare `APPROVATA`, registrare evidenza dell'approvazione; per `ESEGUITA`, registrare evidenza dell'esecuzione (es. ricevuta effettiva), diversa da una mera bozza o checklist. Il validatore richiede un `execution_event_id` collegato a un evento di esecuzione e una fonte verificata, ma **non** dimostra autenticità della ricevuta.

## Sicurezza, confini, aggiornamento

- Nessuna lettura automatica di inbox, account, portali o link privati senza accesso/permesso e strumenti adeguati.
- Niente invii, firme, caricamenti, gestione di ricorsi o operazioni su piattaforme tramite questa skill.
- Non considerare una mail generica come esito definitivo senza controllare provenienza e contenuto.
- In output usare identificativi minimizzati, evitando credenziali, dati sanitari, dati personali superflui e allegati integrali.
- Eventi nuovi non sovrascrivono la storia: ogni aggiornamento richiede data di osservazione e nuova evidenza; evitare duplicazioni di notifiche identiche.
- Dichiarare sempre i canali NON consultati e non equiparare un'assenza di risultati alla certezza di assenza di novità.
