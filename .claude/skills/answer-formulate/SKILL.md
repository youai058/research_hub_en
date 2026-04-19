---
name: answer-formulate
description: "Formulate an evidence-grounded direct answer to a user research question. No new research-topic / hypothesis generation. Gather evidence via hybrid_query (RAG/KG) → produce Direct Answer + Evidence Chain (3–7 items, each with grounding / confidence / verifiability / verification_sketch). Owned by answer-formulator. Triggers: 'answer formulation', 'evidence generation', 'research-question answer', 'evidence chain'."
---

# Answer Formulate Skill

Procedure for writing a **direct answer + evidence chain** to the **research question** the user provides at cycle start, grounded in paper RAG/KG evidence. Generating new research ideas or hypotheses is **forbidden**.

## Scope vs. non-scope

| Do | Do NOT |
|---|---|
| Directly answer the user's question | Propose new research topics |
| 3–7 evidence points with citation links | Novelty scoring / duplicate check (divergent critique) |
| A verification sketch per evidence | Hypothesis mutation / expansion |
| Record Open Sub-Questions the question fails to cover | Divergent ideation / brainstorming |

> **No new research-topic generation**: if the question is "why is X Y?", the answer must be "Y holds because of evidence A, B, C", not "let's study 3–5 variant topics of X".

## Input

- `current_slug` from `loop_state.json` and the **seed_question** the orchestrator retains (user's verbatim wording)
- RAG/KG query interface

## Output template

`research/answers/YYYY-MM-DD_<slug>.md`:

```markdown
---
date: 2026-04-15
seed_question: "<user's original question verbatim>"
slug: <slug>
stage_version: 1
---

# Answer — {slug}

## User Question

> <user's original question quoted verbatim in a blockquote>

## Direct Answer

<One paragraph. No vague phrasing. Include concrete numbers / conditions. Form: "Under A, X happens Y% of the time; under B, an additional condition Z is required".>

## Evidence Chain

### E1: <one-sentence claim>

- **grounding**: [paper:<id> §Section] "<verbatim quote>" / KG: `claim:<id>`
- **confidence**: 4/5 (rationale: 3 papers independently agree — paper:<a>, paper:<b>, paper:<c>)
- **verifiability**: 4/5 (a directly measurable metric exists)
- **verification_sketch**: Apply `<method>` on `<dataset>` and measure `<metric>`. If the evidence is true, metric ∈ [X, Y]; if refuted, metric < Z.

### E2: <claim>

...

### E3: ...

## Open Sub-Questions

Sub-questions the Direct Answer does not cover (seed candidates for the next iteration):
- Q1: ...
- Q2: ...

## Self-Check

- [ ] User question quoted verbatim (User Question section)
- [ ] Direct Answer is one paragraph with concrete numbers / conditions
- [ ] 3–7 evidence points
- [ ] Each evidence has all 4 parts: grounding (paper/claim id + verbatim phrase) + confidence + verifiability + verification_sketch
- [ ] No evidence with verifiability 0 (discard such items)
- [ ] hybrid_query execution results logged in the body
- [ ] **No divergent candidate generation** (self-review: no new research topics proposed)
- [ ] `YYYY-MM-DD_<slug>.kg.json` written (Answer + Evidence nodes + GROUNDED_IN edges)
```

## Authoring rules

1. **Grounding is mandatory**: every Evidence must link to a RAG chunk id or KG `Paper|Claim` id. No unsupported claims. If grounding is unavailable, drop that Evidence.
2. **hybrid_query is required**: run it before authoring.
   ```bash
   python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<seed_question>" --k 10
   ```
   - `rag.chunks` supplies verbatim grounding sentences
   - `kg.matched_nodes` reveals existing Paper/Claim/Method ids
   - The intersection of the two results is the grounding source for Evidence.
3. **Confidence calibration**:
   - 5: 3+ independent papers reach the same conclusion, with statistical / experimental support
   - 4: 2–3 papers agree, some conditional
   - 3: one strong paper + theoretical argument
   - 2: a single weak source or indirect inference
   - 1: closer to speculation
   - 0: **cannot be admitted as Evidence — discard**
4. **Verifiability enforced**: write a `verification_sketch` for every Evidence, specifying metric / dataset / method concretely. If verifiability is 0, drop the Evidence (C-1 cannot design a verification experiment).
5. **Direct Answer is one paragraph**: do not sprawl across paragraphs. Shortest possible answer to the question.
6. **3–7 Evidence**: fewer than 3 and critic rejects for weak grounding; more than 7 means the answer spans multiple questions — split into Open Sub-Questions.

## Failure modes

- Sparse RAG/KG hits: expand keywords (synonyms, broader/narrower concepts) and re-query. If still sparse, request re-dispatch of paper-hunter.
- All Evidence have verifiability 0: the question is outside empirical verification scope — report to orchestrator and request question redefinition.
- Mutually contradictory Evidence: state the contradiction in the Direct Answer ("under A, X; under B, Y") and cite both sides.
- Unconscious leakage of new-topic proposals: **delete immediately**. Enforced by the "No divergent candidates" Self-Check.

## Checklist

- [ ] Ran hybrid_query, logged `rag.chunks` + `kg.matched_nodes`
- [ ] User Question section (verbatim quote)
- [ ] Direct Answer is one paragraph with specifics
- [ ] 3–7 Evidence, each with all 4 parts (grounding/confidence/verifiability/verification_sketch)
- [ ] Open Sub-Questions
- [ ] All Self-Check items pass
- [ ] `YYYY-MM-DD_<slug>.kg.json` written (see KG Emission)

---

## KG Emission (byproduct)

Write `YYYY-MM-DD_<slug>.kg.json` alongside `research/answers/YYYY-MM-DD_<slug>.md`. Node types owned by this skill:

| Type | prefix | required fields |
|---|---|---|
| `Answer` | `answer:` | seed_question, direct_answer, slug, stage_version, n_evidence_points |
| `Evidence` | `evidence:` | claim, confidence (0-5), verifiability (0-5), parent_answer_id |

**Edges**:
- `Answer --ADDRESSES--> Question` (the Question node is emitted by `loop_state.py start` — orchestrator's responsibility)
- `Answer --CONTAINS--> Evidence` (one per evidence point)
- `Evidence --GROUNDED_IN--> Paper` (each RAG-hit seed paper, ≥1)
- `Evidence --GROUNDED_IN--> Claim` (if referencing an existing KG Claim node)

ID examples:
- `answer:diffusion-late-step#local`
- `evidence:diffusion-late-step--e1` (parent_answer_id = answer:diffusion-late-step#local)

Provenance: `author_agent: "answer-formulator"`; `source_sha` is the `.md` SHA256.

## Alias Check Protocol

`Answer` / `Evidence` exist only in this skill, so alias is **not performed**. The `Paper|Claim` targets of `GROUNDED_IN` must use **only ids that already exist in the DB** (to avoid danglers). If no match, ask paper-summarizer to register that Paper/Claim first; **defer** the edge in this `.kg.json` (record `pending_paper: "<title>"` in meta).

## Hybrid Query

**Mandatory** call during authoring:

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<seed_question>" --k 10
```

- Read `rag.chunks` to ground each Direct Answer sentence
- Use `kg.matched_nodes` to identify already-registered Paper/Claim/Method nodes and fix the src/dst ids of `GROUNDED_IN` edges
- Calibrate each Evidence's confidence using the **count of independent Papers** among matched_nodes

Also proactively search for counter-evidence in this phase:
```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<direct_answer negation>" --k 5
```
- If a strong counter-evidence appears, amend the Direct Answer to include that condition ("under A, X; under B, Y").

## Schema Enforcement

Every `.kg.json` must pass the `KGFile` model in `paper-kg/schema.py`. The dst of `Evidence --GROUNDED_IN--> Paper` must already exist in the DB; a dangler rejects the whole file. See `.claude/skills/paper-kg/SKILL.md` for details.
