#!/usr/bin/env python3
"""Tests for paper-summarizer token optimization (2026-04-17).

Run: conda run -n LLDM python -m pytest .claude/tests/test_summarizer_optimization.py -v
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent  # research_hub/
sys.path.insert(0, str(REPO / ".claude" / "scripts"))

from chunk_helper import chunk_paths

import json
import subprocess
import textwrap

SKELETON_SCRIPT = (
    REPO / ".claude" / "skills" / "paper-summarize" / "scripts" / "kg_skeleton.py"
)


def _write_digest(tmp_path, body: str, frontmatter: dict) -> Path:
    """Helper — write a fake digest.md with given YAML frontmatter."""
    def _fmt_val(v):
        if isinstance(v, list):
            if not v:
                return "[]"
            return "\n" + "\n".join(f"  - {x!r}" for x in v)
        return f'"{v}"'

    lines = ["---"]
    for k, v in frontmatter.items():
        if isinstance(v, list):
            if not v:
                lines.append(f"{k}: []")
            else:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item!r}")
        else:
            lines.append(f'{k}: "{v}"')
    lines.append("---")
    lines.append(body)
    p = tmp_path / "fake.digest.md"
    p.write_text("\n".join(lines), encoding="utf-8")
    return p


def _run_skeleton(digest_path: Path, out_path: Path, slug: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            "python3", str(SKELETON_SCRIPT),
            "--digest", str(digest_path),
            "--slug", slug,
            "--out", str(out_path),
        ],
        capture_output=True, text=True, check=False,
    )


class TestChunkHelper(unittest.TestCase):
    def test_chunk_b5_uneven(self):
        paths = [f"p{i}" for i in range(12)]
        self.assertEqual(
            chunk_paths(paths, batch_size=5),
            [["p0", "p1", "p2", "p3", "p4"],
             ["p5", "p6", "p7", "p8", "p9"],
             ["p10", "p11"]],
        )

    def test_chunk_exact_multiple(self):
        paths = [f"p{i}" for i in range(10)]
        self.assertEqual(
            chunk_paths(paths, batch_size=5),
            [["p0", "p1", "p2", "p3", "p4"],
             ["p5", "p6", "p7", "p8", "p9"]],
        )

    def test_chunk_empty(self):
        self.assertEqual(chunk_paths([], batch_size=5), [])

    def test_chunk_single_batch(self):
        self.assertEqual(
            chunk_paths(["a", "b"], batch_size=5),
            [["a", "b"]],
        )

    def test_chunk_default_b5(self):
        # Default batch_size must be 5 per spec §3.4.
        paths = [f"p{i}" for i in range(7)]
        self.assertEqual(len(chunk_paths(paths)), 2)
        self.assertEqual(len(chunk_paths(paths)[0]), 5)

    def test_chunk_invalid_batch_size(self):
        with self.assertRaises(ValueError):
            chunk_paths(["a"], batch_size=0)
        with self.assertRaises(ValueError):
            chunk_paths(["a"], batch_size=-1)


class TestKgSkeleton(unittest.TestCase):
    def test_skeleton_minimal(self):
        """Digest without methods/datasets/... → only Paper+Venue nodes."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            digest = _write_digest(tmp, "body text", {
                "source_raw": "/fake/raw.md",
                "source_pdf_sha256": "a" * 64,
                "prompt_version": "v7",
                "slug": "minimal-paper",
                "venue": "ICLR",
                "year": "2025",
                "venue_class": "whitelist",
            })
            out = tmp / "out.kg.json"
            proc = _run_skeleton(digest, out, "minimal-paper")
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            data = json.loads(out.read_text())
            types = sorted({n["type"] for n in data["nodes"]})
            self.assertEqual(types, ["Paper", "Venue"],
                             "minimal digest lacks authors too — skeleton emits only Paper+Venue")
            # No Claim/Result (Claude fills those).
            self.assertNotIn("Claim", types)
            self.assertNotIn("Result", types)

    def test_skeleton_full(self):
        """Digest with all lists → Method/Dataset/Model/Metric nodes + USES_* edges."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            digest = _write_digest(tmp, "body", {
                "source_raw": "/fake/raw.md",
                "source_pdf_sha256": "b" * 64,
                "prompt_version": "v7",
                "slug": "full-paper",
                "venue": "NeurIPS",
                "year": "2024",
                "venue_class": "whitelist",
                "authors": ["Alice Smith", "Bob Lee"],
                "methods": ["MDLM", "AR baseline"],
                "datasets": ["OpenWebText", "LM1B"],
                "models": ["GPT-2 124M"],
                "metrics": ["Perplexity", "Bits-per-token"],
            })
            out = tmp / "out.kg.json"
            proc = _run_skeleton(digest, out, "full-paper")
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            data = json.loads(out.read_text())
            types = {n["type"] for n in data["nodes"]}
            self.assertIn("Method", types)
            self.assertIn("Dataset", types)
            self.assertIn("Model", types)
            self.assertIn("Metric", types)
            edge_types = {e["type"] for e in data["edges"]}
            self.assertIn("USES_METHOD", edge_types)
            self.assertIn("USES_DATASET", edge_types)
            self.assertIn("USES_MODEL", edge_types)
            self.assertIn("AUTHORED_BY", edge_types)
            self.assertIn("PUBLISHED_IN", edge_types)

    def test_skeleton_no_claim_no_result(self):
        """Skeleton never emits Claim/Result (those are Claude's job)."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            digest = _write_digest(tmp, "body", {
                "source_raw": "/fake/raw.md",
                "source_pdf_sha256": "c" * 64,
                "prompt_version": "v7",
                "slug": "x",
                "venue": "ICLR", "year": "2025", "venue_class": "whitelist",
                "methods": ["M1"],
            })
            out = tmp / "out.kg.json"
            _run_skeleton(digest, out, "x")
            data = json.loads(out.read_text())
            self.assertFalse(any(n["type"] == "Claim" for n in data["nodes"]))
            self.assertFalse(any(n["type"] == "Result" for n in data["nodes"]))
            self.assertFalse(any(e["type"] == "MAKES_CLAIM" for e in data["edges"]))
            self.assertFalse(any(e["type"] == "REPORTS_RESULT" for e in data["edges"]))
            self.assertFalse(any(e["type"] == "EVIDENCED_BY" for e in data["edges"]))

    def test_skeleton_schema_valid(self):
        """Output JSON passes KGFile Pydantic validation."""
        import tempfile
        sys.path.insert(0, str(REPO / ".claude" / "skills" / "paper-kg" / "scripts"))
        from schema import KGFile  # noqa: E402

        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            digest = _write_digest(tmp, "body", {
                "source_raw": "/fake/raw.md",
                "source_pdf_sha256": "d" * 64,
                "prompt_version": "v7",
                "slug": "sv-paper",
                "venue": "ACL", "year": "2024", "venue_class": "whitelist",
                "authors": ["Carol Chen"],
                "methods": ["MethodA"],
            })
            out = tmp / "out.kg.json"
            _run_skeleton(digest, out, "sv-paper")
            KGFile.model_validate_json(out.read_text())  # must not raise

    def test_skeleton_idempotent(self):
        """Same digest twice → same JSON output."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            digest = _write_digest(tmp, "body", {
                "source_raw": "/fake/raw.md",
                "source_pdf_sha256": "e" * 64,
                "prompt_version": "v7",
                "slug": "idem", "venue": "ICLR", "year": "2025",
                "venue_class": "whitelist",
                "authors": ["D"], "methods": ["M"],
            })
            out1 = tmp / "out1.kg.json"
            out2 = tmp / "out2.kg.json"
            _run_skeleton(digest, out1, "idem")
            _run_skeleton(digest, out2, "idem")
            self.assertEqual(out1.read_text(), out2.read_text())


CACHE_GATE_SCRIPT = (
    REPO / ".claude" / "skills" / "paper-summarize" / "scripts" / "cache_gate.py"
)


def _write_raw_md(tmp: Path, slug: str, venue: str, year: str,
                  venue_class: str = "whitelist") -> Path:
    """Write a minimal raw.md under tmp/papers/metadata/<V>/<Y>/<slug>.raw.md."""
    raw = tmp / "papers" / "metadata" / venue / year / f"{slug}.raw.md"
    raw.parent.mkdir(parents=True, exist_ok=True)
    raw.write_text(
        f'---\nslug: "{slug}"\nvenue: "{venue}"\nyear: "{year}"\n'
        f'venue_class: "{venue_class}"\n---\nabstract here\n',
        encoding="utf-8",
    )
    return raw


def _write_digest_file(tmp: Path, slug: str, venue: str, year: str,
                       body: str = "body") -> Path:
    """Write papers/digest/<V>/<Y>/<slug>.digest.md. Returns its path."""
    d = tmp / "papers" / "digest" / venue / year / f"{slug}.digest.md"
    d.parent.mkdir(parents=True, exist_ok=True)
    d.write_text(
        f'---\nslug: "{slug}"\nsource_pdf_sha256: "x"\nprompt_version: "v7"\n---\n{body}\n',
        encoding="utf-8",
    )
    return d


def _write_summary(tmp: Path, slug: str, venue: str, year: str,
                   source_digest_sha256: str, prompt_version: str = "v7",
                   venue_class: str = "whitelist") -> Path:
    """Write papers/marp-summary/<V>/<Y>/<slug>.md with matching frontmatter."""
    if venue_class == "whitelist":
        s = tmp / "papers" / "marp-summary" / venue / year / f"{slug}.md"
    else:
        s = tmp / "papers" / "marp-summary" / "etc" / year / f"{slug}.md"
    s.parent.mkdir(parents=True, exist_ok=True)
    s.write_text(
        f'---\nmarp: true\nvenue_class: "{venue_class}"\n'
        f'source_digest_sha256: "{source_digest_sha256}"\n'
        f'prompt_version: "{prompt_version}"\n---\n# x\n',
        encoding="utf-8",
    )
    return s


def _sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def _run_cache_gate(paths: list[Path], out_path: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["python3", str(CACHE_GATE_SCRIPT),
         "--paths", *[str(p) for p in paths],
         "--out", str(out_path)],
        capture_output=True, text=True, check=False,
    )


import hashlib  # noqa: E402 — needed by helpers above


class TestCacheGate(unittest.TestCase):
    def test_miss_no_digest(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            raw = _write_raw_md(tmp, "s1", "ICLR", "2025")
            out = tmp / "out.json"
            proc = _run_cache_gate([raw], out)
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            data = json.loads(out.read_text())
            self.assertIn(str(raw), data["misses"])
            self.assertEqual(data["hits"], [])
            self.assertEqual(data["stale"], [])

    def test_miss_no_summary(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            raw = _write_raw_md(tmp, "s2", "ICLR", "2025")
            _write_digest_file(tmp, "s2", "ICLR", "2025")
            out = tmp / "out.json"
            proc = _run_cache_gate([raw], out)
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            data = json.loads(out.read_text())
            self.assertIn(str(raw), data["misses"])

    def test_hit_matching_sha(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            raw = _write_raw_md(tmp, "s3", "ICLR", "2025")
            digest = _write_digest_file(tmp, "s3", "ICLR", "2025")
            digest_sha = _sha256_file(digest)
            _write_summary(tmp, "s3", "ICLR", "2025", digest_sha)
            out = tmp / "out.json"
            proc = _run_cache_gate([raw], out)
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            data = json.loads(out.read_text())
            self.assertIn(str(raw), data["hits"])

    def test_stale_mismatched_sha(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            raw = _write_raw_md(tmp, "s4", "ICLR", "2025")
            _write_digest_file(tmp, "s4", "ICLR", "2025")
            _write_summary(tmp, "s4", "ICLR", "2025", "deadbeef" * 8)  # wrong sha
            out = tmp / "out.json"
            proc = _run_cache_gate([raw], out)
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            data = json.loads(out.read_text())
            self.assertIn(str(raw), data["stale"])

    def test_stale_missing_frontmatter_field(self):
        """Pre-v7 summary missing source_digest_sha256 → stale."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            raw = _write_raw_md(tmp, "s5", "ICLR", "2025")
            _write_digest_file(tmp, "s5", "ICLR", "2025")
            # Write summary WITHOUT source_digest_sha256.
            s = tmp / "papers" / "marp-summary" / "ICLR" / "2025" / "s5.md"
            s.parent.mkdir(parents=True, exist_ok=True)
            s.write_text('---\nmarp: true\n---\n# x\n', encoding="utf-8")
            out = tmp / "out.json"
            proc = _run_cache_gate([raw], out)
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            data = json.loads(out.read_text())
            self.assertIn(str(raw), data["stale"])

    def test_stale_corrupted_digest(self):
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            raw = _write_raw_md(tmp, "s6", "ICLR", "2025")
            digest = _write_digest_file(tmp, "s6", "ICLR", "2025")
            # Corrupt the digest: write garbage without frontmatter.
            digest.write_bytes(b"\x00\x01not a valid markdown")
            _write_summary(tmp, "s6", "ICLR", "2025", "x" * 64)
            out = tmp / "out.json"
            proc = _run_cache_gate([raw], out)
            # Corrupt digest still has a sha — but since its sha won't match
            # an older summary's, we expect stale (not a crash).
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            data = json.loads(out.read_text())
            self.assertIn(str(raw), data["stale"])

    def test_output_json_shape(self):
        """Output always has exactly 3 keys: hits, stale, misses — all lists."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            raw = _write_raw_md(tmp, "s7", "ICLR", "2025")
            out = tmp / "out.json"
            _run_cache_gate([raw], out)
            data = json.loads(out.read_text())
            self.assertEqual(sorted(data.keys()), ["hits", "misses", "stale"])
            self.assertIsInstance(data["hits"], list)
            self.assertIsInstance(data["stale"], list)
            self.assertIsInstance(data["misses"], list)

    def test_etc_venue_class_routing(self):
        """venue_class=etc → summary lives in papers/marp-summary/etc/<Y>/."""
        import tempfile
        with tempfile.TemporaryDirectory() as td:
            tmp = Path(td)
            raw = _write_raw_md(tmp, "s8", "Workshop", "2024", venue_class="etc")
            digest = _write_digest_file(tmp, "s8", "Workshop", "2024")
            digest_sha = _sha256_file(digest)
            _write_summary(tmp, "s8", "Workshop", "2024", digest_sha,
                           venue_class="etc")
            out = tmp / "out.json"
            proc = _run_cache_gate([raw], out)
            self.assertEqual(proc.returncode, 0, msg=proc.stderr)
            data = json.loads(out.read_text())
            self.assertIn(str(raw), data["hits"])


if __name__ == "__main__":
    unittest.main()
