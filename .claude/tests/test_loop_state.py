#!/usr/bin/env python3
"""Unit tests for loop_state.py v3.

Run: python3 .claude/tests/test_loop_state.py

Exercises:
  - empty state defaults to v3 idle
  - stage-enter allocates v1 on first call, v2 on second
  - stage-advance A→B is free
  - stage-advance B→C requires a trigger phrase
  - sub-phase advance is sequential within STAGE_SUBPHASES
  - stage-complete resets to idle
  - migrate_to_v3 converts legacy schemas without data loss
  - is_trigger_phrase whitelist behavior
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
from pathlib import Path

# Import from sibling .claude/scripts/ directory (loop_state.py lives there).
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "scripts"))

import loop_state as ls  # noqa: E402


def _mk_root(tmp: Path) -> Path:
    """Create a minimal research_hub-like tree."""
    root = tmp / "research_hub"
    (root / "research").mkdir(parents=True)
    (root / "papers").mkdir(parents=True)
    (root / "papers" / "kg").mkdir(parents=True)
    return root


def test_empty_state_is_v3() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = _mk_root(Path(td))
        sp = root / "research" / "loop_state.json"
        st = ls.load_state(sp)
        assert st["version"] == 3, st
        assert st["stage"] == "idle", st
        assert st["inner_phase"] is None, st
        assert st["sub_phase"] is None, st
        assert st["stage_version"] is None, st
    print("[ok] empty_state_is_v3")


def test_is_trigger_phrase() -> None:
    assert ls.is_trigger_phrase("구현해줘")
    assert ls.is_trigger_phrase("  proceed  ")
    assert ls.is_trigger_phrase("GO AHEAD")
    assert ls.is_trigger_phrase("run it")
    assert not ls.is_trigger_phrase("maybe")
    assert not ls.is_trigger_phrase("")
    assert not ls.is_trigger_phrase("그만")
    print("[ok] is_trigger_phrase")


def test_scan_versions_empty() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = _mk_root(Path(td))
        assert ls.scan_existing_versions(root, "papers", "nope") == []
        assert ls.next_version(root, "papers", "nope") == 1
    print("[ok] scan_versions_empty")


def test_stage_enter_and_versioning() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = _mk_root(Path(td))
        sp = root / "research" / "loop_state.json"
        st = ls.load_state(sp)
        assert st["stage"] == "idle"

        # First enter: v1
        v = ls.next_version(root, "papers", "dpo-test")
        assert v == 1
        dirs = ls.ensure_version_dirs(root, "papers", "dpo-test", v)
        assert dirs["plan_dir"].is_dir()
        # Write a dummy PLAN.md so v2 scan can see it.
        (dirs["plan_dir"] / "PLAN.md").write_text("# dummy\n")

        # Second enter for the same slug: v2
        v2 = ls.next_version(root, "papers", "dpo-test")
        assert v2 == 2, v2
        dirs2 = ls.ensure_version_dirs(root, "papers", "dpo-test", v2)
        assert dirs2["plan_dir"].name == "v2"
    print("[ok] stage_enter_and_versioning")


def test_inner_phase_advance_needs_trigger() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = _mk_root(Path(td))
        sp = root / "research" / "loop_state.json"
        state = ls.load_state(sp)
        state.update({
            "stage": "qa",
            "slug": "dpo-test",
            "stage_version": 1,
            "inner_phase": "A",
            "sub_phase": None,
        })
        ls.save_state(sp, state)

        # Simulate: A → B via cmd_stage_advance
        import argparse
        ns = argparse.Namespace(root=str(root), to="B", trigger=None, force=False)
        rc = ls.cmd_stage_advance(ns)
        assert rc == 0
        state = ls.load_state(sp)
        assert state["inner_phase"] == "B", state
        assert state["sub_phase"] is None, state

        # B → C without a trigger phrase: must fail.
        ns = argparse.Namespace(root=str(root), to="C", trigger=None, force=False)
        try:
            ls.cmd_stage_advance(ns)
        except SystemExit as e:
            assert "trigger" in str(e).lower() or "whitelist" in str(e).lower()
        else:
            raise AssertionError("B→C without trigger must fail")

        # B → C with whitelisted trigger: OK.
        ns = argparse.Namespace(root=str(root), to="C", trigger="구현해줘", force=False)
        rc = ls.cmd_stage_advance(ns)
        assert rc == 0
        state = ls.load_state(sp)
        assert state["inner_phase"] == "C", state
        assert state["sub_phase"] == "B-1", state  # qa starts at B-1
    print("[ok] inner_phase_advance_needs_trigger")


def test_sub_phase_sequential() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = _mk_root(Path(td))
        sp = root / "research" / "loop_state.json"
        state = ls.load_state(sp)
        state.update({
            "stage": "papers",
            "slug": "x",
            "stage_version": 1,
            "inner_phase": "C",
            "sub_phase": "A-1",
        })
        ls.save_state(sp, state)

        import argparse
        # A-1 → A-2 (auto)
        ns = argparse.Namespace(root=str(root), to=None, trigger=None, force=False)
        ls.cmd_stage_advance(ns)
        state = ls.load_state(sp)
        assert state["sub_phase"] == "A-2", state

        # Skip A-3 → A-4 without force: must fail.
        ns = argparse.Namespace(root=str(root), to="A-4", trigger=None, force=False)
        try:
            ls.cmd_stage_advance(ns)
        except SystemExit as e:
            assert "non-sequential" in str(e).lower() or "force" in str(e).lower()
        else:
            raise AssertionError("non-sequential jump must fail without --force")

        # A-2 → A-3 (explicit, sequential)
        ns = argparse.Namespace(root=str(root), to="A-3", trigger=None, force=False)
        ls.cmd_stage_advance(ns)
        state = ls.load_state(sp)
        assert state["sub_phase"] == "A-3"
    print("[ok] sub_phase_sequential")


def test_stage_complete() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = _mk_root(Path(td))
        sp = root / "research" / "loop_state.json"
        state = ls.load_state(sp)
        state.update({
            "stage": "analyze",
            "slug": "x",
            "stage_version": 1,
            "inner_phase": "C",
            "sub_phase": "F-2",  # last sub-phase of analyze
        })
        ls.save_state(sp, state)

        import argparse
        ns = argparse.Namespace(root=str(root), force=False, reset_slug=False)
        rc = ls.cmd_stage_complete(ns)
        assert rc == 0
        state = ls.load_state(sp)
        assert state["stage"] == "idle", state
        assert state["inner_phase"] is None, state
        assert state["sub_phase"] is None, state
        assert state["stage_version"] is None, state
        assert state["slug"] == "x", state  # preserved by default
    print("[ok] stage_complete")


def test_migrate_v1_to_v3() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = _mk_root(Path(td))
        sp = root / "research" / "loop_state.json"
        legacy = {
            "version": 1,
            "iteration": 3,
            "phase": "E-2",
            "current_slug": "old-slug",
            "started_at": "2026-01-01T00:00:00+09:00",
            "last_update": "2026-01-02T00:00:00+09:00",
            "history": [{"iteration": 3, "phase_entered": "E-2", "at": "x"}],
        }
        sp.parent.mkdir(parents=True, exist_ok=True)
        sp.write_text(json.dumps(legacy), encoding="utf-8")

        state = ls.load_state(sp)
        assert state["version"] == 3, state
        assert state["stage"] == "experiments", state  # E-2 lives in experiments
        assert state["inner_phase"] == "C", state
        assert state["sub_phase"] == "E-2", state
        assert state["slug"] == "old-slug", state
        assert state["stage_version"] == 1, state
        assert "iteration" not in state, state
        bak = sp.with_name("loop_state.v1.bak.json")
        assert bak.is_file(), "v1 backup must exist"
    print("[ok] migrate_v1_to_v3")


def test_migrate_v2_to_v3_done_phase() -> None:
    with tempfile.TemporaryDirectory() as td:
        root = _mk_root(Path(td))
        sp = root / "research" / "loop_state.json"
        legacy = {
            "version": 2,
            "iteration": 1,
            "phase": "done",
            "current_slug": "x",
            "started_at": "2026-01-01T00:00:00+09:00",
            "last_update": "2026-01-02T00:00:00+09:00",
            "history": [],
        }
        sp.parent.mkdir(parents=True, exist_ok=True)
        sp.write_text(json.dumps(legacy), encoding="utf-8")

        state = ls.load_state(sp)
        assert state["version"] == 3, state
        assert state["stage"] == "idle", state  # phase=done → idle
        assert state["slug"] == "x", state
        assert "iteration" not in state
    print("[ok] migrate_v2_to_v3_done_phase")


def run_all() -> int:
    tests = [
        test_empty_state_is_v3,
        test_is_trigger_phrase,
        test_scan_versions_empty,
        test_stage_enter_and_versioning,
        test_inner_phase_advance_needs_trigger,
        test_sub_phase_sequential,
        test_stage_complete,
        test_migrate_v1_to_v3,
        test_migrate_v2_to_v3_done_phase,
    ]
    for t in tests:
        t()
    print(f"\nAll {len(tests)} tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(run_all())
