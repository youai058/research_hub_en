#!/usr/bin/env bash
# PreToolUse(Bash) hook — block destructive operations on papers/kg/ state.
# Exits with code 2 to abort the tool call and feed stderr back to the model.
#
# Strategy: verb-first matching. If the command contains any destructive verb
# AND any token that references papers/kg/<critical>, block it. This catches
# variants the previous file-target regex missed (rm without flags, rm --,
# cp /dev/null, dd, install, sqlite3 UPDATE/DELETE, tee, > redirect, Python
# unlink, etc.). Use .claude/skills/paper-kg/scripts/index.py --rebuild for
# legitimate resets.
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

# Critical targets under papers/kg/. Any mention of these + destructive verb → block.
TARGET_RE = re.compile(
    r"papers/kg/(?:kg\.sqlite|manifest\.json|extraction_log\.jsonl|"
    r"rejected\.jsonl|schema\.version|\.stale|\.rejected_cursor)"
    r"|papers/kg/?(?:\s|$|;|&|\||>)",
    re.IGNORECASE,
)
# Also flag whole-dir references like `papers/kg` as a standalone path token.
KG_DIR_RE = re.compile(r"(?:^|[\s;&|><])papers/kg(?:/|\b)", re.IGNORECASE)

def targets_kg(s: str) -> bool:
    return bool(TARGET_RE.search(s) or KG_DIR_RE.search(s))

# Destructive verbs / patterns. Each is checked independently; if matched AND
# the command references papers/kg, we block.
DESTRUCTIVE = [
    # File removal family
    (r"\brm\b(?!\s+-i\b)",                 "rm"),
    (r"\bunlink\b",                         "unlink"),
    (r"\bshred\b",                          "shred"),
    # Overwrite / emptying
    (r"\bcp\s+/dev/null\b",                 "cp /dev/null"),
    (r"\bcp\s+-[a-zA-Z]*\s*/dev/null\b",    "cp /dev/null"),
    (r"\bdd\b[^|;&]*\bof=",                 "dd of="),
    (r"\binstall\b\s+[^|;&]*/dev/null",     "install /dev/null"),
    (r"\btruncate\b",                       "truncate"),
    # Move / rename away from canonical path
    (r"\bmv\b",                             "mv"),
    # Shell redirection overwrite (>, >|, tee without -a).
    # Negative lookbehind excludes fd redirects (1>, 2>, &>, 3>) and >> append,
    # so read-only commands with stderr redirection (`ls ... 2>/dev/null`) pass.
    (r"(?<![0-9&>])>[^>&]",                 "> redirect"),
    (r"\btee\b(?!\s+-[aA])",                "tee (non-append)"),
    # sqlite3 destructive SQL
    (r"\bsqlite3\b[^|;&]*\b(?:DROP|DELETE\s+FROM|UPDATE\s+\w+\s+SET|VACUUM|TRUNCATE|REPLACE\s+INTO)\b",
     "sqlite3 destructive SQL"),
    # Python one-liner unlink / rmtree / write
    (r"python3?\s+-c\b[^|;&]*\b(?:unlink|rmtree|remove|write_text|write_bytes|open\([^)]*,\s*['\"]w)",
     "python destructive one-liner"),
    # chmod/chown that can lock the DB
    (r"\bchmod\s+0*0\b",                    "chmod 000"),
]

# Whitelist: index.py --rebuild is the sanctioned reset path.
WHITELIST_RE = re.compile(
    r"paper-kg/scripts/index\.py[^|;&]*--rebuild\b",
    re.IGNORECASE,
)
if WHITELIST_RE.search(cmd):
    sys.exit(0)

# Also allow writes whose only papers/kg/ reference is inside a quoted path
# argument to index.py (the sanctioned writer). Rough check: if index.py is
# invoked and no shell redirect goes into papers/kg/, let it through.
INDEX_INVOKE_RE = re.compile(r"paper-kg/scripts/index\.py\b", re.IGNORECASE)
REDIRECT_TO_KG = re.compile(r">\s*[^|;&]*papers/kg/", re.IGNORECASE)
if INDEX_INVOKE_RE.search(cmd) and not REDIRECT_TO_KG.search(cmd):
    sys.exit(0)

if not targets_kg(cmd):
    sys.exit(0)

for pat, label in DESTRUCTIVE:
    if re.search(pat, cmd, re.IGNORECASE):
        print(
            f"[protect_kg] blocked: '{cmd}' — destructive verb '{label}' "
            f"against papers/kg/. Use index.py --rebuild for legitimate resets, "
            f"or ask the user to confirm manually.",
            file=sys.stderr,
        )
        sys.exit(2)
PY
