#!/usr/bin/env python3
"""Refactor invariants for the Phase C dispatch refactor (2026-04-16).

Run: python3 .claude/tests/test_phase_c_refactor.py

This test intentionally fails before the refactor is applied and must pass
when every task in docs/superpowers/plans/2026-04-16-phase-c-dispatch.md is
complete.
"""
from __future__ import annotations

import re
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent  # research_hub/
AGENTS = REPO / ".claude" / "agents"
SKILLS = REPO / ".claude" / "skills"
COMMANDS = REPO / ".claude" / "commands"
DOCS = REPO / "docs"

PLANNER_AGENTS = [
    "paper-hunter.md",
    "answer-formulator.md",
    "experiment-planner.md",
    "results-analyst.md",
]

STAGE_COMMANDS = {
    "research-papers.md": ["A-1", "A-1.5", "A-2", "A-3", "A-4"],
    "research-qa.md": ["B-1", "B-2"],
    "research-experiments.md": ["E-1", "E-2", "E-3"],
    "research-analyze.md": ["F-1", "F-2"],
}


class OrchestratorRemoved(unittest.TestCase):
    def test_orchestrator_agent_file_deleted(self):
        self.assertFalse(
            (AGENTS / "orchestrator.md").exists(),
            ".claude/agents/orchestrator.md must be deleted",
        )

    def test_orchestrate_skill_dir_deleted(self):
        self.assertFalse(
            (SKILLS / "orchestrate").exists(),
            ".claude/skills/orchestrate/ must be deleted recursively",
        )

    def test_no_orchestrator_agent_references_in_commands(self):
        # Commands must not dispatch Agent(subagent_type="orchestrator")
        pat = re.compile(r"subagent[_\s]*type\s*[:=]\s*[\"']?orchestrator", re.I)
        for name in STAGE_COMMANDS:
            text = (COMMANDS / name).read_text(encoding="utf-8")
            self.assertFalse(
                pat.search(text),
                f"{name} must not dispatch the orchestrator agent",
            )

    def test_no_orchestrator_agent_references_in_agents(self):
        # Surviving agents must not delegate to orchestrator
        pat = re.compile(r"subagent[_\s]*type\s*[:=]\s*[\"']?orchestrator", re.I)
        for md in AGENTS.glob("*.md"):
            self.assertFalse(
                pat.search(md.read_text(encoding="utf-8")),
                f"{md.name} must not reference the orchestrator agent",
            )


class PlannerAgentsHaveModeParam(unittest.TestCase):
    """Each of the four planner agents must declare a `mode` parameter."""

    def test_mode_section_present(self):
        for name in PLANNER_AGENTS:
            text = (AGENTS / name).read_text(encoding="utf-8")
            self.assertRegex(
                text,
                r"##\s*Mode\b",
                f"{name} must contain a '## Mode' section",
            )
            self.assertIn(
                "plan-only", text,
                f"{name} must document mode=plan-only",
            )
            self.assertIn(
                "execute", text,
                f"{name} must document mode=execute",
            )


class CommandsDispatchSubphasesAsBackgroundAgents(unittest.TestCase):
    """Each /research-* command owns the Phase C chain and dispatches
    every sub-phase as a separate Agent(..., run_in_background=true)."""

    def test_each_command_mentions_every_subphase(self):
        for name, subphases in STAGE_COMMANDS.items():
            text = (COMMANDS / name).read_text(encoding="utf-8")
            for sp in subphases:
                self.assertIn(
                    sp, text,
                    f"{name} must name sub-phase {sp} explicitly",
                )

    def test_each_command_requires_run_in_background(self):
        for name in STAGE_COMMANDS:
            text = (COMMANDS / name).read_text(encoding="utf-8")
            self.assertIn(
                "run_in_background", text,
                f"{name} must dispatch sub-phase Agents with run_in_background",
            )
            # The refactor mandates bg=true by default for every sub-phase;
            # the literal token "true" must appear near the flag.
            self.assertRegex(
                text,
                r"run_in_background[^\n]{0,40}true",
                f"{name} must set run_in_background: true on sub-phase dispatch",
            )

    def test_papers_still_has_topic_refine_step(self):
        text = (COMMANDS / "research-papers.md").read_text(encoding="utf-8")
        self.assertIn(
            "topic-refine", text,
            "research-papers.md must keep the topic-refine skill step",
        )


class DocsAgentCountConsistent(unittest.TestCase):
    def test_claude_md_says_14_agents(self):
        text = (REPO / "CLAUDE.md").read_text(encoding="utf-8")
        self.assertRegex(
            text,
            r"14\s*에이전트",
            "CLAUDE.md §7 must say '14 에이전트' after abstract-indexer addition",
        )
        self.assertNotIn(
            "13 에이전트", text,
            "CLAUDE.md must no longer say '13 에이전트'",
        )

    def test_harness_layout_has_14_agents(self):
        text = (DOCS / "harness-layout.md").read_text(encoding="utf-8")
        self.assertNotIn(
            "13 에이전트", text,
            "docs/harness-layout.md must say 14 now",
        )
        self.assertRegex(
            text,
            r"(?mi)abstract-indexer",
            "docs/harness-layout.md must list the abstract-indexer agent",
        )

    def test_lesson_appended(self):
        text = (DOCS / "lessons.md").read_text(encoding="utf-8")
        self.assertIn(
            "Phase C subagent dispatch", text,
            "docs/lessons.md must record the new bg-default lesson",
        )


class TokenOptimizationContract(unittest.TestCase):
    """Lock in the paper-summarizer token-optimization file contracts.

    These assertions pin the tokens that must appear in the stage command,
    agent, and skill after the 2026-04-17 optimization is applied. They
    guard against accidental rollback of the batch_paths / cache_gate
    / kg_skeleton wiring.
    """

    def test_research_papers_contains_cache_gate(self):
        text = (COMMANDS / "research-papers.md").read_text(encoding="utf-8")
        self.assertIn("cache_gate.py", text,
                      "research-papers.md §Step 6 A-3 must invoke cache_gate.py")

    def test_research_papers_contains_chunk_helper(self):
        text = (COMMANDS / "research-papers.md").read_text(encoding="utf-8")
        self.assertIn("chunk_helper", text,
                      "research-papers.md §Step 6 A-3 must reference chunk_helper")

    def test_research_papers_contains_batch_paths(self):
        text = (COMMANDS / "research-papers.md").read_text(encoding="utf-8")
        self.assertIn("batch_paths", text,
                      "research-papers.md §Step 6 A-3 must pass batch_paths to the agent")

    def test_paper_summarizer_agent_accepts_batch_paths(self):
        text = (AGENTS / "paper-summarizer.md").read_text(encoding="utf-8")
        self.assertIn("batch_paths", text,
                      "paper-summarizer agent must declare batch_paths input")
        self.assertIn("source_digest_sha256", text,
                      "paper-summarizer must write source_digest_sha256 to summary frontmatter")
        self.assertIn("kg_skeleton.py", text,
                      "paper-summarizer must invoke kg_skeleton.py")

    def test_paper_summarize_skill_has_cache_recheck(self):
        text = (SKILLS / "paper-summarize" / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("cache_gate", text,
                      "paper-summarize SKILL.md must reference cache_gate in Step 2.0")
        self.assertIn("kg_skeleton", text,
                      "paper-summarize SKILL.md must reference kg_skeleton in Step 2f")

    def test_gemini_digest_at_prompt_v7(self):
        text = (SKILLS / "paper-summarize" / "scripts" / "gemini_digest.py").read_text(encoding="utf-8")
        self.assertIn('PROMPT_VERSION = "v7"', text,
                      "gemini_digest.py PROMPT_VERSION must be v7")
        self.assertIn("## Entities", text,
                      "gemini_digest.py DIGEST_PROMPT must instruct Gemini to emit ## Entities block")

    def test_cache_gate_script_exists(self):
        p = SKILLS / "paper-summarize" / "scripts" / "cache_gate.py"
        self.assertTrue(p.exists(), f"{p} missing")

    def test_kg_skeleton_script_exists(self):
        p = SKILLS / "paper-summarize" / "scripts" / "kg_skeleton.py"
        self.assertTrue(p.exists(), f"{p} missing")

    def test_chunk_helper_script_exists(self):
        p = REPO / ".claude" / "scripts" / "chunk_helper.py"
        self.assertTrue(p.exists(), f"{p} missing")


class AbstractIndexerPresent(unittest.TestCase):
    """A-1.5 abstract-indexer must be fully wired into the harness."""

    def test_stage_subphases_contains_a15(self):
        # Import the live constant, not a copy
        sys.path.insert(0, str(REPO / ".claude" / "scripts"))
        from loop_state import STAGE_SUBPHASES
        sps = STAGE_SUBPHASES["papers"]
        self.assertIn("A-1.5", sps,
                      "STAGE_SUBPHASES['papers'] must contain 'A-1.5'")
        # Must be positioned between A-1 and A-2
        i1 = sps.index("A-1")
        i15 = sps.index("A-1.5")
        i2 = sps.index("A-2")
        self.assertLess(i1, i15, "A-1.5 must come after A-1")
        self.assertLess(i15, i2, "A-1.5 must come before A-2")

    def test_abstract_indexer_agent_file_exists(self):
        self.assertTrue((AGENTS / "abstract-indexer.md").exists(),
                        ".claude/agents/abstract-indexer.md must exist")

    def test_abstract_index_skill_dir_exists(self):
        d = SKILLS / "abstract-index"
        self.assertTrue(d.is_dir(), ".claude/skills/abstract-index/ must exist")
        self.assertTrue((d / "SKILL.md").is_file(),
                        ".claude/skills/abstract-index/SKILL.md must exist")
        self.assertTrue((d / "scripts" / "index.py").is_file(),
                        ".claude/skills/abstract-index/scripts/index.py must exist")

    def test_retrieve_script_exists(self):
        p = SKILLS / "paper-triage" / "scripts" / "retrieve.py"
        self.assertTrue(p.exists(), f"{p} missing")

    def test_research_papers_dispatches_a15(self):
        text = (COMMANDS / "research-papers.md").read_text(encoding="utf-8")
        self.assertIn("A-1.5", text,
                      "research-papers.md must reference A-1.5 sub-phase")
        self.assertIn("abstract-indexer", text,
                      "research-papers.md must dispatch abstract-indexer agent")


if __name__ == "__main__":
    unittest.main(verbosity=2)
