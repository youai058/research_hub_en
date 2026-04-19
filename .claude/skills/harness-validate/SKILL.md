---
name: harness-validate
description: "Validate the entire harness structure. settings.json JSON validity, agents / skills / commands frontmatter, hook script +x, MCP registration, description trigger conflicts, naming conventions. Mandatory immediately after harness-engineer edits. Triggers: 'validate harness', 'structure check', 'harness healthcheck', 'settings validity'."
---

# Harness Validator

The structural validator skill to run after every harness edit. On failure, stop immediately and report to the user.

## Checks

### 1. settings.json syntax

- JSON-parse `.claude/settings.json`, `.claude/settings.local.json`, `~/.claude/settings.json` if present
- Use `python3 -c "import json; json.load(open('PATH'))"`
- On failure, **abort immediately** — a non-parsing settings file breaks the session

### 2. settings.json schema

- `permissions.defaultMode` ∈ {`plan`, `default`, `acceptEdits`, `bypassPermissions`}
- Each `permissions.allow` / `deny` / `ask` entry has form `ToolName(pattern)`
- If `statusLine.type == "command"`, the `command` key exists and the path exists
- Each item in `hooks.{Event}` array has `matcher` (optional) and `hooks[]`
- `hooks[].command` paths exist as real files with execute permission (`os.access(path, os.X_OK)`)

### 3. Agents (`.claude/agents/*.md`)

- Frontmatter parses (YAML)
- Required keys: `name`, `description`
- Recommended: `model: opus` (warn otherwise)
- `name` matches filename (sans extension)
- Body contains 6 section headings (Core Role / Working Principles / I/O Protocol / Team Comms / Error Handling / Collaboration) (warn-level)

### 4. Skills (`.claude/skills/*/SKILL.md`)

- Frontmatter parses
- Required: `name`, `description`
- `name` matches the directory name
- Body line count ≤ 500 (warning; suggest splitting to references on overflow)
- `references/*.md` files > 300 lines should have a table of contents (warning)

### 5. Slash commands (`.claude/commands/**/*.md`)

- Frontmatter parses (optional, but if present must be valid)
- If `allowed-tools` is present, it must be an array
- If body contains `$ARGUMENTS` / `$1..9`, recommend an `argument-hint` in frontmatter

### 6. Hooks

- Command paths registered under settings.json's `hooks` key actually exist
- Check execute permission on `.claude/hooks/*.py` / `*.sh`
- Syntax-check Python scripts: `python3 -c "import ast; ast.parse(open('PATH').read())"`

### 7. MCP

- If `.mcp.json` exists, JSON-parse it
- `mcpServers.{name}.type` ∈ {`stdio`, `sse`, `http`}
- For stdio servers, verify `command` path exists (if absolute)

### 8. Trigger conflicts

- Gather every skill description
- Pairwise semantic-duplicate check (first pass via simple keyword overlap)
- Print duplicate candidates as warnings

## Execution

Bundle the validator as `.claude/skills/harness-validate/scripts/validate.py` (see template below) and invoke:

```bash
python3 .claude/skills/harness-validate/scripts/validate.py /home/irteam/sw
```

Exit codes:
- `0`: all checks passed
- `1`: warnings only (fix recommended)
- `2`: fatal error (session at risk, abort immediately)

## Report format

```
== Harness Validation Report ==
[OK]    settings.json syntax
[OK]    7 agents frontmatter
[WARN]  skills/foo/SKILL.md: 523 lines (exceeds 500)
[ERROR] settings.json: hooks.PreToolUse[0].command → path not executable
```

If there is any `[ERROR]`, harness-engineer must roll back or request a fix from the user.

## When to invoke

1. **Immediately after** harness-settings / harness-hooks / harness-agent-author / harness-skill-author / harness-command-author / harness-mcp finish editing
2. When the user explicitly requests "check harness"
3. Optionally: auto-run from a `SessionStart` hook at session start

## Checklist

- [ ] All 3 layers of settings.json valid
- [ ] All agents frontmatter valid; name == filename
- [ ] All skills frontmatter valid; 500-line rule
- [ ] Hook paths exist + execute permission
- [ ] MCP JSON valid + type correct
- [ ] Trigger-duplication check executed
- [ ] Report printed; abort on ERROR
