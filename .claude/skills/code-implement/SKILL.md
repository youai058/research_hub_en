---
name: code-implement
description: "Implement experiment code from PLAN.md. Minimally invasive integration of external paper repos, placed under experiments/<slug>/code/, with IMPL_MAP.md mapping PLAN↔code, enforcing configurable paths / licenses / conventions. Owned by code-implementer. Triggers: 'code implementation', 'integrate external repo', 'write experiment module'."
---

# Code Implement Skill

Procedure for turning each checkbox in PLAN.md into **runnable code**. Pairs with implementation-verifier for incremental QA.

## Input

- `research/plans/<slug>/PLAN.md`
- External paper repo URLs (identified in PLAN or via RAG)

## Output layout

```
experiments/<slug>/
├── code/
│   ├── data/              data loaders, preprocessing
│   ├── models/            model wrappers, method implementations
│   ├── training/          training loops
│   ├── eval/              metrics, statistical tests
│   ├── ablations/         ablation runners
│   └── utils/             shared helpers
├── configs/
│   └── default.yaml
├── run.sh
└── IMPL_MAP.md
```

## External repo exploration

1. **Read README first**: understand purpose, dependencies, entry point
2. **Find the entry point**: `main.py`, `train.py`, `run_*.py`
3. **Trace dependencies**: identify core modules via the import graph
4. **License check**: MIT/Apache → code reuse allowed (with attribution comment); GPL → avoid or reference only
5. **Minimal extraction**: pull only the needed functions and wrap them in adapters. No wholesale repo copying.

## Minimally invasive integration

1. **Adapter pattern**: do not call external functions directly; wrap them in a thin wrapper
   ```python
   # experiments/<slug>/code/models/external_adapter.py
   """Adapter for [Paper X] method.
   Source: https://github.com/.../paper-x (MIT License)
   Only func_Y is used.
   """
   from external_lib import func_Y

   def call_method_A(x, config):
       return func_Y(x, **_map_config(config))
   ```

2. **Config-driven**: externalize paths / hyperparameters into `configs/default.yaml`
3. **CLI-friendly**: `run.sh` uses the form `--method A --seed 0 --output results_<slug>/seed0/`
4. **Naming preservation**: do not forcibly rename external code (local variables may follow this project's style)

## IMPL_MAP.md template (3-way mapping)

`experiments/<slug>/IMPL_MAP.md`. Tracks **Evidence ↔ Experiment ↔ Code** 3-way:

```markdown
# Implementation Map — {slug}

Map each Experiment cell of PLAN.md to actual code. Each Experiment verifies exactly one Evidence.

## Evidence ↔ Experiment ↔ Code (full mapping)

| Evidence id | Experiment | PLAN §  | Code entry | Verification metric | Expected range |
|---|---|---|---|---|---|
| evidence:<slug>--e1 | E1 | PLAN §E1 | `code/experiments/e1.py::run()` | accuracy@k | [0.75, 0.95] |
| evidence:<slug>--e2 | E2 | PLAN §E2 | `code/experiments/e2.py::run()` | bootstrap CI | [0.10, 0.30] |
| evidence:<slug>--e3 | E3 | PLAN §E3 | `code/experiments/e3.py::run()` | paired-diff | [0.02, 0.08] |

## Experiment E1: Verify Evidence evidence:<slug>--e1

For each checkbox in PLAN §E1:

| PLAN item | File | Function | Line |
|---|---|---|---|
| Load {dataset} | `code/data/loader.py` | `load_dataset()` | 12 |
| Model wrapper | `code/models/wrapper.py` | `MethodA` | 34 |
| Metric computation | `code/eval/metrics.py` | `accuracy_at_k()` | 18 |
| Expected-range check | `code/experiments/e1.py` | `decide_verdict()` | 55 |

> `decide_verdict()` returns one of `CONFIRMED / REFUTED / INCONCLUSIVE`, compared against the PLAN's Expected Under / If Wrong ranges.

## Experiment E2: Verify Evidence evidence:<slug>--e2
...

## External Dependencies

| Package | Version | Source | License |
|---|---|---|---|
| transformers | 4.40.0 | pip | Apache-2.0 |
| paper-x-lib | commit abc123 | GitHub | MIT |
```

> 3-way requirement: if an Evidence id is missing from this table, F-1 results-analyst cannot produce per-evidence CONFIRMED/REFUTED verdicts. **Required**.

## run.sh template

```bash
#!/usr/bin/env bash
set -euo pipefail

SLUG="$(basename "$(dirname "$0")")"
OUT_ROOT="/home/irteam/sw/research_hub/results_${SLUG}"
mkdir -p "$OUT_ROOT"

METHODS=("A" "B" "C")
SEEDS=(0 1 2)

for method in "${METHODS[@]}"; do
  for seed in "${SEEDS[@]}"; do
    OUT="${OUT_ROOT}/method${method}_seed${seed}"
    mkdir -p "$OUT"
    python3 code/training/main.py \
      --config configs/default.yaml \
      --method "$method" \
      --seed "$seed" \
      --output "$OUT" \
      2>&1 | tee "$OUT/log.txt"
  done
done

echo "done: $OUT_ROOT"
```

## Incremental work unit

1. **Commit per module**: finish a module → call verifier → pass → next
2. **Verifier message format**:
   ```
   SendMessage(verifier,
     "Module 1 (Data loader) complete.
      Files: code/data/loader.py
      IMPL_MAP: §Module 1
      PLAN items: 3 checkboxes
      Ready for verification.")
   ```
3. **Do not start the next module before passing**

## Failure modes

- External repo unreachable: fall back to an alternative implementation or minimal stub, with an "external missing" flag in IMPL_MAP
- Dependency conflict: ask the user before installing into the existing `LLDM` conda env. Split a venv if necessary.
- Verifier fails twice in a row: report to orchestrator, roll back that module, redesign
- Ambiguous PLAN: request clarification from experiment-planner

## Checklist

- [ ] Full PLAN.md review, module boundaries identified
- [ ] External repo URLs confirmed, licenses checked
- [ ] `experiments/<slug>/code/` directory scaffolded
- [ ] `configs/default.yaml` drafted
- [ ] Module 1 implemented → verifier → pass → module 2...
- [ ] IMPL_MAP.md updated (covers every PLAN checkbox)
- [ ] `run.sh` written and smoke-tested
- [ ] PLAN.md `[ ]` flipped to `[x]`
- [ ] `experiments/<slug>/IMPL_MAP.kg.json` written (see KG Emission)

---

## KG Emission (byproduct)

Write `IMPL_MAP.kg.json` next to `experiments/<slug>/IMPL_MAP.md`. This skill is the **sole owner of experiment nodes**:

| Type | prefix | required fields |
|---|---|---|
| `Experiment` | `experiment:` | slug, plan_id, evidence_id, expected_under, expected_if_wrong, run_sh_path, output_dir, commit_hash (if any), seeds[] |

**Edges**:
- `Experiment --IMPLEMENTS--> Plan`
- `Experiment --VERIFIES--> Evidence` (**required** — core of 3-way tracking)
- `Experiment --USES_DATASET--> Dataset` (existing DB id)
- `Experiment --USES_MODEL--> Model`
- `Experiment --USES_METHOD--> Method` (including PLAN baselines)

ID example: `experiment:late-step-generation-gap#local`

Provenance: `author_agent: "code-implementer"`.

> ⚠️ Without this node, results-analyst cannot map results back to Plan, leaving a graph gap. **Required**.

## Alias Check Protocol

The dst of `USES_DATASET|USES_MODEL|USES_METHOD` edges must be looked up to an existing id:

```bash
python3 .claude/skills/paper-kg/scripts/query.py lookup --type Model --name-fuzzy "LLaMA-2-7B"
```

No match → go back to the Plan phase (verify experiment-planner finalized that node's alias). Do not mint new Model/Dataset/Method nodes here.

## Hybrid Query

Reference during external repo exploration:

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "<method> implementation" --k 5
```

- From `kg.matched_nodes` → Paper, look up the source paper's repo link
- From `rag.chunks` → § Setup / § Methodology paragraphs, extract verbatim hyperparameters
- Record license / commit hash metadata into the provenance of the `Experiment` node

## Schema Enforcement

For `Experiment --IMPLEMENTS--> Plan`, the Plan id must exist in the DB. If experiment-planner's `PLAN.kg.json` was not ingested first, ask orchestrator to re-dispatch. See `.claude/skills/paper-kg/SKILL.md` for details.
