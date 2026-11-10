# Review qualitativa argomentata — Skill 08

Questo protocollo estende i controlli formali e di copertura (già nel [protocollo di revisione](review-protocol.md)) con un'analisi **qualitativa e argomentata** della proposta rispetto ai criteri di valutazione **effettivamente pubblicati** per la specifica call/topic/avviso. È un metodo interno: non attribuisce valutazioni dell'autorità e non integra criteri non disponibili.

## 1. Quando si può eseguire

- La review qualitativa richiede: (a) **criteri e sottocriteri ufficiali identificati**, con fonte, versione e punto di riferimento; (b) **la versione della proposta** oggetto della review; (c) le evidenze disponibili. Se i criteri pubblicati mancano o non sono accessibili, **non eseguire una review qualitativa su criteri presunti**: registrare `CRITERI_NON_DISPONIBILI` e limitarsi ai rilievi formali e alle osservazioni incontroverse.
- La simulazione qualitativa è sempre distinta da una reale valutazione dell'autorità: nessun punteggio, esito o probabilità di finanziamento.

## 2. Assi qualitativi (solo dove pertinenti al tipo di opportunità)

| Asse | Domande guida | Non fare |
| --- | --- | --- |
| **Obiettivi** | Sono chiari, necessari e collegati agli obiettivi documentati dell'opportunità? Distinguono generale/specifici? Sono misurabili o falsificabili? | Non riempire gli obiettivi specifici con contenuti non documentati |
| **Contesto e bisogni** | L'analisi del contesto/dei bisogni cita fonti ed è pertinente al territorio o al settore? | Non inventare dati statistici né trasformare una semplice affermazione in un bisogno accertato |
| **Metodologia** | L'approccio è plausibile, coerente con le competenze e sostenibile nel tempo? Le ipotesi e le condizioni sono esplicite? | Non confondere attività con risultati, né plausibilità con soddisfacimento del criterio |
| **Catena d'intervento** | Problema → intervento → attività → output → outcome → impatto è continua e testabile? | Non considerare la catena dimostrata solo perché la terminologia è presente |
| **Indicatori e verifica** | Ogni risultato significativo ha un indicatore verificabile (definizione, baseline, target, periodo, metodi di rilevazione)? | I valori non provati restano `STIMA_NON_VALIDATA`, mai dati accertati |
| **Rischi e sostenibilità** | Rischi, assunzioni e condizioni esterne sono dichiarate? Le piste di sostenibilità dopo il finanziamento sono fondate? | Non accettare il capitolo «rischi» generico senza base documentata |
| **Coerenza interna** | Esistono discordanze fra parti del testo (obiettivi vs attività vs budget vs cronologia)? | Non cercare coerenza per anticipazione; indicare le discordanza senza risolverle arbitrariamente |

Ogni asse è **applicabile solo se pertinente** al tipo di opportunità e alla sua griglia ufficiale: la skill adatta gli assi, non impone uno schema universale.

## 3. Tracciatura e struttura dei rilievi qualitativi

Ogni rilievo qualitativo `QLM-*` è tracciato con almeno cinque campi:

| Campo | Contenuto |
| --- | --- |
| **Sezione/estratto** | Localizzazione nel testo della proposta (sezione, paragrafo o citazione breve) |
| **Criterio applicabile** | Criterio/sottocriterio ufficiale con fonte, versione e localizzatore; oppure «osservazione di metodo, non normativa» |
| **Evidenza** | Cosa nei materiali della proposta o nella documentazione fonda il rilievo |
| **Impatto potenziale** | Come il punto può incidere sulla valutazione dell'autorità, senza quantificare in punteggi |
| **Suggerimento di miglioramento** | Correzione proposta, indicata come raccomandazione, non come riscrittura automatica dell'estensore |

«Non trovato nella proposta» vale solo per le **parti realmente esaminate**: dove non è stato letto integralmente, dichiararlo.

## 4. Tipologia dei rilievi (distinzione obbligatoria)

Classificare ogni rilievo in una delle categorie, senza mescolarle:

1. **Non conformità accertata** — rispetto a un requisito/criterio documentato e verificato con localizzatori a due estremità (fonte ufficiale + passaggio della proposta).
2. **Debolezza argomentativa** — il testo esiste, ma la difesa del punto non funziona (es. impatto rivendicato senza logica dimostrabile). Non è un inadempimento.
3. **Rischio o ipotesi** — prospettiva non accertata, con conseguenze potenziali segnalate e materiale etichettato `STIMA_NON_VALIDATA` o da confermare.
4. **Mancanza di dati** — materiale non disponibile alla review, da richiedere al proponente; non è un inadempimento dimostrato.
5. **Osservazione editoriale** — sempre classificata `OSSERVAZIONE_REDAZIONALE`, separata dagli obblighi del bando.
6. **Decisione riservata al proponente** — alternative legittime dove la scelta appartiene all'utente, non alla review.

## 5. Valutatore critico simulato (opzionale, chiaramente etichettato)

Su richiesta, la skill può presentare **una prospettiva di valutatore critico simulato** sul testo:

- il titolo della sezione dichiara **«valutazione simulata — non rappresenta il giudizio di alcun valutatore reale, dell'autorità o della Commissione»**;
- il contesto della simulazione è esplicito («assumendo i criteri X versione Y, senza disporre dell'elaborato ufficiale dell'autorità»);
- **non** assegna punteggi equivalenti a scale ufficiali, non predice esiti né probabilità di finanziamento;
- **non** attribuisce affermazioni a valutatori reali senza fonte.

## 6. Programmi diversi da Horizon Europe

La review qualitativa si adatta alla struttura dell'opportunità: avvisi Erasmus+, LIFE, Digital Europe, Creative Europe, Interreg e FESR/FSE+ hanno griglie e formulari propri. Non applicare automaticamente criteri standard Horizon; se la griglia dell'autorità non è documentata, il perimetro è limitato alla coerenza interna e alle osservazioni incontroverse, con dichiarazione del limite. Le evidenze condivise dall'attività di progettazione (Skill 11 `eu-funding-project-designer`, quando disponibile) e dalla redazione (Skill 07) restano **input citati**, mai sostituzione del riscontro sui documenti ufficiali della call/avviso.

## 7. Coordinamento con la redazione (Skill 07)

I rilievi qualitativi `QLM-*` usano gli stessi ID di tracciabilità `REQ-*`/`SEC-*`/`CLM-*` quando presenti; la conclusione della review è un **input per la revisione della bozza**, non una modifica automatica del progetto: le scelte restano approvate dal proponente.
