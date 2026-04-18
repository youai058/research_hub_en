# Lessons Injection Split — Design Spec

**Date**: 2026-04-19
**Scope**: research_hub harness hooks (`.claude/hooks/inject_lessons.sh`, `.claude/settings.json`)
**Goal**: Eliminate the ~3k-token-per-turn re-injection of `docs/lessons.md` bodies on every `UserPromptSubmit`, while preserving the SessionStart "full context load" contract.
**Parent brainstorm**: 2026-04-19 token reduction, Approach 2 (incremental per-lever), PR #1 of 4.

---

## 1. Problem

`/home1/irteam/sw/research_hub/.claude/hooks/inject_lessons.sh` is currently registered on `UserPromptSubmit` in `settings.json` (and nowhere else). Every user turn triggers the hook, which:

- Parses `docs/lessons.md`, extracts the last 3 `## YYYY-MM-DD` entries, and emits each entry's full body (up to 20 lines each, after whitespace filtering).
- Emits one-line entry counts for the 4 domain files (`lessons-paper/research/impl/analysis`).

Per-turn payload measured at ~3000 tokens (Rule + Why + When-to-apply triples × 3 entries). For a 10-turn session, ~30k tokens of duplicate rule content re-enters the main-session context — waste, not signal, because the content is identical turn-to-turn and the agent has durable context from the first occurrence.

`SessionStart` currently runs a different hook (`session_start.sh`) that emits loop-state summary only — no lessons. So there is no existing "full body on session start, lighter on subsequent turns" pattern.

### Why this is pure waste ("A strict" quality floor)

- Global lessons rules are durable: once the agent reads them at SessionStart, restating the full body on every turn adds no new information.
- Domain rules are not auto-injected anyway (count-only line) — agents Read their domain `lessons-*.md` on demand via the existing "agents must Read docs/lessons.md + their domain file before starting" convention.
- Therefore full-body re-emission on `UserPromptSubmit` fails a minimum-information-per-token bar.

---

## 2. Architecture

**Single script, CLI-argument branch.** `inject_lessons.sh` accepts one positional argument `full` or `titles` and `settings.json` registers the script at both hook events with the respective argument:

```
SessionStart     → inject_lessons.sh full      (unchanged output format)
UserPromptSubmit → inject_lessons.sh titles    (new compact format)
```

No environment-variable sniffing, no JSON stdin parsing (Claude Code does not set `HOOK_EVENT_NAME` as an env var for bash hooks; it passes JSON on stdin, which the current script does not consume). CLI arg is the simplest branch.

### Output formats

**`full` mode (existing, unchanged):**

```
<research-hub-lessons>
global: 12 entries total, showing last 3
## 2026-04-15 — Dedup Stage 1 — TRIGGER_WHITELIST SSOT 고정
- **Rule**: ...
- **Why**: ...
- **When to apply**: ...
## 2026-04-16 — 시간 캡 제거 ...
...
lessons-paper: 17 entries (Read the file in-session when working in this domain)
...
</research-hub-lessons>
```

~3000 tokens. Consumed once per session (SessionStart).

**`titles` mode (new):**

```
<research-hub-lessons>
global: 12 entries — last 3 titles:
- 2026-04-15: Dedup Stage 1 — TRIGGER_WHITELIST SSOT 고정
- 2026-04-16: 시간 캡 제거 (30분 제약 삭제, escalate 조건은 유료 API·외부 경로만)
- 2026-04-16: Phase C subagent dispatch is `run_in_background: true` by harness default
(Read docs/lessons.md for full bodies)
lessons-paper: 17 entries (Read the file in-session when working in this domain)
lessons-research: 4 entries (Read the file in-session when working in this domain)
lessons-impl: 6 entries (Read the file in-session when working in this domain)
lessons-analysis: 5 entries (Read the file in-session when working in this domain)
</research-hub-lessons>
```

~280 tokens. Consumed once per user turn (UserPromptSubmit).

### Title extraction rule

Each `## YYYY-MM-DD — <title-phrase>` heading in `lessons.md` contributes:
- `YYYY-MM-DD` from the heading.
- Everything after the first ` — ` (em-dash) as the title phrase, trimmed.
- If the heading lacks an em-dash, emit the full heading text after the date.

No body lines are parsed in `titles` mode. This keeps the parser trivial and robust.

### Fallback & safety

| Condition | Behavior |
|---|---|
| `$1` unset or unknown | Emit `full` (fail-safe to current behavior) |
| `docs/lessons.md` missing | Emit `global: (docs/lessons.md missing)` + exit 0 (unchanged) |
| `## YYYY-MM-DD` pattern matches 0 entries | Emit `global: (no dated entries)` + exit 0 (unchanged) |
| Entry heading has no ` — ` separator | Title = full line after date prefix |

---

## 3. Components

### 3.1 `.claude/hooks/inject_lessons.sh` (MODIFIED)

**Structural changes:**

- Script accepts `MODE="${1:-full}"`.
- Emit `<research-hub-lessons>` opener and closer unchanged.
- Factor the existing Python heredoc into two code paths behind a bash `case "$MODE"` switch:
  - `full)` — current Python block (last 3 entries, full body, 20-line trim per entry). Unchanged.
  - `titles)` — new Python block that prints `global: N entries — last 3 titles:` then 3 lines of `- YYYY-MM-DD: <title>`, then one line `(Read docs/lessons.md for full bodies)`.
  - `*)` — print a stderr warning `"inject_lessons.sh: unknown mode '$MODE', defaulting to full"`, then fall through to `full`.
- The 4-domain counts block (`for name in lessons-paper ...`) runs identically in both modes.
- No other behavior change (e.g., exit codes, error paths).

### 3.2 `.claude/settings.json` (MODIFIED)

**Registration changes:**

- `hooks.SessionStart[]`: retain existing `session_start.sh` registration. **Append** a second hook object that runs `inject_lessons.sh full`. (Claude Code runs hooks registered on the same event in order.)
- `hooks.UserPromptSubmit[]`: change the existing `inject_lessons.sh` command to `inject_lessons.sh titles`.

No other settings surface touched. No permission-allowlist changes (script path is already trusted).

### 3.3 `.claude/tests/test_inject_lessons.py` (NEW)

Python test (matches existing test convention in `.claude/tests/`). Uses `subprocess.run` to invoke the hook script with different `$1` values and a temp `docs/lessons.md` fixture.

**Test cases:**

| ID | Input | Assertion |
|---|---|---|
| T1 | `mode=full`, lessons.md has 3 entries | stdout contains `**Rule**:` `**Why**:` `**When to apply**:` labels (full body present) |
| T2 | `mode=titles`, same fixture | stdout contains `last 3 titles:` and 3 `- YYYY-MM-DD:` lines; does NOT contain `**Why**:` or `**When to apply**:` |
| T3 | `mode=` (empty first arg) | behaves as `full` (fallback) |
| T4 | `mode=bogus` | stderr warning emitted; stdout behaves as `full` |
| T5 | `lessons.md` missing | stdout contains `global: (docs/lessons.md missing)`; exit 0 |
| T6 | `lessons.md` entry has no em-dash separator | title row shows the full heading text |
| T7 | `mode=titles`, domain files present | domain count lines still emitted (line format identical to current) |

Fixture directory: write `lessons.md` to a `tmp_path` and point the hook at it by temporarily overriding `ROOT` via an env var `RESEARCH_HUB_ROOT` (new; script checks this before falling back to the computed `ROOT`). This keeps test hermeticity.

### 3.4 `docs/lessons.md` (APPEND)

Add a new entry documenting this split as a harness convention (meta-rule about hooks):

> `## 2026-04-19 — Hook event branch convention: positional CLI arg, not env var`
> Rule / Why / When-to-apply triple (per lessons format).

---

## 4. Testing & rollout

### 4.1 Unit tests

- `pytest .claude/tests/test_inject_lessons.py` — all 7 cases green.
- Existing hook tests (if any touch `inject_lessons`) remain green.

### 4.2 Smoke (live)

After merge, start a fresh session in `research_hub` and verify:

1. SessionStart message contains `**Rule**:` + `**Why**:` + `**When to apply**:` (full body, ~3k tokens).
2. First user message: injected `<research-hub-lessons>` block contains `last 3 titles:` and NO `**Why**:` (titles mode, ~280 tokens).
3. Tenth user message: same compact format, content identical to first.
4. Agent behavior on a random Phase B trigger phrase (e.g. "진행해") still routes correctly (proves the agent still has the rule from SessionStart).

Token delta target: ≥90 % reduction on the lessons block after the first turn. Full-session budget reduction: ~(N-1) × 2.7k tokens for N turns.

### 4.3 Rollback

One-line revert: in `settings.json`, change `inject_lessons.sh titles` back to `inject_lessons.sh` (the script still defaults to `full` if no arg). No code deletion required; the new `titles` branch and tests can stay dormant.

Trigger condition for rollback: any observed agent behavior regression attributable to missing rule context (e.g., agent ignores `run_in_background: true` mandate, re-introduces `>30min` caps, invents new trigger phrases). Mitigation during rollback: full body restored instantly; no data loss.

---

## 5. Out of scope (explicit)

- Domain `lessons-*.md` injection changes — already count-only, no waste.
- `session_start.sh` modification — separate concern (loop-state summary).
- JSON-stdin parsing in hooks — not needed for this change; deferred if a future hook needs it.
- Any agent/skill/command file edits — the `Read docs/lessons.md + domain file before starting` convention already handles on-demand full-body access.

---

## 6. Success criteria

1. Token count of the `<research-hub-lessons>` block on `UserPromptSubmit` turns drops from ~3000 to ~280 (≥90 % cut).
2. SessionStart still emits full body (unchanged contract).
3. All 7 unit tests green.
4. Live smoke: agent correctly handles a Phase B trigger phrase after 5+ turns (proof that rule context survives on session-scope).
5. Lessons entry appended to `docs/lessons.md` documenting the hook-branch convention.

---

## 7. Open questions (for plan stage)

- Should the `titles` mode also include domain-file titles (last 1 entry title per domain), or keep it count-only? Default: count-only (current behavior), but reconsider if user wants cross-domain salience in the per-turn block.
- Should `RESEARCH_HUB_ROOT` env-var override be introduced only for tests, or made a general capability? Default: tests-only, gated by the env var being set.
