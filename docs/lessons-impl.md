---
domain: impl
updated: 2026-04-15
covers: [code-implementer, implementation-verifier]
---

# Lessons — Implementation (implement / verify)

code-implementer and implementation-verifier MUST Read this file before starting work. Append-only.

Phase C-1 domain: external repo integration, IMPL_MAP, boundary crossing, smoke tests, edge cases.

## How to add

`/research-lesson impl "<rule title>"`

---

<!-- append entries below this line -->

## 2026-04-15 — IMPL_MAP.md is required
- **Rule**: code-implementer first creates `experiments/<slug>/IMPL_MAP.md` and 1:1 maps each checklist item in PLAN.md to actual file paths / functions / CLI flags BEFORE implementation starts
- **Why**: without the mapping the verifier cannot check the PLAN↔code boundary crossing, and impl/setup boundaries blur when classifying failure causes
- **When to apply**: at the start of Phase C-1 — missing IMPL_MAP.md is a hard stop

## 2026-04-15 — External repos: minimally invasive integration
- **Rule**: clone external paper implementations as a subdirectory under `experiments/<slug>/code/` and do NOT edit the original files in place; keep wrapper/patch files separately
- **Why**: editing the original breaks both upstream-update tracking and reproducibility at the same time
- **When to apply**: at the first integration of an external repo — isolate required modifications into `patches/*.diff` or `overrides/*.py`

## 2026-04-15 — No hardcoded machine paths
- **Rule**: new code does NOT hardcode absolute paths like `/home/irteam/...`; it takes them via CLI arguments such as `--root`, `--data-dir`
- **Why**: the harness moves between two symlinked paths (`/home1/irteam/` and `/home/irteam/`) and hardcoding blocks portability to other machines
- **When to apply**: when writing any new script under `experiments/<slug>/code/`

## 2026-04-15 — Smoke test first, full run later
- **Rule**: implementation-verifier runs a 1-batch + 1-step smoke test to validate IV/DV shapes and metric boundaries BEFORE the full dataset run
- **Why**: discovering a shape mismatch after 8 hours of training wastes GPU and time
- **When to apply**: at the end of Phase C-1, as the gate before handing off to the analyst

<!-- seeded 2026-04-15 -->

## 2026-04-15 — force-commit hooks must cover every block with a global step counter
- **Rule**: the force-commit hook triggers on the global `abs_step` and, at fire time, overwrites all still-masked positions across the entire generation region (every block) in one pass, then short-circuits the scheduler loop
- **Why**: a block-local implementation only allows writing to current/prior blocks at fire time — but those are already committed, so the hook becomes a no-op and the smoke test produces bit-exact identical results to baseline. Actually happened at diffusion-llm-step iter1 on 2026-04-15
- **When to apply**: when inserting an intervention hook into a masked-diffusion LM sampler — if the result equals the baseline exactly, suspect this immediately and verify via `touched-positions` count

## 2026-04-15 — Batch drivers require the nohup+disown+heartbeat+sentinel 4-set
- **Rule**: long-running (>2min) batch drivers must be launched as `nohup ./driver.sh > logs/driver.log 2>&1 & disown`, and the driver internally must include all four of: (a) a per-cell `.heartbeat` touch (b) a completion sentinel `batch.done` (c) a failure list `batch_failed.txt` (d) a per-cell `metrics.json` existence check (skip). `set -e` is FORBIDDEN — a single cell failure must not kill the whole batch.
- **Why**: at diffusion-llm-step iter1 wave2 on 2026-04-15, running the parent bash in the background without `nohup`/`disown` caused the driver to be killed by SIGHUP when the Claude-Code session refreshed, stopping after seed0 at seed1 step 8/50. Also the driver had no CSV-append logic, so even the completed seed0 result was missing from `results.csv`.
- **When to apply**: when writing or launching any batch driver like `experiments/*/code/run_wave_*.sh` — and the driver MUST include an **inline append** step that writes per-cell results to the shared CSV/JSON aggregator (do NOT rely on a separate aggregator pass after cell execution).
