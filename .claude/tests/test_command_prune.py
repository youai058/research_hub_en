"""Static checks that the 4 research stage commands have been pruned
and that CLAUDE.md absorbed the user-interrupt sentence.

These tests are expected to FAIL before Tasks 9-13 prune the files, and
PASS after. Running before implementation is the TDD baseline.
"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COMMANDS = {
    "papers":      ROOT / ".claude/commands/research-papers.md",
    "qa":          ROOT / ".claude/commands/research-qa.md",
    "experiments": ROOT / ".claude/commands/research-experiments.md",
    "analyze":     ROOT / ".claude/commands/research-analyze.md",
}
CLAUDE_MD = ROOT / "CLAUDE.md"

LINE_CAPS = {"papers": 250, "qa": 130, "experiments": 160, "analyze": 140}


def test_T1_no_dispatch_explainer_paragraph():
    for name, p in COMMANDS.items():
        body = p.read_text()
        assert "How to read these dispatch specs" not in body, (
            f"{name}: explainer paragraph still present"
        )


def test_T2_no_user_interrupt_paragraph():
    for name, p in COMMANDS.items():
        body = p.read_text()
        assert "User-interrupt handling" not in body, (
            f"{name}: user-interrupt paragraph still present"
        )


def test_T3_no_pre_count_bash_pattern():
    rx = re.compile(r"PRE_[A-Z0-9_]*_COUNT=\$\(find")
    for name, p in COMMANDS.items():
        body = p.read_text()
        matches = rx.findall(body)
        assert matches == [], (
            f"{name}: {len(matches)} legacy PRE_*_COUNT=$(find patterns remain"
        )


def test_T4_line_caps():
    for name, cap in LINE_CAPS.items():
        n = sum(1 for _ in COMMANDS[name].read_text().splitlines())
        assert n <= cap, f"{name}: {n} lines > cap {cap}"


def test_T5_claude_md_absorbed_user_interrupt_sentence():
    body = CLAUDE_MD.read_text()
    assert "Phase C chain 중 user-interrupt" in body, (
        "CLAUDE.md did not absorb user-interrupt sentence"
    )
