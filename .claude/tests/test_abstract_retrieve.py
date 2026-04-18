#!/usr/bin/env python3
"""Unit tests for .claude/skills/paper-triage/scripts/retrieve.py.

Uses the same fixture raw.md pool as test_abstract_index.py, runs the
indexer once, then exercises retrieve.py against it.
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
INDEX_FIX = Path(__file__).resolve().parent / "_fixtures" / "abstract_index"
TOPIC_FIX = Path(__file__).resolve().parent / "_fixtures" / "abstract_retrieve" / "topic.json"
INDEX_SCRIPT = REPO / ".claude" / "skills" / "abstract-index" / "scripts" / "index.py"
RETRIEVE_SCRIPT = REPO / ".claude" / "skills" / "paper-triage" / "scripts" / "retrieve.py"


def _deps_available() -> bool:
    try:
        import chromadb  # noqa: F401
        import sentence_transformers  # noqa: F401
    except ImportError:
        return False
    return True


@unittest.skipUnless(_deps_available(), "chromadb + sentence-transformers required (conda env LLDM)")
class RetrieveBehavior(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = Path(tempfile.mkdtemp(prefix="abstract_retrieve_"))
        cls.papers = cls.tmp / "papers" / "metadata" / "FIXTURE" / "2025"
        cls.papers.mkdir(parents=True)
        for f in sorted(INDEX_FIX.glob("*.raw.md")):
            shutil.copy2(f, cls.papers / f.name)
        # One-time index of the fixture corpus (shared across tests)
        r = subprocess.run(
            [sys.executable, str(INDEX_SCRIPT), "--root", str(cls.tmp)],
            capture_output=True, text=True,
        )
        assert r.returncode == 0, f"fixture index failed: {r.stderr}"

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.tmp, ignore_errors=True)

    def _run_retrieve(self, *args: str) -> subprocess.CompletedProcess:
        cmd = [
            sys.executable, str(RETRIEVE_SCRIPT),
            "--root", str(self.tmp),
            "--topic-spec", str(TOPIC_FIX),
            *args,
        ]
        return subprocess.run(cmd, capture_output=True, text=True)

    def test_topic_spec_mode_returns_json_list(self):
        r = self._run_retrieve()
        self.assertEqual(r.returncode, 0, f"stderr: {r.stderr}")
        hits = json.loads(r.stdout)
        self.assertIsInstance(hits, list)
        self.assertGreater(len(hits), 0, "retrieve must return at least one candidate")
        for h in hits:
            for k in ("path", "slug", "title", "abstract", "cos_score", "signal_hit"):
                self.assertIn(k, h, f"hit missing key {k!r}")

    def test_on_topic_papers_rank_above_off_topic(self):
        r = self._run_retrieve()
        hits = json.loads(r.stdout)
        top_slug = hits[0]["slug"]
        # paper_a (diffusion defense) and paper_e (jailbreak) are on-topic
        self.assertIn(top_slug, ("paper_a", "paper_e"),
                      f"top hit should be on-topic; got {top_slug}. hits={[(h['slug'], h['cos_score']) for h in hits]}")

    def test_exclude_veto_drops_image_diffusion(self):
        # topic.json excludes "image diffusion" which is in paper_c
        r = self._run_retrieve()
        hits = json.loads(r.stdout)
        slugs = [h["slug"] for h in hits]
        self.assertNotIn("paper_c", slugs,
                         f"paper_c should be vetoed by exclude 'image diffusion'. slugs={slugs}")

    def test_signal_methods_boost_flagged(self):
        # paper_a abstract mentions "masked diffusion" and "iterative denoising"
        # both of which are in signal_methods
        r = self._run_retrieve()
        hits = json.loads(r.stdout)
        by_slug = {h["slug"]: h for h in hits}
        self.assertIn("paper_a", by_slug, "paper_a must be in hits")
        self.assertTrue(by_slug["paper_a"]["signal_hit"],
                        "paper_a must have signal_hit=true (masked diffusion, denoising)")

    def test_k_cap_respected(self):
        r = self._run_retrieve("--k-cap", "2")
        hits = json.loads(r.stdout)
        self.assertLessEqual(len(hits), 2)

    def test_cosine_threshold_filters(self):
        # Very high threshold — must drop everything
        r = self._run_retrieve("--cosine-threshold", "0.99")
        hits = json.loads(r.stdout)
        self.assertEqual(len(hits), 0)

    def test_exit_5_when_collection_missing(self):
        empty = Path(tempfile.mkdtemp(prefix="abstract_retrieve_empty_"))
        try:
            (empty / "papers" / "vector_db" / "chroma").mkdir(parents=True)
            r = subprocess.run(
                [sys.executable, str(RETRIEVE_SCRIPT),
                 "--root", str(empty),
                 "--topic-spec", str(TOPIC_FIX)],
                capture_output=True, text=True,
            )
            self.assertEqual(r.returncode, 5,
                             f"must exit 5 when abstracts collection missing; got {r.returncode}, stderr={r.stderr}")
            self.assertIn("abstract-indexer", r.stderr.lower() + r.stdout.lower(),
                          "error message must hint at running abstract-indexer first")
        finally:
            shutil.rmtree(empty, ignore_errors=True)


if __name__ == "__main__":
    unittest.main(verbosity=2)
