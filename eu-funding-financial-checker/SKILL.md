---
name: eu-funding-financial-checker
description: Analizza la finanziabilità economica di un topic o avviso UE distinguendo budget, contributo per progetto e beneficiario, costi ammissibili, tassi, cofinanziamento, liquidità e rendicontazione; restituisce dati documentati, ipotesi e simulazioni verificabili senza inventare condizioni o garantire sovvenzioni.
---

# EU Funding Financial Checker — Skill 05

## Scopo

Rispondere con fonti e calcoli controllabili a: **«Quanto finanzia davvero questa opportunità, su quali costi, per quale beneficiario, e quanta liquidità serve?»**. Analizzare un **topic/avviso identificabile** e, se forniti, budget e profilo del richiedente. Distinguere **sovvenzione, prestito, garanzia, investimento in equity e finanziamento misto**. Non trasferire tassi e criteri di un programma a un altro.

Questa skill segue logicamente `eu-funding-eligibility-checker`, ma può essere usata da sola. Non garantisce attribuzione di un grant, non sostituisce il grant agreement o la consulenza fiscale e non prepara/invia candidature.

## Input e regola di non invenzione

- **Per una verifica di un bando reale:** URL/ID della pagina ufficiale del topic/avviso, regime/azione applicabile e fonte vigente (call document, Annex, Grant Agreement o base normativa); data del controllo.
- **Per una simulazione numerica:** importi dei costi per categoria, ruolo del beneficiario, percentuale di finanziamento **esplicitamente attribuita alla fonte o dichiarata come ipotesi**, eventuale massimale per progetto/beneficiario (`grant_cap` nella simulazione), forma di finanziamento, metodo di costo, quota non ammissibile, calendario pagamenti se noto.
- Se l'utente chiede solo «quanto finanzia?» ma non fornisce il proprio budget, restituisci i **parametri documentati** senza inventare un progetto o importi per beneficiario.
- Se manca la fonte decisiva, segnala `NON_VERIFICATO`; non adottare il tasso Horizon per default, né il 25% indiretto per altri programmi. Se manca un input, puoi mostrare una simulazione **esplicitamente illustrativa** soltanto se utile.

## Gerarchia delle fonti e verifica

1. **Fonte vincolante dell'opportunità:** pagina topic/avviso, call document e rettifiche, condizioni finanziarie, scheda dell'azione e allegati applicabili.
2. **Regole generali applicabili:** General Annexes, programma di lavoro, EU Grants Annotated Grant Agreement (AGA), condizioni del grant specifico. Per fondi in gestione concorrente: programma nazionale/regionale, avviso, regime d'aiuto, linee guida e autorità attuatrice. Per gestione indiretta: regole dell'organismo incaricato.
3. **Confronta versioni, date e perimetro di applicazione.** Un AGA illustra contratti; non sostituisce le condizioni pubblicate del singolo topic. In Horizon Europe i General Annexes del programma principale non coprono automaticamente ERC, EIC, EIT o altre iniziative con work programme separati.
4. Registra **URL diretto, sezione/pagina, data di verifica e stato della fonte** per ogni parametro determinante; se due fonti sembrano in conflitto non decidere senza fondamento quale prevalga: descrivi il conflitto e sospendi il calcolo dipendente.

Vedi [fonti ufficiali e perimetro](references/official-sources.md).

## Procedura operativa — 8 passaggi

### 1 — Identificare la forma giuridico-finanziaria del sostegno

Classifica `GRANT_ACTUAL_COST`, `GRANT_UNIT_COST`, `GRANT_LUMP_SUM`, `FINANCING_NOT_LINKED_TO_COSTS`, `LOAN`, `GUARANTEE`, `EQUITY`, `BLENDED` o `ALTRO_NON_VERIFICATO`. Una combinazione di grant ed equity non è un unico fondo perduto; un prestito non è una sovvenzione. Premi e procurement richiedono trattamento distinto.

### 2 — Disambiguare gli importi pubblicati

Traccia separatamente:

- **Program budget:** disponibilità totale del programma/periodo, mai contributo del progetto.
- **Call budget:** dotazione totale della call, **non** attribuita automaticamente a un topic.
- **Topic budget:** dotazione aggregata del topic; non è grant per progetto.
- **Expected EU contribution per project:** contributo atteso/indicativo per progetto, **non** necessariamente minimo/massimo o diritto acquisito.
- **Minimum/maximum grant per project/beneficiary:** limite vincolante solo se il testo lo qualifica tale; annota unità, annualità, categoria di soggetto.
- **Beneficiary budget share:** porzione documentata o proposta per il singolo beneficiario di un consorzio. Non dividere il budget della call per i partner o per un numero arbitrario di progetti.

### 3 — Identificare le modalità di costo

Individua regime a **costi effettivi**, **unit costs**, **flat rate**, **lump sum** o **finanziamento non collegato ai costi**. Per unit e lump sum il metodo di calcolo/riconoscimento e la prova richiesta sono differenti: **non applicare meccanicamente la formula “spesa sostenuta × tasso”** a importi lump sum già fissati e non richiedere fatture di costo effettivo come unica prova di ammissibilità delle lump sum. Consultare le condizioni del grant.

### 4 — Classificare i costi

Per ogni voce riportare: categoria, importo, ente che lo sostiene, ammissibilità `AMMISSIBILE`/`NON_AMMISSIBILE`/`CONDIZIONATO`/`NON_VERIFICATO`, eventuale quota imputabile e fonte. Verificare espressamente personale, subappalti, acquisti, viaggi, attrezzature e ammortamento, servizi, supporto a terzi, IVA, costi indiretti, eventuali massimali e costi anteriori all'avvio. Non assimilare «costo utile al progetto» a «costo ammissibile». Non conteggiare due volte diretti/indiretti né costi coperti da più grant in violazione delle regole di cumulo.

### 5 — Determinare l'intensità e l'eventuale massimale

Il tasso può dipendere da **programma, tipo di azione, beneficiario, territorio, impresa, dimensioni, regime di aiuto e categoria di costo**. Non presumere che una categoria riceva il tasso massimo previsto dal programma. Distinguere tasso ordinario, eccezione per enti no profit, intensità degli aiuti di Stato, limiti de minimis ove pertinenti e massimali assoluti. Registrare i parametri **per beneficiario** se diversi tra partner.

**Riferimento non universale (Horizon Europe, General Annexes 2026–2027, Annex G):** RIA 100%; IA 70%, fino al 100% per enti non profit; CSA 100%, salvo condizioni specifiche. Per i costi indiretti dell'Horizon main work programme si applica un flat rate del 25% **sulla base ammissibile**, escludendo fra gli altri subappalti e sostegno finanziario a terzi. Queste percentuali sono **esempi settoriali, non impostazioni predefinite della skill**.

### 6 — Stimare la quota di finanziamento con formule esplicite

**Solo per grant a costi ammissibili con tasso noto:**

- `costi_ammissibili_diretti = somma voci dirette ammissibili`, attribuite correttamente;
- `indiretti = base_indiretti_documentata × aliquota_flat_rate` **solo** se prevista e correttamente definita;
- `costi_ammissibili_totali = diretti + indiretti + altre categorie ammissibili non già incluse`;
- `contributo_teorico = costi_ammissibili_totali × tasso_applicabile`;
- `contributo_stimato = minimo(contributo_teorico, massimali vincolanti applicabili)`; non usare il budget complessivo del topic come massimale del singolo progetto se non documentato;
- `fabbisogno_non_coperto = costi_totali_previsti − contributo_stimato` **a parità di perimetro** (quota da finanziare con risorse proprie o altre fonti compatibili), che **non è automaticamente** la cassa iniziale.

Per tassi/categorie differenziati calcolare per riga/beneficiario prima di aggregare. Se il budget è provvisorio, esplicitare ipotesi e sensibilità; se manca base di calcolo, **non** dare una cifra apparentemente certa.

È disponibile un **calcolatore deterministico illustrativo** per una singola aliquota documentata: `python3 eu-funding-financial-checker/scripts/estimate_grant.py input.json` (formato in [modello di calcolo](references/calculation-model.md)). Non acquisisce bandi, non fa verifiche normative né attribuisce finanziamenti.

### 7 — Separare cofinanziamento, anticipo e fabbisogno di cassa

Analizzare distintamente:

- **Quota di cofinanziamento** derivante da tasso e costi ammissibili, oltre ai **costi non ammissibili**, dove applicabile;
- **Prefinancing** (eventuale anticipo), **interim payments**, saldo, rendicontazioni e ritardi possibili; valori/tempi **solo se documentati** nel grant agreement/Data Sheet o nell'avviso;
- **Trattenute/garanzie**, fra cui il Mutual Insurance Mechanism (MIM) in Horizon Europe se pertinente: verificare percentuale **del caso**; i General Annexes 2026–2027 menzionano un intervallo 5–8%, non un 5% universale;
- **Fabbisogno di circolante temporaneo**, che dipende da scadenze reali di pagamento/spesa e dai trasferimenti del coordinatore: se questi dati mancano, riportare `NON_CALCOLABILE`, senza equipararlo al cofinanziamento.

Indica chiaramente che prefinancing non incrementa il grant complessivo e che il contributo teorico non equivale a fondi già concessi o liquidati.

### 8 — Restituire valutazione finanziaria con limiti

Compila [scheda risultato](references/output-template.md) e chiudi con:

- `VERIFICATO_DA_FONTE`: parametro esatto e fonte;
- `CALCOLATO_SU_INPUT`: formula, importi, tasso e assunzioni dichiarate;
- `IPOTESI_ILLUSTRATIVA`: variabile introdotta **solo** a scopo didattico;
- `NON_VERIFICATO` o `NON_CALCOLABILE`: dati mancanti o contraddizioni;
- `NON_APPLICABILE`: forma finanziaria differente;
- `DECISIONE_AUTORITA`: concessione effettiva e liquidazione riservate all'ente competente.

La risposta può concludere con eventuali verifiche necessarie o dati minimi da reperire, **senza** imporre procedure, avviare richieste o promettere un finanziamento.

## Guardrail indispensabili

1. **Fondo perduto ≠ 100% delle spese.** Un tasso 100% copre al più il perimetro *ammissibile* previsto dalle condizioni; spese escluse restano scoperte.
2. **Budget del topic ≠ contributo per beneficiario**. `Expected contribution` ≠ contributo garantito.
3. **Tasso 70% non è sempre equivalente a cofinanziamento proprio 30% del costo globale**: costi esclusi, indiretti e massimali possono modificare l'onere totale.
4. **Costi indiretti**: l'aliquota deve avere una base giuridicamente corretta; non applicare il 25% a tutto, né ai subappalti Horizon se esclusi dalla base.
5. **Lump sum**: distinguere budget ex ante da condizioni di pagamento ex post; non sovrapporre il modello actual cost.
6. **Prestiti/equity/garanzie**: analizzare rimborso, diluizione, copertura e costo economico con regole ad hoc; non stimarne il valore come fondo perduto.
7. **Consorzi**: distinguere risorse di progetto da quota del singolo beneficiario.
8. **Regimi nazionali/regionali e aiuti di Stato**: applicare solo le percentuali e le regole della specifica misura; non importare le regole Horizon o Digital Europe.
9. **Pagamenti e liquidità**: anticipo, eventuale quota trattenuta e calendario non sono presumibili.
10. **No doppio finanziamento della stessa voce**, salve specifiche regole di sinergia documentate.
11. **Nessuna fonte certa → nessuna cifra certa**. Riportare la lacuna anziché completarla per analogia.

## Test e stato della skill

- Controlli struttura/metadati/fonti: `python3 eu-funding-financial-checker/scripts/check_skill.py`.
- Test del calcolatore matematico: `python3 eu-funding-financial-checker/scripts/test_calculations.py`.
- Casi di comportamento agentico (da eseguire con documenti reali) in [test-cases](references/test-cases.md). Non confondere **test unitari del calcolatore** e **validazione giuridica della normativa applicabile**.
