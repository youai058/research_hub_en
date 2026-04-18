#!/usr/bin/env python3
"""Research-hub loop state manager (v3 — stage-split).

Encapsulates all deterministic reads/writes on research/loop_state.json
for the 4-stage split architecture. Slash commands and the orchestrator
go through this module; no hand-rolled JSON.

Schema v3
---------
{
  "version": 3,
  "stage": "papers|qa|experiments|analyze|idle",
  "inner_phase": "A|B|C|completed|null",
  "sub_phase": "A-1|A-2|A-3|A-4|B-1|B-2|C-1|E-1|E-2|E-3|F-1|F-2|null",
  "slug": "<stage-scoped 1st-class identifier>",
  "stage_version": <int|null>,
  "started_at": "<kst>",
  "last_update": "<kst>",
  "history": [ { "stage": ..., "slug": ..., "stage_version": ...,
                 "inner_phase": ..., "sub_phase": ..., "event": ...,
                 "at": "<kst>" }, ... ]
}

Five-field core: stage, inner_phase, sub_phase, slug, stage_version.

Stage mapping: each stage owns a bounded list of Phase C sub-phases.
  papers      → A-1 A-1.5 A-2 A-3 A-4
  qa          → B-1 B-2
  experiments → E-1 E-2 E-3     (C-1 is covered by Phase A/design skill;
                                  in Phase C only E-1..E-3 execute)
  analyze     → F-1 F-2

Subcommands
-----------
stage-enter     enter a stage (idle → stage, allocate next version)
stage-advance   move inner_phase (A→B, B→C) or sub_phase forward within stage
stage-complete  terminate the stage (→ inner_phase=completed → idle)
stage-restart   restart within the current stage (C→B or B→A, same version)
status          consolidated report (loop + RAG + KG + artifacts)
show            dump loop_state.json
history         append a free-form history entry

iteration counter and autonomous flag are REMOVED in v3.
--force bypasses the transition guard where allowed.

Every mutation writes atomically (tmp + rename) and updates last_update (KST).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

KST = timezone(timedelta(hours=9))

# --------------------------------------------------------------- schema v3

SCHEMA_VERSION = 3

STAGES = ["papers", "qa", "experiments", "analyze"]
IDLE = "idle"

INNER_PHASES = ["A", "B", "C", "completed"]

STAGE_SUBPHASES: dict[str, list[str]] = {
    "papers":      ["A-1", "A-1.5", "A-2", "A-3", "A-4"],
    "qa":          ["B-1", "B-2"],
    # C-1 is design (Phase A via experiment-design); Phase C runs E-1..E-3.
    "experiments": ["E-1", "E-2", "E-3"],
    "analyze":     ["F-1", "F-2"],
}

ALL_SUBPHASES: set[str] = {sp for seq in STAGE_SUBPHASES.values() for sp in seq}

# Only these exact phrases unlock B → C.
# NOTE: `해줘` and `그래` were removed in 2026-04-15 codex-review M2 — too ambiguous
# as standalone Korean fillers. Keep composites (구현해줘, ok 해, 좋아 진행).
TRIGGER_WHITELIST_KO = [
    "구현해줘", "실행해줘", "진행해줘", "ok 해", "시작해",
    "좋아 진행", "ok 진행", "진행해",
]
TRIGGER_WHITELIST_EN = [
    "proceed", "go ahead", "run it", "execute", "ok run it", "ok proceed",
]
TRIGGER_WHITELIST = [p.lower() for p in (TRIGGER_WHITELIST_KO + TRIGGER_WHITELIST_EN)]


def is_trigger_phrase(utterance: str) -> bool:
    """Case-insensitive + trim match against the whitelist.

    Exact match after strip + lowercase. Used by orchestrator / Phase B gate.
    """
    if not utterance:
        return False
    u = utterance.strip().lower()
    return u in TRIGGER_WHITELIST


# ------------------------------------------------------------------ root

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


def now_kst() -> str:
    return datetime.now(KST).isoformat(timespec="seconds")


# --------------------------------------------------------- state I/O + migration

def _empty_state_v3() -> dict[str, Any]:
    return {
        "version": SCHEMA_VERSION,
        "stage": IDLE,
        "inner_phase": None,
        "sub_phase": None,
        "slug": None,
        "stage_version": None,
        "started_at": None,
        "last_update": None,
        "history": [],
    }


def migrate_to_v3(state: dict[str, Any], state_path: Path) -> dict[str, Any]:
    """Convert v1/v2 state (iteration + phase) into v3 (stage + inner + sub).

    v1/v2 fields we read: version, iteration, phase, current_slug, history,
                           started_at, last_update.
    v3 fields we write:   version, stage, inner_phase, sub_phase, slug,
                           stage_version, started_at, last_update, history.

    iteration is dropped entirely. autonomous_on references are not here by
    design (they lived in the module, not the JSON). stage_version is set
    to 1 initially; callers should re-scan via scan_existing_versions() on
    the next stage-enter.

    Backup is written once, in-place, next to state_path:
      v1 → loop_state.v1.bak.json
      v2 → loop_state.v2.bak.json
    """
    old_version = int(state.get("version") or 1)
    if old_version >= SCHEMA_VERSION:
        return state

    # Backup the raw file before any in-memory rewrite.
    if state_path.is_file():
        bak = state_path.with_name(f"loop_state.v{old_version}.bak.json")
        if not bak.is_file():
            shutil.copy2(state_path, bak)

    old_phase = state.get("phase")
    slug = state.get("current_slug")
    history = state.get("history") or []

    new_state: dict[str, Any] = {
        "version": SCHEMA_VERSION,
        "stage": IDLE,
        "inner_phase": None,
        "sub_phase": None,
        "slug": slug,
        "stage_version": None,
        "started_at": state.get("started_at"),
        "last_update": state.get("last_update"),
        "history": history,
    }

    # If the old loop was mid-flight, approximate the stage from the phase.
    # This is a best-effort convenience; v3 callers are expected to run
    # stage-enter for the stage they actually want next.
    if old_phase and old_phase != "done":
        stage_guess = None
        for stage, sps in STAGE_SUBPHASES.items():
            if old_phase in sps:
                stage_guess = stage
                break
        # Legacy C-1 maps to experiments (design/planning subphase).
        if old_phase == "C-1":
            stage_guess = "experiments"
        # Legacy D was alignment-only and has no v3 equivalent; fall back to
        # parked-in-idle. Caller decides what to do next.
        if stage_guess:
            new_state["stage"] = stage_guess
            new_state["inner_phase"] = "C"
            new_state["sub_phase"] = old_phase
            new_state["stage_version"] = 1

    new_state["history"].append({
        "event": "migrated_to_v3",
        "from_version": old_version,
        "from_phase": old_phase,
        "at": now_kst(),
    })
    return new_state


def load_state(state_path: Path) -> dict[str, Any]:
    if not state_path.is_file():
        return _empty_state_v3()
    try:
        raw = json.loads(state_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"loop_state.json is corrupt: {e}")
    ver = int(raw.get("version") or 1)
    if ver < SCHEMA_VERSION:
        migrated = migrate_to_v3(raw, state_path)
        save_state(state_path, migrated)
        return migrated
    # Fill any missing v3 keys (forward-compatible).
    for k, v in _empty_state_v3().items():
        raw.setdefault(k, v)
    return raw


def save_state(path: Path, state: dict[str, Any]) -> None:
    state["last_update"] = now_kst()
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(tmp, path)


def slugify(topic: str, maxlen: int = 60) -> str:
    s = topic.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    return s[:maxlen] or "untitled"


# ----------------------------------------------------- versioning helpers

_V_DIR_RE = re.compile(r"^v(\d+)$")


def scan_existing_versions(root: Path, stage: str, slug: str) -> list[int]:
    """Return sorted list of existing v<N> numbers under research/plans/<stage>/<slug>/.

    Also considers research/reports/<stage>/<slug>/ to be conservative — a
    version exists if EITHER directory has it.
    """
    nums: set[int] = set()
    for base in ("plans", "reports"):
        d = root / "research" / base / stage / slug
        if not d.is_dir():
            continue
        for child in d.iterdir():
            if not child.is_dir():
                continue
            m = _V_DIR_RE.match(child.name)
            if m:
                nums.add(int(m.group(1)))
    return sorted(nums)


def next_version(root: Path, stage: str, slug: str) -> int:
    existing = scan_existing_versions(root, stage, slug)
    return (max(existing) + 1) if existing else 1


def ensure_version_dirs(root: Path, stage: str, slug: str, version: int) -> dict[str, Path]:
    """Create v<N>/ under plans and reports. Return absolute paths.

    Asserts no overwrite: if the v<N> plan dir already exists, raises.
    """
    plan_dir = root / "research" / "plans" / stage / slug / f"v{version}"
    report_dir = root / "research" / "reports" / stage / slug / f"v{version}"
    if plan_dir.is_dir():
        # Allow re-entering the same version ONLY if the PLAN.md is not yet
        # written (e.g., crash between mkdir and first write). Otherwise abort.
        if (plan_dir / "PLAN.md").is_file():
            raise SystemExit(
                f"stage-enter: version dir already has PLAN.md: {plan_dir}. "
                f"Choose a new version (re-run stage-enter)."
            )
    plan_dir.mkdir(parents=True, exist_ok=True)
    report_dir.mkdir(parents=True, exist_ok=True)

    # Best-effort 'latest' symlink; non-fatal.
    for base in (plan_dir.parent, report_dir.parent):
        latest = base / "latest"
        target = f"v{version}"
        try:
            if latest.is_symlink() or latest.exists():
                latest.unlink()
            latest.symlink_to(target)
        except Exception:
            pass

    return {"plan_dir": plan_dir, "report_dir": report_dir}


# ----------------------------------------------------- KG byproduct (v3)

def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _emit_loop_kg(
    root: Path,
    state_path: Path,
    state: dict[str, Any],
    event: str,
) -> dict[str, Any]:
    """Append a LoopStage node to research/loop_state.kg.json.

    v3 node id form: loop:<slug>-<stage>-v<n>-<inner>-<event>
    (iteration is gone; stage_version replaces it.)
    """
    kg_path = state_path.with_name("loop_state.kg.json")

    stage = state.get("stage") or IDLE
    inner = state.get("inner_phase") or "null"
    sub = state.get("sub_phase") or "null"
    slug = state.get("slug") or "untitled"
    version = state.get("stage_version") or 0
    ts = state.get("last_update") or now_kst()

    slug_clean = re.sub(r"[^a-z0-9]+", "-", slug.lower()).strip("-") or "untitled"
    stage_clean = re.sub(r"[^a-z0-9]+", "-", stage.lower()).strip("-") or "idle"
    inner_clean = re.sub(r"[^a-z0-9]+", "-", inner.lower()).strip("-") or "null"
    event_clean = re.sub(r"[^a-z0-9]+", "-", event.lower()).strip("-") or "event"
    node_id = f"loop:{slug_clean}-{stage_clean}-v{version}-{inner_clean}-{event_clean}"

    if kg_path.is_file():
        try:
            existing = json.loads(kg_path.read_text(encoding="utf-8"))
        except Exception:
            existing = {}
    else:
        existing = {}

    nodes = existing.get("nodes") or []
    if any(n.get("id") == node_id for n in nodes):
        return {"status": "duplicate", "id": node_id}

    nodes.append({
        "id": node_id,
        "type": "LoopStage",
        "name": f"{stage} v{version} {inner}/{sub} ({event})",
        "meta": {
            "stage": stage,
            "stage_version": version,
            "inner_phase": inner,
            "sub_phase": sub,
            "slug": slug,
            "event": event,
            "at": ts,
        },
    })

    source_sha = _sha256_file(state_path) if state_path.is_file() else None
    payload = {
        "version": 1,
        "source_file": str(state_path.as_posix()),
        "source_sha": source_sha,
        "extracted_at": now_kst(),
        "author_agent": "loop_state.py",
        "nodes": nodes,
        "edges": existing.get("edges") or [],
    }

    kg_path.parent.mkdir(parents=True, exist_ok=True)
    tmp = kg_path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(kg_path)

    try:
        stale = root / "papers" / "vector_db" / "kg.stale"
        stale.parent.mkdir(parents=True, exist_ok=True)
        stale.touch()
    except Exception:
        pass

    return {"status": "appended", "id": node_id, "nodes": len(nodes)}


def _emit_question_kg(root: Path, slug: str, topic: str, stage: str, stage_version: int) -> dict[str, Any]:
    """Emit a Question node for qa-stage seed. For non-qa stages this is a no-op."""
    if stage != "qa" or not topic:
        return {"status": "skipped"}

    q_dir = root / "research" / "questions"
    q_dir.mkdir(parents=True, exist_ok=True)
    kg_path = q_dir / f"{slug}.kg.json"

    node_id = f"question:{slug}"
    ts = now_kst()
    payload = {
        "version": 1,
        "source_file": str((q_dir / f"{slug}.md").as_posix()),
        "source_sha": hashlib.sha256(topic.encode("utf-8")).hexdigest(),
        "extracted_at": ts,
        "author_agent": "loop_state.py",
        "nodes": [
            {
                "id": node_id,
                "type": "Question",
                "name": topic[:200],
                "meta": {
                    "text": topic,
                    "slug": slug,
                    "stage_version": stage_version,
                    "date": ts,
                },
            }
        ],
        "edges": [],
    }

    tmp = kg_path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(kg_path)

    try:
        stale = root / "papers" / "vector_db" / "kg.stale"
        stale.parent.mkdir(parents=True, exist_ok=True)
        stale.touch()
    except Exception:
        pass

    return {"status": "emitted", "id": node_id, "path": str(kg_path.relative_to(root))}


# ------------------------------------------------------- stage transitions

def _push_history(state: dict[str, Any], event: str) -> None:
    state.setdefault("history", []).append({
        "stage": state.get("stage"),
        "slug": state.get("slug"),
        "stage_version": state.get("stage_version"),
        "inner_phase": state.get("inner_phase"),
        "sub_phase": state.get("sub_phase"),
        "event": event,
        "at": now_kst(),
    })


def cmd_stage_enter(args: argparse.Namespace) -> int:
    """idle → <stage> with a new version. Phase A.

    Required: --stage, --slug (or --topic to derive one).
    """
    if args.stage not in STAGES:
        raise SystemExit(f"stage-enter: --stage must be one of {STAGES}")

    root = find_root(args.root)
    state_path = root / "research" / "loop_state.json"
    state = load_state(state_path)

    current_stage = state.get("stage") or IDLE
    if current_stage != IDLE and not args.force:
        print(json.dumps({
            "status": "busy",
            "stage": current_stage,
            "inner_phase": state.get("inner_phase"),
            "sub_phase": state.get("sub_phase"),
            "slug": state.get("slug"),
            "stage_version": state.get("stage_version"),
            "hint": "run stage-complete first, or pass --force to override",
        }, ensure_ascii=False, indent=2))
        return 2

    slug = args.slug
    topic = (args.topic or "").strip()
    if not slug and topic:
        date = datetime.now(KST).strftime("%Y-%m-%d")
        slug = f"{date}_{slugify(topic)}"
    if not slug:
        raise SystemExit("stage-enter: --slug or --topic is required")

    version = next_version(root, args.stage, slug)
    dirs = ensure_version_dirs(root, args.stage, slug, version)

    state.update({
        "stage": args.stage,
        "inner_phase": "A",
        "sub_phase": None,
        "slug": slug,
        "stage_version": version,
        "started_at": state.get("started_at") or now_kst(),
    })
    _push_history(state, "stage-enter")
    save_state(state_path, state)

    kg = _emit_loop_kg(root, state_path, state, event="stage-enter")
    qkg = _emit_question_kg(root, slug, topic, args.stage, version)

    print(json.dumps({
        "status": "stage-entered",
        "stage": args.stage,
        "slug": slug,
        "stage_version": version,
        "inner_phase": "A",
        "plan_dir": str(dirs["plan_dir"]),
        "report_dir": str(dirs["report_dir"]),
        "state_path": str(state_path),
        "kg": kg,
        "question_kg": qkg,
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_stage_advance(args: argparse.Namespace) -> int:
    """Advance inner_phase (A→B, B→C) or sub_phase forward within stage.

    If --to is given, it must be one of {"B","C"} (inner) or a sub-phase
    within the current stage. If omitted, auto-advance:
      A → B
      B → C (requires --trigger <phrase> matching whitelist, or --force)
      C → next sub-phase (or sub_phase=first when entering C)
    """
    root = find_root(args.root)
    state_path = root / "research" / "loop_state.json"
    state = load_state(state_path)

    stage = state.get("stage")
    if stage in (None, IDLE):
        raise SystemExit("stage-advance: not inside a stage; call stage-enter first")

    inner = state.get("inner_phase")
    sub = state.get("sub_phase")

    to = args.to

    # --- inner-phase transitions ------------------------------------------
    if to in ("B", "C") or (to is None and inner in ("A", "B")):
        # Enforce explicit --to targets strictly: do NOT silently rewrite the
        # target to whatever one-step transition happens to be legal from
        # `inner`. This prevents the A→C footgun where the caller intends
        # B→C (consuming a trigger) but current state is still A, which would
        # otherwise advance A→B and discard the trigger.
        if to == "B" and inner != "A":
            raise SystemExit(
                f"stage-advance --to B: only valid from inner_phase='A' "
                f"(current={inner!r}). Valid sequence: A → B → C."
            )
        if to == "C" and inner != "B":
            raise SystemExit(
                f"stage-advance --to C: only valid from inner_phase='B' "
                f"(current={inner!r}). Advance A → B first, then B → C with "
                "--trigger <phrase>. Valid sequence: A → B → C."
            )

        if inner == "A":
            # A → B: free.
            state["inner_phase"] = "B"
            state["sub_phase"] = None
            _push_history(state, "A->B")
        elif inner == "B":
            # B → C: requires a whitelisted trigger phrase unless --force.
            if not args.force:
                phrase = args.trigger or ""
                if not is_trigger_phrase(phrase):
                    raise SystemExit(
                        "stage-advance: B → C requires --trigger <phrase> "
                        f"matching the whitelist {sorted(TRIGGER_WHITELIST)}. "
                        "Pass --force to override."
                    )
            state["inner_phase"] = "C"
            # Start C at the first sub-phase of this stage.
            first_sub = STAGE_SUBPHASES[stage][0]
            state["sub_phase"] = first_sub
            _push_history(state, "B->C")
        else:
            raise SystemExit(
                f"stage-advance: cannot inner-advance from inner_phase={inner!r}"
            )

        save_state(state_path, state)
        kg = _emit_loop_kg(root, state_path, state, event="inner-advance")
        print(json.dumps({
            "status": "inner-advanced",
            "stage": stage,
            "slug": state.get("slug"),
            "stage_version": state.get("stage_version"),
            "inner_phase": state["inner_phase"],
            "sub_phase": state.get("sub_phase"),
            "kg": kg,
        }, ensure_ascii=False, indent=2))
        return 0

    # --- sub-phase transitions (inner_phase must be C) --------------------
    if inner != "C":
        raise SystemExit(
            f"stage-advance: sub-phase advance requires inner_phase='C' "
            f"(current={inner!r}). Run `stage-advance --to C --trigger <phrase>` first."
        )

    sps = STAGE_SUBPHASES[stage]
    if to:
        if to not in sps:
            raise SystemExit(
                f"stage-advance: sub-phase {to!r} is not valid for stage {stage!r} "
                f"(allowed: {sps})"
            )
        target = to
    else:
        if sub is None:
            target = sps[0]
        else:
            if sub not in sps:
                raise SystemExit(
                    f"stage-advance: current sub_phase {sub!r} not in stage {stage!r}"
                )
            idx = sps.index(sub)
            if idx + 1 >= len(sps):
                raise SystemExit(
                    f"stage-advance: already at last sub-phase {sub!r} of stage {stage!r}. "
                    f"Call stage-complete next."
                )
            target = sps[idx + 1]

    # Guard: only allow forward movement by 1 step unless --force.
    if sub is not None and not args.force:
        if sub in sps:
            idx = sps.index(sub)
            if sps.index(target) != idx + 1:
                raise SystemExit(
                    f"stage-advance: non-sequential sub-phase jump {sub!r} → {target!r} "
                    f"requires --force"
                )

    state["sub_phase"] = target
    _push_history(state, "sub-advance")
    save_state(state_path, state)
    kg = _emit_loop_kg(root, state_path, state, event="sub-advance")
    print(json.dumps({
        "status": "sub-advanced",
        "stage": stage,
        "slug": state.get("slug"),
        "stage_version": state.get("stage_version"),
        "inner_phase": "C",
        "sub_phase": target,
        "kg": kg,
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_stage_complete(args: argparse.Namespace) -> int:
    """<stage>.C (last sub) → completed → idle."""
    root = find_root(args.root)
    state_path = root / "research" / "loop_state.json"
    state = load_state(state_path)

    stage = state.get("stage")
    if stage in (None, IDLE):
        raise SystemExit("stage-complete: no active stage")

    inner = state.get("inner_phase")
    sub = state.get("sub_phase")
    if inner != "C" and not args.force:
        raise SystemExit(
            f"stage-complete: inner_phase must be 'C' to complete (current={inner!r}). "
            "Pass --force to override."
        )
    sps = STAGE_SUBPHASES.get(stage, [])
    if sub and sub != sps[-1] and not args.force:
        raise SystemExit(
            f"stage-complete: sub_phase is {sub!r} but stage {stage!r} expects "
            f"last={sps[-1]!r}. Pass --force to override."
        )

    # Record the completion, then reset to idle.
    state["inner_phase"] = "completed"
    _push_history(state, "stage-completed")
    save_state(state_path, state)
    _emit_loop_kg(root, state_path, state, event="stage-completed")

    done_stage = state.get("stage")
    done_slug = state.get("slug")
    done_version = state.get("stage_version")

    state.update({
        "stage": IDLE,
        "inner_phase": None,
        "sub_phase": None,
        # Keep slug so subsequent /research-status can still reference it.
        # Callers who truly want a clean slate can pass --reset-slug.
        "stage_version": None,
    })
    if getattr(args, "reset_slug", False):
        state["slug"] = None
    _push_history(state, "idle")
    save_state(state_path, state)
    kg = _emit_loop_kg(root, state_path, state, event="idle")

    print(json.dumps({
        "status": "stage-completed",
        "stage": done_stage,
        "slug": done_slug,
        "stage_version": done_version,
        "now": {"stage": IDLE, "inner_phase": None, "sub_phase": None},
        "kg": kg,
    }, ensure_ascii=False, indent=2))
    return 0


def cmd_stage_restart(args: argparse.Namespace) -> int:
    """Move inner_phase backward within the current stage (same version).

    --to A: replanning (resets sub_phase=None, inner_phase=A)
    --to B: re-alignment (resets sub_phase=None, inner_phase=B)
    """
    root = find_root(args.root)
    state_path = root / "research" / "loop_state.json"
    state = load_state(state_path)

    if state.get("stage") in (None, IDLE):
        raise SystemExit("stage-restart: no active stage")
    if args.to not in ("A", "B"):
        raise SystemExit("stage-restart: --to must be 'A' or 'B'")

    state["inner_phase"] = args.to
    state["sub_phase"] = None
    _push_history(state, f"restart-to-{args.to}")
    save_state(state_path, state)
    kg = _emit_loop_kg(root, state_path, state, event=f"restart-{args.to}")
    print(json.dumps({
        "status": "restarted",
        "stage": state.get("stage"),
        "slug": state.get("slug"),
        "stage_version": state.get("stage_version"),
        "inner_phase": args.to,
        "kg": kg,
    }, ensure_ascii=False, indent=2))
    return 0


# ------------------------------------------------------------------ history

def cmd_history(args: argparse.Namespace) -> int:
    root = find_root(args.root)
    state_path = root / "research" / "loop_state.json"
    state = load_state(state_path)
    entry = {
        "stage": state.get("stage"),
        "slug": state.get("slug"),
        "stage_version": state.get("stage_version"),
        "inner_phase": state.get("inner_phase"),
        "sub_phase": state.get("sub_phase"),
        "event": args.event,
        "outcome": args.outcome,
        "note": args.note or "",
        "at": now_kst(),
    }
    state.setdefault("history", []).append(entry)
    save_state(state_path, state)
    print(json.dumps({"status": "logged", "entry": entry}, ensure_ascii=False, indent=2))
    return 0


# ------------------------------------------------------------------ show

def cmd_show(args: argparse.Namespace) -> int:
    root = find_root(args.root)
    state_path = root / "research" / "loop_state.json"
    state = load_state(state_path)
    print(json.dumps(state, ensure_ascii=False, indent=2))
    return 0


# ------------------------------------------------------------------ status

def _slug_artifacts(root: Path, slug: str | None) -> dict[str, Any]:
    if not slug:
        return {}
    out: dict[str, Any] = {}
    answer_glob = list((root / "research" / "answers").glob(f"*_{slug}.md")) if (root / "research" / "answers").is_dir() else []
    out["answer"] = [str(p.relative_to(root)) for p in answer_glob]
    out["critique"] = str((root / "research" / "critiques" / f"{slug}.md").relative_to(root)) if (root / "research" / "critiques" / f"{slug}.md").is_file() else None
    out["plan_experiments"] = str((root / "research" / "plans" / slug / "PLAN.md").relative_to(root)) if (root / "research" / "plans" / slug / "PLAN.md").is_file() else None
    out["impl_map"] = str((root / "experiments" / slug / "IMPL_MAP.md").relative_to(root)) if (root / "experiments" / slug / "IMPL_MAP.md").is_file() else None
    out["results_dir"] = str((root / f"results_{slug}").relative_to(root)) if (root / f"results_{slug}").is_dir() else None
    out["diagnosis"] = str((root / "research" / "diagnoses" / f"{slug}.md").relative_to(root)) if (root / "research" / "diagnoses" / f"{slug}.md").is_file() else None

    # Per-stage plan/report versions (v3 versioning).
    versions: dict[str, Any] = {}
    for stage in STAGES:
        vs = scan_existing_versions(root, stage, slug)
        if vs:
            versions[stage] = {
                "all": vs,
                "latest": vs[-1],
                "plan_path": str((root / "research" / "plans" / stage / slug / f"v{vs[-1]}" / "PLAN.md").relative_to(root))
                    if (root / "research" / "plans" / stage / slug / f"v{vs[-1]}" / "PLAN.md").is_file() else None,
                "report_path": str((root / "research" / "reports" / stage / slug / f"v{vs[-1]}" / "Report.md").relative_to(root))
                    if (root / "research" / "reports" / stage / slug / f"v{vs[-1]}" / "Report.md").is_file() else None,
            }
    out["stage_versions"] = versions
    return out


def _kg_status(root: Path) -> dict[str, Any]:
    kg_dir = root / "papers" / "vector_db"
    db_path = kg_dir / "kg.sqlite"
    stale_path = kg_dir / "kg.stale"
    manifest_path = kg_dir / "kg-manifest.json"
    rejected_path = kg_dir / "rejected.jsonl"
    schema_version_path = kg_dir / "schema.version"

    out: dict[str, Any] = {
        "db_exists": db_path.is_file(),
        "stale": stale_path.is_file(),
        "nodes": 0,
        "edges": 0,
        "by_type": {},
        "files_tracked": 0,
        "last_upsert": None,
        "rejected_count": 0,
        "schema_version": None,
    }

    if schema_version_path.is_file():
        try:
            out["schema_version"] = schema_version_path.read_text(encoding="utf-8").strip()
        except Exception:
            pass

    if manifest_path.is_file():
        try:
            m = json.loads(manifest_path.read_text(encoding="utf-8"))
            out["files_tracked"] = len(m.get("files", {}))
            out["last_upsert"] = m.get("last_update")
        except Exception as e:
            out["manifest_error"] = str(e)

    if rejected_path.is_file():
        try:
            with rejected_path.open(encoding="utf-8") as fh:
                out["rejected_count"] = sum(1 for _ in fh)
        except Exception:
            pass

    if db_path.is_file():
        try:
            import sqlite3

            conn = sqlite3.connect(str(db_path))
            try:
                out["nodes"] = conn.execute("SELECT COUNT(*) FROM nodes").fetchone()[0]
                out["edges"] = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
                rows = conn.execute(
                    "SELECT type, COUNT(*) FROM nodes GROUP BY type ORDER BY type"
                ).fetchall()
                out["by_type"] = {r[0]: r[1] for r in rows}
            finally:
                conn.close()
        except Exception as e:
            out["db_error"] = str(e)

    return out


def cmd_status(args: argparse.Namespace) -> int:
    root = find_root(args.root)
    state_path = root / "research" / "loop_state.json"
    rag_dir = root / "papers" / "vector_db"
    manifest_path = rag_dir / "manifest.json"
    stale_flag = rag_dir / "rag.stale"

    state = load_state(state_path)

    if getattr(args, "short", False):
        stage = state.get("stage") or IDLE
        inner = state.get("inner_phase") or "-"
        sub = state.get("sub_phase") or "-"
        slug = state.get("slug") or "-"
        ver = state.get("stage_version")
        ver_s = f"v{ver}" if ver else "-"
        print(f"{stage} {ver_s} {inner}/{sub} {slug}")
        return 0

    report: dict[str, Any] = {
        "root": str(root),
        "loop": {
            "stage": state.get("stage"),
            "inner_phase": state.get("inner_phase"),
            "sub_phase": state.get("sub_phase"),
            "slug": state.get("slug"),
            "stage_version": state.get("stage_version"),
            "started_at": state.get("started_at"),
            "last_update": state.get("last_update"),
            "history_tail": state.get("history", [])[-3:],
        },
        "rag": {
            "manifest_exists": manifest_path.is_file(),
            "stale": stale_flag.is_file(),
        },
        "kg": _kg_status(root),
        "artifacts": _slug_artifacts(root, state.get("slug")),
    }

    if manifest_path.is_file():
        try:
            m = json.loads(manifest_path.read_text(encoding="utf-8"))
            files = m.get("files", {})
            report["rag"]["files_tracked"] = len(files)
            report["rag"]["chunks_tracked"] = sum(f.get("chunks", 0) for f in files.values())
            report["rag"]["last_update"] = m.get("last_update")
            report["rag"]["embed_model"] = m.get("embed_model")
        except Exception as e:
            report["rag"]["manifest_error"] = str(e)

    lessons_dir = root / "docs"
    lessons: dict[str, int] = {}
    for name in ("lessons", "lessons-paper", "lessons-research", "lessons-impl", "lessons-analysis"):
        f = lessons_dir / f"{name}.md"
        if f.is_file():
            try:
                txt = f.read_text(encoding="utf-8")
                lessons[name] = len(re.findall(r"^## \d{4}-\d{2}-\d{2}", txt, re.MULTILINE))
            except Exception:
                lessons[name] = -1
    report["lessons"] = lessons

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


# ------------------------------------------------------------------ trigger-check

def cmd_trigger_check(args: argparse.Namespace) -> int:
    """Utility: return exit 0 if the phrase is a valid trigger, else 2."""
    ok = is_trigger_phrase(args.phrase)
    print(json.dumps({
        "phrase": args.phrase,
        "is_trigger": ok,
        "whitelist": sorted(TRIGGER_WHITELIST),
    }, ensure_ascii=False, indent=2))
    return 0 if ok else 2


# ------------------------------------------------------------------ main

def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=None)
    sub = ap.add_subparsers(dest="cmd", required=True)

    # stage-enter
    s = sub.add_parser("stage-enter", help="idle → <stage>")
    s.add_argument("--stage", required=True, choices=STAGES)
    s.add_argument("--slug", default=None)
    s.add_argument("--topic", default=None, help="free-text; used to derive slug if --slug absent")
    s.add_argument("--force", action="store_true", help="override busy-stage guard")
    s.set_defaults(func=cmd_stage_enter)

    # stage-advance
    s = sub.add_parser("stage-advance", help="advance inner phase or sub-phase")
    s.add_argument("--to", default=None, help="'B', 'C', or a valid sub-phase of the current stage")
    s.add_argument("--trigger", default=None, help="trigger phrase for B → C (must be whitelisted)")
    s.add_argument("--force", action="store_true", help="bypass trigger/sequence guards")
    s.set_defaults(func=cmd_stage_advance)

    # stage-complete
    s = sub.add_parser("stage-complete", help="close the current stage → idle")
    s.add_argument("--force", action="store_true")
    s.add_argument("--reset-slug", action="store_true", help="also clear slug (default keeps it for status)")
    s.set_defaults(func=cmd_stage_complete)

    # stage-restart
    s = sub.add_parser("stage-restart", help="move inner phase backward within current stage")
    s.add_argument("--to", required=True, choices=["A", "B"])
    s.set_defaults(func=cmd_stage_restart)

    # status / show / history
    s = sub.add_parser("status", help="consolidated status report")
    s.add_argument("--short", action="store_true", help="one-line statusLine summary")
    s.set_defaults(func=cmd_status)

    s = sub.add_parser("show", help="dump loop_state.json")
    s.set_defaults(func=cmd_show)

    s = sub.add_parser("history", help="append a free-form history entry")
    s.add_argument("--event", required=True)
    s.add_argument("--outcome", default="")
    s.add_argument("--note", default="")
    s.set_defaults(func=cmd_history)

    # trigger-check (helper for orchestrator / tests)
    s = sub.add_parser("trigger-check", help="test if a phrase is in the trigger whitelist")
    s.add_argument("phrase")
    s.set_defaults(func=cmd_trigger_check)

    return ap


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
