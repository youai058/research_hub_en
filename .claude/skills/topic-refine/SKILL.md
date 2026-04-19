---
name: topic-refine
description: "Socratic interview that turns a vague user topic into a structured `topic.json` spec before `/research-papers` Phase A. 3 perspectives (Scope Definer / Keyword Strategist / Triage Sharpener), 2–7 adaptive turns (one question per turn), floor-rule termination at clarity ≥0.7 on all 3 dimensions. Triggers: 'refine topic', 'topic refinement', 'interview'."
---

# Topic Refine Skill

Invoked by the main session (NOT a subagent — requires TUI interactivity) at the very start of `/research-papers`. Transforms the raw `$ARGUMENTS` string into a staging spec at `research/topics/.pending.topic.json`, which the `/research-papers` command renames to `research/topics/<slug>.topic.json` after `stage-enter` allocates the slug. Downstream consumers (paper-hunter, paper-triage, orchestrator, report_builder) read the canonical `<slug>.topic.json` — this skill itself only ever writes the staging path.

**Divergent ideation is forbidden.** This skill narrows existing intent; it does not propose new methods, datasets, or research directions.

## Inputs / Outputs

- **Input**: raw user topic string (may be empty — then ask user once; if still empty, abort).
- **Output**: `research/topics/.pending.topic.json` (staging path, renamed to `<slug>.topic.json` after the command's `stage-enter` allocates the slug).

## The 3-Perspective Panel

Every turn, Claude chooses exactly **1** of these perspectives to ask from — the one most valuable given the current clarity scores.

| Perspective | Probes | Sample question stems |
|---|---|---|
| **Scope Definer** | venues, years, `include_arxiv` | **Bounded**: "Venue range: (A) all 6 whitelist (B) NLP first (ACL/EMNLP) (C) ML first (ICML/NeurIPS/ICLR) (D) specify manually" · "Year range: (A) last 3 years (B) last 5 years (C) specify manually" · "Include arXiv preprints: (A) no — whitelist venues only (B) yes (--include-arxiv)" |
| **Keyword Strategist** | which 2 axes, 3-variant expansion | **Open-ended**: "The first axis looks like `<field name>`. Need a second axis? (e.g. evaluation / training dynamics / sampling)" · "Any of the 3 variants of `<term>` (abbrev / full name / word-order) missing?" |
| **Triage Sharpener** | core question, include/exclude, signal methods | **Bounded**: "Paper type: (A) new method (B) survey/analysis (C) both (D) specify manually" · **Open-ended**: "Areas to clearly exclude? (e.g. image diffusion is out because this is about text)" · "What are the 3–5 landmark methods triage must not miss?" |

## Question Presentation Rules

Each question falls into one of two modes:

| Mode | When | Format |
|---|---|---|
| **Bounded choice** | Answer is a finite enumerable set (venue choice, yes/no, range choice, style choice, etc.) | `(A)` `(B)` `(C)` ... labels + one-line descriptions. End with "or answer in free text" |
| **Open-ended** | Needs user free-text input (keyword suggestions, exclusion-area description, landmark-method listing, etc.) | Question only, no labels. Add examples inline as `e.g. ...` when helpful |

**Formatting contract:**
- Choice labels must be `(A)`, `(B)`, `(C)`, ... alphabetic with parentheses.
- Number of choices: 2–5.
- Accept user answers as label-only ("B"), with parentheses ("(B)"), or free text.
- **Exactly 1** question per message. Bounded or open-ended — not both.

## Turn Flow

**One question per turn.** Claude picks the single most valuable question from the 3 perspectives given the current clarity scores, and presents it alone in one message.

```
Turn N (of max 7):
  1. Claude picks the SINGLE most important question
     from the 3 perspectives (Scope / Keywords / Triage).
  2. Presents it in ONE message — one question only.
     Labeled with the perspective name.
     — Bounded: (A)/(B)/... labeled options.
     — Open-ended: no labels, free-text expected.
  3. User answers in free text or by label (e.g. "B").
  4. Claude updates its working topic.json draft internally.
  5. Claude scores clarity on 3 dimensions (scope / triage / keywords).
  6. Claude prints: [turn N/7] scope=X.XX triage=X.XX keywords=X.XX — MILESTONE
  7. Claude decides: continue or terminate (see Termination).
```

## Clarity Scoring (self-assessment)

Each dimension is 0.0–1.0. Claude judges based on the current topic.json draft:

| Dimension | Ask yourself |
|---|---|
| **scope** | "If I ran `hunt.py` now, do I know venues + years + `--include-arxiv`? Any missing dimension docks 0.3–0.5." |
| **triage** | "If I wrote paper-triage `core_question` + `include` + `exclude` + `signal_methods` now, can it reject an off-topic paper without guessing?" |
| **keywords** | "Do I have ≤2 axes with 3-variant expansion (abbrev / full / word-order), matching the topic's vocabulary?" |

**No weighted aggregate.** Termination is governed purely by the floor rule below.

## Termination (any ONE triggers)

- **Floor**: all 3 dimension scores ≥ 0.7 → `termination_reason: "floor"`
- **Plateau**: 2 consecutive turns with delta < 0.05 on every dimension → `termination_reason: "plateau"`
- **Ceiling**: turn 7 completed → `termination_reason: "ceiling"`
- **User early-exit**: user types `proceed` / `go ahead` / `done` / `as-is` → `termination_reason: "user_early_exit"`

**Minimum 2 turns** unless user early-exits. The escape phrases above are **interview-local** — they do not advance the harness Phase B→C gate (that's a separate later prompt after PLAN.md).

## Milestones (display only)

| Milestone | Condition |
|---|---|
| INITIAL | turn 1 starting |
| PROGRESS | at least one dimension ≥ 0.5 |
| REFINED | all dimensions ≥ 0.5 |
| READY | termination criteria met |

## Divergence Guard

If the user's answer invites divergence ("what's interesting?", "suggest a new direction"), respond:

> "Suggesting interesting topics or new research directions is not this interview's role (divergent ideation is forbidden). This step narrows the direction you already want to pursue. Which way would you like to narrow it?"

Never propose methods, datasets, or evaluation ideas the user has not already mentioned.

## Emitting `topic.json`

On termination:

1. Build the final topic.json dict matching the schema in `scripts/topic_spec.py`.
2. Write to `research/topics/.pending.topic.json` (staging — the slug is not yet allocated at this point; the caller `/research-papers` command renames this file after `stage-enter`).
3. Validate with `python3 .claude/skills/topic-refine/scripts/topic_spec.py validate research/topics/.pending.topic.json` — if exit != 0, report the error list and abort.
4. Print the `refined_topic` + final clarity scores + `termination_reason` for the user.

## Schema (canonical — enforced by topic_spec.py)

See `scripts/topic_spec.py template` for the full blank template. Required top-level fields:

```
version, created, raw_input, refined_topic,
triage_context{core_question, include, exclude, signal_methods},
keyword_groups (≤2 lists of strings),
scope{venues, years, include_arxiv},
clarity_scores{scope, triage, keywords},   # each 0.0–1.0
termination_reason ∈ {floor, plateau, ceiling, user_early_exit},
interview_rounds (int),                # counts turns (1 question each)
interview_log (array of {round, perspectives_used, questions, user_answer, scores_after})  # each entry = 1 turn
```

## Failure Modes

- User gives empty topic → ask once more; if still empty, abort with "topic required".
- User refuses to answer any question → early-exit with `user_early_exit`, clarity_scores reflect current state (low).
- `topic_spec.py validate` fails → print errors, try once to self-repair the draft, otherwise abort.

## Checklist

- [ ] **One question per turn** — never present multiple questions in one message
- [ ] Minimum 2 turns unless user early-exits
- [ ] Never propose new research directions
- [ ] Each turn's question is labeled by perspective; bounded questions use `(A)`/`(B)` labels
- [ ] `[turn N/7] scope=X triage=X keywords=X — MILESTONE` printed between turns
- [ ] Final topic.json passes `topic_spec.py validate` (exit 0)
- [ ] File written to `research/topics/.pending.topic.json` (caller renames)
- [ ] `interview_log` populated with all turns (each entry = 1 question)
