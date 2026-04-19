---
name: harness-command-author
description: "Slash prompt templates (.claude/commands/{name}.md). $ARGUMENTS / $1.. / ! shell / @file directives + description·argument-hint·allowed-tools·model header. Triggers: 'new slash command', '/custom prompt', 'command template'."
---

# Harness Command Author

A slash command is a **prompt template the user invokes with `/name`**. It is not auto-execution; it is a user-driven shortcut that makes repeated compound prompts reusable.

## Storage locations

```
.claude/commands/{name}.md      (project scope, /name)
~/.claude/commands/{name}.md    (user global, /name)
```

Project commands override user-global commands. Subdirectories provide namespacing: `.claude/commands/git/commit.md` → `/git:commit`.

## Frontmatter

```yaml
---
description: "One-line summary of what this command does (shown in `/help`)"
argument-hint: "<file> [--flag]"
allowed-tools: ["Bash", "Read", "Edit"]
model: opus
---
```

- `description`: shown in `/help`. Works without it but recommended.
- `argument-hint`: hint for arguments; used for autocomplete.
- `allowed-tools`: tools permitted in this command's execution context. Omit to use default session permissions.
- `model`: model to force for this command (optional).

## Body directives

| Directive | Meaning |
|---|---|
| `$ARGUMENTS` | When called as `/name foo bar`, the full string `foo bar` |
| `$1`, `$2`, … | Individual positional arguments |
| `!command` | Executes the shell command **at command-authoring time** and inlines the result into the prompt |
| `@path/to/file` | Inlines the file's contents into the prompt |

### Example: `/commit`

```markdown
---
description: Commit staged changes
argument-hint: "[message]"
allowed-tools: ["Bash"]
---

Look at the state below and either suggest a commit message or use the message "$ARGUMENTS" given by the user.

Current state:
!git status --short

Change summary:
!git diff --stat
```

### Example: `/review-pr`

```markdown
---
description: Review a GitHub PR
argument-hint: "<pr-number>"
allowed-tools: ["Bash", "Read"]
---

Review the changes in PR #$1.

!gh pr view $1
!gh pr diff $1
```

## Authoring steps

1. Scan existing commands: check `.claude/commands/**/*.md` for name/description collisions
2. Write the file (frontmatter + body)
3. If using `!` shell directives, verify execution permission at the command level
4. Test: actually invoke `/name [sample args]`
5. Validate frontmatter via harness-validate

## Command vs. skill vs. hook — which to pick

| Situation | Pick |
|---|---|
| User explicitly invokes a reusable prompt | **command** |
| Compound workflow auto-triggered by keywords | **skill** |
| Auto-runs on events (tool call, prompt submit, etc.) | **hook** |

Don't conflate: command is active (user-invoked), hook is passive (event-driven), skill is automatic (description-matched).

## Checklist

- [ ] File under `.claude/commands/`
- [ ] Valid frontmatter (description recommended; argument-hint / allowed-tools optional)
- [ ] If using `$ARGUMENTS` / `$1..$n`, also provide argument-hint
- [ ] `!` / `@` directives actually executable
- [ ] No name collision with existing commands
