"""Tests for .claude/scripts/verify_sub_phase.py — Task 1/13: unknown guard."""

import os
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify_sub_phase.py"


def run(args, root, check=False):
    env = os.environ.copy()
    env["RESEARCH_HUB_ROOT"] = str(root)
    return subprocess.run(
        [sys.executable, str(SCRIPT)] + args,
        capture_output=True,
        text=True,
        env=env,
        check=check,
    )


def test_T8_unknown_sub_phase(tmp_path):
    result = run(["verify", "BOGUS", "--slug", "x"], tmp_path)
    assert result.returncode == 2
    assert "unknown sub_phase" in result.stderr.lower()


def _mk(root: Path, rel: str, body: str = "x") -> Path:
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body)
    return p


def test_T1_default_ok(tmp_path):
    # snapshot B-1 → write research/answers/x.md → verify
    (tmp_path / "research/answers").mkdir(parents=True)
    snap = run(["snapshot", "B-1", "--slug", "demo"], tmp_path)
    assert snap.returncode == 0, snap.stderr
    _mk(tmp_path, "research/answers/2026-04-19_demo.md")
    ver = run(["verify", "B-1", "--slug", "demo"], tmp_path)
    assert ver.returncode == 0, ver.stderr
    assert "B-1: OK" in ver.stdout


def test_T2_default_fail(tmp_path):
    (tmp_path / "research/answers").mkdir(parents=True)
    run(["snapshot", "B-1", "--slug", "demo"], tmp_path, check=True)
    # no artifact written
    ver = run(["verify", "B-1", "--slug", "demo"], tmp_path)
    assert ver.returncode == 9
    assert "did not emit an answer file" in ver.stderr


def test_T_mtime_ok(tmp_path):
    # A-4 uses mode=mtime on papers/vector_db/manifest.json
    manifest = tmp_path / "papers/vector_db/manifest.json"
    manifest.parent.mkdir(parents=True)
    manifest.write_text("{}")
    old = manifest.stat().st_mtime - 10
    os.utime(manifest, (old, old))
    run(["snapshot", "A-4", "--slug", "demo"], tmp_path, check=True)
    manifest.write_text('{"files": {"a": "h"}}')  # touches mtime to now
    ver = run(["verify", "A-4", "--slug", "demo"], tmp_path)
    assert ver.returncode == 0, ver.stderr


def test_T_mtime_fail(tmp_path):
    manifest = tmp_path / "papers/vector_db/manifest.json"
    manifest.parent.mkdir(parents=True)
    manifest.write_text("{}")
    run(["snapshot", "A-4", "--slug", "demo"], tmp_path, check=True)
    # do not touch manifest
    ver = run(["verify", "A-4", "--slug", "demo"], tmp_path)
    assert ver.returncode == 7
    assert "did not grow manifest" in ver.stderr


def test_T_E1_extra_required(tmp_path):
    code_dir = tmp_path / "experiments/demo/code"
    code_dir.mkdir(parents=True)
    run(["snapshot", "E-1", "--slug", "demo"], tmp_path, check=True)
    (code_dir / "run.py").write_text("print(1)")
    # Missing IMPL_MAP.md → fail
    ver = run(["verify", "E-1", "--slug", "demo"], tmp_path)
    assert ver.returncode == 12
    assert "IMPL_MAP" in ver.stderr
    # Now add IMPL_MAP and re-snapshot+verify
    (tmp_path / "experiments/demo/IMPL_MAP.md").write_text("# map")
    run(["snapshot", "E-1", "--slug", "demo"], tmp_path, check=True)
    (code_dir / "another.py").write_text("x")
    ver2 = run(["verify", "E-1", "--slug", "demo"], tmp_path)
    assert ver2.returncode == 0, ver2.stderr


def test_T6_E2_no_new_ok(tmp_path):
    (tmp_path / "experiments/demo").mkdir(parents=True)
    run(["snapshot", "E-2", "--slug", "demo"], tmp_path, check=True)
    ver = run(["verify", "E-2", "--slug", "demo"], tmp_path)
    assert ver.returncode == 0, ver.stderr


def test_T6b_E2_no_new_fail(tmp_path):
    (tmp_path / "experiments/demo").mkdir(parents=True)
    run(["snapshot", "E-2", "--slug", "demo"], tmp_path, check=True)
    (tmp_path / "experiments/demo/qa_fail_20260419.md").write_text("fail")
    ver = run(["verify", "E-2", "--slug", "demo"], tmp_path)
    assert ver.returncode == 13
    assert "emitted qa_fail" in ver.stderr


def _write_review(root: Path, rel: str, verdict: str | None):
    fm = f"---\nverdict: {verdict}\n---\nbody\n" if verdict else "---\nno verdict\n---\nbody\n"
    p = root / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(fm)


def test_T3_E3_approve(tmp_path):
    run(["snapshot", "E-3", "--slug", "demo"], tmp_path, check=True)
    _write_review(tmp_path, "research/reviews/experiments_demo_codex_review.md", "approve")
    ver = run(["verify", "E-3", "--slug", "demo"], tmp_path)
    assert ver.returncode == 0, ver.stderr
    assert "verdict: approve" in ver.stdout


def test_T4_E3_reject(tmp_path):
    # reject is not a script failure — exit 0 and print verdict for main-session Stop-rule
    run(["snapshot", "E-3", "--slug", "demo"], tmp_path, check=True)
    _write_review(tmp_path, "research/reviews/experiments_demo_codex_review.md", "reject")
    ver = run(["verify", "E-3", "--slug", "demo"], tmp_path)
    assert ver.returncode == 0, ver.stderr
    assert "verdict: reject" in ver.stdout


def test_T5_E3_missing_verdict(tmp_path):
    run(["snapshot", "E-3", "--slug", "demo"], tmp_path, check=True)
    _write_review(tmp_path, "research/reviews/experiments_demo_codex_review.md", None)
    ver = run(["verify", "E-3", "--slug", "demo"], tmp_path)
    assert ver.returncode == 14
    assert "(E-3)" in ver.stderr


def test_T7_A3_batch(tmp_path):
    ms = tmp_path / "papers/marp-summary"
    ms.mkdir(parents=True)
    # Batch 0
    run(["snapshot", "A-3", "--slug", "demo", "--batch-i", "0"],
        tmp_path, check=True)
    (ms / "p1.md").write_text("x")
    v0 = run(["verify", "A-3", "--slug", "demo", "--batch-i", "0"], tmp_path)
    assert v0.returncode == 0, v0.stderr
    # Batch 1
    run(["snapshot", "A-3", "--slug", "demo", "--batch-i", "1"],
        tmp_path, check=True)
    (ms / "p2.md").write_text("x")
    v1 = run(["verify", "A-3", "--slug", "demo", "--batch-i", "1"], tmp_path)
    assert v1.returncode == 0, v1.stderr
    # Per-batch snapshots are independent files
    assert Path("/tmp/.verify_A-3_demo_b0.json").exists()
    assert Path("/tmp/.verify_A-3_demo_b1.json").exists()
