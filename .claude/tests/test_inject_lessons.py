# .claude/tests/test_inject_lessons.py
"""Tests for .claude/hooks/inject_lessons.sh (full/titles modes + fallbacks).

Each test builds a hermetic fixture tree in tmp_path and invokes the hook
script with RESEARCH_HUB_ROOT=tmp_path. This isolates the test from the
real repo's docs/lessons.md.
"""
from __future__ import annotations

import os
import subprocess
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
HOOK = REPO_ROOT / ".claude" / "hooks" / "inject_lessons.sh"


def _run(mode: str | None, root: Path) -> subprocess.CompletedProcess:
    cmd = [str(HOOK)] + ([mode] if mode is not None else [])
    env = {**os.environ, "RESEARCH_HUB_ROOT": str(root)}
    return subprocess.run(cmd, capture_output=True, text=True, env=env)


def _write_fixture(root: Path, lessons_body: str | None = None,
                   domains: dict[str, str] | None = None) -> None:
    docs = root / "docs"
    docs.mkdir(parents=True, exist_ok=True)
    if lessons_body is not None:
        (docs / "lessons.md").write_text(lessons_body, encoding="utf-8")
    for name, body in (domains or {}).items():
        (docs / f"{name}.md").write_text(body, encoding="utf-8")


THREE_ENTRIES = """# Lessons

## 2026-04-15 — Alpha Rule Title
- **Rule**: alpha rule body
- **Why**: alpha why
- **When to apply**: alpha when

## 2026-04-16 — Beta Rule Title
- **Rule**: beta rule body
- **Why**: beta why
- **When to apply**: beta when

## 2026-04-17 — Gamma Rule Title
- **Rule**: gamma rule body
- **Why**: gamma why
- **When to apply**: gamma when
"""


def test_t1_full_mode_emits_full_body(tmp_path: Path):
    _write_fixture(tmp_path, THREE_ENTRIES)
    r = _run("full", tmp_path)
    assert r.returncode == 0, r.stderr
    assert "**Rule**:" in r.stdout
    assert "**Why**:" in r.stdout
    assert "**When to apply**:" in r.stdout
    assert "global: 3 entries total, showing last 3" in r.stdout


def test_t2_titles_mode_emits_compact_titles(tmp_path: Path):
    _write_fixture(tmp_path, THREE_ENTRIES)
    r = _run("titles", tmp_path)
    assert r.returncode == 0, r.stderr
    assert "last 3 titles:" in r.stdout
    assert "- 2026-04-15: Alpha Rule Title" in r.stdout
    assert "- 2026-04-16: Beta Rule Title" in r.stdout
    assert "- 2026-04-17: Gamma Rule Title" in r.stdout
    # body labels must NOT leak into titles mode
    assert "**Why**:" not in r.stdout
    assert "**When to apply**:" not in r.stdout
    # but the closing pointer line should be there
    assert "(Read docs/lessons.md for full bodies)" in r.stdout


def test_t3_empty_arg_falls_back_to_full(tmp_path: Path):
    _write_fixture(tmp_path, THREE_ENTRIES)
    r = _run(None, tmp_path)  # no positional arg
    assert r.returncode == 0, r.stderr
    assert "**Rule**:" in r.stdout
    assert "**Why**:" in r.stdout


def test_t4_bogus_mode_warns_and_falls_back_to_full(tmp_path: Path):
    _write_fixture(tmp_path, THREE_ENTRIES)
    r = _run("bogus", tmp_path)
    assert r.returncode == 0, r.stderr
    assert "unknown mode 'bogus'" in r.stderr
    # stdout still emits full body
    assert "**Rule**:" in r.stdout
    assert "**Why**:" in r.stdout


def test_t5_missing_lessons_md(tmp_path: Path):
    # Do not write lessons.md. Do create docs/ so ROOT is valid.
    (tmp_path / "docs").mkdir()
    r = _run("titles", tmp_path)
    assert r.returncode == 0, r.stderr
    assert "global: (docs/lessons.md missing)" in r.stdout


def test_t7_domain_counts_emitted_in_both_modes(tmp_path: Path):
    domains = {
        "lessons-paper":    "## 2026-01-01 — e1\nbody\n\n## 2026-01-02 — e2\nbody\n",
        "lessons-research": "## 2026-01-01 — e1\nbody\n",
        "lessons-impl":     "",
        "lessons-analysis": "## 2026-01-01 — e1\nbody\n## 2026-01-02 — e2\nbody\n## 2026-01-03 — e3\nbody\n",
    }
    _write_fixture(tmp_path, THREE_ENTRIES, domains)
    for mode in ("full", "titles"):
        r = _run(mode, tmp_path)
        assert r.returncode == 0, r.stderr
        assert "lessons-paper: 2 entries" in r.stdout, f"mode={mode}"
        assert "lessons-research: 1 entries" in r.stdout, f"mode={mode}"
        assert "lessons-impl: 0 entries" in r.stdout, f"mode={mode}"
        assert "lessons-analysis: 3 entries" in r.stdout, f"mode={mode}"


NO_DASH_ENTRIES = """# Lessons

## 2026-05-01
Body paragraph without em-dash heading.

## 2026-05-02 - ascii dash title
Body.

## 2026-05-03 — proper em-dash title
Body.
"""


def test_t6_heading_without_em_dash(tmp_path: Path):
    _write_fixture(tmp_path, NO_DASH_ENTRIES)
    r = _run("titles", tmp_path)
    assert r.returncode == 0, r.stderr
    # date-only heading should still produce a line (no trailing colon garbage)
    assert "- 2026-05-01" in r.stdout
    # ascii dash is accepted as separator
    assert "- 2026-05-02: ascii dash title" in r.stdout
    # em-dash path still works
    assert "- 2026-05-03: proper em-dash title" in r.stdout
