#!/usr/bin/env python3
"""Report builder for stage-split architecture (v3).

Generates a pair of files at:
  research/reports/<stage>/<slug>/v<N>/Report.md
  research/reports/<stage>/<slug>/v<N>/Report.slides.md

Each stage has its own body template (papers / qa / experiments / analyze),
injected atop a shared YAML header (markdown) + Marp header (slides).

Usage
-----
Called from orchestrator / experiment-report skill / directly. The caller
supplies a JSON payload (via --payload path or stdin) with the sections
already filled in. This script only enforces the structure.

Payload schema (JSON)
---------------------
{
  "stage": "papers|qa|experiments|analyze",
  "slug": "<slug>",
  "stage_version": <int>,
  "started_at": "<kst>",
  "completed_at": "<kst>",
  "plan_path": "research/plans/<stage>/<slug>/v<n>/PLAN.md",
  "sub_phase_trace": ["A-1", "A-2", ...],
  "status": "success|partial|failed",
  "executive_summary": "3-5 line string",
  "success_criteria": [
    {"criterion": "...", "result": "pass|fail|na", "note": "..."}
  ],
  "artifacts": [{"path": "...", "size": "...", "note": "..."}],
  "deviations": "<str or empty>",
  "known_gaps": "<str or empty>",
  "outcome_summary": "<str>",
  "body": { /* stage-specific — see per-stage sections below */ }
}

Stage-specific `body` keys
--------------------------
papers:
  refined_topic: "<str — from research/topics/<slug>.topic.json>"
  clarity_scores: {"scope": float, "triage": float, "keywords": float}
  interview_rounds: int
  termination_reason: "floor|plateau|ceiling|user_early_exit"
  collection_stats: {"venue_year_matrix": [...], "totals": {...}}
  triage: {"histogram": "<ascii>", "accepted": [...], "rejected": [...], "threshold": 3.0}
  summarized: [{"slug": "...", "venue": "...", "year": "...", "title": "...", "completeness": "..."}]
  rag_delta: {"chunks_added": N, "total_files": N, "total_chunks": N, "embed_model": "..."}
  kg_delta: {"nodes_added": N, "by_type": {...}}
  anomalies: ["..."]

qa:
  question_restatement: "..."
  direct_answer: "<single paragraph>"
  evidence_chain: [{"id": "e1", "claim": "...", "grounding": 4, "confidence": "...", "verifiability": 3, "verification_sketch": "...", "cited_papers": ["..."]}]
  critic_scores: [{"evidence_id": "e1", "grounding": 4, "support": 3, "counter": 2, "verifiability": 3, "verdict": "pass|weak|fail"}]
  pass_fail_counts: {"pass": N, "weak": N, "fail": N}
  codex_review: {"agreements": [...], "disagreements": [...]}
  weak_points: ["..."]

experiments:
  plan_mapping: [{"evidence_id": "...", "experiment": "...", "iv": "...", "dv": "...", "expected_under": "...", "if_wrong": "..."}]
  resource_budget: {"time": "...", "disk": "...", "gpu": "...", "api_cost": "..."}
  impl_modules: [{"path": "...", "loc": N, "external_repo": "..."}]
  verifier_results: {"boundary_checks": "...", "shape_match": "..."}
  smoke_result: {"passed": true, "duration_s": N, "log": "..."}
  codex_e3_verdict: {"approve": true, "notes": "..."}
  remaining_todos: ["..."]

analyze:
  verdict_matrix: [{"evidence_id": "...", "CONFIRMED": 0, "REFUTED": 1, "INCONCLUSIVE": 0, "IMPL_BUG": 0}]
  answer_status: "fully supported|partially supported|needs revision|fully refuted"
  refuted_classification: [{"evidence_id": "...", "class": "claim wrong|impl bug|setup error|data issue", "note": "..."}]
  visualizations: [{"path": "...", "kind": "png|html"}]
  revision_seed: {"drop_evidence_ids": [...], "add_conditions": [...], "reframe_hints": [...]}
  codex_f2_verdict: {"approve": true, "notes": "..."}
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

KST = timezone(timedelta(hours=9))
VALID_STAGES = {"papers", "qa", "experiments", "analyze"}


def now_kst() -> str:
    return datetime.now(KST).isoformat(timespec="seconds")


def find_root(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).resolve()
    here = Path(__file__).resolve()
    for p in [here.parent, *here.parents]:
        if (p / "research").is_dir() and (p / "papers").is_dir():
            return p
    fallback = Path("/home/irteam/sw/research_hub")
    if fallback.is_dir():
        return fallback
    raise SystemExit("cannot locate research_hub root (use --root)")


# ---------------------------------------------------------- header emitters

def _md_header(payload: dict[str, Any]) -> str:
    sub_trace = payload.get("sub_phase_trace") or []
    lines = [
        "---",
        f"stage: {payload['stage']}",
        f"slug: {payload['slug']}",
        f"stage_version: {payload['stage_version']}",
        f"started_at: {payload.get('started_at', '')}",
        f"completed_at: {payload.get('completed_at', now_kst())}",
        f"plan_path: {payload.get('plan_path', '')}",
        f"sub_phase_trace: {json.dumps(sub_trace, ensure_ascii=False)}",
        f"status: {payload.get('status', 'success')}",
        "---",
    ]
    return "\n".join(lines)


def _marp_header(payload: dict[str, Any]) -> str:
    stage = payload["stage"]
    slug = payload["slug"]
    ver = payload["stage_version"]
    completed = payload.get("completed_at") or now_kst()
    return (
        "---\n"
        "marp: true\n"
        "theme: default\n"
        "paginate: true\n"
        "size: 16:9\n"
        f'header: "research_hub | {stage} | {slug} v{ver}"\n'
        f'footer: "Generated {completed}"\n'
        "style: |\n"
        "  section { font-size: 22px; }\n"
        "  h1 { color: #1a1a1a; }\n"
        "  code { background: #f4f4f4; }\n"
        "---\n"
    )


# ---------------------------------------------------------- common sections

def _common_md(payload: dict[str, Any]) -> str:
    out: list[str] = []

    out.append("# Executive Summary\n")
    out.append(payload.get("executive_summary", "_(summary missing)_"))
    out.append("")

    out.append("# Success Criteria Check\n")
    sc = payload.get("success_criteria") or []
    if sc:
        out.append("| Criterion | Result | Note |")
        out.append("|---|---|---|")
        for row in sc:
            result = row.get("result", "na")
            mark = {"pass": "✓", "fail": "✗", "na": "NA"}.get(result, result)
            out.append(
                f"| {row.get('criterion','')} | {mark} | {row.get('note','')} |"
            )
    else:
        out.append("_(no success criteria provided)_")
    out.append("")

    out.append("# Artifacts Produced\n")
    arts = payload.get("artifacts") or []
    if arts:
        out.append("| Path | Size | Note |")
        out.append("|---|---|---|")
        for a in arts:
            out.append(
                f"| `{a.get('path','')}` | {a.get('size','')} | {a.get('note','')} |"
            )
    else:
        out.append("_(none)_")
    out.append("")

    out.append("# Deviations from PLAN\n")
    out.append(payload.get("deviations") or "_(none)_")
    out.append("")

    out.append("# Known Gaps / Caveats\n")
    out.append(payload.get("known_gaps") or "_(none)_")
    out.append("")

    out.append("# Outcome Summary\n")
    out.append(payload.get("outcome_summary") or "_(pending)_")
    out.append("")

    return "\n".join(out)


# ---------------------------------------------------------- stage bodies (md)

def _fmt_score(v: Any) -> str:
    """Format a clarity-score float as 2-decimal string, falling back to '?'."""
    if isinstance(v, (int, float)):
        return f"{v:.2f}"
    return "?"


def _body_papers_md(body: dict[str, Any]) -> str:
    out: list[str] = []
    # Topic Refinement (from research/topics/<slug>.topic.json)
    out.append("## Topic Refinement\n")
    refined = body.get("refined_topic")
    clarity = body.get("clarity_scores") or {}
    if refined:
        out.append(f"- **Refined topic**: {refined}")
    out.append(
        f"- **Clarity scores**: scope={_fmt_score(clarity.get('scope'))} "
        f"triage={_fmt_score(clarity.get('triage'))} keywords={_fmt_score(clarity.get('keywords'))}"
    )
    out.append(f"- **Interview rounds**: {body.get('interview_rounds','?')}")
    out.append(f"- **Termination**: {body.get('termination_reason','?')}")
    out.append("")
    out.append("## Collection Statistics\n")
    cs = body.get("collection_stats") or {}
    if cs:
        out.append("```json")
        out.append(json.dumps(cs, ensure_ascii=False, indent=2))
        out.append("```")
    else:
        out.append("_(none)_")
    out.append("")

    out.append("## Triage Results\n")
    tri = body.get("triage") or {}
    if tri:
        out.append(f"- Threshold: **{tri.get('threshold','?')}**")
        out.append(f"- Accepted: {len(tri.get('accepted', []))}")
        out.append(f"- Rejected: {len(tri.get('rejected', []))}")
        hist = tri.get("histogram")
        if hist:
            out.append("\n```")
            out.append(hist)
            out.append("```")
    else:
        out.append("_(none)_")
    out.append("")

    out.append("## Summarized Papers\n")
    sm = body.get("summarized") or []
    if sm:
        out.append("| Slug | Venue | Year | Title | Completeness |")
        out.append("|---|---|---|---|---|")
        for p in sm:
            out.append(
                f"| `{p.get('slug','')}` | {p.get('venue','')} | {p.get('year','')} "
                f"| {p.get('title','')[:60]} | {p.get('completeness','')} |"
            )
    else:
        out.append("_(none)_")
    out.append("")

    out.append("## RAG Delta\n")
    rd = body.get("rag_delta") or {}
    out.append(f"- Chunks added: {rd.get('chunks_added','?')}")
    out.append(f"- Total files: {rd.get('total_files','?')}")
    out.append(f"- Total chunks: {rd.get('total_chunks','?')}")
    out.append(f"- Embed model: {rd.get('embed_model','?')}")
    out.append("")

    out.append("## KG Delta\n")
    kd = body.get("kg_delta") or {}
    out.append(f"- Nodes added: {kd.get('nodes_added','?')}")
    if kd.get("by_type"):
        out.append(f"- By type: `{json.dumps(kd['by_type'], ensure_ascii=False)}`")
    out.append("")

    anomalies = body.get("anomalies") or []
    if anomalies:
        out.append("## Anomalies\n")
        for a in anomalies:
            out.append(f"- {a}")
        out.append("")

    return "\n".join(out)


def _body_qa_md(body: dict[str, Any]) -> str:
    out: list[str] = []
    out.append("## Question Restatement\n")
    out.append(body.get("question_restatement") or "_(none)_")
    out.append("")

    out.append("## Direct Answer\n")
    out.append(body.get("direct_answer") or "_(none)_")
    out.append("")

    out.append("## Evidence Chain\n")
    ec = body.get("evidence_chain") or []
    if ec:
        out.append("| ID | Claim | Grounding | Confidence | Verifiability | Sketch | Citations |")
        out.append("|---|---|---|---|---|---|---|")
        for e in ec:
            out.append(
                f"| {e.get('id','')} | {e.get('claim','')[:30]} | {e.get('grounding','')} "
                f"| {e.get('confidence','')} | {e.get('verifiability','')} "
                f"| {e.get('verification_sketch','')[:60]} "
                f"| {', '.join(e.get('cited_papers', []))} |"
            )
    else:
        out.append("_(none)_")
    out.append("")

    out.append("## Critic Scores (4-axis)\n")
    cs = body.get("critic_scores") or []
    if cs:
        out.append("| Evidence ID | Grounding | Support | Counter | Verifiability | Verdict |")
        out.append("|---|---|---|---|---|---|")
        for s in cs:
            out.append(
                f"| {s.get('evidence_id','')} | {s.get('grounding','')} | {s.get('support','')} "
                f"| {s.get('counter','')} | {s.get('verifiability','')} | {s.get('verdict','')} |"
            )
    out.append("")

    counts = body.get("pass_fail_counts") or {}
    if counts:
        out.append(
            f"**Pass/Weak/Fail**: {counts.get('pass',0)} / {counts.get('weak',0)} / {counts.get('fail',0)}"
        )
        out.append("")

    cr = body.get("codex_review") or {}
    if cr:
        out.append("## Codex-reviewer (parallel) Verdict\n")
        out.append(f"- Agreements: {len(cr.get('agreements', []))}")
        out.append(f"- Disagreements: {len(cr.get('disagreements', []))}")
        out.append("")

    wp = body.get("weak_points") or []
    if wp:
        out.append("## Weak Points (retrieval gaps)\n")
        for w in wp:
            out.append(f"- {w}")
        out.append("")

    return "\n".join(out)


def _body_experiments_md(body: dict[str, Any]) -> str:
    out: list[str] = []

    out.append("## Section 1 — Plan\n")
    pm = body.get("plan_mapping") or []
    if pm:
        out.append("| Evidence ID | Experiment | IV | DV | Expected Under | If Wrong |")
        out.append("|---|---|---|---|---|---|")
        for r in pm:
            out.append(
                f"| {r.get('evidence_id','')} | {r.get('experiment','')} | {r.get('iv','')} "
                f"| {r.get('dv','')} | {r.get('expected_under','')} | {r.get('if_wrong','')} |"
            )
    rb = body.get("resource_budget") or {}
    if rb:
        out.append("")
        out.append(f"**Resource budget**: time={rb.get('time','?')}, disk={rb.get('disk','?')}, "
                   f"gpu={rb.get('gpu','?')}, api={rb.get('api_cost','?')}")
    out.append("")

    out.append("## Section 2 — Implementation\n")
    mods = body.get("impl_modules") or []
    if mods:
        out.append("| Path | LoC | External repo |")
        out.append("|---|---|---|")
        for m in mods:
            out.append(
                f"| `{m.get('path','')}` | {m.get('loc','')} | {m.get('external_repo','-')} |"
            )
    vr = body.get("verifier_results") or {}
    if vr:
        out.append("")
        out.append(f"**Verifier**: boundary_checks={vr.get('boundary_checks','?')}, "
                   f"shape_match={vr.get('shape_match','?')}")
    out.append("")

    out.append("## Section 3 — Smoke Result\n")
    sr = body.get("smoke_result") or {}
    out.append(f"- Passed: **{sr.get('passed','?')}**")
    out.append(f"- Duration: {sr.get('duration_s','?')} s")
    if sr.get("log"):
        out.append(f"- Log: `{sr['log']}`")
    cv = body.get("codex_e3_verdict") or {}
    if cv:
        out.append("")
        out.append(f"**Codex E-3 verdict**: approve={cv.get('approve','?')} — {cv.get('notes','')}")
    todos = body.get("remaining_todos") or []
    if todos:
        out.append("")
        out.append("### Remaining TODOs / skipped cells\n")
        for t in todos:
            out.append(f"- {t}")
    out.append("")

    return "\n".join(out)


def _body_analyze_md(body: dict[str, Any]) -> str:
    out: list[str] = []

    out.append("## Verdict Matrix (Experiment × Evidence)\n")
    vm = body.get("verdict_matrix") or []
    if vm:
        out.append("| Evidence ID | CONFIRMED | REFUTED | INCONCLUSIVE | IMPL_BUG |")
        out.append("|---|---|---|---|---|")
        for r in vm:
            out.append(
                f"| {r.get('evidence_id','')} | {r.get('CONFIRMED',0)} | {r.get('REFUTED',0)} "
                f"| {r.get('INCONCLUSIVE',0)} | {r.get('IMPL_BUG',0)} |"
            )
    out.append("")

    out.append("## Direct Answer Status\n")
    out.append(f"**{body.get('answer_status','?')}**")
    out.append("")

    rc = body.get("refuted_classification") or []
    if rc:
        out.append("## REFUTED 4-way Classification\n")
        out.append("| Evidence ID | Class | Note |")
        out.append("|---|---|---|")
        for r in rc:
            out.append(f"| {r.get('evidence_id','')} | {r.get('class','')} | {r.get('note','')} |")
        out.append("")

    viz = body.get("visualizations") or []
    if viz:
        out.append("## Visualizations\n")
        for v in viz:
            out.append(f"- `{v.get('path','')}` ({v.get('kind','')})")
        out.append("")

    rs = body.get("revision_seed") or {}
    if rs:
        out.append("## Revision Seed (payload for next qa call, manual delivery)\n")
        out.append("```json")
        out.append(json.dumps(rs, ensure_ascii=False, indent=2))
        out.append("```")
        out.append("")

    cv = body.get("codex_f2_verdict") or {}
    if cv:
        out.append("## Codex F-2 Verdict\n")
        out.append(f"- approve: {cv.get('approve','?')}")
        out.append(f"- notes: {cv.get('notes','')}")
        out.append("")

    return "\n".join(out)


STAGE_BODY_MD = {
    "papers": _body_papers_md,
    "qa": _body_qa_md,
    "experiments": _body_experiments_md,
    "analyze": _body_analyze_md,
}


# ---------------------------------------------------------- stage bodies (slides)

def _slides_common_opening(payload: dict[str, Any], title_suffix: str) -> str:
    return (
        f"# {payload['stage']} Report — {payload['slug']} v{payload['stage_version']}\n\n"
        f"{title_suffix}\n\n"
        f"Status: **{payload.get('status','?')}** · "
        f"Completed: {payload.get('completed_at', now_kst())}\n\n"
        "---\n\n"
    )


def _slides_common_closing(payload: dict[str, Any]) -> str:
    out: list[str] = []
    out.append("# Success Criteria\n\n")
    for row in (payload.get("success_criteria") or []):
        mark = {"pass": "✓", "fail": "✗", "na": "NA"}.get(row.get("result", "na"), "?")
        out.append(f"- {mark} {row.get('criterion','')}")
    out.append("\n---\n\n")

    out.append("# Outcome Summary\n\n")
    out.append(payload.get("outcome_summary") or "_(pending)_")
    out.append("\n")
    return "\n".join(out)


def _slides_papers(payload: dict[str, Any]) -> str:
    body = payload.get("body") or {}
    out = [_slides_common_opening(payload, "Paper collection stage")]
    cs = body.get("collection_stats") or {}
    out.append("# Collection Stats\n\n")
    out.append(f"```json\n{json.dumps(cs, ensure_ascii=False, indent=2)[:800]}\n```\n")
    out.append("\n---\n\n")

    tri = body.get("triage") or {}
    out.append("# Triage\n\n")
    out.append(f"- Threshold: {tri.get('threshold','?')}\n")
    out.append(f"- Accepted: {len(tri.get('accepted', []))}\n")
    out.append(f"- Rejected: {len(tri.get('rejected', []))}\n")
    out.append("\n---\n\n")

    sm = body.get("summarized") or []
    out.append("# Summarized (top 10)\n\n")
    if sm:
        out.append("| Slug | Venue/Year | Title |\n")
        out.append("|---|---|---|\n")
        for p in sm[:10]:
            out.append(
                f"| `{p.get('slug','')[:30]}` | {p.get('venue','')}/{p.get('year','')} "
                f"| {p.get('title','')[:40]} |\n"
            )
    out.append("\n---\n\n")

    rd = body.get("rag_delta") or {}
    kd = body.get("kg_delta") or {}
    out.append("# RAG / KG Delta\n\n")
    out.append(f"- RAG chunks added: {rd.get('chunks_added','?')}\n")
    out.append(f"- KG nodes added: {kd.get('nodes_added','?')}\n")
    out.append("\n---\n\n")

    out.append(_slides_common_closing(payload))
    return "".join(out)


def _slides_qa(payload: dict[str, Any]) -> str:
    body = payload.get("body") or {}
    out = [_slides_common_opening(payload, "Answer + Evidence + Critic")]

    out.append("# Question & Direct Answer\n\n")
    out.append(f"**Q**: {body.get('question_restatement','?')}\n\n")
    da = body.get("direct_answer", "")
    out.append(f"**A**: {da[:400]}{'…' if len(da) > 400 else ''}\n")
    out.append("\n---\n\n")

    out.append("# Evidence Chain\n\n")
    ec = body.get("evidence_chain") or []
    for e in ec[:7]:
        out.append(
            f"- **{e.get('id','')}**: {e.get('claim','')[:80]} (G{e.get('grounding','')}/"
            f"V{e.get('verifiability','')})\n"
        )
    out.append("\n---\n\n")

    out.append("# Critic 4-axis\n\n")
    cs = body.get("critic_scores") or []
    if cs:
        out.append("| ID | G | S | C | V | verdict |\n")
        out.append("|---|---|---|---|---|---|\n")
        for s in cs:
            out.append(
                f"| {s.get('evidence_id','')} | {s.get('grounding','')} | {s.get('support','')} "
                f"| {s.get('counter','')} | {s.get('verifiability','')} | {s.get('verdict','')} |\n"
            )
    out.append("\n---\n\n")

    cr = body.get("codex_review") or {}
    if cr:
        out.append("# Codex (parallel)\n\n")
        out.append(f"- Agreements: {len(cr.get('agreements',[]))}\n")
        out.append(f"- Disagreements: {len(cr.get('disagreements',[]))}\n")
        out.append("\n---\n\n")

    out.append(_slides_common_closing(payload))
    return "".join(out)


def _slides_experiments(payload: dict[str, Any]) -> str:
    body = payload.get("body") or {}
    out = [_slides_common_opening(payload, "Plan → Impl → Smoke")]

    pm = body.get("plan_mapping") or []
    out.append("# Plan Mapping (Evidence → Experiment)\n\n")
    if pm:
        out.append("| Ev | Exp | IV | DV |\n")
        out.append("|---|---|---|---|\n")
        for r in pm:
            out.append(
                f"| {r.get('evidence_id','')} | {r.get('experiment','')[:20]} "
                f"| {r.get('iv','')[:15]} | {r.get('dv','')[:15]} |\n"
            )
    out.append("\n---\n\n")

    mods = body.get("impl_modules") or []
    out.append("# Modules\n\n")
    for m in mods[:10]:
        out.append(f"- `{m.get('path','')}` ({m.get('loc','?')} LoC)\n")
    out.append("\n---\n\n")

    sr = body.get("smoke_result") or {}
    out.append("# Smoke Result\n\n")
    out.append(f"- passed: **{sr.get('passed','?')}**\n")
    out.append(f"- duration: {sr.get('duration_s','?')} s\n")
    out.append("\n---\n\n")

    cv = body.get("codex_e3_verdict") or {}
    if cv:
        out.append("# Codex E-3\n\n")
        out.append(f"- approve: {cv.get('approve','?')}\n")
        out.append(f"- notes: {cv.get('notes','')[:200]}\n")
        out.append("\n---\n\n")

    out.append(_slides_common_closing(payload))
    return "".join(out)


def _slides_analyze(payload: dict[str, Any]) -> str:
    body = payload.get("body") or {}
    out = [_slides_common_opening(payload, "Evidence verdict + diagnosis")]

    out.append("# Verdict Matrix\n\n")
    vm = body.get("verdict_matrix") or []
    if vm:
        out.append("| Ev | C | R | I | Bug |\n")
        out.append("|---|---|---|---|---|\n")
        for r in vm:
            out.append(
                f"| {r.get('evidence_id','')} | {r.get('CONFIRMED',0)} | {r.get('REFUTED',0)} "
                f"| {r.get('INCONCLUSIVE',0)} | {r.get('IMPL_BUG',0)} |\n"
            )
    out.append("\n---\n\n")

    out.append("# Answer Status\n\n")
    out.append(f"**{body.get('answer_status','?')}**\n")
    out.append("\n---\n\n")

    rc = body.get("refuted_classification") or []
    if rc:
        out.append("# 4-way Classification (REFUTED)\n\n")
        for r in rc:
            out.append(f"- **{r.get('evidence_id','')}**: {r.get('class','')} — {r.get('note','')[:80]}\n")
        out.append("\n---\n\n")

    viz = body.get("visualizations") or []
    if viz:
        out.append("# Visualizations\n\n")
        for v in viz[:8]:
            out.append(f"- `{v.get('path','')}` ({v.get('kind','')})\n")
        out.append("\n---\n\n")

    rs = body.get("revision_seed") or {}
    if rs:
        out.append("# Revision Seed (manual handoff)\n\n")
        out.append(f"```json\n{json.dumps(rs, ensure_ascii=False, indent=2)[:600]}\n```\n")
        out.append("\n---\n\n")

    cv = body.get("codex_f2_verdict") or {}
    if cv:
        out.append("# Codex F-2\n\n")
        out.append(f"- approve: {cv.get('approve','?')}\n")
        out.append(f"- notes: {cv.get('notes','')[:200]}\n")
        out.append("\n---\n\n")

    out.append(_slides_common_closing(payload))
    return "".join(out)


STAGE_SLIDES = {
    "papers": _slides_papers,
    "qa": _slides_qa,
    "experiments": _slides_experiments,
    "analyze": _slides_analyze,
}


# ---------------------------------------------------------- build + write

def build_report(payload: dict[str, Any]) -> tuple[str, str]:
    """Return (markdown, marp_slides)."""
    stage = payload["stage"]
    if stage not in VALID_STAGES:
        raise SystemExit(f"invalid stage {stage!r}; must be one of {sorted(VALID_STAGES)}")
    body = payload.get("body") or {}

    md = "\n".join([
        _md_header(payload),
        "",
        _common_md(payload),
        "---",
        "",
        f"# Stage-specific details ({stage})",
        "",
        STAGE_BODY_MD[stage](body),
    ])
    slides = _marp_header(payload) + "\n" + STAGE_SLIDES[stage](payload)
    return md, slides


def write_report(root: Path, payload: dict[str, Any]) -> dict[str, str]:
    stage = payload["stage"]
    slug = payload["slug"]
    version = payload["stage_version"]
    report_dir = root / "research" / "reports" / stage / slug / f"v{version}"
    report_dir.mkdir(parents=True, exist_ok=True)

    md_path = report_dir / "Report.md"
    slides_path = report_dir / "Report.slides.md"

    # No overwrite: if a Report.md already exists, refuse unless payload says
    # status=='partial' (the caller is deliberately re-writing an incomplete
    # run before finalization).
    if md_path.is_file() and payload.get("status") != "partial":
        raise SystemExit(f"write_report: refuses to overwrite {md_path}")

    md, slides = build_report(payload)
    md_path.write_text(md, encoding="utf-8")
    slides_path.write_text(slides, encoding="utf-8")

    # Keep `latest` symlink current.
    latest = report_dir.parent / "latest"
    try:
        if latest.is_symlink() or latest.exists():
            latest.unlink()
        latest.symlink_to(f"v{version}")
    except Exception:
        pass

    return {
        "report_md": str(md_path),
        "report_slides": str(slides_path),
    }


# ---------------------------------------------------------- CLI

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None)
    ap.add_argument("--payload", required=True,
                    help="path to JSON payload, or '-' to read stdin")
    args = ap.parse_args(argv)

    if args.payload == "-":
        payload_txt = sys.stdin.read()
    else:
        payload_txt = Path(args.payload).read_text(encoding="utf-8")
    payload = json.loads(payload_txt)

    for k in ("stage", "slug", "stage_version"):
        if k not in payload:
            raise SystemExit(f"payload missing required field: {k}")

    root = find_root(args.root)
    result = write_report(root, payload)
    print(json.dumps({"status": "ok", **result}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
