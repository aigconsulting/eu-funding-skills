# EU Funding Skills

Raccolta autonoma di skill per orientarsi nei finanziamenti dell'Unione europea, dalla struttura istituzionale fino alla preparazione della proposta e al tracciamento documentale successivo alla presentazione, nel rispetto della disciplina dello specifico avviso. Contenuti generali, senza riferimenti a specifici progetti aziendali.

## Skill disponibili

1. [`eu-funding-hierarchy`](eu-funding-hierarchy/SKILL.md) — ricostruisce gerarchia e nessi documentati fra priorità, QFP, programma, work programme, call e topic, tenendo conto delle modalità di gestione.
2. [`eu-funding-programme-finder`](eu-funding-programme-finder/SKILL.md) — parte da un obiettivo e individua programmi, fondi e strumenti UE plausibili, distinguendo finalità, modalità e canali ufficiali.
3. [`eu-funding-call-finder`](eu-funding-call-finder/SKILL.md) — cerca e verifica topic, call e avvisi specifici, con stato, fasi, scadenze, condizioni e link primari.
4. [`eu-funding-eligibility-checker`](eu-funding-eligibility-checker/SKILL.md) — verifica preliminarmente requisiti di richiedente, finanziabilità, partenariato, progetto e presentazione, distinguendo blocchi accertati, condizioni e lacune documentali. Non emette certificazioni di ammissibilità.
5. [`eu-funding-financial-checker`](eu-funding-financial-checker/SKILL.md) — distingue budget di programma/call/topic/progetto, grant, costi ammissibili, tassi, massimali, cofinanziamento e flussi di cassa; comprende una simulazione aritmetica controllabile, senza attribuire finanziamenti.
6. [`eu-funding-application-planner`](eu-funding-application-planner/SKILL.md) — ricostruisce per ogni specifico avviso/fase la documentazione richiesta, i criteri, le scadenze e la preparazione della candidatura, senza applicare schemi di altri programmi né presentare domande.
7. [`eu-funding-proposal-drafter`](eu-funding-proposal-drafter/SKILL.md) — redige la bozza secondo il formulario realmente applicabile, tracciando requisiti, fonti ed evidenze, con segnaposto per i dati mancanti e un validatore formale del manifest.
8. [`eu-funding-proposal-reviewer`](eu-funding-proposal-reviewer/SKILL.md) — confronta una versione identificata della proposta con i criteri e le condizioni della specifica opportunità, separando rilievi accertati, rischi, lacune informative e suggerimenti redazionali. Integra un validatore formale del rapporto; non certifica la proposta.
9. [`eu-funding-submission-checker`](eu-funding-submission-checker/SKILL.md) — esegue pre-check documentali su versione finale, allegati, canale, scadenze e condizioni della specifica opportunità; distingue blocchi, lacune e controlli soddisfatti senza presentare domande.

10. [`eu-funding-post-submission-tracker`](eu-funding-post-submission-tracker/SKILL.md) — ricostruisce in sola lettura eventi successivi alla presentazione, comunicazioni dell’autorità, esiti, eventuali richieste e scadenze; distingue aggiornamenti verificati, lacune e azioni proposte, senza monitoraggio ricorrente o modifiche ai portali.

## Ordine operativo

**Gerarchia → Programma → Call/topic → Ammissibilità preliminare → Analisi economico-finanziaria → Piano di candidatura → Bozza della proposta → Review documentale → Pre-check di presentazione → Tracciamento degli eventi post-invio.** È possibile eseguire le singole skill autonomamente quando si conoscono già programma e topic.

## Installazione

Le skill seguono lo standard **Agent Skills**: ogni cartella contiene `SKILL.md`, `references/` e `scripts/`, quindi lo stesso pacchetto funziona con Claude Code, OpenCode e gli altri client compatibili. Installare significa rendere disponibili le cartelle `eu-funding-*` nella directory di skill del client.

### Script di installazione

```bash
python3 install.py --list              # skill e destinazioni disponibili
python3 install.py claude              # ~/.claude/skills (Claude Code, tutti i progetti)
python3 install.py claude-project      # .claude/skills (solo il repository corrente)
python3 install.py opencode            # ~/.config/opencode/skills
python3 install.py opencode-project    # .opencode/skills
python3 install.py ~/.agents/skills    # percorso esplicito
python3 install.py claude --link       # symlink: gli aggiornamenti del repo sono immediati
python3 install.py claude --dry-run    # mostra le operazioni senza modificare nulla
python3 install.py claude --uninstall  # rimuove le skill installate
```

Opzioni: `--force` sovrascrive versioni diverse già presenti, `--verify` esegue prima i controlli statici. Lo script non installa dipendenze e non modifica la configurazione dei client; senza `--force` non sovrascrive nulla e segnala le skill già installate.

### Claude Code

| Ambito | Comando | Percorso |
| --- | --- | --- |
| Personale (tutti i progetti) | `python3 install.py claude` | `~/.claude/skills/<skill>/SKILL.md` |
| Progetto (da committare per condividerlo) | `python3 install.py claude-project` | `.claude/skills/<skill>/SKILL.md` |
| Plugin | copia manuale | `<plugin>/skills/<skill>/SKILL.md` |

Le skill compaiono in `/skills` e si invocano con `/eu-funding-hierarchy`. Se la directory `~/.claude/skills` o `.claude/skills` non esisteva all'avvio della sessione, eseguire `/reload-skills`.

### OpenCode

| Ambito | Comando | Percorso |
| --- | --- | --- |
| Globale | `python3 install.py opencode` | `~/.config/opencode/skills` (o `$XDG_CONFIG_HOME/opencode/skills`) |
| Progetto | `python3 install.py opencode-project` | `.opencode/skills` |

OpenCode cerca le skill anche in `~/.claude/skills` e `~/.agents/skills` (e nelle rispettive directory di progetto): l'installazione per Claude Code è quindi già sufficiente. Le skill si caricano con `@eu-funding-hierarchy` oppure automaticamente quando pertinenti; `/reload` forza il ricaricamento. Directory aggiuntive si possono elencare nella chiave `skills` di `opencode.json(c)`.

### Altri client

Qualsiasi client che implementi lo standard Agent Skills carica le cartelle `eu-funding-*` dalla propria directory di skill; `~/.agents/skills` è la convenzione condivisa. Per i client che leggono soltanto un file di istruzioni di progetto (`AGENTS.md`, `CLAUDE.md`, regole dell'editor) conviene rimandare al `SKILL.md` della skill pertinente, che resta la fonte unica: l'installazione con `--link` evita copie divergenti.

## Controlli statici

Dalla radice del pacchetto:

```bash
python3 eu-funding-hierarchy/scripts/check_skill.py
python3 eu-funding-programme-finder/scripts/check_skill.py
python3 eu-funding-call-finder/scripts/check_skill.py
python3 eu-funding-eligibility-checker/scripts/check_skill.py
python3 eu-funding-financial-checker/scripts/check_skill.py
python3 eu-funding-financial-checker/scripts/test_calculations.py
python3 eu-funding-application-planner/scripts/check_skill.py
python3 eu-funding-proposal-drafter/scripts/check_skill.py
python3 eu-funding-proposal-drafter/scripts/test_validator.py
python3 eu-funding-proposal-reviewer/scripts/check_skill.py
python3 eu-funding-proposal-reviewer/scripts/test_validator.py
python3 eu-funding-submission-checker/scripts/check_skill.py
python3 eu-funding-submission-checker/scripts/test_validator.py
python3 eu-funding-post-submission-tracker/scripts/check_skill.py
python3 eu-funding-post-submission-tracker/scripts/test_validator.py
python3 tests/test_install.py
```

I controlli `check_skill.py` attestano **solo struttura, metadati e coerenza locale**, non capacità agentiche o conformità giuridica. La Skill 05 aggiunge 10 test unitari aritmetici del calcolatore; la Skill 07 aggiunge 16 test unitari del validatore formale, la Skill 08 ne aggiunge 25 per il rapporto di revisione e la Skill 09 ne aggiunge 49 per il pre-check e la Skill 10 ne aggiunge 56 per il tracciamento post-invio; `tests/test_install.py` aggiunge 10 test dello script di installazione (copia, collegamento, sovrascrittura, dry-run, disinstallazione). Nessuno è una verifica di conformità normativa. Le fonti devono essere verificate all'atto dell'uso; i casi nei file `references/test-cases.md` non sono test agentici eseguiti. Nessuna skill presenta domande di finanziamento, risponde a richieste delle autorità, effettua registrazioni o controlli ricorrenti autonomi. Il pre-check della Skill 09 non certifica ammissibilità e non è una ricevuta di invio.

## Versioni

- Skill 01–10: ciascuna v0.1 (bozza operativa testabile).
- Pacchetto cumulativo: **v0.11**, 10 novembre 2026.
- v0.11 aggiunge `install.py` e `tests/test_install.py` per installare le skill in Claude Code, OpenCode e gli altri client compatibili con Agent Skills.
