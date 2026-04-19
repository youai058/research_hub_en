---
domain: research
updated: 2026-04-15
covers: [answer-formulator, critic, experiment-planner]
---

# Lessons — Research (answer-formulate / critique / experiment-plan)

answer-formulator, critic, and experiment-planner MUST Read this file before starting work. Append-only — do not edit existing entries, only append new ones.

Phase B-1/B-2/C-1 domain: Direct Answer + Evidence Chain writing, 4-axis evidence critique, Evidence verification experiment planning. (Entries before 2026-04-15 use the divergent-ideation framing; legacy labels are preserved as-is.)

## How to add

`/research-lesson research "<rule title>"`

---

<!-- append entries below this line -->

## 2026-04-15 — answer-formulator ↔ critic independence
- **Rule**: critic reads only the answer-formulator output and does NOT share the same session prompt or presets — it is activated in a separate agent thread
- **Why**: mixing generation and criticism in the same context creates "self-defense bias" that shrinks weaknesses, which inflates the 4-axis Evidence scores
- **When to apply**: when activating critic at Phase B-2 — take `answers/<slug>.md` as independent input and score on the 4 axes (Grounding Validity / Support Strength / Counter-Evidence / Verifiability)

## 2026-04-15 — codex cross-validation pass criteria
- **Rule**: an Answer moves to the C-1 planner only when every Evidence satisfies all four conditions: Grounding ≥ 3 AND Support ≥ 3 AND Verifiability ≥ 3 AND codex-review pass
- **Why**: internal critic scores alone couldn't escape the echo chamber; codex plays the independent moderator role
- **When to apply**: before the end of Phase B-2 — if any condition fails, send back to answer-formulator for rework

## 2026-04-15 — PLAN.md must specify IV/DV/control
- **Rule**: the PLAN.md written by experiment-planner MUST include Evidence mapping, IV, DV, control, baseline, metric, ablation, resource, and Expected Under / If Wrong sections
- **Why**: a PLAN missing IV/DV forces code-implementer to fill in interpretation by guessing, which makes it impossible to decide the Evidence verdict (CONFIRMED / REFUTED / INCONCLUSIVE / IMPL_BUG) during result interpretation
- **When to apply**: as the Phase C-1 artifact gate — if any required section is missing, reject immediately

## 2026-04-15 — Evidence grounding first, then Direct Answer
- **Rule**: answer-formulator first runs hybrid_query to collect RAG chunks + KG-matched Paper/Claim, records the results with citations in `answers/<slug>.md`, and ONLY THEN writes the Direct Answer paragraph and Evidence Chain
- **Why**: answers written without grounding carry high fabrication risk and score 0 on the critic's Grounding Validity axis, causing expensive rework
- **When to apply**: at the start of Phase B-1 — paste the `hybrid_query.py` execution log and top-k chunks/nodes at the top of the answers file

<!-- seeded 2026-04-15 -->
