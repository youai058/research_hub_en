#!/usr/bin/env bash
# UserPromptSubmit / SessionStart hook — inject lessons.md context.
#
# Usage: inject_lessons.sh [full|titles]
#   - full   : emit last 3 entries with full body (SessionStart default).
#   - titles : emit last 3 entries as date + title line only (UserPromptSubmit).
#   - (unset or unknown) : fall back to `full` (safe default).
#
# Env override for tests:
#   - RESEARCH_HUB_ROOT : absolute path that replaces the auto-computed ROOT.
#
# Stdout is appended to the user prompt context.
set -euo pipefail

MODE="${1:-full}"
if [[ "$MODE" != "full" && "$MODE" != "titles" ]]; then
  echo "inject_lessons.sh: unknown mode '$MODE', defaulting to full" >&2
  MODE="full"
fi

if [[ -n "${RESEARCH_HUB_ROOT:-}" ]]; then
  ROOT="$RESEARCH_HUB_ROOT"
else
  ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
fi
GLOBAL="$ROOT/docs/lessons.md"

emit_full() {
  if [[ -f "$GLOBAL" ]]; then
    python3 - "$GLOBAL" <<'PY'
import re, sys
path = sys.argv[1]
try:
    txt = open(path, encoding="utf-8").read()
except Exception:
    print("lessons.md: unreadable")
    sys.exit(0)

parts = re.split(r"(?m)^## (\d{4}-\d{2}-\d{2}[^\n]*)$", txt)
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
}

emit_titles() {
  if [[ -f "$GLOBAL" ]]; then
    python3 - "$GLOBAL" <<'PY'
import re, sys
path = sys.argv[1]
try:
    txt = open(path, encoding="utf-8").read()
except Exception:
    print("lessons.md: unreadable")
    sys.exit(0)

parts = re.split(r"(?m)^## (\d{4}-\d{2}-\d{2}[^\n]*)$", txt)
pairs = []
for i in range(1, len(parts), 2):
    heading = parts[i].strip()
    pairs.append(heading)

if not pairs:
    print("global: (no dated entries)")
    sys.exit(0)

recent = pairs[-3:]
print(f"global: {len(pairs)} entries — last {len(recent)} titles:")
for heading in recent:
    # heading format: "YYYY-MM-DD — Title phrase" or "YYYY-MM-DD" alone
    date = heading[:10]
    rest = heading[10:].lstrip()
    if rest.startswith("—"):
        title = rest.lstrip("—").strip()
    elif rest.startswith("-"):
        title = rest.lstrip("-").strip()
    else:
        title = rest.strip()
    if title:
        print(f"- {date}: {title}")
    else:
        print(f"- {date}")
print("(Read docs/lessons.md for full bodies)")
PY
  else
    echo "global: (docs/lessons.md missing)"
  fi
}

emit_domain_counts() {
  for name in lessons-paper lessons-research lessons-impl lessons-analysis; do
    f="$ROOT/docs/${name}.md"
    if [[ -f "$f" ]]; then
      count=$(awk '/^## [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/ {c++} END{print c+0}' "$f")
      printf "%s: %s entries (Read the file in-session when working in this domain)\n" "$name" "$count"
    fi
  done
}

echo "<research-hub-lessons>"
case "$MODE" in
  full)   emit_full ;;
  titles) emit_titles ;;
esac
emit_domain_counts
echo "</research-hub-lessons>"
