---
name: install
description: Installa, aggiorna o disinstalla le skill EU Funding presenti in questo repository nella directory di skill di Claude Code, OpenCode o di un altro client compatibile con Agent Skills. Usare quando l'utente chiede di installare le skill o invoca /install.
---

# Installazione delle EU Funding Skills

Installa le cartelle `eu-*` di questo repository nella directory di skill del client scelto, copiandole o collegandole. Non modificare il contenuto delle skill.

## 1. Destinazione

Se l'utente non l'ha indicata, chiedi una sola volta, proponendo le opzioni:

| Client | Ambito | Destinazione |
| --- | --- | --- |
| Claude Code | personale, tutti i progetti | `~/.claude/skills` |
| Claude Code | progetto corrente | `<progetto>/.claude/skills` |
| OpenCode | globale | `~/.config/opencode/skills` (o `$XDG_CONFIG_HOME/opencode/skills`) |
| OpenCode | progetto corrente | `<progetto>/.opencode/skills` |
| Altro client Agent Skills | globale | `~/.agents/skills` |

Se l'utente dice solo "installa" e non ci sono elementi per scegliere, proponi **Claude Code personale** (`~/.claude/skills`): è letta anche da OpenCode, che cerca pure in `~/.claude/skills` e `~/.agents/skills`.

## 2. Copia o collegamento

- **Copia** (predefinita): indipendente da questo repository, che può essere spostato o eliminato.
- **Collegamento** (`ln -s`): gli aggiornamenti del repository sono immediati, ma le skill si rompono se il repository viene spostato.

Scegli la copia se l'utente non esprime preferenza. Non usare i collegamenti su Windows senza verificare che siano disponibili.

## 3. Controlla prima di scrivere

Elenca le cartelle `eu-*` già presenti nella destinazione e indica se sono identiche, diverse o collegate a un altro percorso. Se una versione diversa verrebbe sovrascritta, chiedi conferma prima di procedere. Non toccare mai cartelle che non iniziano con `eu-`.

## 4. Esegui

Dalla radice di questo repository:

```bash
DEST="$HOME/.claude/skills"
mkdir -p "$DEST"
for d in eu-*/; do
  name="${d%/}"
  rm -rf "$DEST/$name"
  cp -R "$d" "$DEST/$name"
done
```

Per il collegamento, sostituisci le ultime due righe con:

```bash
  ln -sfn "$PWD/$name" "$DEST/$name"
```

## 5. Verifica

```bash
for f in "$DEST"/eu-*/scripts/check_skill.py; do python3 "$f" || echo "FAIL $f"; done
```

Se un controllo fallisce, riportalo e non dichiarare l'installazione completata.

## 6. Riporta

Indica destinazione, modalità (copia o collegamento), numero di skill installate e come usarle:

- **Claude Code:** compaiono in `/skills` e si invocano con `/eu-funding-hierarchy`. Se la directory di skill non esisteva all'avvio della sessione, eseguire `/reload-skills`.
- **OpenCode:** si caricano con `@eu-funding-hierarchy` o automaticamente; `/reload` ricarica la configurazione.

## Disinstallazione

Se l'utente chiede di rimuovere le skill, elenca le cartelle `eu-*` nella destinazione, chiedi conferma e rimuovi solo quelle. Non eliminare altre skill e non cancellare questo repository.
