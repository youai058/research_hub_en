#!/usr/bin/env bash
# Stop hook — detect phase-boundary conditions and emit an advisory.
#
# v3 schema: reads stage / inner_phase / sub_phase / slug / stage_version.
# Emits a one-line suggestion when the current sub-phase's exit criteria
# look satisfied, so the orchestrator can call `loop_state.py stage-advance`
# or `stage-complete`. SUGGESTION ONLY — never mutates loop_state.json.
# Autonomous branches removed (v3 refactor).
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
LOOP="$ROOT/research/loop_state.json"

[[ -f "$LOOP" ]] || exit 0

python3 - "$ROOT" "$LOOP" <<'PY'
import json, os, re, sys
root, loop_path = sys.argv[1], sys.argv[2]
try:
    s = json.load(open(loop_path, encoding="utf-8"))
except Exception:
    sys.exit(0)

stage = s.get("stage")
inner = s.get("inner_phase")
sub   = s.get("sub_phase")
slug  = s.get("slug")
ver   = s.get("stage_version")

# Early-return when no active stage. harness-engineer / meta sessions
# should leave stage="idle" / slug=null; skip sentinel slugs too.
if not stage or stage == "idle" or not slug:
    sys.exit(0)
if slug in ("none", "null", "harness", "meta"):
    sys.exit(0)
if slug.startswith("harness-") or slug.startswith("meta-"):
    sys.exit(0)
# advisory only fires during Phase C execution
if inner != "C" or not sub:
    sys.exit(0)

def exists(rel):
    return os.path.isfile(os.path.join(root, rel))

def dir_nonempty(rel):
    p = os.path.join(root, rel)
    return os.path.isdir(p) and any(os.scandir(p))

# Stage-level plan (new v3 location, versioned)
stage_plan = f"research/plans/{stage}/{slug}/v{ver}/PLAN.md" if ver else None
# Experiments per-slug artifacts (unchanged paths — code-implementer convention)
experiment_plan = f"research/plans/{slug}/PLAN.md"  # experiment-level PLAN consumed by code-implementer
impl_map  = f"experiments/{slug}/IMPL_MAP.md"
run_sh    = f"experiments/{slug}/run.sh"
results   = f"results_{slug}"
diagnosis = f"research/diagnoses/{slug}.md"
report_md = f"research/reports/{stage}/{slug}/v{ver}/Report.md" if ver else None
report_slides = f"research/reports/{stage}/{slug}/v{ver}/Report.slides.md" if ver else None

suggestion = None

# STAGE_SUBPHASES terminal sub-phases → suggest stage-complete + Report gen
TERMINAL_SUBPHASES = {
    "papers":      "A-4",
    "qa":          "B-2",
    "experiments": "E-3",
    "analyze":     "F-2",
}

if stage == "papers":
    if sub == "A-1":
        # paper-hunter done when raw.md files have been written this cycle.
        # cannot easily detect per-cycle delta from disk; advisory when papers/ exists
        if os.path.isdir(os.path.join(root, "papers")):
            suggestion = f"A-1 → A-2: raw.md collected. Route to paper-triage via `loop_state.py stage-advance`."
    elif sub == "A-2":
        suggestion = "A-2 → A-3: triage accepted list ready. Route to paper-summarizer."
    elif sub == "A-3":
        suggestion = "A-3 → A-4: 5-part summaries written. Route to rag-curator for incremental upsert."
    elif sub == "A-4":
        manifest = os.path.join(root, "papers", "rag", "manifest.json")
        if os.path.isfile(manifest):
            suggestion = f"A-4 terminal: manifest.json updated. Build Report pair and `stage-complete`."

elif stage == "qa":
    if sub == "B-1":
        answers_dir = os.path.join(root, "research", "answers")
        if os.path.isdir(answers_dir):
            suggestion = "B-1 → B-2: Direct Answer + Evidence Chain drafted. Route to critic (+ codex-reviewer parallel)."
    elif sub == "B-2":
        critique = os.path.join(root, "research", "critiques", f"{slug}.md")
        if os.path.isfile(critique):
            suggestion = f"B-2 terminal: critique written. Build Report pair and `stage-complete`."

elif stage == "experiments":
    if sub == "C-1":
        # C-1 is already satisfied by Phase A (experiment-design) in v3; advisory only if plan absent.
        if not exists(experiment_plan):
            suggestion = "C-1: experiment-level PLAN.md missing at research/plans/<slug>/PLAN.md. experiment-planner should have produced it in Phase A."
    elif sub == "E-1":
        if exists(impl_map) and exists(run_sh):
            suggestion = "E-1 → E-2: IMPL_MAP.md + run.sh present. Hand off to implementation-verifier."
    elif sub == "E-2":
        if exists(impl_map) and exists(run_sh):
            suggestion = "E-2 → E-3: IMPL_MAP.md + run.sh present. If verifier passed, route to codex-reviewer (E-3)."
    elif sub == "E-3":
        if dir_nonempty(results):
            suggestion = f"E-3 terminal: results_{slug}/ populated. codex-reviewer verdict + Report pair + `stage-complete`."

elif stage == "analyze":
    if sub == "F-1":
        if dir_nonempty(results) and exists(diagnosis):
            suggestion = f"F-1 → F-2: results_{slug}/ populated and diagnosis written. Route to codex-reviewer for adversarial review."
    elif sub == "F-2":
        if exists(diagnosis):
            suggestion = "F-2 terminal: diagnosis written. Build Report pair (revision seed included) and `stage-complete`."

if suggestion:
    print("<phase-advance-advisory>")
    print(f"[{stage} v{ver} / inner={inner} / sub={sub}] {suggestion}")
    print(f"(plan={stage_plan or '(n/a)'}, report={report_md or '(n/a)'})")
    print("Run `python3 .claude/scripts/loop_state.py stage-advance` to step to the next sub-phase,")
    print("or `stage-complete` after the terminal sub-phase + Report pair is written.")
    print("(advisory only — not persisted; next session will not see this unless loop_state.json was actually advanced)")
    print("</phase-advance-advisory>")
PY
