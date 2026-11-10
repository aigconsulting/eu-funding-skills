---
name: eu-funding-call-finder
description: Cerca e verifica call for proposals, topic e avvisi pubblici nei programmi e fondi UE, usando fonti ufficiali aggiornate. Ricostruisce programma, call, topic e documenti applicabili; controlla stato, scadenze, fasi, budget, beneficiari e attività ammissibili senza inventare requisiti né confondere grant, appalti o strumenti finanziari. Restituisce schede comparabili con link primari e livello di verifica, senza candidare né monitorare automaticamente.
---

# EU Funding Call Finder — Skill 03

## Obiettivo

Passare da **programma o ambito di intervento** a una lista **verificata e tracciabile di opportunità concrete**, in particolare *Call for Proposals* e relativi *Topic*, oppure avvisi equivalenti delle autorità nazionali e regionali. Non trasformare il nome di un programma in un bando, non assumere che tutte le opportunità siano nel Funding & Tenders Portal e non creare proposte progettuali.

- **Skill 01 — `eu-funding-hierarchy`:** chiarisce le relazioni fra livelli istituzionali e documentali.
- **Skill 02 — `eu-funding-programme-finder`:** individua programmi e strumenti da esplorare.
- **Skill 03 — questa skill:** identifica i **singoli topic/avvisi** e ne verifica i dati operativi. È utilizzabile anche senza output delle altre due.

## Input

**Minimo sufficiente:** un programma UE **oppure** un obiettivo preciso da finanziare con almeno un riferimento geografico o settoriale utile alla ricerca. Se l'utente indica soltanto un programma (es. Horizon Europe), cercare le opportunità per il tema richiesto, non una lista indiscriminata di ogni topic.

**Facoltativi:** Paese/Regione, beneficiario (PMI, impresa da costituire, università, ente pubblico, associazione, persona fisica), attività, maturità/TRL se pertinente, importo, data limite di interesse, preferenza per sole call aperte, lingua, partenariato, strumento economico. Non imporre un questionario: esporre i campi non noti e trattarli come condizioni da verificare.

## Processo operativo

1. **Definire l'unità di ricerca.** Distinguere: programma; linea/azione/destination; *call*; *topic*; *avviso nazionale/regionale*. Una call può contenere molti topic; la candidatura si presenta contro lo specifico topic/avviso pertinente. Registrare l'unità effettivamente selezionata e non etichettare ogni risultato come «bando» senza precisarne il livello.
2. **Identificare il canale ufficiale.** Per programmi gestiti sul portale UE, usare il [Funding & Tenders Portal](references/official-sources.md); per gestione concorrente, individuare il programma nazionale/regionale e la relativa Autorità di gestione; per gestione indiretta o strumenti finanziari, consultare l'autorità/partner ufficiale. Non dare per esaustivo il portale della Commissione.
3. **Cercare per programma, ambito e testo.** Usare identificatori, parole-chiave in italiano/inglese, sinonimi e descrizioni delle attività; filtrare per programma, anno e stato quando disponibili. Provare anche `forthcoming` e `closed` se l'utente cerca una prospettiva temporale, non solo bandi aperti. Registrare data della ricerca, filtri e sito consultato. Non spacciare un risultato di ricerca o un'anteprima per conferma di apertura.
4. **Aprire la pagina primaria del topic/avviso.** Acquisire l'identificativo **esatto** e un link diretto al record; verificare titolo, programma, eventuale call padre, ente concedente e work programme/call document. Se la pagina del risultato è inaccessibile, classificare `DA_VERIFICARE`; non ricostruire campi mancanti dal pattern dell'ID.
5. **Leggere documenti applicabili e aggiornamenti.** Controllare topic page, call document, work programme, general annexes, application form, corrigenda, FAQ e aggiornamenti ufficiali pertinenti. Le regole di ammissibilità e finanziamento sono determinate dagli atti applicabili alla specifica opportunità. Registrare documento, versione/data e sezioni utilizzate; se emergono contraddizioni, descriverle senza inventare una gerarchia giuridica universale.
6. **Verificare lo stato e la scadenza.** Trascrivere opening date, deadline, ora e fuso orario **come pubblicati**; distinguere `single-stage`, `two-stage`, `multiple cut-offs` e altre procedure. Una deadline di fase 2 non autorizza a dire che si può accedere direttamente alla fase 2; una call continua non equivale a uno sportello senza cut-off. Registrare lo stato **alla data/ora della verifica**. Se assenti informazioni aggiornate, usare `STATO_NON_VERIFICATO`.
7. **Verificare l'oggetto finanziabile.** Riassumere `scope`, `expected outcomes` e, dove presente, `expected impact`, distinguendo attività richieste, facoltative e non ammesse. Non dedurre coerenza dalla presenza di parole generiche come «AI», «digitale» o «green».
8. **Controllare i requisiti preliminari.** Paesi, natura giuridica, dimensione, consorzio/numero di beneficiari, ruolo coordinatore/partner, capacità e altri vincoli, compresi TRL, forma giuridica e data di costituzione **solo se espressi nei documenti specifici**. Classificare `COERENTE_IN_VIA_PRELIMINARE`, `CONDIZIONATO`, `INCOMPATIBILE_DOCUMENTATO` o `NON_VERIFICATO`; mai `ammissibile al finanziamento` sulla base della sola skill.
9. **Separare i dati economici.** Non confondere **budget complessivo della call**, **budget del topic**, **contributo indicativo per progetto**, **percentuale di finanziamento**, **cofinanziamento**, **costi eleggibili** e **forma del sostegno**. Le cifre non presenti nella fonte vanno marcate `non pubblicato/non verificato`; `lump sum` è una modalità di grant, non una copertura integrale implicita.
10. **Rilevare le variazioni ufficiali.** Riaprendo la fonte primaria alla data della verifica, ricercare rettifiche, proroghe, FAQ e aggiornamenti di formulari e allegati pubblicati dopo l'eventuale analisi precedente, seguendo [references/change-log-protocol.md](references/change-log-protocol.md): scheda di differenze prima/dopo con fonte diretta (URL, documento, sezione); se non emerge nulla, «nessuna variazione ufficiale rilevata nelle fonti controllate alla data X»; se la fonte non è consultabile, «non verificabile alla data X». Segnalare l'effetto sulle skill 04–10 come avviso di riesame, mai come riscrittura automatica delle decisioni. La rilevazione è **puntuale, su richiesta**: la skill non esegue controlli ricorrenti in background, che richiedono uno strumento esterno attivato separatamente ed esplicitamente dall'utente.
11. **Classificare senza falsi positivi.** Escludere *calls for tenders* (appalti) se il mandato riguarda grant; non includere automaticamente premi, prestiti, garanzie o equity. Mantenere traccia di esclusioni motivate. Confrontare fino a **cinque topic/avvisi**, mostrando per ciascuno pertinenza, ostacolo principale, stato e fonte diretta. Se manca qualsiasi opportunità confermata, dichiararlo e indicare limiti della ricerca.
12. **Restituire schede ed evidenze** secondo [references/output-template.md](references/output-template.md). Mostrare verifiche completate, limiti e informazioni necessarie prima di candidarsi. Non effettuare registrazioni, submission, invii, contatti, modifiche a Drive/GitHub o monitoraggi ricorrenti senza distinta richiesta esplicita.

## Regole di stato e freschezza

- `OPEN_VERIFICATO`: la fonte **ufficiale corrente** mostra apertura/cut-off utilizzabile, verificata alla data indicata. Non confondere status della call padre con quello del topic.
- `FORTHCOMING_VERIFICATO`: pubblicazione/indicazione ufficiale di imminente apertura, **non** candidatura già presentabile.
- `CLOSED_VERIFICATO`: scadenza superata o chiusura espressamente dichiarata dalla fonte ufficiale; specificare la fase/cut-off di riferimento.
- `STATO_NON_VERIFICATO`: dato non disponibile, pagina inattendibile, fonte non accessibile, discrepanze non risolte o notizia non ufficiale. La mancata consultabilità della fonte **non** significa «nessuna modifica»: si dichiara «non verificabile alla data X», mai assenza di rettifiche.

Per le date considerare **l'istante della verifica**, non la data del documento isolata dal contesto. Non convertire fusi in autonomia se la fonte è ambigua; non trasformare date indicativamente pianificate in date di apertura confermate.

## Priorità delle fonti

1. Scheda ufficiale topic/avviso **e relativi aggiornamenti**; documenti di call e allegati vigenti.
2. Work programme/programma di attuazione; general annexes; normative e guide ufficiali applicabili.
3. Portali delle autorità nazionali/regionali o dei soggetti attuatori competenti, per la relativa modalità di gestione.
4. Pagine di riepilogo istituzionali per scoperta; terze parti solo come segnalazione da verificare **sulla fonte primaria**.

Non attribuire contenuto a una fonte mai aperta. Citare URL dell'atto o record specifico, data di accesso e sezioni/pagine determinanti. Link raccolti in [references/official-sources.md](references/official-sources.md).

## Evidenze minime per ogni opportunità

- Programma + call ID + topic ID (ove applicabile) **o** autorità + avviso ID.
- URL primario **specifico** e data/ora dell'ultima verifica, più documento applicabile.
- Stato temporalmente verificato, date e scadenze per fase/cut-off (ora/fuso se presenti).
- Obiettivo/attività finanziabili, beneficiari/territorio/partenariato, tipo di finanziamento.
- Distinzione fra budget call, budget topic, contributo progetto e tasso; `NON_VERIFICATO` dove mancano dati.
- Confronto tra necessità dell'utente e condizioni note; vincoli residui; motivazione delle esclusioni.

## Esiti, condizioni di arresto e casi limite

- Se il portale non risponde, **non** sostituire un link generico a un programma con un topic inventato.
- Se si trova una call ma non i suoi topic, dichiarare il livello di dettaglio raggiunto.
- Se call/topic sono aggiornati, registrare *versione della verifica*; non riutilizzare scadenze storiche senza riapertura ufficiale.
- Se non è nota la forma giuridica del richiedente, non considerarla ostativa né presumere la candidabilità di una società da costituire.
- Se una misura è nazionale o regionale con fondi UE, usare la denominazione dell'**avviso** dell'autorità competente, senza forzare la tassonomia call/topic di Horizon.
- Non eseguire un processo di candidatura. Una lista di opportunità non costituisce una valutazione legale della loro eleggibilità.

## Test di accettazione

Controllare i casi di [references/test-cases.md](references/test-cases.md): call con più topic; procedura a due fasi; cut-off ripetuti; una società ancora da costituire; dati economici eterogenei; avviso regionale; appalto erroneamente classificato come grant; URL e status indisponibili; rettifica ufficiale documentata con conferma prima/dopo. Il controllo `scripts/check_skill.py` testa **solo struttura e riferimenti**, non l'esecuzione effettiva dell'agente né la verifica live delle opportunità.

## Esempi di richieste

> «Trova i topic Horizon Europe su materiali sostenibili aperti oggi; voglio ID, deadline, budget topic e fonti ufficiali.»

> «Per il programma LIFE individua le call pertinenti al ripristino di habitat; separa quelle aperte e future.»

> «Cerco avvisi FESR per imprese in Lazio: non voglio proposte generiche sui fondi, ma link alle misure e requisiti del soggetto attuatore.»

I testi degli esempi indicano **richieste-tipo**, non la prova che esistano oggi avvisi corrispondenti.
