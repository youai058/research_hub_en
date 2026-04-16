#!/usr/bin/env bash
# PreToolUse(Bash) hook — WARN (do not block) when RAG-dependent commands
# are invoked against an empty RAG index.
#
# v3 refactor: Decision #1 requires advisory-only preflight. The stage
# commands (`/research-qa`, `/research-experiments`, `/research-analyze`)
# must remain invocable without a prior `/research-papers` run; PLAN.md
# captures the missing-prerequisite state and the user decides whether to
# proceed. This hook now emits a stderr advisory but exits 0 so the tool
# call passes. Silenceable via env var `RESEARCH_HUB_GUARD_QUIET=1`.
#
# Exempt: /research-index (the rebuild path itself).
set -euo pipefail

payload="$(cat)"

python3 - <<'PY' "$payload"
import json, os, re, sys

try:
    data = json.loads(sys.argv[1]) if sys.argv[1].strip() else {}
except Exception:
    sys.exit(0)

if (data.get("tool_name") or data.get("tool")) != "Bash":
    sys.exit(0)

cmd = (data.get("tool_input") or data.get("input") or {}).get("command", "") or ""
if not cmd:
    sys.exit(0)

# Exempt the rebuild path itself.
EXEMPT = [
    r"/research-index\b",
    r"paper-rag/scripts/index\.py",
]
for pat in EXEMPT:
    if re.search(pat, cmd):
        sys.exit(0)

# Trigger tokens — RAG-dependent phase commands / skills / stage commands.
TRIGGERS = [
    r"/answer-formulate\b",
    r"/critique\b",
    r"/research-rag\b",
    r"/research-qa\b",
    r"\bexperiment-plan\b",
    # Direct script invocations for these skills
    r"skills/answer-formulate\b",
    r"skills/critique\b",
    r"skills/experiment-plan\b",
]
triggered = None
for pat in TRIGGERS:
    if re.search(pat, cmd):
        triggered = pat
        break
if not triggered:
    sys.exit(0)

# Find manifest. Allow env override; default to symlinked path.
root_candidates = [
    "/home/irteam/sw/research_hub",
    "/home1/irteam/sw/research_hub",
]
manifest_path = None
for r in root_candidates:
    p = os.path.join(r, "papers/vector_db/manifest.json")
    if os.path.exists(p):
        manifest_path = p
        break

if manifest_path is None:
    files_count = 0
else:
    try:
        with open(manifest_path) as f:
            m = json.load(f)
        files_count = len(m.get("files") or {})
    except Exception:
        sys.exit(0)

if files_count == 0:
    # Advisory only; quiet when env var set.
    if os.environ.get("RESEARCH_HUB_GUARD_QUIET") == "1":
        sys.exit(0)
    msg = (
        "[guard_empty_rag advisory only] RAG index empty "
        f"(manifest.files=0 at {manifest_path or '(missing)'}); "
        f"command matches /{triggered}/. "
        "Stage will produce low-quality output — PLAN.md should include a "
        "'Prerequisite Missing' block. Run `/research-index --rebuild` to "
        "populate, or set RESEARCH_HUB_GUARD_QUIET=1 to silence this warning. "
        "(not blocking — continuing)"
    )
    print(msg, file=sys.stderr)

sys.exit(0)
PY
