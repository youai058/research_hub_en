#!/usr/bin/env python3
"""Topic spec validator / loader / template generator.

Used by topic-refine skill (main session) and by paper-triage when given
`--topic-spec <path>`. Schema is defined inline (no jsonschema dep).
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

UTC = timezone.utc
VALID_TERMINATION = {"floor", "plateau", "ceiling", "user_early_exit"}
REQUIRED_TOP = [
    "version", "created", "raw_input", "refined_topic",
    "triage_context", "keyword_groups", "scope", "clarity_scores",
    "termination_reason", "interview_rounds", "interview_log",
]
REQUIRED_TRIAGE = ["core_question", "include", "exclude", "signal_methods"]
REQUIRED_SCOPE = ["venues", "years", "include_arxiv"]
REQUIRED_CLARITY = ["scope", "triage", "keywords"]


def now_iso() -> str:
    return datetime.now(UTC).isoformat(timespec="seconds")


def validate(payload: dict[str, Any]) -> list[str]:
    errs: list[str] = []
    for k in REQUIRED_TOP:
        if k not in payload:
            errs.append(f"missing top-level field: {k}")
    if errs:
        return errs
    if payload["version"] != 1:
        errs.append(f"version must be 1, got {payload['version']!r}")
    tc = payload["triage_context"]
    if not isinstance(tc, dict):
        errs.append("triage_context must be object")
    else:
        for k in REQUIRED_TRIAGE:
            if k not in tc:
                errs.append(f"triage_context missing: {k}")
        for list_key in ["include", "exclude", "signal_methods"]:
            if list_key in tc and not isinstance(tc[list_key], list):
                errs.append(f"triage_context.{list_key} must be array")
    sc = payload["scope"]
    if not isinstance(sc, dict):
        errs.append("scope must be object")
    else:
        for k in REQUIRED_SCOPE:
            if k not in sc:
                errs.append(f"scope missing: {k}")
        if "include_arxiv" in sc and not isinstance(sc["include_arxiv"], bool):
            errs.append("scope.include_arxiv must be boolean")
    cs = payload["clarity_scores"]
    if not isinstance(cs, dict):
        errs.append("clarity_scores must be object")
    else:
        for k in REQUIRED_CLARITY:
            if k not in cs:
                errs.append(f"clarity_scores missing: {k}")
            else:
                v = cs[k]
                if not isinstance(v, (int, float)) or not 0.0 <= v <= 1.0:
                    errs.append(f"clarity_scores.{k} must be 0.0–1.0, got {v!r}")
    if payload["termination_reason"] not in VALID_TERMINATION:
        errs.append(
            f"termination_reason must be one of {sorted(VALID_TERMINATION)}, "
            f"got {payload['termination_reason']!r}"
        )
    kg = payload["keyword_groups"]
    if not isinstance(kg, list) or any(not isinstance(g, list) for g in kg):
        errs.append("keyword_groups must be list of lists of strings")
    elif len(kg) > 2:
        errs.append(f"keyword_groups: max 2 groups allowed, got {len(kg)}")
    return errs


def _get(payload: dict[str, Any], dotted: str) -> Any:
    cur: Any = payload
    for part in dotted.split("."):
        if isinstance(cur, dict) and part in cur:
            cur = cur[part]
        else:
            print(f"[topic_spec] no such field: {dotted}", file=sys.stderr)
            sys.exit(3)
    return cur


def template(raw_input: str) -> dict[str, Any]:
    return {
        "version": 1,
        "created": now_iso(),
        "raw_input": raw_input,
        "refined_topic": "",
        "triage_context": {
            "core_question": "",
            "include": [],
            "exclude": [],
            "signal_methods": [],
        },
        "keyword_groups": [],
        "scope": {
            "venues": ["NeurIPS", "AAAI", "ICLR", "ICML", "ACL", "EMNLP"],
            "years": [],
            "include_arxiv": False,
        },
        "clarity_scores": {"scope": 0.0, "triage": 0.0, "keywords": 0.0},
        "termination_reason": "floor",
        "interview_rounds": 0,
        "interview_log": [],
    }


def main() -> int:
    ap = argparse.ArgumentParser(description="topic.json validator/loader/template")
    sub = ap.add_subparsers(dest="cmd", required=True)

    s_val = sub.add_parser("validate", help="Validate topic.json against schema")
    s_val.add_argument("path")

    s_get = sub.add_parser("get", help="Print dotted field from topic.json")
    s_get.add_argument("path")
    s_get.add_argument("field", help="e.g. triage_context.core_question")

    s_tpl = sub.add_parser("template", help="Print blank topic.json template")
    s_tpl.add_argument("--raw-input", default="")

    args = ap.parse_args()

    if args.cmd == "validate":
        try:
            data = json.loads(Path(args.path).read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as e:
            print(f"[topic_spec] cannot load {args.path}: {e}", file=sys.stderr)
            return 2
        errs = validate(data)
        if errs:
            for e in errs:
                print(e, file=sys.stderr)
            return 2
        print("ok")
        return 0

    if args.cmd == "get":
        data = json.loads(Path(args.path).read_text(encoding="utf-8"))
        val = _get(data, args.field)
        if isinstance(val, (list, dict)):
            print(json.dumps(val, ensure_ascii=False))
        else:
            print(val)
        return 0

    if args.cmd == "template":
        print(json.dumps(template(args.raw_input), ensure_ascii=False, indent=2))
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
