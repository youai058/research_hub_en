# Dispatch Prompt Diet — Design Spec

**Date**: 2026-04-19
**Scope**: research_hub 4 stage slash commands + `.claude/scripts/` + `CLAUDE.md` §4.2
**Goal**: Cut ≥35 % of boilerplate lines across `.claude/commands/research-{papers,qa,experiments,analyze}.md` (~1000 → ≤650 lines) without changing any Agent-dispatch fidelity.
**Parent brainstorm**: 2026-04-19 token reduction, Approach 2 (incremental per-lever), PR #2 of 4.

Preceded by PR #1 (lessons injection split, merged 2026-04-19, commits `575a072`..`7692668` on `refactor/phase-c-dispatch`).

---

## 1. Problem

The four stage slash commands contain ~40 % duplicated or low-signal prose:

| Duplicate | Copies | Lines each | Total |
|---|---|---|---|
| "How to read these dispatch specs" paragraph | 4 (identical) | ~5 | 20 |
| "`<slug>` is a placeholder" blockquote | 4 | ~2 | 8 |
| "User-interrupt handling" paragraph | 4 (identical) | ~2 | 8 |
| `PRE_*_COUNT=$(find…)` / `POST_*_COUNT=…` / `test -gt` verify block | 15+ (one per sub-phase) | ~8 | 120+ |
| Stop-rule narrative (consecutive-fail, resets-on-pass, session-local) | 4 | ~6 | 24 |

Every slash-command `.md` file is prepended to the main-session context on invocation. That duplicated prose lives in context for the rest of the session. The Agent(prompt="…") payload actually sent to subagents (Surface 2) is already compact — this spec targets only the slash-command body (Surface 1).

### Quality floor ("A strict")
- Every subagent receives byte-identical dispatch keys/values.
- Every verify step retains the same exit code (9–14).
- Every stage-advance boundary preserved.
- Stop-rule thresholds (retry=3 for B-2, =2 for E-2/E-3/F-2) preserved.

Only prose-with-zero-information and bash-pattern-duplication are targets. No semantic drift.

---

## 2. Architecture

**Single new script + inline prune of five existing files.** No new directories, no new include-file mechanism.

| Path | Action | Responsibility |
|---|---|---|
| `.claude/scripts/verify_sub_phase.py` | CREATE | Per-sub-phase snapshot/verify/advance wrapper. Single dict SSOT for artifact expectations. |
| `.claude/commands/research-papers.md` | MODIFY | Prune to ≤250 lines |
| `.claude/commands/research-qa.md` | MODIFY | Prune to ≤130 lines |
| `.claude/commands/research-experiments.md` | MODIFY | Prune to ≤160 lines |
| `.claude/commands/research-analyze.md` | MODIFY | Prune to ≤140 lines |
| `CLAUDE.md` | MODIFY | §4.2 appended with a single-sentence user-interrupt contract |
| `.claude/tests/test_verify_sub_phase.py` | CREATE | 8 hermetic pytest cases (T1–T8) |
| `.claude/tests/test_command_prune.py` | CREATE | 5 static-grep pytest cases (T1–T5) |

### 2.1 `verify_sub_phase.py` CLI

```
verify_sub_phase.py snapshot <sub_phase_id> --slug <slug> [--stage-version <N>] [--batch-i <i>]
verify_sub_phase.py verify   <sub_phase_id> --slug <slug> [--stage-version <N>] [--batch-i <i>]
```

- `snapshot` writes pre-state JSON to `/tmp/.verify_<stage>_<slug>_<sub_phase>[_b<i>].json` then `exit 0`. State includes artifact path list, count, mtimes.
- `verify` reads the snapshot, re-lists the artifact glob, compares, and:
  - Success → stdout `"<sub_phase>: OK (+N artifacts)"`, `exit 0`.
  - Failure → stderr `<on_fail_msg>`, `exit <on_fail_code>` preserving the exact existing per-sub-phase codes (see §2.2 table).
  - `verdict_parse: True` sub-phases (E-3, F-2) additionally parse YAML frontmatter `verdict:` and **always print the verdict on stdout**:
    - `approve` / `approve_with_revisions` → `exit 0` (main session advances).
    - `reject` → `exit 0` (not a script failure; main session reads stdout and applies Stop-rule via CLAUDE.md §4.5 — this matches current `case` statement behavior where `reject` is a noop exit from the case).
    - missing / unknown → `exit <E-3|F-2 on_fail_code>` (fail-closed; main session must not silently treat as approve).
  - `expect: "no-new"` sub-phases (E-2) invert comparison: an *increase* in the glob count is failure.

### 2.2 `SUB_PHASES` dict (13 entries)

```python
# Exit codes are preserved verbatim from the current command files (see
# `git grep '|| exit'` across .claude/commands/research-*.md). Overlaps
# across stages (9, 10) are intentional — each code is scoped to its owning
# sub-phase and the main session already handles that overlap.
SUB_PHASES = {
    "A-1":   {"glob": "papers/metadata/**/*.raw.md",                               "on_fail": ("paper-hunter did not collect any new raw.md", 6)},
    "A-1.5": {"glob": "papers/vector_db/manifest.json",                             "mode": "mtime", "on_fail": ("abstract-indexer did not preserve/grow manifest", 10)},
    "A-2":   {"glob": "research/topics/{slug}.ranks.json",                          "on_fail": ("paper-triage did not append a log line", 5)},
    "A-3":   {"glob": "papers/marp-summary/**/*.md",                                "mode": "batch", "on_fail": ("paper-summarizer batch produced no summary", 9)},
    "A-4":   {"glob": "papers/vector_db/manifest.json",                             "mode": "mtime", "on_fail": ("rag-curator did not grow manifest", 7)},
    "B-1":          {"glob": "research/answers/*.md",                               "on_fail": ("answer-formulator did not emit an answer file", 9)},
    "B-2-critic":   {"glob": "research/critiques/*.md",                             "on_fail": ("critic did not emit a critique file", 10)},
    "B-2-codex":    {"glob": "research/reviews/qa_{slug}_codex_review.md",          "on_fail": ("codex-reviewer did not emit a review file", 11)},
    "E-1":   {"glob": "experiments/{slug}/code/**",
              "extra_required": ["experiments/{slug}/IMPL_MAP.md"],
              "on_fail": ("code-implementer did not add code or IMPL_MAP", 12)},
    "E-2":   {"glob": "experiments/{slug}/qa_fail_*.md", "expect": "no-new",
              "on_fail": ("implementation-verifier emitted qa_fail_*.md", 13)},
    "E-3":   {"glob": "research/reviews/experiments_{slug}_codex_review.md",
              "verdict_parse": True,
              "on_fail": ("codex-reviewer did not emit a review file (E-3)", 14)},
    "F-1":   {"glob": "research/diagnoses/{slug}.md",                               "on_fail": ("results-analyst did not emit diagnosis", 15)},
    "F-2":   {"glob": "research/reviews/analyze_{slug}_codex_review.md",
              "verdict_parse": True,
              "on_fail": ("codex-reviewer did not emit a review file (F-2)", 16)},
}
```

Glob strings use `{slug}` placeholder substituted by CLI `--slug`. The `"mtime"` mode is used for files that already exist (manifests) and must have a newer mtime than the snapshot. Batch mode stores per-batch-index snapshots so A-3 can verify incrementally.

### 2.3 Main-session command pattern (before → after)

**Before** (typical sub-phase block, 8 lines):

```markdown
Before dispatch, snapshot:
\`\`\`bash
PRE_B1_ANSWER_COUNT=$(find research/answers -name '*.md' 2>/dev/null | wc -l)
\`\`\`
Dispatch `answer-formulator` with: ...
After task-notification, verify:
\`\`\`bash
POST_B1_ANSWER_COUNT=...
test "$POST_B1..." -gt "$PRE_B1..." || { echo "..."; exit 9; }
\`\`\`
```

**After** (3 lines):

```markdown
Snapshot: `python3 .claude/scripts/verify_sub_phase.py snapshot B-1 --slug <slug>`
Dispatch `answer-formulator` with: ...
Verify: `python3 .claude/scripts/verify_sub_phase.py verify B-1 --slug <slug>`
```

### 2.4 Deletable prose

Removed verbatim from all 4 commands:
- "How to read these dispatch specs" paragraph.
- "Throughout Step N, the literal string `<slug>`…" blockquote.
- "User-interrupt handling" paragraph.
- Long-form Stop-rule narrative. Replaced by one line per applicable sub-phase: `**Stop**: CLAUDE.md §4.5 — consecutive fail limit=N, resets on pass, session-local.`

### 2.5 CLAUDE.md §4.2 addition

Exactly one sentence appended at the end of §4.2:

> Phase C chain 중 user-interrupt: `run_in_background: true` Agent는 cancel되지 않는다. main session은 dialogue → intent 파악 → 다음 sub-phase dispatch 여부 결정 (wait / continue / abort). Do not dispatch next sub-phase without intent.

---

## 3. Components

### 3.1 `.claude/scripts/verify_sub_phase.py` (NEW)

Implementation outline:

- `argparse` subparsers: `snapshot`, `verify`. Both take `<sub_phase_id>` positional, `--slug`, optional `--stage-version`, optional `--batch-i`.
- `SUB_PHASES` dict at module top (SSOT). Each entry resolved against `ROOT = Path(__file__).resolve().parents[2]` or `RESEARCH_HUB_ROOT` env var (same override pattern as PR #1's hook).
- `_glob(pattern, slug)` returns `list[Path]` — supports `**` recursion.
- `snapshot` serialises `{"sub_phase": str, "slug": str, "glob": str, "paths": [...], "count": int, "mtimes": {path: float}, "batch_i": int|None}` to `/tmp/.verify_<stage>_<slug>_<sp>[_b<i>].json`. Stage is parsed from sub_phase_id prefix (`A-*` → papers, `B-*` → qa, `E-*` → experiments, `F-*` → analyze).
- `verify` reads the snapshot, re-globs, and applies the comparator:
  - Default: `post_count > pre_count` else fail.
  - `mode: "mtime"`: require `max(post_mtimes) > max(pre_mtimes)` on the tracked files.
  - `expect: "no-new"`: require `post_count <= pre_count` else fail with `on_fail`.
  - `verdict_parse: True`: additionally open the single expected file, parse YAML frontmatter, dispatch exit codes (0 / 15 / 14) as described in §2.1.
  - `extra_required`: each listed path must exist post-dispatch; otherwise fail.
- Error path: unknown `sub_phase_id` → `SystemExit(2)` with usage hint. Missing snapshot on `verify` → `SystemExit(2)` with "run `snapshot` first".

### 3.2 Test file `.claude/tests/test_verify_sub_phase.py` (NEW)

pytest `tmp_path` fixture + `RESEARCH_HUB_ROOT` override (same mechanism as PR #1).

| ID | Case | Assertion |
|---|---|---|
| T1 | snapshot B-1 → write `research/answers/x.md` → verify | exit 0, stdout contains `"B-1: OK"` |
| T2 | snapshot B-1 → (no artifact) → verify | exit 9, stderr contains "did not emit an answer file" |
| T3 | snapshot E-3 → write review with `verdict: approve` → verify | exit 0, stdout contains `"verdict: approve"` |
| T4 | snapshot E-3 → write review with `verdict: reject` → verify | exit 0, stdout contains `"verdict: reject"` (main-session owns Stop-rule branch) |
| T5 | snapshot E-3 → write review with no `verdict:` key → verify | exit 14, stderr mentions "(E-3)" |
| T6 | snapshot E-2 → artifact unchanged → verify | exit 0 (no-new comparator) |
| T6b | snapshot E-2 → write `qa_fail_20260419.md` → verify | exit 13 |
| T7 | snapshot A-3 --batch-i 0 → summary written → verify --batch-i 0 → snapshot --batch-i 1 → more written → verify --batch-i 1 | both exit 0, independent pre/post snapshots |
| T8 | `verify_sub_phase.py verify BOGUS --slug x` | exit 2, stderr "unknown sub_phase" |

### 3.3 Test file `.claude/tests/test_command_prune.py` (NEW)

Static grep over `.claude/commands/research-{papers,qa,experiments,analyze}.md` and `CLAUDE.md`.

| ID | Assertion |
|---|---|
| T1 | Each of the 4 command files contains `"How to read these dispatch specs"` **zero** times. |
| T2 | Each of the 4 command files contains `"User-interrupt handling"` **zero** times. |
| T3 | Each of the 4 command files has **zero** matches for `PRE_[A-Z0-9_]*_COUNT=\$\(find` regex. |
| T4 | Line counts: `research-papers.md` ≤ 250, `research-qa.md` ≤ 130, `research-experiments.md` ≤ 160, `research-analyze.md` ≤ 140. |
| T5 | `CLAUDE.md` contains the exact sentence fragment `"Phase C chain 중 user-interrupt"`. |

### 3.4 4 stage command file edits

For each command, apply the following transforms in order:

1. Delete "How to read these dispatch specs" paragraph.
2. Delete `> Throughout Step N, the literal string <slug>…` blockquote.
3. Replace every `PRE_*_COUNT=$(find...)` / `POST_*_COUNT=...` / `test -gt` verify trio with the two-line `verify_sub_phase.py snapshot|verify` pattern.
4. Shorten each Stop-rule block to one line: `**Stop**: CLAUDE.md §4.5 — consecutive fail limit=N, resets on pass, session-local.` (preserve N exactly: B-2 → 3, E-2 → 2, E-3 → 2, F-2 → 2).
5. Delete the "User-interrupt handling" paragraph.

Keep unchanged: Agent(prompt=…) bullet payloads, Phase A planner dispatch, Step 7 Completion narrative, stage-advance bash commands.

### 3.5 `CLAUDE.md` edit

Append the sentence from §2.5 at the end of the existing §4.2 "Phase A/B/C 프로토콜 (공통)" block. Location: immediately after the current Phase C paragraph that ends with "다음 stage 권장 문구 출력 금지 (Decision #6).". Do not renumber anything.

---

## 4. Testing & rollout

### 4.1 Unit tests
- `pytest .claude/tests/test_verify_sub_phase.py -v` — all 9 cases (T1–T8 plus T6b) green.
- `pytest .claude/tests/test_command_prune.py -v` — all 5 cases green.
- Existing `pytest .claude/tests/test_inject_lessons.py -v` still green (no overlap).

### 4.2 Static check
- `wc -l .claude/commands/research-{papers,qa,experiments,analyze}.md` output totals ≤ 650.

### 4.3 Rollback
- Each of the following is a separate commit and can be individually reverted:
  1. `verify_sub_phase.py` + unit test
  2. `research-papers.md` prune
  3. `research-qa.md` prune
  4. `research-experiments.md` prune
  5. `research-analyze.md` prune
  6. `CLAUDE.md` §4.2 sentence
  7. `test_command_prune.py`
- Reverting a command prune leaves the script dormant but functional; no coupling failure.
- No live smoke required (Q4 decision: hermetic unit + static grep suffices for this refactor).

---

## 5. Out of scope (explicit)

- Surface 2 (Agent prompt bullets) — will be addressed in PR #3 or #4.
- `loop_state.py` schema change — not needed; the new script only *reads* slug/stage_version.
- A-3 batch loop redesign — stays inline; script only exposes `--batch-i`.
- Stop-rule counter lift into the script — still session-local main-session reasoning.
- Slash-command generation or template engine — not introduced.
- CLAUDE.md renumbering — a single sentence appended, no heading movement.
- PR #1 hook/injection surfaces — untouched.

---

## 6. Success criteria

1. 4 stage commands total line count ≤ 650 (from ~991).
2. Individual command files meet per-file caps (§3.3 T4).
3. `verify_sub_phase.py` unit test T1–T8 (+T6b) green.
4. Static-grep test T1–T5 green.
5. Existing `test_inject_lessons.py` 7/7 still green (smoke for no regression in the shared test convention).
6. Any subagent dispatch payload diff = 0 bytes (verified by `git diff` of the Agent key-value bullet blocks — no changes there).

---

## 7. Open questions / defaults

- Do we move Stop-rule counter state into `loop_state.json`? **Default: no** (session-local reasoning preserved — future PR if ever needed).
- Does `verify_sub_phase.py` need JSON-Lines output for downstream machine parsing? **Default: no** (human stdout line sufficient for main-session consumption).
- Should `/tmp/.verify_*.json` be cleaned up by `stage-complete`? **Default: no** (tmpfs-backed, session-bounded; overwrite on next snapshot). Can add in a separate PR if tmp noise becomes a complaint.
