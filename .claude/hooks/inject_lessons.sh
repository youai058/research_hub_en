#!/usr/bin/env bash
# UserPromptSubmit hook — inject the most recent lessons.md entries into the
# session so the agent is reminded of current rules without having to Read
# the whole file. Stdout is appended to the user prompt context.
#
# - Global lessons (docs/lessons.md): inject last 3 entries (full body).
# - Domain lessons (lessons-paper/research/impl/analysis): count only,
#   to keep the injected block small.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
GLOBAL="$ROOT/docs/lessons.md"

echo "<research-hub-lessons>"

if [[ -f "$GLOBAL" ]]; then
  python3 - "$GLOBAL" <<'PY'
import re, sys
path = sys.argv[1]
try:
    txt = open(path, encoding="utf-8").read()
except Exception:
    print("lessons.md: unreadable")
    sys.exit(0)

# Entries are ## YYYY-MM-DD headings. Split on them and keep the last 3.
parts = re.split(r"(?m)^## (\d{4}-\d{2}-\d{2}[^\n]*)$", txt)
# parts = [preamble, date1, body1, date2, body2, ...]
pairs = []
for i in range(1, len(parts), 2):
    date = parts[i].strip()
    body = parts[i + 1] if i + 1 < len(parts) else ""
    pairs.append((date, body.rstrip()))

if not pairs:
    print("global: (no dated entries)")
    sys.exit(0)

recent = pairs[-3:]
print(f"global: {len(pairs)} entries total, showing last {len(recent)}")
for date, body in recent:
    print(f"## {date}")
    # Trim each body to ~20 lines to stay lightweight.
    lines = [ln for ln in body.splitlines() if ln.strip()]
    if len(lines) > 20:
        lines = lines[:20] + ["...(truncated)"]
    for ln in lines:
        print(ln)
    print()
PY
else
  echo "global: (docs/lessons.md missing)"
fi

# Domain counts only.
for name in lessons-paper lessons-research lessons-impl lessons-analysis; do
  f="$ROOT/docs/${name}.md"
  if [[ -f "$f" ]]; then
    count=$(awk '/^## [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/ {c++} END{print c+0}' "$f")
    printf "%s: %s entries (Read the file in-session when working in this domain)\n" "$name" "$count"
  fi
done

echo "</research-hub-lessons>"
