---
name: harness-hooks
description: "Register / edit / validate hooks. PreToolUse / PostToolUse / UserPromptSubmit / Stop / SubagentStop / SessionStart / SessionEnd / PreCompact / Notification. Automatic behaviors of the form \"do Y whenever X\" must be hooks. Triggers: 'add hook', 'PreToolUse', 'enforce lint', 'block tool call', 'auto-format', 'run on session start'."
---

# Harness Hooks Editor

Hooks are the **actual enforcer** of the harness. The main model tends to forget across sessions, so behaviors that must be enforced are implemented as hooks.

## Hook events

| Event | When | Blocking? |
|---|---|---|
| `PreToolUse` | Just before a tool call | **Yes** (non-zero exit → blocked; stderr forwarded to the model) |
| `PostToolUse` | Just after a tool call | No (for logging / post-processing) |
| `UserPromptSubmit` | Right after a user message is sent | Yes (prompt mutation / rejection) |
| `SessionStart` | Session start | No (initial context injection) |
| `SessionEnd` | Session end | No (cleanup) |
| `Stop` | Just before the model response terminates | Yes (reject response / restart) |
| `SubagentStop` | Subagent exit | No |
| `PreCompact` | Just before context compaction | No (chance to persist key info) |
| `Notification` | When a user notification fires | No |

## Registration location

Under the `hooks` key of settings.json:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {"type": "command", "command": "/home/irteam/sw/.claude/hooks/block-rm-rf.sh"}
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {"type": "command", "command": "/home/irteam/sw/.claude/hooks/format.sh"}
        ]
      }
    ]
  }
}
```

- `matcher`: tool-name regex. Omit matcher for events without a tool (`SessionStart`, etc.).
- `hooks[]`: each item is one shell command. Multiple may be registered.
- Use an **absolute path** for the command (avoids cwd drift).

## Hook-script conventions

Scripts live under `.claude/hooks/`. Input is JSON on stdin; output:
- **exit 0**: pass; stdout is recorded only as log
- **non-zero exit (PreToolUse / UserPromptSubmit / Stop)**: block; stderr is delivered to the model for its next turn

### Minimal template (Python)

```python
#!/usr/bin/env python3
import json, sys

payload = json.load(sys.stdin)
# payload example: {"tool_name": "Bash", "tool_input": {"command": "..."}}

cmd = payload.get("tool_input", {}).get("command", "")
if "rm -rf /" in cmd:
    print("blocked: rm -rf /", file=sys.stderr)
    sys.exit(1)
sys.exit(0)
```

### Minimal template (Bash)

```bash
#!/usr/bin/env bash
payload=$(cat)
echo "$payload" | jq -e '.tool_input.command | test("rm -rf /")' >/dev/null \
  && { echo "blocked" >&2; exit 1; }
exit 0
```

Always grant execute permission (`chmod +x`).

## Authoring steps

1. Write the hook script at `.claude/hooks/{name}.py` and `chmod +x`
2. **Local dry-run** with a sample stdin JSON payload: `echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | python3 .claude/hooks/{name}.py`
3. Register in the `hooks.{Event}` array of settings.json (delegated to the harness-settings skill)
4. Verify no duplicate registration for the same event+matcher
5. For PreToolUse hooks, **explicitly report the blocking scope** to the user

## Common patterns

### Enforce lint before commit
`PreToolUse` + `matcher: "Bash"` + when payload shows `git commit`, run `npm run lint` / `ruff`; exit 1 on failure.

### Auto-format
`PostToolUse` + `matcher: "Write|Edit"` + invoke `ruff format` / `prettier` based on file extension.

### Protect dangerous paths
`PreToolUse` + `matcher: "Write|Edit"` + block if `tool_input.file_path` is under `LLM/` or `LLDM/`.

### Inject context on session start
`SessionStart` → print current branch / recent commits / experiment status to stdout; the model sees this in its initial context.

## Failure modes & debugging

- PreToolUse hook accidentally always returns non-zero → **every tool call blocked**. Revert by removing the hook from settings.json.
- Relative paths → hook script not found when cwd changes. Use absolute paths.
- Missing execute permission → execution fails, possibly silently.
- Slow hook → every tool call slows down. Target < 1 second.

## Safety principles

- **Keep PreToolUse minimal**: aggressively overriding the main model's judgment costs flexibility
- **Always dry-run new hooks**: test locally against several payloads before registration
- **Rollback plan**: remember the original settings.json before registration so you can revert immediately
- **User notice**: when registering a blocking hook (PreToolUse, UserPromptSubmit, Stop), report its impact scope to the user
