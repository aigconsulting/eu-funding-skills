# Tassonomia e relazioni

## Prima distinzione: modalità di gestione

| Modalità | Gestione | Dove cercare gli avvisi |
| --- | --- | --- |
| Diretta | Commissione europea, servizi o agenzie esecutive | Funding & Tenders Portal e siti degli enti competenti |
| Concorrente (shared) | Commissione + Stati membri/autorità di gestione | Portali nazionali e regionali; programmi adottati |
| Indiretta | Partner attuatori, organismi delegati o intermediari | Ente attuatore e sue fonti ufficiali |

Un programma o intervento può presentare particolarità: verificare sempre la modalità specifica.

## Modello di riferimento per Horizon Europe

**Relazioni di governo e di indirizzo (non necessariamente parent-child):**

- Priorità politiche dell'Unione → contribuiscono a orientare il bilancio e la programmazione.
- Quadro finanziario pluriennale (QFP) → colloca finanziariamente i programmi, secondo le rubriche di bilancio.
- Programma `Horizon Europe` → regolamento istitutivo, struttura in pilastri/parti, risorse, obiettivi.
- `Strategic plan` → orienta l'elaborazione di determinati work programme. Per Horizon Europe, il piano 2025–2027 definisce orientamenti per gli investimenti.

**Articolazione operativa (verificare il documento e le relazioni reali):**

```text
Horizon Europe (programma)
├── pilastri e parti (classificazione)
│   └── es. Pillar II → Cluster 5 (classificazione)
├── piano strategico (indirizzo)
└── work programme / parte di work programme (attuazione)
    ├── destination (quando presente)
    └── call for proposals
        └── topic
            └── proposta progettuale (eventuale)
```

Non presupporre che `destination` sia sempre un genitore tecnico della `call`: nei documenti il raggruppamento e l'identificativo possono variare. Registrare le associazioni documentate come **relazioni tipizzate** (es. `covered_by`, `part_of`, `addresses`, `funded_under`, `implements`).

**Dati di un topic:** titolo e codice, action type (es. RIA/IA/CSA se previsti), expected outcomes, scope, condizioni e annex applicabili, budget indicativo, contributo per progetto, eventuali deroghe e scadenze effettive.

## Modello orientativo per i fondi a gestione concorrente

```text
Priorità UE / politica di coesione
  → QFP / fondo pertinente (es. FESR)
  → Accordo di partenariato (se pertinente)
  → Programma nazionale o regionale adottato
  → Priorità / obiettivo specifico / azione (se presenti)
  → Avviso pubblico / bando dell'autorità competente
  → Domanda / progetto
```

Gli atti di programmazione e le denominazioni variano per fondo, ciclo e territorio. Non usare questo schema come obbligo normativo universale.

## Relazioni e grado di evidenza

- `part_of` = appartenenza formale (es. un topic a una call, se attestato).
- `implements` = attuazione documentata di un obiettivo/programma.
- `addresses` = intervento che affronta una priorità o destination, se documentato.
- `aligned_with` = corrispondenza interpretativa, **non** gerarchia formalmente dimostrata.
- `published_by` = ente che pubblica il documento/avviso.

Ogni arco rilevante deve avere la propria evidenza: URL ufficiale, riferimento a sezione/pagina o codice, e data/versione quando disponibili.
