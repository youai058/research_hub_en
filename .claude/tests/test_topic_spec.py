#!/usr/bin/env python3
"""Unit tests for topic_spec.py.

Run: python3 .claude/tests/test_topic_spec.py
"""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parent / "skills" / "topic-refine" / "scripts" / "topic_spec.py"


def _valid_payload() -> dict:
    return {
        "version": 1,
        "created": "2026-04-16T19:30:00+09:00",
        "raw_input": "Diffusion LLM analysis papers",
        "refined_topic": "Collect papers analyzing Diffusion LM training/sampling",
        "triage_context": {
            "core_question": "Is this a Diffusion LM analysis paper?",
            "include": ["Discrete/masked diffusion applied to text generation"],
            "exclude": ["Image/audio diffusion"],
            "signal_methods": ["MDLM", "LLaDA"],
        },
        "keyword_groups": [
            ["diffusion language model", "diffusion LLM"],
            ["discrete diffusion", "masked diffusion"],
        ],
        "scope": {
            "venues": ["NeurIPS", "ICLR"],
            "years": [2026, 2025, 2024],
            "include_arxiv": False,
        },
        "clarity_scores": {"scope": 0.8, "triage": 0.7, "keywords": 0.75},
        "termination_reason": "floor",
        "interview_rounds": 3,
        "interview_log": [],
    }


def _run(args: list[str], stdin: str | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        input=stdin,
        capture_output=True,
        text=True,
    )


def test_validate_ok() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(_valid_payload(), f)
        path = f.name
    res = _run(["validate", path])
    assert res.returncode == 0, f"validate failed: {res.stderr}"


def test_validate_missing_top_level() -> None:
    payload = _valid_payload()
    del payload["triage_context"]
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(payload, f)
        path = f.name
    res = _run(["validate", path])
    assert res.returncode == 2
    assert "triage_context" in res.stderr


def test_validate_bad_clarity_range() -> None:
    payload = _valid_payload()
    payload["clarity_scores"]["scope"] = 1.5
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(payload, f)
        path = f.name
    res = _run(["validate", path])
    assert res.returncode == 2
    assert "scope" in res.stderr


def test_validate_bad_termination_reason() -> None:
    payload = _valid_payload()
    payload["termination_reason"] = "nope"
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(payload, f)
        path = f.name
    res = _run(["validate", path])
    assert res.returncode == 2
    assert "termination_reason" in res.stderr


def test_get_nested_field() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(_valid_payload(), f)
        path = f.name
    res = _run(["get", path, "triage_context.core_question"])
    assert res.returncode == 0, res.stderr
    assert res.stdout.strip() == "Is this a Diffusion LM analysis paper?"


def test_get_list_field_as_jsonl() -> None:
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(_valid_payload(), f)
        path = f.name
    res = _run(["get", path, "keyword_groups"])
    assert res.returncode == 0, res.stderr
    # list fields print as JSON so consumers can parse round-trip
    parsed = json.loads(res.stdout)
    assert parsed == [
        ["diffusion language model", "diffusion LLM"],
        ["discrete diffusion", "masked diffusion"],
    ]


def test_template_has_all_required_fields() -> None:
    res = _run(["template", "--raw-input", "foo"])
    assert res.returncode == 0, res.stderr
    tpl = json.loads(res.stdout)
    for key in [
        "version", "created", "raw_input", "refined_topic",
        "triage_context", "keyword_groups", "scope", "clarity_scores",
        "termination_reason", "interview_rounds", "interview_log",
    ]:
        assert key in tpl, f"template missing {key}"
    assert tpl["raw_input"] == "foo"


def test_report_builder_papers_body_includes_topic_json_fields() -> None:
    """report_builder.py papers body renders refined_topic + clarity_scores."""
    import importlib.util
    rb_path = HERE.parent / "scripts" / "report_builder.py"
    spec = importlib.util.spec_from_file_location("report_builder", rb_path)
    rb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rb)

    body = {
        "refined_topic": "Collect Diffusion LM analysis papers",
        "clarity_scores": {"scope": 0.85, "triage": 0.80, "keywords": 0.75},
        "interview_rounds": 3,
        "termination_reason": "floor",
        "collection_stats": {},
        "triage": {},
        "summarized": [],
        "rag_delta": {},
        "kg_delta": {},
    }
    out = rb._body_papers_md(body)
    assert "Collect Diffusion LM analysis papers" in out, "refined_topic not rendered"
    assert "0.85" in out and "0.80" in out and "0.75" in out, "clarity_scores not rendered"
    assert "floor" in out, "termination_reason not rendered"
    assert "3" in out, "interview_rounds not rendered"


def main() -> int:
    tests = [
        test_validate_ok,
        test_validate_missing_top_level,
        test_validate_bad_clarity_range,
        test_validate_bad_termination_reason,
        test_get_nested_field,
        test_get_list_field_as_jsonl,
        test_template_has_all_required_fields,
        test_report_builder_papers_body_includes_topic_json_fields,
    ]
    for t in tests:
        t()
        print(f"ok  {t.__name__}")
    print(f"{len(tests)} passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
