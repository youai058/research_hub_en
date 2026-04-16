# Topic Refine: One Question Per Turn

**Date**: 2026-04-16
**Status**: Approved
**Parent spec**: `2026-04-16-topic-refiner-design.md`

## Problem

topic-refine SKILL.md의 Round Flow는 한 라운드에 1~3개 질문을 한 메시지에 제시한다. 사용자가 여러 질문을 한꺼번에 받으면 답변 부담이 크고, superpowers:brainstorming의 "one question at a time" 원칙과 불일치한다.

## Goal

topic-refine 인터뷰를 **1 message = 1 question** 으로 전환하여 brainstorming과 동일한 UX 패턴을 따르게 한다. "round" 개념을 제거하고 **turn** 단위로 관리한다.

## Design

### 1. Turn Flow (Round Flow 대체)

기존 "Round Flow" 섹션을 아래로 교체:

```
Turn N (of max 7):
  1. Claude picks the SINGLE most important question
     from the 3 perspectives (Scope / Keywords / Triage).
  2. Presents it in ONE message — one question only.
     Labeled with the perspective name.
     — Bounded: (A)/(B)/... labeled options.
     — Open-ended: no labels, free-text expected.
  3. User answers in free text or by label.
  4. Claude updates working topic.json draft internally.
  5. Claude scores clarity on 3 dimensions (scope / triage / keywords).
  6. Claude prints: [turn N/7] scope=X.XX triage=X.XX keywords=X.XX — MILESTONE
  7. Claude decides: continue or terminate.
```

Key changes from Round Flow:
- "1–3 questions per round" -> "1 question per turn"
- Claude picks the **single most valuable** perspective/question for the current state
- Perspective label shown before the question (one per turn)

### 2. Termination Rules Update

| Condition | Before | After |
|---|---|---|
| Ceiling | round 5 completed | **turn 7 completed** |
| Floor | all 3 scores >= 0.7 | unchanged |
| Plateau | 2 consecutive rounds, delta < 0.05 on all dims | **2 consecutive turns**, delta < 0.05 on all dims |
| User early-exit | `proceed`/`done` etc. | unchanged |
| Minimum | 2 rounds | **2 turns** |

### 3. interview_log Compatibility

`topic_spec.py` schema is **not modified**. Existing fields are reused with narrower semantics:

- `interview_rounds` (int): now counts turns (1 question each), not multi-question rounds
- `interview_log[].round` (int): turn number (1-indexed)
- `interview_log[].perspectives_used` (array): always length 1
- `interview_log[].questions` (string): always a single question
- `interview_log[].user_answer` (string): unchanged
- `interview_log[].scores_after` (object): unchanged

Example entry:
```json
{
  "round": 3,
  "perspectives_used": ["Keyword Strategist"],
  "questions": "...(single question)...",
  "user_answer": "...",
  "scores_after": {"scope": 0.7, "triage": 0.5, "keywords": 0.6}
}
```

### 4. 3-Perspective Panel

The panel table (Scope Definer / Keyword Strategist / Triage Sharpener) is unchanged. The only behavioral change: Claude selects **one** perspective per turn instead of up to three. Later turns naturally gravitate toward the dimension with the lowest clarity score.

### 5. Question Presentation Rules

Unchanged — bounded choice `(A)`/`(B)` labels and open-ended modes still apply. The only difference: a single message never contains both modes simultaneously (since there's only one question).

Update the formatting contract line: remove "bounded + open-ended 질문이 섞여도 OK" clause (no longer applicable with 1 question/turn).

## Scope

**Modified file: 1**
- `.claude/skills/topic-refine/SKILL.md`

**Intentionally unchanged:**
- `topic_spec.py` — schema field names preserved
- `CLAUDE.md` — parent doc references "adaptive rounds"; cosmetic, not blocking
- `report_builder.py` — reads `interview_rounds` as a number, unaffected
- Parent spec (`2026-04-16-topic-refiner-design.md`) — historical record, not updated

## SKILL.md Edit Summary

| Section | Change |
|---|---|
| Description (frontmatter) | "2–5 adaptive rounds" -> "2–7 adaptive turns, one question per turn" |
| The 3-Perspective Panel | Add: "Each turn, Claude chooses exactly 1 perspective." Remove: "1–3 of these perspectives" |
| Round Flow -> Turn Flow | Full rewrite per Section 1 above |
| Termination | ceiling 5->7, "round"->"turn", minimum 2 turns |
| Milestones | "round N/5" -> "turn N/7" |
| Question Presentation Rules | Remove "bounded + open-ended 혼합" clause |
| Schema section | `interview_rounds` comment: "counts turns (1 question each)" |
| Checklist | Update wording: "round" -> "turn", "1–3 questions" -> "1 question" |

## Success Criteria

1. topic-refine 인터뷰에서 매 메시지에 질문이 정확히 1개만 나감
2. 최대 7 turns 후 자동 종료
3. clarity score가 매 turn 갱신되고 `[turn N/7]` 포맷으로 표시
4. `interview_log` entry의 `perspectives_used`가 항상 길이 1
5. 기존 `topic_spec.py validate`가 수정 없이 통과
