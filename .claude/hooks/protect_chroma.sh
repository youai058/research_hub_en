#!/usr/bin/env bash
# PreToolUse(Bash) hook — block destructive operations on papers/vector_db/chroma/.
# Exits with code 2 to abort the tool call and feed stderr back to the model.
set -euo pipefail

payload="$(cat)"

python3 - <<'PY' "$payload"
import json, re, sys
try:
    data = json.loads(sys.argv[1]) if sys.argv[1].strip() else {}
except Exception:
    sys.exit(0)
if (data.get("tool_name") or data.get("tool")) != "Bash":
    sys.exit(0)
cmd = (data.get("tool_input") or data.get("input") or {}).get("command", "")
if not cmd:
    sys.exit(0)
danger = [
    r"rm\s+-[rRf]+\s+[^|;&]*papers/vector_db/chroma",
    r"rm\s+-[rRf]+\s+[^|;&]*papers/vector_db\b",
    r">\s*papers/vector_db/manifest\.json",
    r"chromadb.*delete_collection",
]
for pat in danger:
    if re.search(pat, cmd):
        print(
            f"[protect_chroma] blocked: '{cmd}' matches guard /{pat}/. "
            "Use index.py --rebuild instead, or ask the user to confirm manually.",
            file=sys.stderr,
        )
        sys.exit(2)
PY
