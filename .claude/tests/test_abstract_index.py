#!/usr/bin/env python3
"""Unit tests for .claude/skills/abstract-index/scripts/index.py.

Runs against a temporary ChromaDB dir populated from the fixture raw.md pool.
Skipped if sentence-transformers / chromadb are not installed (the LLDM conda
env is required).
"""
from __future__ import annotations

import json
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent  # research_hub/
FIXTURES = Path(__file__).resolve().parent / "_fixtures" / "abstract_index"
INDEX_SCRIPT = REPO / ".claude" / "skills" / "abstract-index" / "scripts" / "index.py"


def _deps_available() -> bool:
    try:
        import chromadb  # noqa: F401
        import sentence_transformers  # noqa: F401
    except ImportError:
        return False
    return True


@unittest.skipUnless(_deps_available(), "chromadb + sentence-transformers required (conda env LLDM)")
class AbstractIndexBehavior(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="abstract_index_"))
        self.papers = self.tmp / "papers" / "metadata" / "FIXTURE" / "2025"
        self.papers.mkdir(parents=True)
        for f in sorted(FIXTURES.glob("*.raw.md")):
            shutil.copy2(f, self.papers / f.name)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def _run_index(self, *args: str) -> subprocess.CompletedProcess:
        cmd = [sys.executable, str(INDEX_SCRIPT), "--root", str(self.tmp), *args]
        return subprocess.run(cmd, capture_output=True, text=True)

    def _collection_count(self) -> int:
        import chromadb
        c = chromadb.PersistentClient(path=str(self.tmp / "papers" / "vector_db" / "chroma"))
        col = c.get_collection("abstracts")
        return col.count()

    def _load_manifest(self) -> dict:
        p = self.tmp / "papers" / "vector_db" / "abstracts_manifest.json"
        return json.loads(p.read_text(encoding="utf-8"))

    def test_initial_index_indexes_all_five(self):
        r = self._run_index()
        self.assertEqual(r.returncode, 0, f"index.py failed: {r.stderr}")
        self.assertEqual(self._collection_count(), 5,
                         f"expected 5 docs in abstracts collection; got {self._collection_count()}. stderr={r.stderr}")
        m = self._load_manifest()
        self.assertEqual(len(m["files"]), 5)
        self.assertEqual(m["embed_model"], "BAAI/bge-m3")

    def test_reindex_unchanged_is_noop(self):
        self._run_index()
        r2 = self._run_index()
        self.assertEqual(r2.returncode, 0)
        # stderr JSON summary must report added=0 updated=0 deleted=0
        self.assertIn('"added": 0', r2.stderr)
        self.assertIn('"updated": 0', r2.stderr)

    def test_modified_raw_md_triggers_update(self):
        self._run_index()
        target = self.papers / "paper_a.raw.md"
        text = target.read_text(encoding="utf-8")
        target.write_text(text + "\n<!-- trailing edit -->\n", encoding="utf-8")
        r = self._run_index()
        self.assertEqual(r.returncode, 0)
        self.assertIn('"updated": 1', r.stderr)
        self.assertEqual(self._collection_count(), 5)  # still 5

    def test_deleted_raw_md_is_removed_from_collection(self):
        self._run_index()
        (self.papers / "paper_c.raw.md").unlink()
        r = self._run_index()
        self.assertEqual(r.returncode, 0)
        self.assertIn('"deleted": 1', r.stderr)
        self.assertEqual(self._collection_count(), 4)

    def test_rebuild_manifest_only_no_chroma_touch(self):
        self._run_index()
        r = self._run_index("--rebuild-manifest")
        self.assertEqual(r.returncode, 0)
        self.assertIn('"rebuilt_manifest": true', r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
