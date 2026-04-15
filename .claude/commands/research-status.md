---
description: Print the current research_hub loop state (v3 schema), RAG index status, KG stats, lessons counts, and per-slug artifacts. Read-only.
---

# /research-status

Read-only observability. Reports the v3 loop state surface (stage / inner_phase / sub_phase / slug / stage_version) — autonomous mode is not a concept in v3.

```bash
python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py status
```

The script aggregates deterministically:
- `loop`: stage, inner_phase, sub_phase, slug, stage_version, last 3 history entries
- `rag`: manifest presence, stale flag, files/chunks tracked, embed model
- `artifacts`: existence of PLAN.md / Report.md / Report.slides.md at `research/plans/<stage>/<slug>/v<N>/` + `research/reports/<stage>/<slug>/v<N>/`; legacy per-slug artifacts (answer, critique, IMPL_MAP, results dir, diagnosis)
- `kg`: node/edge count, last upsert, rejected count, stale flag
- `lessons`: entry counts per domain

Print the JSON **plus** a short human summary (2–4 lines) highlighting anything unusual (stale RAG, missing artifacts for current stage, v1/v2 schema requiring migration).

Do not run agents. Do not modify any files.
