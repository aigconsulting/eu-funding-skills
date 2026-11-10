---
name: eu-funding-eligibility-checker
description: Verifica preliminarmente, su fonti ufficiali del topic o avviso UE, requisiti di ammissibilità del richiedente, partenariato, progetto e candidatura; distingue partecipazione, diritto a ricevere contributi, ammissibilità formale, capacità, esclusioni e criteri di valutazione. Fornisce matrice requisito-evidenza, condizioni residue e blocchi documentati senza dichiarare approvazioni o candidare automaticamente.
---

# EU Funding Eligibility Checker — Skill 04

## Scopo

Analizzare se **un soggetto, il suo partenariato e un progetto descritto** soddisfino, **in via preliminare e alla data della verifica**, i requisiti *documentati* di una specifica opportunità di finanziamento dell'Unione europea. Ogni conclusione è legata alla fonte, al ruolo del partecipante e al momento in cui la condizione deve risultare soddisfatta.

Questa skill **non determina l'ammissione ufficiale**, non sostituisce i controlli dell'autorità finanziatrice e non valuta la probabilità di vittoria. Distingue sempre:

- **Partecipazione**: poter figurare nel progetto in un ruolo ammesso (coordinatore, beneficiario, affiliata, associated partner, subcontractor o altro ruolo definito nel bando).
- **Finanziabilità**: poter **ricevere** fondi in quello specifico ruolo/territorio, che non coincide necessariamente con il diritto di partecipare.
- **Elegibilità del progetto**: oggetto, attività, localizzazione, durata e vincoli tecnici prescritti.
- **Ammissibilità formale**: requisiti di presentazione (fase, scadenza, modulistica, allegati, limiti di pagina, modalità).
- **Capacity / exclusion**: capacità operativa/finanziaria ed eventuali condizioni di esclusione, quando applicabili; non richiedere dati personali non necessari.
- **Criteri di valutazione/award**: qualità, impatto e punteggio, che non dimostrano ammissibilità e non vanno trasformati in requisiti obbligatori se non lo sono.

Per la classificazione delle evidenze usare le dimensioni codificate `PARTECIPAZIONE`, `FINANZIABILITA`, `PROGETTO` e `AMMISSIBILITA_FORMALE`; trattare separatamente `CAPACITY_EXCLUSION` e `MERITO`.

Usare la [matrice decisionale](references/decision-model.md) e il [modello di output](references/output-template.md). Se è necessario individuare prima una call o un topic, usare `eu-funding-call-finder`; questa skill rimane utilizzabile senza le altre tre.

## Input minimo e informazioni facoltative

**Per una conclusione sul caso specifico:** link o ID esatto del **topic/avviso** e un profilo almeno parziale del richiedente/progetto. Profilo utile: Stato/Regione di stabilimento, tipo di soggetto (impresa, università, PA, associazione, persona fisica ecc.), ruolo richiesto, stato di costituzione; attività/obiettivo; partner previsti, se noti.

Informazioni aggiuntive da richiedere **solo se materialmente necessarie** a un requisito trovato nei documenti: indipendenza dei partner, rapporto di controllo/affiliazione, dimensione PMI, anzianità dell'impresa, sede operativa, TRL, capacità finanziaria, costi, durata, settori esclusi, requisiti territoriali. Non chiedere tutte queste informazioni preventivamente e non presumere valori mancanti.

Se manca l'ID/link, individuare l'avviso dalla descrizione con la Skill 03 o chiedere **una sola informazione determinante** quando non è individuabile in modo univoco. Se il richiedente è solo parzialmente descritto, fornire l'analisi delle condizioni documentate e i controlli `NON_VERIFICATO`, non inventare dati.

## Processo: sette passaggi

1. **Identificare la fonte primaria applicabile.** Aprire il topic/avviso corrente, annotare ID, ente concedente, programma, call, data di consultazione e stato. Individuare `call document`, work programme, allegati generali applicabili, FAQ, rettifiche, amendments e modulistica ufficiale. Per gestione concorrente/indiretta privilegiare l'autorità competente dell'avviso. Consultare [fonti ufficiali](references/official-sources.md). Se non sono disponibili documenti determinanti, dichiarare `DATI_INSUFFICIENTI`.
2. **Separare le regole, non le parole chiave.** Estrarre requisiti *obbligatori* e distinguerli da `expected outcomes`, raccomandazioni, criteri di merito e istruzioni operative. Registrare per ciascuno testo sintetico, tipo di condizione, ruolo/soggetto cui si applica, data di riferimento, fonte diretta e sezione. Quando il testo è ambiguo, riportare l'ambiguità e l'eventuale chiarimento ufficiale: nessuna deduzione normativa automatica.
3. **Verificare soggetto e finanziabilità.** Natura giuridica, Paese di stabilimento, localizzazione, data di costituzione quando prescritta, dimensione PMI/età di impresa solo se documentate, eventuali restrizioni su proprietari e paese di controllo, settore e forma giuridica. Verificare *separatamente* partecipazione e diritto a contributo. Registrazione/PIC o validazione legale richiesta alla candidatura vs prima del grant **secondo l'avviso**; non considerare automaticamente il PIC una condizione di ammissibilità al giorno della ricerca.
4. **Verificare partenariato.** Requisiti minimi e massimi, indipendenza, Paesi, ruoli ammessi, capacità del coordinatore, categorie obbligatorie (es. end-user, enti pubblici) ed eventuali restrizioni per Paese finanziatore. **Non trasferire** la regola tipica di tre partner di alcune call Horizon Europe a ERC, EIC, altre action, o ai bandi regionali: leggere l'eccezione del topic.
5. **Verificare oggetto e disegno progettuale.** Scope, attività obbligatorie/proibite, beneficiari finali, luogo di esecuzione, TRL minimo/massimo ove indicato, durata, tipologia di azione, aiuti di Stato e regime di costi quando applicabile. Non equiparare una *buona affinità tematica* alla conformità del progetto. Non equiparare importo previsto, massimale o budget al diritto a ricevere quella somma.
6. **Verificare ammissibilità formale e capacità.** Canale di submission, fase, termine (ora/fuso se pubblicati), lingua, documenti e limiti, condizioni di non cumulabilità e dichiarazioni esplicite. Distinguere `requisito già posseduto`, `da possedere entro la scadenza`, `da provare in fase di grant` e `non definito`. Screening di capacità ed esclusioni: segnalare le verifiche richieste senza pronunciare sentenze su cause non documentate.
7. **Produrre una valutazione basata su prove.** Applicare l'algoritmo in [decision-model.md](references/decision-model.md); restituire una matrice completa delle condizioni decisive, evidenze del profilo, link e lacune, con conclusione **preliminare** per partecipazione, finanziabilità, progetto e forma. Separare i blocchi documentati dalle condizioni ancora soddisfacibili e da quelle non verificate. Specificare prossimo controllo utile, senza effettuare candidature o contatti.

## Priorità e gestione delle fonti

- Fonte primaria: **pagina ufficiale del topic/avviso e versioni vigenti dei documenti che essa richiama**, incluse rettifiche e FAQ ufficiali quando chiariscono l'avviso.
- Fonti di supporto: work programme, annexes, guide al programma, normativa, regole nazionali/regionali applicabili e canali istituzionali competenti.
- Sintesi di terzi o contenuti di marketing sono validi **solo per discovery**. Non certificano ammissibilità.
- Quando documenti ufficiali discordano, **non inventare una gerarchia legale astratta**: segnalare testo, documenti e date e sospendere il giudizio sul requisito fino a verifica ufficiale. La versione più recente non prevale automaticamente se non è applicabile al topic.
- Ogni requisito chiave deve avere URL diretto e riferimento a sezione, pagina o paragrafo individuabile; niente citazioni a pagine generiche del programma in sostituzione del topic.
- Registrare lo stato alla data/ora della verifica; nessuna supposizione di apertura, estensione o riapertura della call.

## Tassonomia dei risultati

### Per singolo requisito

- `SODDISFATTO`: evidenza concreta del profilo coerente con una regola ufficiale specifica.
- `NON_SODDISFATTO`: evidenza concreta incompatibile con la condizione richiesta. Specificare *quando* deve essere soddisfatta e se può essere rimediata prima di tale istante.
- `NON_VERIFICATO`: condizione o evidenza incerta, documentazione ufficiale assente o dato del richiedente non disponibile.
- `NON_APPLICABILE`: la regola non si applica al ruolo/azione, **con motivazione**.

### Esito preliminare (quattro dimensioni separate)

- `COERENTE_PRELIMINARE`: tutte le condizioni decisive applicabili per quella dimensione sono fondate e soddisfatte; non equivale ad ammissione.
- `CONDIZIONATO`: vi sono condizioni **esplicitamente note**, attualmente non soddisfatte ma documentatamente soddisfacibili entro il termine utile; indicare condizioni, prova e termine. Non assegnarlo se non è possibile dimostrare la rimediabilità.
- `INCOMPATIBILE_DOCUMENTATO`: almeno una condizione obbligatoria risulta incompatibile e non vi è evidenza di una via ammissibile per soddisfarla entro il termine rilevante.
- `DATI_INSUFFICIENTI`: mancano fonti o evidenze per pronunciarsi o esiste conflitto documentale irrisolto. Questo stato prevale sul sospetto di compatibilità; eventuali incompatibilità **già documentate** restano riportate come blocchi e non sono cancellate da altri dati mancanti.

Un esito globale può essere formulato **solo** con tutte le dimensioni chiaramente coperte e condizionate; in caso contrario riportare i quattro esiti, non un `SI`/`NO` unico. Niente punteggi, percentuali di probabilità, semafori arbitrarî o classifiche di ammissione.

## Casi che richiedono cautela particolare

- **Società in via di costituzione:** non dichiarare eleggibile una società non ancora esistente salvo disposizione specifica; distinguere candidatura da parte dei promotori, data prevista di costituzione e richiesta di entità giuridica al momento della domanda o del grant.
- **Paese associato/non UE:** distinguere accesso al programma, partecipazione e ricezione di grant; verificare associazione e regime **per programma e data**.
- **Consorzio transnazionale:** un partner non finanziabile può eventualmente partecipare in un ruolo diverso *solo se permesso dall'avviso*; la sua presenza non soddisfa automaticamente le condizioni minime sui beneficiari.
- **Bando regionale con fondi UE:** usare i requisiti dell'avviso dell'Autorità di gestione/soggetto attuatore, non i General Annexes Horizon.
- **Proposta a due fasi:** ammissibilità e documenti richiesti possono variare per stage; non simulare accesso alla fase successiva.
- **Scadenza già trascorsa:** dichiarare l'impossibilità della candidatura al cut-off trascorso; non attribuire retroattivamente la mancata ammissibilità sostanziale del soggetto.
- **Dati aziendali riservati:** limitarsi agli attributi strettamente necessari; non richiedere documenti fiscali, identità o informazioni personali senza necessità specifica e consenso.

## Output minimo

Seguire [references/output-template.md](references/output-template.md), includendo: identificativo dell'opportunità; data e fonti; quadro delle quattro dimensioni; matrice dei requisiti decisivi; prove e mancanze; eventuali condizioni da soddisfare **entro una data specifica**; blocchi documentati; passo istruttorio rimanente. Link alla fonte diretta di **ogni requisito determinante**.

## Cosa non eseguire

Non registrare entità, non creare PIC, non inviare proposte, non inserire dati su portali, non produrre dichiarazioni per conto del richiedente, non presentare una verifica preliminare come autorizzazione/approvazione e non avviare monitoraggio o procedimenti non richiesti. La scelta di candidarsi spetta all'utente; la verifica ufficiale spetta all'autorità competente.

## Verifiche e test

Eseguire `python3 eu-funding-eligibility-checker/scripts/check_skill.py` dalla radice del pacchetto. Il controllo verifica **solo file, frontmatter, collegamenti e guardrail testuali**. I casi di comportamento atteso sono elencati in [references/test-cases.md](references/test-cases.md) e **non** costituiscono prove funzionali in assenza di una esecuzione con agente e documenti reali.
