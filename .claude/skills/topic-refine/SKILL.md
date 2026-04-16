---
name: topic-refine
description: "Socratic interview that turns a vague user topic into a structured `topic.json` spec before `/research-papers` Phase A. 3 perspectives (Scope Definer / Keyword Strategist / Triage Sharpener), 2–5 adaptive rounds, floor-rule termination at clarity ≥0.7 on all 3 dimensions. Trigger: '주제 구체화', 'refine topic', '인터뷰'."
---

# Topic Refine Skill

Invoked by the main session (NOT a subagent — requires TUI interactivity) at the very start of `/research-papers`. Transforms the raw `$ARGUMENTS` string into `research/topics/<slug>.topic.json` that paper-hunter, paper-triage, and orchestrator consume downstream.

**Divergent ideation is forbidden.** This skill narrows existing intent; it does not propose new methods, datasets, or research directions.

## Inputs / Outputs

- **Input**: raw user topic string (may be empty — then ask user once; if still empty, abort).
- **Output**: `research/topics/.pending.topic.json` (staging path, renamed to `<slug>.topic.json` after the command's `stage-enter` allocates the slug).

## The 3-Perspective Panel

Every round, Claude chooses 1–3 of these perspectives to ask from. Later rounds typically use fewer (narrowing).

| Perspective | Probes | Sample question stems |
|---|---|---|
| **Scope Definer** | venues, years, `include_arxiv` | "Whitelist 6 venue 전부 대상? NLP vs ML conference 우선이 있나요?" · "연도 범위는 기본 3년 버킷 [today, -1, -2]? 더 과거까지?" · "arXiv preprint까지 포함할까요 (`--include-arxiv`)?" |
| **Keyword Strategist** | which 2 axes, 3-variant expansion | "첫 번째 축은 `<분야명>`으로 보임. 두 번째 축 필요? (예: evaluation / training dynamics / sampling)" · "`<term>`의 약어/풀네임/어순변형 3종 중 누락된 것?" |
| **Triage Sharpener** | core question, include/exclude, signal methods | "이 분야 논문 중 어떤 성격을 원하나요 — survey? 새 method? analysis?" · "명확히 제외할 영역? (예: image diffusion은 text가 아니라 out)" · "Triage가 놓치면 안 되는 landmark method 3–5개는?" |

## Round Flow

```
Round N:
  1. Claude picks 1–3 questions (one per chosen perspective).
  2. Presents them in ONE message, one question per paragraph,
     each labeled with the perspective name.
  3. User answers in free text.
  4. Claude updates its working topic.json draft internally.
  5. Claude scores clarity on 3 dimensions (scope / triage / keywords).
  6. Claude prints: [round N/5] scope=X.XX triage=X.XX keywords=X.XX — MILESTONE
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
- **Plateau**: 2 consecutive rounds with delta < 0.05 on every dimension → `termination_reason: "plateau"`
- **Ceiling**: round 5 completed → `termination_reason: "ceiling"`
- **User early-exit**: user types `proceed` / `진행` / `done` / `이대로` → `termination_reason: "user_early_exit"`

**Minimum 2 rounds** unless user early-exits. The escape phrases above are **interview-local** — they do not advance the harness Phase B→C gate (that's a separate later prompt after PLAN.md).

## Milestones (display only)

| Milestone | Condition |
|---|---|
| INITIAL | round 1 starting |
| PROGRESS | at least one dimension ≥ 0.5 |
| REFINED | all dimensions ≥ 0.5 |
| READY | termination criteria met |

## Divergence Guard

If the user's answer invites divergence ("재미있는 게 뭐야?", "새로운 방향 제안해줘"), respond:

> "재미있는 주제 추천·새 연구 방향 제안은 이 interview의 역할이 아닙니다 (divergent ideation 금지). 기존에 보고 싶은 방향을 좁히는 단계입니다. 어느 쪽으로 좁히고 싶으신가요?"

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
interview_rounds (int),
interview_log (array of {round, perspectives_used, questions, user_answer, scores_after})
```

## Failure Modes

- User gives empty topic → ask once more; if still empty, abort with "topic required".
- User refuses to answer any question → early-exit with `user_early_exit`, clarity_scores reflect current state (low).
- `topic_spec.py validate` fails → print errors, try once to self-repair the draft, otherwise abort.

## Checklist

- [ ] Minimum 2 rounds unless user early-exits
- [ ] Never propose new research directions
- [ ] Each round's questions are labeled by perspective
- [ ] `[round N/5] scope=X triage=X keywords=X — MILESTONE` printed between rounds
- [ ] Final topic.json passes `topic_spec.py validate` (exit 0)
- [ ] File written to `research/topics/.pending.topic.json` (caller renames)
- [ ] `interview_log` populated with all rounds
