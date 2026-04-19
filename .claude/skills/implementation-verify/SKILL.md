---
name: implementation-verify
description: "Incremental QA of an implementation. PLAN.md ↔ IMPL_MAP.md cross-boundary comparison (IV/DV/metric shape), smoke test, edge cases, feedback to implementer on failure. Owned by implementation-verifier. Triggers: 'verify implementation', 'QA', 'smoke test', 'boundary check'."
---

# Implementation Verify Skill

QA based on **cross-boundary comparison + proof of execution**. Goes beyond existence checks to verify shape matching and actual behavior.

## Input

- `research/plans/<slug>/PLAN.md`
- `experiments/<slug>/IMPL_MAP.md`
- The **list of changed files** code-implementer sends via SendMessage

## 4-step verification

### 1. Mapping Completeness

- Does every `[ ]` item in PLAN.md exist in IMPL_MAP.md?
- Do all IMPL_MAP mappings point to real files / functions / lines?
- Missing → **fail**: "PLAN §3.2 'Ablation A1' not mapped in IMPL_MAP"

### 2. Boundary Crossing Check (Evidence-aware)

Cross-compare PLAN IV/DV/metric against actual code types. Key is **shape, not existence**. Also check **Evidence-verification fidelity**.

Example:
- PLAN: "DV = accuracy (scalar, 0-100)"
- IMPL: `def compute_accuracy(preds, labels) -> float`
- Pass: float scalar matches

Counter-example:
- PLAN: "DV = latency (ms, per-sample)"
- IMPL: `def compute_latency(batch) -> float  # batch avg`
- Fail: "PLAN expects per-sample but IMPL returns batch average"

**Evidence-verification boundary (new, required)**:
- Does PLAN §E<i>'s `verification metric` match IMPL_MAP's `Verification metric` column?
- Does each Experiment point to **exactly one** Evidence id? (confirm IMPL_MAP Evidence ↔ Experiment 1:1)
- Does `decide_verdict()` decide CONFIRMED/REFUTED/INCONCLUSIVE using the same numbers as PLAN's `Expected Under / If Wrong`?
  - PLAN: Expected Under [0.75, 0.95], If Wrong < 0.55
  - IMPL: `if metric >= 0.75: return "CONFIRMED"; elif metric < 0.55: return "REFUTED"; else: return "INCONCLUSIVE"`
  - If numbers diverge, fail (wrong verdict at F-1)

### 3. Smoke Test (proof of actual execution)

- Call the module with a single minimal sample
- Verify expected output shape / range
- Must pass without exceptions

```python
# Example
from experiments.slug.code.data.loader import load_dataset, split
ds = load_dataset(debug=True, max_samples=4)
tr, va, te = split(ds, ratios=(0.5, 0.25, 0.25))
assert len(tr) == 2 and len(va) == 1 and len(te) == 1
```

- No dry-run: exercise the actual data flow
- Synthetic samples are enough. Do NOT load the full dataset (waste of time).

### 4. Edge Case probe

Try at least 3 edge cases:
- Empty input (empty list, zero rows)
- Single sample (batch_size=1)
- Max length / large values
- NaN / None / empty string
- Seed equivalence (same seed → same output)

## Feedback format on failure

SendMessage(code-implementer):

```
[FAIL] Module X verification

1. Mapping: PASS
2. Boundary crossing:
   - FAIL: function foo at code/models/wrapper.py:42
     - PLAN §2.1 expects input shape (B, N, D)
     - IMPL signature: foo(x: Tensor[N, D])  # missing batch dim
   - Fix suggestion: add batch dimension or wrap with vmap
3. Smoke test: SKIPPED (boundary fail)
4. Edge case: SKIPPED

Please fix boundary issue and re-request verification.
```

**Specificity required**: no vague statements like "function exists but wrong shape". Cite file, line, and PLAN section — all three.

## On pass

```
[PASS] Module X verification

1. Mapping: all PLAN §2 items covered
2. Boundary crossing: all shapes match
3. Smoke test: 4 samples processed, output shape (4, 10) as expected
4. Edge case: empty/single/nan all handled gracefully

PLAN checkboxes §2.1-2.3 → [x]. Ready for Module Y.
```

## Environment-issue handling

- Import error → verify `experiments/<slug>/code/__init__.py` exists; verify venv active
- Dataset path error → point out a typo in the config or absolute/relative confusion
- CUDA OOM → try the smoke test with `CUDA_VISIBLE_DEVICES=""` or `device='cpu'`

## Incremental timing

- Single batch QA after all modules complete → **forbidden**
- Immediate QA right after each module completes → **required**
- On failure, fix only that module and re-QA. Skip re-verification of unaffected adjacent modules.

## Failure modes

- Corrupted venv: recovery script or user guidance
- Ambiguous PLAN: ask experiment-planner for clarification
- 2 consecutive failures: report to orchestrator, trigger loop abort

## Checklist

- [ ] IMPL_MAP existence confirmed
- [ ] Mapping Completeness
- [ ] Boundary Crossing Check (shape comparison)
- [ ] Smoke test executed (actual data flow)
- [ ] ≥ 3 edge cases
- [ ] Pass/Fail decision + specific feedback
- [ ] (On pass) Approve flipping PLAN checkboxes to `[x]`
