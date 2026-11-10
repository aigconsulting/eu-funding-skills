# Cicli QFP, programmi e specializzazione della redazione — Skill 07

Questa reference documenta la **strategia di specializzazione per programma e ciclo di programmazione** senza duplicare la skill e senza imporre un formulario universale. È una guida di metodo: le regole del bando specifico prevalgono su tutto ciò che qui si descrive.

## 1. Cicli QFP e status giuridico (da verificare all'uso)

| Ciclo | Status alla scrittura (10/11/2026) | Note di verifica |
| --- | --- | --- |
| **2014–2020** | Concluso; programmi in fase di *closing* (pagamenti, controlli, esiti in chiusura) | Salvo rettifiche, non accoglie nuove candidature: rilevante solo per continuità storica o per esiti ancora pendenti |
| **2021–2027** | In vigore; il Quadro finanziario pluriennale 2021–2027 e i regolamenti istitutivi dei programmi sono adottati | Ciclo operativo di riferimento: annualità, work programme e call vigenti si consultano sulla fonte ufficiale |
| **2028–2034** | **Solo proposizioni**: il nuovo QFP e i programmi post-2027 sono fasi di proposta e negoziazione | **Nessuna regola futura va presentata come vigente** senza conferma di adozione. Le bozze di work programme sono anticipazioni indicative, non disciplina applicabile |

⚠️ Cicli e status si **verificano sempre alla data d'uso**: adozioni, rettifiche, proroghe tra cicli e annualità cambiano. Distinguere sempre: atto proposto, atti adottati, atti applicabili alla call/avviso specifico. Il ciclo dura ordinariamente **sette anni**: questo giustifica conoscenze specialistiche per programma/ciclo aggiornate in modo controllato, non un formulario per tutte le combinazioni.

## 2. Strategia: skill trasversale + fonti dinamiche + moduli solo dove servono

- **La Skill 07 resta trasversale** e accoglie qualsiasi programma, ciclo QFP e modalità di gestione: la specializzazione entra **dai documenti della specifica call/topic/avviso**, non da template hardcoded.
- **Ricerca dinamica obbligatoria:** per ogni opportunità, reperire dalla fonte ufficiale competente formulari, limiti, criteri, allegati e aggiornamenti vigenti; ciò che si indica qui descrive il **lessico**, mai i requisiti (le regole di consulta e tracciamento restano nel [protocollo delle evidenze](evidence-protocol.md)).
- **Scheda di lessico per programma/ciclo:** quando un programma ricorre, l'agente può mantenere una scheda di nomenclatura, documenti di riferimento e canali ufficiali, **distinta sempre** dai requisiti del bando vigente. In questo repository si mantiene la sola tabella della sezione 3: nessuna copia integrale di documenti procedurali.
- **Quando non c'è proposta narrativa, non forzarne una:** premi con sole dichiarazioni, strumenti finanziari senza formulario di progetto, avvisi riservati a enti che devono usare esclusivamente il modulo ufficiale → esito `NON_APPLICABILE` oppure bozza ridotta ai soli campi documentati.
- **Interfaccia con le skill adiacenti invariata:** 04 ammissibilità, 05 economia, 06 piano, 08 review restano fuori perimetro; preservare le tracce `REQ-*`, `SEC-*`, `CLM-*`.

## 3. Nomenclatura per programma (guida, non regola)

| Programma | Canale tipico della fonte | Lessico ricorrente |
| --- | --- | --- |
| Horizon Europe | Funding & Tenders Portal | call, topic, work programme, cluster, destination, Part A / Part B, General Annexes |
| Digital Europe, EDF | Funding & Tenders Portal | call, topic, work programme; requisiti di possesso e restrizioni particolari |
| Erasmus+ | Sito ufficiale del programma e National Agencies competenti per l'azione/Key Action | scadenze di KA e moduli del gestore; la denominazione del modulo varia per il gestore |
| LIFE | Funding & Tenders Portal (call dell'agenzia competente) | full proposal a due fasi; flussi specifici per le call di azione tecnica |
| Creative Europe | Funding & Tenders Portal (EACEA) | call dell'agenzia; modelli del singolo call document |
| Interreg | Sito del singolo programma di cooperazione e della segreteria | espressioni e allegati programma |
| FESR, FSE+ | Autorità di gestione nazionale/regionale | avviso, finestre di raccolta, criteri/nomenclatura dell'autorità |

Questi esempi sono **indicativi e da riscontrare**: se una struttura non è provabile per la call specifica, non entra nella bozza.

## 4. Confronto fra procedure (minimo due programmi, fonti realmente consultate alla data)

Quando si usa la skill con un programma diverso da Horizon, documentare nel registro:

1. **Un topic Horizon Europe** (es. azione di ricerca sul Funding & Tenders Portal): la bozza segue la **Part B** pubblicata per il singolo topic (struttura delle sezioni **solo come previsto nel formulario vigente**), con General Annexes e call documents.
2. **Un bando di un programma differente** (es. avviso Erasmus+ o FESR): la bozza segue il **modulo/avviso dell'autorità o agenzia gestore** (struttura, denominazioni, allegati) **senza trasportare la struttura Horizon** (Part A/B, destination, budget call/topic).

Ogni scenario va aggiunto come caso di test dedicato in [test-cases.md](test-cases.md); la conferma della struttura richiede sempre la consultazione puntuale della fonte primaria alla data d'uso.

## 5. Prevalenza del bando specifico

- Schede orientative, esempi e know-how precedente **non prevalgono** sull'atto del bando: rettifiche, addenda e istruzioni dell'autorità competente hanno priorità nelle proporzioni in cui gli atti applicabili lo prevedano.
- In caso di conflitto non risolto fra testi vigenti, etichettare i punti coinvolti `BLOCCATA_DA_FONTI`, senza dedurre una gerarchia giuridica universale.
- Elementi assenti o non verificabili restano segnaposto o `BLOCCATA_DA_FONTI`: nessun dato su beneficiari, costi, percentuali o obblighi viene inventato per uniformare la bozza a un modello generico.
