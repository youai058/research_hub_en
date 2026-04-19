---
name: critique
description: "Independent critique of an Answer's evidence chain. Four axes (Grounding Validity / Support Strength / Counter-Evidence / Verifiability) scored 0–5; each Evidence passes only if Grounding≥3 AND Support≥3 AND Verifiability≥3. On failure, send a fix request back to answer-formulator. Owned by critic. Triggers: 'critique answer', 'validate evidence', 'review grounding', 'assess support strength'."
---

# Critique Skill

Independently critique the **Direct Answer + Evidence Chain** in `research/answers/YYYY-MM-DD_<slug>.md`. Novelty is no longer scored — the only question is whether the answer stands on its evidence.

## Input

- `research/answers/YYYY-MM-DD_<slug>.md` (from answer-formulator)
- RAG/KG query interface

## 4-axis critique frame (new)

| Axis | Meaning | 0–5 interpretation |
|---|---|---|
| **Grounding Validity** | Does the Evidence's citation actually support that claim? Penalize out-of-context or reversed citations | 5 = accurate citation, 3 = right paper but section mismatch, 0 = out-of-context / opposite |
| **Support Strength** | Does the Evidence logically support the Direct Answer? Check for non-sequitur and missing links | 5 = necessary and sufficient, 3 = reinforcing / mildly indirect, 0 = non-sequitur |
| **Counter-Evidence** | Use `hybrid_query("<counter claim>")` to search for refuting papers. Lower = more dangerous | 5 = no rebuttal, 3 = minor conditional rebuttal, 0 = strong rebuttal |
| **Verifiability** | Can E-1 actually verify this Evidence experimentally? Does the verification_sketch name concrete metric / dataset? | 5 = immediately testable, 3 = partly vague, 0 = not empirically verifiable |

## Pass criteria

- **Per-Evidence**: `Grounding ≥ 3 AND Support ≥ 3 AND Verifiability ≥ 3`
- Evidence with `Counter-Evidence ≤ 2` is tagged **"weak"** and passed, but flagged as **priority verification** target for C-1
- **Answer-level**: `≥ 3` passing Evidence. If ≤ 2, the whole Answer FAILs → re-invoke B-1

## Output template

`research/critiques/<slug>.md`:

```markdown
---
critic_of: research/answers/YYYY-MM-DD_<slug>.md
date: 2026-04-15
stage_version: 1
---

# Critique — {slug}

## Evidence Scoring Table

| Evidence | Grounding | Support | Counter-Evidence | Verifiability | Pass? |
|---|---|---|---|---|---|
| E1 | 5 | 4 | 4 | 5 | YES |
| E2 | 3 | 2 | 3 | 4 | NO (Support) |
| E3 | 4 | 5 | 1 | 4 | YES (weak — counter!) |

## Per-Evidence Analysis

### E1 (PASS)

**Grounding Validity 5**: citation of "X increases when Y" in paper:<id> §3.2 is accurate.
**Support Strength 4**: directly supports the Direct Answer's claim that "under A, X occurs". "Condition C" still needs additional support.
**Counter-Evidence 4**: `hybrid_query("X decreases when Y")` surfaces paper:<z> reporting a reducing effect, but in a different setting. Minor.
**Verifiability 5**: verification_sketch names a concrete metric (accuracy@k) and dataset (HumanEval).

---

### E2 (FAIL — Support)

**Grounding Validity 3**: citation is correct but the source paper states a general tendency without the specific "Y%" number.
**Support Strength 2**: logical link to the Direct Answer's core claim is weak; risk of non-sequitur.
**Counter-Evidence 3**: no direct rebuttal.
**Verifiability 4**: verifiable.

**Fix suggestion**: explicitly rewrite which sub-claim of the Direct Answer E2 supports, OR re-search for a paper with a more direct quote.

---

### E3 (PASS — weak, counter flagged)

**Counter-Evidence 1**: `hybrid_query` returns paper:<w> reporting the opposite direction (n=500, p<0.01). Strong rebuttal.
→ C-1 must mark this Evidence as **priority verification** in the PLAN.

---

## Counter-Evidence Review

Rebutting papers found by `hybrid_query`:

| Evidence | Counter Paper | Impact | Action |
|---|---|---|---|
| E3 | paper:<w> (ACL 2024) | Opposing effect significant (p<0.01) | Priority verify E3 in C-1 |
| — | paper:<q> | Unrelated to Direct Answer, different domain | No impact |

## Answer Revision Suggestions

Direct Answer revision proposals:
- E2's support is weak, so the "Y%" number in the Direct Answer should be amended to the "Y%±δ" range actually reported in paper:<id> §3.2
- Reflect E3's counter-evidence conditionally: "under A, X; however in B, the opposite tendency (paper:<w>)"

## Pass/Fail Decision

- Evidence pass: E1, E3 (weak)
- Evidence fail: E2
- Answer-level: **PASS** (≥ 2 evidence passing) — C-1 may proceed
- Condition: E2 must be reworked by answer-formulator and re-critiqued

## Feedback to answer-formulator

**E2**:
- Re-check the verbatim text of paper:<id> §3.2. Verify whether "Y%" is actually reported.
- Alternative: re-ground the same claim on the direct number in paper:<a> §4.
- Target: Grounding Validity 3→5 + Support 2→4.
```

## Authoring rules

1. **Do NOT read answer-formulator's self-check**: to block independent-verification bias
2. **hybrid_query is required**: the Counter-Evidence axis must be scored from `python3 .claude/skills/paper-kg/scripts/hybrid_query.py` output. Do not just write "none".
3. **Specific feedback**: not "unclear" but "citation of paper:<id> §X does not match the source".
4. **No novelty / prior-work dedup scoring**: this loop is evidence-grounded answering, not invention.
5. **Out-of-context grounding probe**: verify paper quotes against actual RAG hits (one grep). Fabricated citations → Grounding 0.

## Failure modes

- All Evidence fail: re-enter the answer-formulator cycle (max 3 times)
- Counter-Evidence axis ambiguous: score conservatively low (≤ 2) so C-1 verifies first
- RAG/KG search failure: fall back to manual keyword matching + Known tag

## Checklist

- [ ] Evidence Scoring Table covers every Evidence
- [ ] All 4 axes applied to every Evidence
- [ ] hybrid_query results logged (especially Counter-Evidence)
- [ ] Counter-Evidence Review table
- [ ] Answer Revision Suggestions
- [ ] Pass/Fail Decision (per-Evidence + Answer-level)
- [ ] Concrete feedback for each failing Evidence
- [ ] `<slug>.kg.json` written in the same directory (see KG Emission)

---

## KG Emission (byproduct)

Write `<slug>.kg.json` next to `research/critiques/<slug>.md`. Node types owned by this skill:

| Type | prefix | required fields |
|---|---|---|
| `Critique` | `critique:` | target_answer_id, per_evidence_scores (dict: Evidence id → 4 axes), answer_pass (bool), summary |

**Edges**:
- `Critique --REVIEWS--> Answer`
- `Critique --CITES--> Paper` (papers used for grounding verification / counter search)
- `Critique --CONTRADICTS--> Claim` (claim of a rebutting paper found in counter-evidence)
- `Critique --FLAGS_WEAK--> Evidence` (Evidence that passed but has Counter-Evidence ≤ 2)

ID example: `critique:diffusion-late-step#local`

Provenance: `author_agent: "critic"`.

## Hybrid Query

**Mandatory** when scoring the Counter-Evidence axis:

```bash
# Negate each Evidence's claim as a query
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<negated claim>" --k 10
```

- If a Paper node in `kg.matched_nodes` reports opposite results, deduct points
- Read `rag.chunks` for concrete context and quote in the critique body
- Record top-k Paper ids as `CITES` + `CONTRADICTS` edges as needed

Also called for the Grounding Validity axis (citation authenticity):

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<exact quoted phrase>" --k 3
```

- Verify the quoted phrase exists in the paper at chunk granularity. If not, Grounding = 0.

## Schema Enforcement

The `Critique` node's `target_answer_id` must already exist in the DB; otherwise it is rejected as a dangler. The `.kg.json` from answer-formulator must be ingested first. `FLAGS_WEAK --> Evidence` dst must also exist in the DB (already registered via Answer's CONTAINS edge). See `.claude/skills/paper-kg/SKILL.md` for details.

(This skill creates no new `Method|Dataset|Model|Metric` nodes, so **Alias Check does not apply**.)
