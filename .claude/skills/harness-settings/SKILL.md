---
name: harness-settings
description: "Edit / merge / validate settings.json. permissions (allow/deny/ask/defaultMode), env, statusLine, model, outputStyle, keybindings.json, output-styles directory. The `hooks` key belongs to harness-hooks. Triggers: 'edit settings', 'add permission', 'change defaultMode', 'statusline', 'env var', 'output style', 'keybinding change'."
---

# Harness Settings Editor

settings.json is the harness's root configuration. A bad edit breaks the entire session, so always honor **layering / schema / merge rules**.

## Layers

| File | Scope | When |
|---|---|---|
| `~/.claude/settings.json` | user global | Shared across all projects (reusable settings only) |
| `{project}/.claude/settings.json` | project (committable) | Project-specific settings / hooks |
| `{project}/.claude/settings.local.json` | project local (gitignored) | Secrets, personal overrides |

Merge precedence: **local > project > user**. Array fields (e.g. `permissions.allow`) merge; scalars are overridden by the lower layer. Edits to user global affect other projects and require **explicit user approval**.

## Key fields

### permissions
```json
{
  "permissions": {
    "allow": ["Bash(ls:*)", "Read(*)"],
    "deny": ["Bash(rm -rf *)"],
    "ask": ["Bash(git push:*)"],
    "defaultMode": "bypassPermissions"
  }
}
```
- `defaultMode`: `plan` | `default` | `acceptEdits` | `bypassPermissions`
- Tool matcher form: `ToolName(pattern)` — Bash uses prefix matching; other tools take a literal string
- `skipDangerousModePermissionPrompt: true` only has meaning together with `bypassPermissions`

### env
```json
{"env": {"CLAUDE_BASH_DEFAULT_TIMEOUT_MS": "300000"}}
```
Mainly model hints, proxy, timeouts. Keep secrets in `settings.local.json`.

### statusLine
```json
{"statusLine": {"type": "command", "command": "/home/irteam/sw/.claude/hooks/statusline.sh"}}
```
Renders shell command output to the status line. Must return within 1 second.

### model / outputStyle
```json
{"model": "opus", "outputStyle": "default"}
```
`outputStyle` names a file in `.claude/output-styles/{name}.md`. Overrides the persona system prompt.

### MCP toggles
```json
{
  "enableAllProjectMcpServers": false,
  "disabledMcpjsonServers": ["some-server"],
  "enabledMcpjsonServers": ["other-server"]
}
```
MCP server registration lives in `.mcp.json`; only toggles here.

## Editing steps

1. **Read the current file first**. Preserve whitespace / order if possible.
2. Parse the JSON — on parse failure, abort and back up the original.
3. Merge keys (dedup arrays; override scalars).
4. Atomic write — rewrite the full file via Write.
5. Re-validate parse: `python3 -c "import json,sys; json.load(open('...'))"`.

## Output styles

`.claude/output-styles/{name}.md` with frontmatter + system-prompt body. Activate via the `outputStyle` key in settings.

```markdown
---
name: terse-engineer
description: Concise English replies
---
All replies ≤ 100 characters. For code changes, file path + one-line summary.
```

## Keybindings

Only `~/.claude/keybindings.json` exists (no project scope). For authoring details, see the built-in `keybindings-help` skill. This skill provides only the pointer.

## Validation checks

- File is valid JSON (`json.load` passes)
- `defaultMode` is one of the 4 enum values
- Each `permissions.allow` / `deny` / `ask` entry has `ToolName(...)` form
- `statusLine.command` path actually exists and is executable
- If editing user global, user approval obtained

## Failure modes

- Invalid `defaultMode` value → rejected at session start
- Typo in a permission matcher → silently ignored, no guard takes effect
- statusLine script failure → status line blank, session still functions
- JSON syntax error → **entire session fails to start**. Always re-validate.
