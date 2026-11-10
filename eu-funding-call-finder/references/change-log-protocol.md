# Protocollo di verifica versioni, rettifiche e aggiornamenti — Skill 03

Le opportunità cambiano **dopo** la pubblicazione: proroghe, rettifiche (*corrigenda*), FAQ e chiarimenti vincolanti, nuove versioni di formulari, allegati e call topics. Questo protocollo definisce come **riconoscere ed esporre le variazioni ufficiali**, distinguendo la rilevazione puntuale su richiesta dal monitoraggio ricorrente opzionale.

## 1. Fonte ufficiale competente

La fonte della verità dipende dalla modalità di gestione, mai dallo strumento usato per primo:

| Modalità | Fonte primaria delle variazioni |
| --- | --- |
| Gestione diretta (es. Horizon Europe, LIFE) | Funding & Tenders Portal: pagina del topic/call, aggiornamenti (*history of changes*), corrigenda e FAQ pubblicate |
| Gestione concorrente (es. FESR, FSE+) | Sito ufficiale dell'autorità di gestione o dell'ente attuatore del bando nazionale/regionale: rettifiche, avvisi di modifica, FAQ |
| Gestione indiretta | Sito ufficiale dell'organismo attuatore o intermediario designato, come documentato dalla fonte istituzionale |

Per gli avvisi nazionali/regionales in gestione concorrente **non** applicare il canale Funding & Tenders Portal e non usare la sua semantica di aggiornamento: molti portali regionali pubblicano rettifiche come semplici "aggiornamento del bando" senza numerazione formale delle versioni.

## 2. Cosa rilevare: tipologia di variazioni

- **Scadenze e finestre:** proroghe, anticipamenti, modifiche di cut-off o fasi.
- **Requisiti e destinatari:** ammissibilità, composizione del consorzio, Paesi, capacità economico-finanziaria.
- **Budget:** importi di call/topic, contributo indicativo, tassi.
- **Criteri di valutazione e pesi.**
- **Formulari, allegati e documenti di call:** nuove versioni con numerazione o data.
- **FAQ e chiarimenti ufficiali** che completano o reinterpretano il testo del bando.

## 3. Procedura di rilevazione puntuale (su richiesta)

1. **Riapri la fonte primaria corrente** alla data della verifica; non usare copie cache, aggregatori o riepiloghi come prova dello stato attuale. Registrare data e ora (con fuso) della verifica.
2. **Ricostruisci lo stato riferito:** per ogni documento applicabile registrare versione, data di pubblicazione e URL diretto; dove il portale pubblica una *history of changes*, consultarla integralmente.
3. **Confronta con la versione precedente nota** (output precedente della Skill 03, dossier dell'utente o versione precedente dell'analisi). Dove non esiste una versione precedente registrata, dichiararlo: sarà la **baseline** del prossimo confronto.
4. **Compila la scheda di differenze** solo per i valori effettivamente pubblicati:

| Campo | Prima (versione/data) | Dopo (versione/data) | Fonte (URL, documento, sezione) |
| --- | --- | --- | --- |
| Scadenza/budget/requisito… | … | … | … |

5. **Segnala l'effetto a valle** senza riscrivere decisioni già prese: se la variazione tocca ammissibilità, dati economici, documenti richiesti, formulario o scadenze, stampa l'avviso «requisito da riesaminare» con riferimento all'output interessato (Skill 04–09).

## 4. Frasi di stato obbligatorie

- Se dopo il confronto non emerge nulla: «**Nessuna variazione ufficiale rilevata nelle fonti controllate alla data X**», elencando le fonti controllate. **Non** affermare in assoluto che non esistono variazioni.
- Se la fonte non è consultabile (portale offline, pagina rimossa, accesso richiesto): «**Non verificabile alla data X**». L'indisponibilità **non** equivale a "nessuna modifica".
- Ogni favore conciliazione di prima/dopo con fonti terze (aggregatori, newsletter, NCP) va etichettato **indizio**, da riscontrare **sulla fonte primaria** prima di qualsiasi decisione.

## 5. Esempio reale documentato di rettifica

Durante la definizione della versione finale del documenti di call di Health Cluster del *Horizon Europe Work Programme 2026–2027*, le scadenze sono state **anticipate** rispetto alla bozza precedente: per il bilancio HORIZON-HLTH-2027-01 e per lo stage 1 HORIZON-HLTH-2027-02-two-stage la scadenza di presentazione è passata da **13 aprile 2027** a **17 febbraio 2027**, e per HORIZON-HLTH-2027-03 da **22 settembre 2027** a **16 settembre 2027** (con aggiornamento del titolo del topic HORIZON-HLTH-2027-03-TOOL-08). La variazione è riscontrabile confrontando Whithe bozza del work programme (giugno 2026) con la versione finale (ottobre 2026) e i record del Funding & Tenders Portal.

⚠️ L'esempio vale **alla data della sua scrittura (10/11/2026)** ed è riferito da fonti che riportano il work programme ufficiale: all'uso, riscontrare prima/dopo direttamente sulla fonte primaria ed eseguire i passaggi della sezione 3. Un aggiornamento di un work programme non è un *corrigendum* di un singolo topic, ma la conseguenza è la stessa: gli output della Skill 03 relativi a quelle call vanno **rigenerati**, non ereditati.

## 6. Monitoraggio ricorrente: opzionale e separato

La Skill 03 **non esegue controlli in background**. Rilevazione periodica e notifiche richiedono uno strumento esterno (scheduler, cron, agente proattivo o servizio dedicato) attivato **separatamente ed esplicitamente** dall'utente:

- la skill può preparare, su richiesta, una lista di opportunità + fonti da monitorare e la scheda di confronto vuota;
- l'esecuzione ricorrente e le notifiche sono decise e configurate dall'utente;
- non presentare il monitoraggio come "già attivo"/gratuito/disponibile implicitamente, né promette aggiornamento continuo.

## 7. Impatto sulle skill successive (04–09)

- **04 ammissibilità:** requisiti modificati → riesaminare la decisione, senza considerarla automaticamente invalidata (Se non è stato formalmente deciso dall'utente).
- **05 analisi economico-finanziaria:** importi/tassi modificati → ricalcolo e nuova revisione con la fonte aggiornata.
- **06 piano candidatura:** documenti allegati/scadenzario modificati → rimappare produzione documentale.
- **07 redazione:** formulario/versione → verificare gli strumenti usati prima di riutilizzare la bozza.
- **08 review:** criteri/pesi → riesaminare la griglia applicata.
- **09 pre-check e 10 post-invio:** scadenze e canali → ricontrollare i tempi residui; le evidenze post-invio restano quelle del documento ufficiale attivo all'invio.

L'impatto è un **avviso**, non una riscrittura automatica: le versioni precedenti restano negli output per tracciabilità, distinte dalla versione corrente.
