# paper-summarizer Token Optimization Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Reduce A-3 paper-summarizer token consumption by (1) gating already-summarized papers via digest sha cache, (2) chunking remaining work into B=5 sequential agent batches, and (3) offloading deterministic KG nodes/edges to a Python skeleton generator — without cutting any of quality axes A/B/C/E.

**Architecture:** Three composed mechanisms, all orchestrated from `/research-papers` §Step 6 A-3:
1. `cache_gate.py` classifies each accepted raw.md path as `hit | stale | miss` by SHA-comparing the existing Marp summary's `source_digest_sha256` frontmatter against the current digest file sha.
2. The main session chunks `stale + miss` paths into batches of 5 and dispatches `paper-summarizer` sequentially with `run_in_background: true`, verifying file-count delta after each batch.
3. Each paper-summarizer invocation calls `kg_skeleton.py` to pre-emit Paper/Author/Venue/Method/Dataset/Model/Metric nodes + USES_* / AUTHORED_BY / PUBLISHED_IN edges, so Claude only has to author Claim/Result/EVIDENCED_BY.

**Tech Stack:** Python 3.10+ (stdlib hashlib, json, argparse), pydantic v2 (already used by `.claude/skills/paper-kg/scripts/schema.py`), pytest (conda env `LLDM`).

**Spec reference:** `docs/superpowers/specs/2026-04-17-paper-summarizer-token-opt-design.md`

---

## File Structure

### Create

| Path | Purpose | ~LoC |
|---|---|---|
| `.claude/scripts/chunk_helper.py` | Testable pure function for B=5 chunking | ~20 |
| `.claude/skills/paper-summarize/scripts/cache_gate.py` | Classify accepted raw.md paths into `{hits, stale, misses}` | ~130 |
| `.claude/skills/paper-summarize/scripts/kg_skeleton.py` | Emit Paper/Author/Venue/Method/Dataset/Model/Metric KG skeleton from digest frontmatter | ~180 |
| `.claude/tests/test_summarizer_optimization.py` | pytest tests for the three new scripts + frontmatter contract | ~220 |

### Modify

| Path | Change |
|---|---|
| `.claude/skills/paper-summarize/scripts/gemini_digest.py` | PROMPT_VERSION `v6`→`v7`; add methods/datasets/models/metrics YAML lists to digest frontmatter |
| `.claude/agents/paper-summarizer.md` | Accept `batch_paths: List[str]` input; invoke `kg_skeleton.py`; write `source_digest_sha256` + `prompt_version` into Marp frontmatter |
| `.claude/skills/paper-summarize/SKILL.md` | Insert Step 2.0 (cache gate) + Step 2f (KG skeleton patch); add 3 checklist items |
| `.claude/commands/research-papers.md` | Rewrite §Step 6 A-3 block: cache_gate.py → chunk → sequential bg dispatches |
| `.claude/tests/test_phase_c_refactor.py` | Add assertions that `cache_gate.py`, `chunk`, `batch_paths` tokens appear in the expected files |

---

## Task Ordering Rationale

Tasks flow bottom-up along the dependency graph:

1. **Task 1** (`chunk_helper.py`) — pure function, no dependencies, trivial to test.
2. **Task 2** (`kg_skeleton.py`) — pure transform from digest frontmatter → validated KGFile JSON. Depends on existing `schema.py`.
3. **Task 3** (`cache_gate.py`) — classifier that reads digest + existing summary. Depends on an understanding of digest frontmatter (unchanged at this task) and summary frontmatter contract (defined in Task 5).
4. **Task 4** (`gemini_digest.py` bump) — emits new digest frontmatter fields consumed by `kg_skeleton.py`. Independent from Task 3; can run in parallel if subagents are available.
5. **Task 5** (`paper-summarizer.md` agent) — doc change that wires `batch_paths` input, `kg_skeleton.py` invocation, and `source_digest_sha256` output frontmatter.
6. **Task 6** (`SKILL.md`) — doc change that adds Step 2.0 + Step 2f to the summarization flow.
7. **Task 7** (`research-papers.md` §Step 6 A-3) — orchestrator-side rewrite using the scripts from Tasks 1+3 and the agent contract from Task 5.
8. **Task 8** (regression assertions in `test_phase_c_refactor.py`) — lock in the markdown contract from Tasks 5+6+7.

---

## Task 1: `chunk_helper.py`

**Files:**
- Create: `.claude/scripts/chunk_helper.py`
- Test: `.claude/tests/test_summarizer_optimization.py` (new file — test cases for this task are the first ones to land in it)

- [ ] **Step 1: Write the failing test**

Create `.claude/tests/test_summarizer_optimization.py` with only the chunking tests for now:

```python
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


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_summarizer_optimization.py -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'chunk_helper'`

- [ ] **Step 3: Write minimal implementation**

Create `.claude/scripts/chunk_helper.py`:

```python
"""Path batching helper for A-3 paper-summarizer sequential dispatch.

The only public function is `chunk_paths`. It is kept trivial + testable so
that the markdown orchestration in `.claude/commands/research-papers.md` can
reference a concrete implementation instead of an inline pseudo-comprehension.
"""

from __future__ import annotations


def chunk_paths(paths: list[str], batch_size: int = 5) -> list[list[str]]:
    """Split `paths` into consecutive batches of at most `batch_size`.

    Args:
        paths: list of absolute paths (strings). Order is preserved.
        batch_size: positive int. Defaults to 5 per design spec §3.4.

    Returns:
        List of batches. An empty input yields an empty list.

    Raises:
        ValueError: if batch_size <= 0.
    """
    if batch_size <= 0:
        raise ValueError(f"batch_size must be positive, got {batch_size}")
    return [paths[i : i + batch_size] for i in range(0, len(paths), batch_size)]
```

- [ ] **Step 4: Run test to verify it passes**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_summarizer_optimization.py -v`
Expected: PASS, 6 tests in `TestChunkHelper` pass.

- [ ] **Step 5: Commit**

```bash
git add .claude/scripts/chunk_helper.py .claude/tests/test_summarizer_optimization.py
git commit -m "feat(chunk_helper): add B=5 batching helper for A-3 dispatch

Pure function with explicit ValueError on non-positive batch_size.
Tests cover exact multiple, uneven tail, empty input, single batch,
default B=5, and invalid input.

Part of paper-summarizer token optimization (spec 2026-04-17)."
```

---

## Task 2: `kg_skeleton.py`

**Files:**
- Create: `.claude/skills/paper-summarize/scripts/kg_skeleton.py`
- Test: `.claude/tests/test_summarizer_optimization.py` (append `TestKgSkeleton` class)

- [ ] **Step 1: Write the failing test**

Append to `.claude/tests/test_summarizer_optimization.py` (before the `if __name__ == "__main__":` block):

```python
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


class TestKgSkeleton(unittest.TestCase):
    def test_skeleton_minimal(self):
        """Digest without methods/datasets/... → only Paper+Author+Venue nodes."""
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_summarizer_optimization.py::TestKgSkeleton -v`
Expected: FAIL — `kg_skeleton.py` script missing, `proc.returncode` will be non-zero.

- [ ] **Step 3: Write minimal implementation**

Create `.claude/skills/paper-summarize/scripts/kg_skeleton.py`:

```python
#!/usr/bin/env python3
"""kg_skeleton.py — emit the deterministic portion of a paper's `.kg.json`.

Reads a digest.md's YAML frontmatter and emits a schema-valid KGFile JSON
containing Paper, Author, Venue, Method, Dataset, Model, Metric nodes plus
AUTHORED_BY, PUBLISHED_IN, USES_METHOD, USES_DATASET, USES_MODEL edges.

Deliberately does NOT emit Claim, Result, MAKES_CLAIM, REPORTS_RESULT,
EVIDENCED_BY — those require interpretation of the paper content and are
left for paper-summarizer (Claude) to author on top of this skeleton.

Usage:
    python3 kg_skeleton.py --digest <path> --slug <slug> --out <path>

Exit codes:
    0  skeleton written successfully
    1  input/usage error (digest missing, --slug missing, etc.)
    2  output path unwritable
    3  schema validation failed (no file written)
"""

from __future__ import annotations

import argparse
import datetime as _dt
import hashlib
import json
import re
import sys
from pathlib import Path

KST = _dt.timezone(_dt.timedelta(hours=9))


def _log(msg: str) -> None:
    print(f"[kg_skeleton] {msg}", file=sys.stderr, flush=True)


def _now_kst_iso() -> str:
    return _dt.datetime.now(KST).strftime("%Y-%m-%dT%H:%M:%S%z")


def _slugify(name: str) -> str:
    """Collapse arbitrary entity name to a kg ID suffix: lowercase, alnum+hyphen."""
    s = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return s or "unnamed"


def _parse_frontmatter(digest_path: Path) -> tuple[dict, str]:
    """Parse YAML frontmatter. Returns (meta, body).

    Supports the subset produced by gemini_digest.py v7: scalar keys quoted,
    and list keys (authors, methods, datasets, models, metrics, figures)
    with `- "item"` entries OR inline `[]`.
    """
    text = digest_path.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        raise ValueError(f"digest missing YAML frontmatter: {digest_path}")
    end = text.find("\n---", 3)
    if end < 0:
        raise ValueError(f"digest frontmatter not closed: {digest_path}")
    fm_block = text[3:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")

    meta: dict = {}
    current_list_key: str | None = None
    for line in fm_block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            current_list_key = None
            continue
        # List continuation: `  - "item"` or `  - item`
        m_list = re.match(r"^\s+-\s+(.*)$", line)
        if m_list and current_list_key is not None:
            val = m_list.group(1).strip()
            if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
                val = val[1:-1]
            meta[current_list_key].append(val)
            continue
        # Scalar or list-start: `key: value` or `key:` (then list continues)
        m_kv = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", line)
        if not m_kv:
            current_list_key = None
            continue
        key = m_kv.group(1)
        val = m_kv.group(2).strip()
        if val == "":
            meta[key] = []
            current_list_key = key
            continue
        if val == "[]":
            meta[key] = []
            current_list_key = None
            continue
        # scalar
        if len(val) >= 2 and val[0] == val[-1] and val[0] in ("'", '"'):
            val = val[1:-1]
        meta[key] = val
        current_list_key = None
    return meta, body


def _build_skeleton(meta: dict, slug: str, digest_path: Path) -> dict:
    slug_id = _slugify(slug)
    nodes: list[dict] = []
    edges: list[dict] = []

    # --- Paper node ---
    paper_id = f"paper:{slug_id}"
    nodes.append({
        "id": paper_id,
        "type": "Paper",
        "name": meta.get("slug", slug),
        "meta": {
            "venue": meta.get("venue", ""),
            "year": meta.get("year", ""),
            "venue_class": meta.get("venue_class", ""),
            "source_digest": str(digest_path),
        },
    })

    # --- Venue node + PUBLISHED_IN edge ---
    venue = meta.get("venue", "").strip()
    year = meta.get("year", "").strip()
    if venue:
        venue_id = f"venue:{_slugify(venue)}-{_slugify(year)}" if year else f"venue:{_slugify(venue)}"
        nodes.append({
            "id": venue_id, "type": "Venue", "name": venue,
            "meta": {"year": year},
        })
        edges.append({
            "src": paper_id, "type": "PUBLISHED_IN", "dst": venue_id, "meta": {},
        })

    # --- Author nodes + AUTHORED_BY edges ---
    for author_name in meta.get("authors", []) or []:
        aid = f"author:{_slugify(author_name)}"
        nodes.append({
            "id": aid, "type": "Author", "name": author_name, "meta": {},
        })
        edges.append({
            "src": paper_id, "type": "AUTHORED_BY", "dst": aid, "meta": {},
        })

    # --- canonical entity nodes (Method/Dataset/Model/Metric) ---
    # These types are in ALIAS_REQUIRED_TYPES. We emit them with alias_check
    # queried_existing=False + rationale so they pass bootstrap softening
    # (kg-curator handles alias merges; skeleton makes a best-effort identity).
    def _alias_stub(rationale: str) -> dict:
        return {
            "queried_existing": False,
            "matched": None,
            "rationale": rationale,
        }

    entity_specs = [
        ("methods", "Method", "method", "USES_METHOD"),
        ("datasets", "Dataset", "dataset", "USES_DATASET"),
        ("models", "Model", "model", "USES_MODEL"),
        ("metrics", "Metric", "metric", "MEASURES_WITH"),
    ]
    for digest_key, type_name, id_prefix, edge_type in entity_specs:
        for name in meta.get(digest_key, []) or []:
            entity_id = f"{id_prefix}:{_slugify(name)}"
            nodes.append({
                "id": entity_id,
                "type": type_name,
                "name": name,
                "meta": {},
                "alias_check": _alias_stub(
                    f"emitted by kg_skeleton.py from digest frontmatter "
                    f"field `{digest_key}`; kg-curator should resolve aliases"
                ),
            })
            edges.append({
                "src": paper_id, "type": edge_type, "dst": entity_id, "meta": {},
            })

    # --- file envelope ---
    source_sha = hashlib.sha256(digest_path.read_bytes()).hexdigest()
    return {
        "version": 1,
        "source_file": str(digest_path),
        "source_sha": source_sha,
        "author_agent": "kg_skeleton.py",
        "extracted_at": _now_kst_iso(),
        "nodes": nodes,
        "edges": edges,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--digest", required=True, help="path to <slug>.digest.md")
    ap.add_argument("--slug", required=True, help="paper slug")
    ap.add_argument("--out", required=True, help="output .kg.skeleton.json path")
    args = ap.parse_args()

    digest_path = Path(args.digest).resolve()
    out_path = Path(args.out).resolve()

    if not digest_path.exists():
        _log(f"digest not found: {digest_path}")
        return 1

    try:
        meta, _body = _parse_frontmatter(digest_path)
    except Exception as e:  # noqa: BLE001
        _log(f"frontmatter parse failed: {e}")
        return 1

    skeleton = _build_skeleton(meta, args.slug, digest_path)

    # Schema validation (hard requirement — no file written on failure).
    try:
        sys.path.insert(
            0,
            str(Path(__file__).resolve().parent.parent.parent / "paper-kg" / "scripts"),
        )
        from schema import KGFile  # type: ignore
        KGFile.model_validate(skeleton)
    except Exception as e:  # noqa: BLE001
        _log(f"schema validation failed: {e}")
        return 3

    try:
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            json.dumps(skeleton, ensure_ascii=False, indent=2, sort_keys=False) + "\n",
            encoding="utf-8",
        )
    except Exception as e:  # noqa: BLE001
        _log(f"output write failed: {e}")
        return 2

    _log(f"wrote skeleton: {out_path} (nodes={len(skeleton['nodes'])}, edges={len(skeleton['edges'])})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run test to verify it passes**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_summarizer_optimization.py::TestKgSkeleton -v`
Expected: PASS, all 5 `TestKgSkeleton` tests green.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/paper-summarize/scripts/kg_skeleton.py .claude/tests/test_summarizer_optimization.py
git commit -m "feat(kg_skeleton): emit deterministic KG nodes from digest frontmatter

Paper/Author/Venue/Method/Dataset/Model/Metric nodes + AUTHORED_BY,
PUBLISHED_IN, USES_METHOD/DATASET/MODEL, MEASURES_WITH edges.
Does not emit Claim/Result/EVIDENCED_BY — those remain Claude's job.
Output JSON validates against KGFile Pydantic schema.

Part of paper-summarizer token optimization (spec 2026-04-17)."
```

---

## Task 3: `cache_gate.py`

**Files:**
- Create: `.claude/skills/paper-summarize/scripts/cache_gate.py`
- Test: `.claude/tests/test_summarizer_optimization.py` (append `TestCacheGate` class)

- [ ] **Step 1: Write the failing test**

Append to `.claude/tests/test_summarizer_optimization.py`:

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_summarizer_optimization.py::TestCacheGate -v`
Expected: FAIL — script does not exist, `returncode` will be non-zero or `FileNotFoundError`.

- [ ] **Step 3: Write minimal implementation**

Create `.claude/skills/paper-summarize/scripts/cache_gate.py`:

```python
#!/usr/bin/env python3
"""cache_gate.py — classify accepted raw.md paths into {hits, stale, misses}.

Given a list of paper-hunter raw.md paths, determine for each whether its
corresponding Marp summary is:
  - hit:   summary exists AND summary.frontmatter.source_digest_sha256 ==
           sha256(<slug>.digest.md) AND prompt_version matches digest
  - stale: summary exists but the SHA mismatches (including missing field
           from pre-v7 summaries) OR the digest file is corrupt
  - miss:  digest or summary is absent

Output is emitted as JSON (written to --out) with three keys:
    {"hits": [...], "stale": [...], "misses": [...]}

Values are the input raw.md paths verbatim (absolute), so callers can chunk
and re-pass them to the paper-summarizer agent.

Usage:
    python3 cache_gate.py --paths <raw_md> [<raw_md> ...] --out <out.json>

Exit codes:
    0  classification written
    1  input/usage error (a raw.md path does not exist or has no metadata/ ancestor)
    2  output path unwritable
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def _log(msg: str) -> None:
    print(f"[cache_gate] {msg}", file=sys.stderr, flush=True)


def _resolve_slug(raw_md: Path) -> str:
    """Best-effort slug from `<slug>.raw.md` filename, falling back to frontmatter."""
    name = raw_md.name
    if name.endswith(".raw.md"):
        base = name[: -len(".raw.md")]
        if base:
            return base
    # Fallback: parse frontmatter slug scalar.
    text = raw_md.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'^\s*slug\s*:\s*"?([^"\n]+)"?\s*$', text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return raw_md.stem


def _parse_raw_frontmatter(raw_md: Path) -> dict:
    text = raw_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    fm = text[3:end]
    meta: dict = {}
    for line in fm.splitlines():
        m = re.match(r'^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:\s*"?([^"\n]*)"?\s*$', line)
        if m:
            meta[m.group(1)] = m.group(2).strip()
    return meta


def _papers_root(raw_md: Path) -> Path | None:
    """Walk up until we find `.../papers/metadata/...` and return `.../papers`."""
    parts = raw_md.parts
    try:
        idx = parts.index("metadata")
    except ValueError:
        return None
    return Path(*parts[:idx])


def _venue_year_subpath(raw_md: Path) -> Path | None:
    parts = raw_md.parts
    try:
        idx = parts.index("metadata")
    except ValueError:
        return None
    return Path(*parts[idx + 1 : -1])


def _digest_path(raw_md: Path, slug: str) -> Path | None:
    root = _papers_root(raw_md)
    sub = _venue_year_subpath(raw_md)
    if root is None or sub is None:
        return None
    return root / "digest" / sub / f"{slug}.digest.md"


def _summary_path(raw_md: Path, slug: str) -> Path | None:
    """Route by venue_class: whitelist → <V>/<Y>/, etc → etc/<Y>/."""
    root = _papers_root(raw_md)
    sub = _venue_year_subpath(raw_md)
    if root is None or sub is None:
        return None
    meta = _parse_raw_frontmatter(raw_md)
    vc = meta.get("venue_class", "whitelist")
    if vc == "etc":
        # sub is <Venue>/<Year>; etc flattens to etc/<Year>
        year = Path(*sub.parts[1:]) if len(sub.parts) >= 2 else sub
        return root / "marp-summary" / "etc" / year / f"{slug}.md"
    return root / "marp-summary" / sub / f"{slug}.md"


def _parse_summary_cache_fields(summary: Path) -> tuple[str | None, str | None]:
    """Return (source_digest_sha256, prompt_version) from summary frontmatter."""
    try:
        text = summary.read_text(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        return None, None
    if not text.startswith("---"):
        return None, None
    end = text.find("\n---", 3)
    if end < 0:
        return None, None
    fm = text[3:end]
    sha = None
    pv = None
    for line in fm.splitlines():
        m = re.match(r'^\s*source_digest_sha256\s*:\s*"?([^"\n]+)"?\s*$', line)
        if m:
            sha = m.group(1).strip()
        m2 = re.match(r'^\s*prompt_version\s*:\s*"?([^"\n]+)"?\s*$', line)
        if m2:
            pv = m2.group(1).strip()
    return sha, pv


def _parse_digest_prompt_version(digest: Path) -> str | None:
    try:
        text = digest.read_text(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    fm = text[3:end]
    for line in fm.splitlines():
        m = re.match(r'^\s*prompt_version\s*:\s*"?([^"\n]+)"?\s*$', line)
        if m:
            return m.group(1).strip()
    return None


def _classify_one(raw_md: Path) -> str:
    """Return one of 'hit' | 'stale' | 'miss'."""
    slug = _resolve_slug(raw_md)
    digest = _digest_path(raw_md, slug)
    summary = _summary_path(raw_md, slug)
    if digest is None or summary is None:
        return "miss"
    if not digest.exists():
        return "miss"
    if not summary.exists():
        return "miss"

    try:
        digest_sha = hashlib.sha256(digest.read_bytes()).hexdigest()
    except Exception as e:  # noqa: BLE001
        _log(f"digest sha calc failed for {digest}: {e} → stale")
        return "stale"

    cached_sha, cached_pv = _parse_summary_cache_fields(summary)
    if cached_sha is None:
        return "stale"
    if cached_sha != digest_sha:
        return "stale"

    digest_pv = _parse_digest_prompt_version(digest)
    if digest_pv is not None and cached_pv is not None and digest_pv != cached_pv:
        return "stale"
    return "hit"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--paths", nargs="+", required=True,
                    help="absolute paths to <slug>.raw.md files")
    ap.add_argument("--out", required=True, help="output JSON path")
    args = ap.parse_args()

    result: dict[str, list[str]] = {"hits": [], "stale": [], "misses": []}
    for p_str in args.paths:
        raw_md = Path(p_str).resolve()
        if not raw_md.exists():
            _log(f"raw.md missing: {raw_md} → treating as miss")
            result["misses"].append(str(raw_md))
            continue
        cls = _classify_one(raw_md)
        if cls == "hit":
            result["hits"].append(str(raw_md))
        elif cls == "stale":
            result["stale"].append(str(raw_md))
        else:
            result["misses"].append(str(raw_md))

    try:
        out_path = Path(args.out).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(
            json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
    except Exception as e:  # noqa: BLE001
        _log(f"output write failed: {e}")
        return 2

    _log(
        f"classified: hits={len(result['hits'])} "
        f"stale={len(result['stale'])} misses={len(result['misses'])}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

- [ ] **Step 4: Run test to verify it passes**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_summarizer_optimization.py::TestCacheGate -v`
Expected: PASS, 8 `TestCacheGate` tests green.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/paper-summarize/scripts/cache_gate.py .claude/tests/test_summarizer_optimization.py
git commit -m "feat(cache_gate): classify raw.md paths into hits/stale/misses

Compares sha256(<slug>.digest.md) against summary frontmatter's
source_digest_sha256 + prompt_version. When-in-doubt defaults to stale
(regeneration is cheaper than serving a wrong cached output).

Routes etc venue_class summaries to papers/marp-summary/etc/<Year>/.

Part of paper-summarizer token optimization (spec 2026-04-17)."
```

---

## Task 4: Bump `gemini_digest.py` PROMPT_VERSION and add entity-list frontmatter fields

**Files:**
- Modify: `.claude/skills/paper-summarize/scripts/gemini_digest.py`

- [ ] **Step 1: Bump PROMPT_VERSION**

In `.claude/skills/paper-summarize/scripts/gemini_digest.py`, change line 45 from:

```python
PROMPT_VERSION = "v6"
```

to:

```python
PROMPT_VERSION = "v7"
```

- [ ] **Step 2: Extend DIGEST_PROMPT with entity-extraction instructions**

In the same file, inside the `DIGEST_PROMPT` string literal (line 54–109), add a new numbered instruction between the current instruction 4 ("For each section, extract exhaustively") and instruction 5 ("After all paper sections, append these fixed sections"). The new instruction must produce four YAML-compatible lists that `kg_skeleton.py` can read.

Replace the block:

```
5. **After all paper sections, append these fixed sections**:
```

with:

```
5. **Entity extraction block (mandatory, before the Figures/Candidates block)**:
   Emit a `## Entities` H2 section immediately before `# Figures and Tables index`. The section body MUST be exactly four labeled list lines, one per list, bullet style `- `, with items wrapped in double-quotes. Items are case-preserved, deduplicated, max 10 per list. Use empty square brackets `[]` when the paper has none.

```
## Entities
- methods: ["<MethodA>", "<MethodB>"]
- datasets: ["<DatasetX>"]
- models: ["<Model Family Size>"]
- metrics: ["<MetricP>"]
```

   Rules:
   - `methods` = distinct method names the paper introduces or compares as baselines. Not loss functions, not layers.
   - `datasets` = public or described datasets used in training or evaluation. Not generic phrases like "synthetic data".
   - `models` = concrete model families/sizes referenced (e.g. "GPT-2 124M", "Llama-3 8B"). Not architecture classes in general.
   - `metrics` = evaluation metric names (Perplexity, BLEU, Accuracy, ...).
   - Keep items short (≤ 40 chars each). No trailing commas. No nested structures.

6. **After the Entities block, append these fixed sections**:
```

- [ ] **Step 3: Propagate new fields into the digest frontmatter writer**

In `_write_digest` (function starting around line 580), after the existing `fm_lines` list assembly and before the `if figures:` block, add extraction of the entity lists from the body. Insert a helper at the top of `_write_digest` that parses the four list lines from the body:

```python
def _extract_entities(body: str) -> dict[str, list[str]]:
    """Extract the four `- methods:/datasets:/models:/metrics: [...]` lines
    emitted by Gemini under the `## Entities` H2.

    Returns a dict with exactly those four keys, each a list of strings
    (possibly empty). If the Entities block is missing or malformed, all
    four lists are empty (best-effort; downstream kg_skeleton treats missing
    fields as empty too).
    """
    out = {"methods": [], "datasets": [], "models": [], "metrics": []}
    block_match = re.search(
        r"^##\s+Entities\s*$(.*?)^#",
        body,
        flags=re.MULTILINE | re.DOTALL,
    )
    if not block_match:
        return out
    block = block_match.group(1)
    for key in out:
        line_m = re.search(
            rf'^\s*-\s*{key}\s*:\s*\[(.*?)\]\s*$',
            block,
            flags=re.MULTILINE,
        )
        if not line_m:
            continue
        inner = line_m.group(1).strip()
        if not inner:
            continue
        items = re.findall(r'"([^"]+)"', inner)
        # dedup while preserving order
        seen = set()
        ordered = []
        for it in items:
            if it and it not in seen:
                seen.add(it)
                ordered.append(it)
        out[key] = ordered[:10]
    return out
```

Then, in `_write_digest`, extract entities and emit them as YAML list blocks. Find the section that currently emits frontmatter (fm_lines assembly around lines 606–630) and insert entity emission just before the `if figures:` block:

```python
    entities = _extract_entities(body)
    for key in ("methods", "datasets", "models", "metrics"):
        vals = entities.get(key, [])
        if vals:
            fm_lines.append(f"{key}:")
            for v in vals:
                fm_lines.append(f"  - {_yaml_str(v)}")
        else:
            fm_lines.append(f"{key}: []")
```

Also add `authors` if not already present — the raw.md frontmatter exposes authors in the `meta` dict. Append before the entity block:

```python
    authors_raw = meta.get("authors", "")
    # meta["authors"] is a JSON-array string (hunter emits json.dumps(authors));
    # fall back to CSV split only for legacy/malformed raw.md.
    authors: list[str] = []
    if isinstance(authors_raw, list):
        authors = [str(a).strip() for a in authors_raw if str(a).strip()]
    elif isinstance(authors_raw, str):
        s = authors_raw.strip()
        if s.startswith("[") and s.endswith("]"):
            try:
                parsed = json.loads(s)
                if isinstance(parsed, list):
                    authors = [str(a).strip() for a in parsed if str(a).strip()]
            except Exception:
                pass
        if not authors and s:
            authors = [a.strip().strip('"\'') for a in s.split(",") if a.strip()]
    if authors:
        fm_lines.append("authors:")
        for a in authors:
            fm_lines.append(f"  - {_yaml_str(a)}")
    else:
        fm_lines.append("authors: []")
```

- [ ] **Step 4: Sanity check the script parses & imports**

Run: `conda run -n LLDM python -c "import importlib.util, sys; spec = importlib.util.spec_from_file_location('g', '.claude/skills/paper-summarize/scripts/gemini_digest.py'); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); print(m.PROMPT_VERSION)"`
Expected: prints `v7`.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/paper-summarize/scripts/gemini_digest.py
git commit -m "feat(gemini_digest): bump PROMPT_VERSION v6→v7, add entity frontmatter

Gemini now emits a '## Entities' block with methods/datasets/models/metrics
lists. _write_digest parses the block and emits them (plus authors from
raw.md frontmatter) as YAML list fields in the digest frontmatter.

kg_skeleton.py consumes these fields to build the deterministic portion of
the paper's .kg.json without requiring Claude to restate them.

Prompt version bump invalidates all existing digest caches; summaries
built from v6 digests will be classified 'stale' by cache_gate on next run.

Part of paper-summarizer token optimization (spec 2026-04-17)."
```

---

## Task 5: Update `paper-summarizer.md` agent

**Files:**
- Modify: `.claude/agents/paper-summarizer.md`

- [ ] **Step 1: Replace the Input/Output protocol section**

Open `.claude/agents/paper-summarizer.md`. Replace the section currently at lines 72–76:

```markdown
## 입력/출력 프로토콜

- **입력**: `papers/metadata/<V>/<Y>/<slug>.raw.md` + 실제 PDF 전문 (Gemini digest 경유)
- **출력**: `papers/marp-summary/<V>/<Y>/<slug>.md` (Marp, adaptive outline + 4개 앵커)
- **형식**: `paper-summarize` 스킬의 adaptive 템플릿 그대로
```

with:

```markdown
## 입력/출력 프로토콜

- **입력**: `batch_paths: List[str]` — 한 호출에서 B=5개의 `papers/metadata/<V>/<Y>/<slug>.raw.md` 절대경로를 받는다 (cache_gate.py가 stale+miss로 분류한 것만). 단일 paper 호출도 `batch_paths`에 하나만 담아 받는다. 구(舊) `accepted_path` 단일 필드는 더 이상 사용하지 않는다.
- **처리 순서 (각 raw.md에 대해)**:
  1. `python3 .claude/skills/paper-summarize/scripts/gemini_digest.py <raw_md>` 를 실행해 `papers/digest/<V>/<Y>/<slug>.digest.md` 생성 (이미 cache-hit이면 스크립트가 즉시 리턴).
  2. `python3 .claude/skills/paper-summarize/scripts/kg_skeleton.py --digest <digest_path> --slug <slug> --out <papers/digest/<V>/<Y>/<slug>.kg.skeleton.json>` 를 실행. exit code ≠ 0이면 fallback (Claude가 KG 전체 작성).
  3. digest + skeleton을 Read하고, Marp 본문 + KG patch (Claim/Result/EVIDENCED_BY 추가)를 작성.
  4. `papers/marp-summary/<V|etc>/<Y>/<slug>.md` 저장. frontmatter에 **반드시** 다음 4 필드:
     - `source_digest_sha256: "<sha256 of the digest.md file>"`
     - `prompt_version: "<same value as digest frontmatter prompt_version>"`
     - `venue_class: "whitelist" | "etc"`
     - `kg_skeleton_used: true | false` (skeleton fallback이면 false)
  5. `papers/marp-summary/<V|etc>/<Y>/<slug>.kg.json` 저장 — skeleton이 있으면 skeleton을 기반으로 Claim/Result 노드 + MAKES_CLAIM / REPORTS_RESULT / EVIDENCED_BY 엣지만 추가.
- **출력**: `batch_paths` 안의 모든 paper에 대해 (4)와 (5). 중도 실패 시 어느 slug에서 멈췄는지 stderr에 기록.
- **형식**: `paper-summarize` 스킬의 adaptive 템플릿 그대로 (4개 필수 앵커 + PLANNING 블록).
```

- [ ] **Step 2: Add `source_digest_sha256` + skeleton workflow to 작업 원칙**

In the same file, in the `## 작업 원칙` section, after the bullet `**결과표는 Markdown 표**...` (around line 60), append three new bullets at the end of the list (before the `## 입력/출력 프로토콜` heading):

```markdown
- **Frontmatter cache 계약 (필수)**: 저장하는 Marp `<slug>.md`의 YAML frontmatter에 **반드시** `source_digest_sha256`와 `prompt_version`을 써라. 값은 digest.md의 sha256과 digest frontmatter의 `prompt_version`을 그대로 복사. 이 필드가 없으면 cache_gate.py가 다음 실행에서 전부 stale로 재생성시킨다.
- **KG skeleton patch flow (필수)**: `kg_skeleton.py`가 쓴 `<slug>.kg.skeleton.json`을 읽어 그 위에 Claim/Result 노드 + MAKES_CLAIM / REPORTS_RESULT / EVIDENCED_BY 엣지만 얹어라. Paper/Author/Venue/Method/Dataset/Model/Metric 노드와 AUTHORED_BY/PUBLISHED_IN/USES_METHOD/USES_DATASET/USES_MODEL/MEASURES_WITH 엣지는 **다시 쓰지 말 것** — skeleton이 이미 만든 것을 중복 쓰면 nodes/edges가 두 배가 되고 kg-curator가 alias 충돌을 잡는다. skeleton 파일이 없거나 exit code ≠ 0이었으면 예외적으로 Claude가 KG 전체를 작성하고 frontmatter에 `kg_skeleton_used: false`를 써라.
- **Batch 순차 처리**: `batch_paths`의 각 paper를 한 개씩 처리하되, 한 paper 실패(예: gemini_digest exit 3 — PDF 확보 실패)가 배치 전체를 중단시키지 않도록 `try/except`로 감싸고, 실패 slug는 stderr에 `BATCH FAIL: <slug> reason=<...>`로 기록한 뒤 다음 paper로 계속.
```

- [ ] **Step 3: Run the existing phase-C refactor regression test to confirm no breakage**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_phase_c_refactor.py -v`
Expected: PASS — this edit does not touch any invariant the existing tests check.

- [ ] **Step 4: Commit**

```bash
git add .claude/agents/paper-summarizer.md
git commit -m "docs(paper-summarizer): wire batch_paths input + kg_skeleton flow

- Replace single accepted_path with batch_paths: List[str]
- Mandate source_digest_sha256 + prompt_version in output frontmatter
  (cache_gate.py reads these on next run)
- Add kg_skeleton.py invocation + patch flow (Claude only writes
  Claim/Result/EVIDENCED_BY on top of the skeleton)
- Per-paper try/except so one bad PDF doesn't kill the batch

Part of paper-summarizer token optimization (spec 2026-04-17)."
```

---

## Task 6: Update `paper-summarize/SKILL.md`

**Files:**
- Modify: `.claude/skills/paper-summarize/SKILL.md`

Prior read of the file showed Step 2a–2e covering digest read / PLANNING / body fill / image embed / save. We insert Step 2.0 before Step 2a and Step 2f after Step 2e.

- [ ] **Step 1: Read the current SKILL.md structure**

Run: `grep -n '^## \|^### ' .claude/skills/paper-summarize/SKILL.md`
Expected: prints all H2/H3 headings — use this to locate the exact anchor for Step 2.0 insertion. The anchor is immediately before the section describing "Step 2a" (look for the H2 or H3 heading that introduces Stage 2 step-by-step).

- [ ] **Step 2: Insert Step 2.0 (cache gate) at the start of Stage 2**

Find the line that currently reads similar to `### Step 2a — Read the digest` (or `#### 2a.`). Insert above it (as a new heading at the same level):

```markdown
### Step 2.0 — Agent-level cache re-check (idempotency guard)

Before running any summarization work, verify that this paper was not already summarized in a concurrent run. The main-session cache_gate.py filtered the batch, but a race is possible (two `/research-papers` runs on the same slug).

```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-summarize/scripts/cache_gate.py \
    --paths "<this_paper_raw_md>" \
    --out /tmp/cache_gate_recheck_<slug>.json
```

Parse the JSON. If `hits` contains this paper's path, skip the remaining steps for this paper and go to the next one in `batch_paths`. Log `[summarizer] cache re-check: <slug> already fresh — skipping`.

This step is cheap (~100ms per paper) and guards against wasted work when two main sessions race.
```

- [ ] **Step 3: Insert Step 2f (KG skeleton patch flow) after Step 2e**

Find the last numbered step in Stage 2 (Step 2e or its rename — the one that saves the final `.md` and `.kg.json`). Insert a new step immediately before the save step so that the skeleton invocation precedes writing the KG file:

```markdown
### Step 2f — Invoke kg_skeleton.py and patch Claim/Result on top

Before writing `<slug>.kg.json`, generate the deterministic skeleton:

```bash
python3 /home/irteam/sw/research_hub/.claude/skills/paper-summarize/scripts/kg_skeleton.py \
    --digest <papers/digest/<V>/<Y>/<slug>.digest.md> \
    --slug <slug> \
    --out <papers/digest/<V>/<Y>/<slug>.kg.skeleton.json>
```

Capture the exit code:
- `0` — skeleton written successfully. Read the file, preserve every existing node + edge, then **append only**:
  - `Claim` nodes (one per distinct empirical claim the paper makes)
  - `Result` nodes (one per reported metric × method × dataset cell)
  - `MAKES_CLAIM` edges from `paper:<slug>` to each new `claim:<slug>#N`
  - `REPORTS_RESULT` edges from `paper:<slug>` to each new `result:<slug>#N`
  - `EVIDENCED_BY` edges from claims to supporting results (must include `meta.polarity ∈ {support, contradict, mixed}`)

  Write the merged structure to `<slug>.kg.json` (not `.kg.skeleton.json`). Set `kg_skeleton_used: true` in the Marp frontmatter.

- `1`, `2`, or `3` (non-zero) — skeleton step failed. Fall back to authoring the full KG file from scratch (Paper/Author/Venue/Method/.../Claim/Result). Set `kg_skeleton_used: false` in the Marp frontmatter. This is the pre-v7 behavior; no correctness regression.

**Invariant**: the skeleton file itself is a build artefact in `papers/digest/<V>/<Y>/`. It is not versioned, not an agent deliverable, and can be deleted at any time without breaking anything (next run regenerates it).
```

- [ ] **Step 4: Add 3 checklist items**

Locate the checklist at the end of the SKILL.md (search for `## Checklist` or similar heading). Add three new items:

```markdown
- [ ] Frontmatter `source_digest_sha256` matches `sha256(<slug>.digest.md)` byte-for-byte
- [ ] Frontmatter `prompt_version` equals digest's `prompt_version` (both should be `v7` for new summaries)
- [ ] Looped over every entry in `batch_paths` — none silently skipped except via Step 2.0 cache re-check
```

- [ ] **Step 5: Verify SKILL.md still parses as markdown and the skill tests (if any) pass**

Run: `conda run -n LLDM python -m pytest .claude/tests/ -v`
Expected: PASS — all existing tests + new Task 1–3 tests green. No regressions.

- [ ] **Step 6: Commit**

```bash
git add .claude/skills/paper-summarize/SKILL.md
git commit -m "docs(paper-summarize skill): add Step 2.0 cache gate + Step 2f KG skeleton

- Step 2.0 re-checks cache_gate before summarization starts (guards
  against races between concurrent main sessions on the same slug)
- Step 2f invokes kg_skeleton.py and patches Claim/Result on top;
  falls back to full-KG authoring on skeleton failure (kg_skeleton_used=false)
- Three new checklist items lock in the frontmatter contract and
  the batch-loop invariant

Part of paper-summarizer token optimization (spec 2026-04-17)."
```

---

## Task 7: Rewrite `research-papers.md` §Step 6 A-3

**Files:**
- Modify: `.claude/commands/research-papers.md` (lines 189–210, the **A-3 — paper-summarizer** block)

- [ ] **Step 1: Read the current A-3 block to find exact line range**

Run: `grep -n '^\*\*A-3 \|^\*\*A-4 ' .claude/commands/research-papers.md`
Expected: prints the line numbers of the `**A-3 — paper-summarizer**` and `**A-4 — rag-curator**` headings so we can replace the block between them cleanly.

- [ ] **Step 2: Replace the A-3 block**

Replace the entire block from `**A-3 — paper-summarizer**` through (but not including) `**A-4 — rag-curator**` with:

```markdown
**A-3 — paper-summarizer**

A-3 now runs in three phases: (1) classify accepted papers via cache_gate.py, (2) chunk the stale+miss set into batches of 5, (3) dispatch paper-summarizer sequentially with `run_in_background: true` for each batch.

```bash
# --- Phase 1: snapshot + cache classification ---
PRE_A3_SUMMARY_COUNT=$(find papers/marp-summary -name '*.md' 2>/dev/null | wc -l)
CACHE_OUT=$(mktemp --suffix=.json)

# ACCEPTED_PATHS is a bash array of absolute raw.md paths from A-2's return body.
# Build it by splitting the agent return body on newlines (one path per line).
python3 /home/irteam/sw/research_hub/.claude/skills/paper-summarize/scripts/cache_gate.py \
    --paths "${ACCEPTED_PATHS[@]}" \
    --out "$CACHE_OUT"

HITS_N=$(python3 -c "import json, sys; print(len(json.load(open('$CACHE_OUT'))['hits']))")
STALE_N=$(python3 -c "import json, sys; print(len(json.load(open('$CACHE_OUT'))['stale']))")
MISS_N=$(python3 -c "import json, sys; print(len(json.load(open('$CACHE_OUT'))['misses']))")
echo "[A-3 cache] hits=$HITS_N stale=$STALE_N misses=$MISS_N"

# TO_RUN = stale + misses (absolute raw.md paths, as JSON list)
TO_RUN_JSON=$(python3 -c "
import json, sys
d = json.load(open('$CACHE_OUT'))
print(json.dumps(d['stale'] + d['misses']))
")
TO_RUN_COUNT=$(python3 -c "import json, sys; print(len(json.loads('$TO_RUN_JSON')))")

if [ "$TO_RUN_COUNT" -eq 0 ]; then
  echo "[A-3] fully cached — no dispatch needed"
else
  # --- Phase 2: chunk into B=5 batches ---
  BATCHES_JSON=$(python3 -c "
import json, sys
sys.path.insert(0, '/home/irteam/sw/research_hub/.claude/scripts')
from chunk_helper import chunk_paths
print(json.dumps(chunk_paths(json.loads('$TO_RUN_JSON'), batch_size=5)))
")
  N_BATCHES=$(python3 -c "import json; print(len(json.loads('$BATCHES_JSON')))")
  echo "[A-3] chunked $TO_RUN_COUNT papers into $N_BATCHES batches of ≤5"
fi
```

**Phase 3 — sequential dispatch (main session, one Agent call per batch):**

For each batch index `i ∈ [0, N_BATCHES)`:

1. Compute `PRE_BATCH_COUNT = find papers/marp-summary -name '*.md' | wc -l`.
2. Extract the i-th batch as a JSON list: `BATCH_I=$(python3 -c "import json; print(json.dumps(json.loads('$BATCHES_JSON')[$i]))")`.
3. Dispatch the agent:

   ```
   Agent(
     subagent_type: "paper-summarizer",
     run_in_background: true,
     prompt: {
       stage: papers,
       slug: <slug>,
       stage_version: <N>,
       batch_paths: <BATCH_I as JSON array>,
     }
   )
   ```

4. Wait for task-notification.
5. Compute `POST_BATCH_COUNT = find papers/marp-summary -name '*.md' | wc -l`.
6. Compute `BATCH_SIZE = jq 'length' <<< "$BATCH_I"`.
7. **If `POST_BATCH_COUNT - PRE_BATCH_COUNT != BATCH_SIZE`**: FAIL FAST. Do not dispatch subsequent batches. Surface the shortfall to the user with the list of paths in the failed batch, exit 9.
8. Otherwise continue to batch `i+1`.

After all batches complete:

```bash
POST_A3_SUMMARY_COUNT=$(find papers/marp-summary -name '*.md' 2>/dev/null | wc -l)
DELTA=$((POST_A3_SUMMARY_COUNT - PRE_A3_SUMMARY_COUNT))
if [ "$DELTA" -ne "$TO_RUN_COUNT" ]; then
  echo "A-3 aggregate delta mismatch: got $DELTA, expected $TO_RUN_COUNT"
  exit 9
fi
```

Advance to A-4:
```bash
python3 .../loop_state.py stage-advance --to A-4
```

**User-interrupt handling within A-3**: because each batch is a single `run_in_background: true` Agent call, a user mid-batch message does not cancel the batch. Between batches, if the user has intervened, dialogue first and only dispatch batch `i+1` with the user's intent.

```

- [ ] **Step 3: Verify markdown integrity**

Run: `grep -c '^\*\*A-[1-4]' .claude/commands/research-papers.md`
Expected: `4` (one `**A-1**`, `**A-2**`, `**A-3**`, `**A-4**` heading each, same as before).

- [ ] **Step 4: Run existing phase-C refactor regression test**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_phase_c_refactor.py -v`
Expected: PASS — the refactor test only checks for sub-phase tokens and `run_in_background: true`, both of which the new A-3 block contains.

- [ ] **Step 5: Commit**

```bash
git add .claude/commands/research-papers.md
git commit -m "refactor(research-papers): rewrite §Step 6 A-3 with cache gate + B=5 batching

Three-phase A-3:
  1. cache_gate.py classifies accepted paths into hits/stale/misses
  2. chunk_helper.chunk_paths splits stale+misses into B=5 batches
  3. sequential run_in_background Agent dispatches, one batch at a time

Per-batch delta verification catches partial agent failures and fails
fast; no subsequent batches dispatched when a batch underproduces.

Hits are skipped entirely, saving the dominant A-3 token cost for
re-runs of the same slug.

Part of paper-summarizer token optimization (spec 2026-04-17)."
```

---

## Task 8: Regression assertions in `test_phase_c_refactor.py`

**Files:**
- Modify: `.claude/tests/test_phase_c_refactor.py`

- [ ] **Step 1: Append a new test class**

Open `.claude/tests/test_phase_c_refactor.py`. At the end of the file (before any `if __name__ == "__main__":` block), append:

```python
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
```

- [ ] **Step 2: Run all Phase-C refactor tests**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_phase_c_refactor.py -v`
Expected: PASS — both the original classes (`OrchestratorRemoved`, etc.) and the new `TokenOptimizationContract` pass.

- [ ] **Step 3: Run the full new test file to confirm everything is green**

Run: `conda run -n LLDM python -m pytest .claude/tests/test_summarizer_optimization.py .claude/tests/test_phase_c_refactor.py -v`
Expected: PASS across all test classes (`TestChunkHelper`, `TestKgSkeleton`, `TestCacheGate`, plus original + new `test_phase_c_refactor` classes).

- [ ] **Step 4: Commit**

```bash
git add .claude/tests/test_phase_c_refactor.py
git commit -m "test(phase_c): assert token-optimization file contracts

Lock in that research-papers.md, paper-summarizer.md, SKILL.md, and
gemini_digest.py all carry the token-optimization wiring tokens
(cache_gate, chunk_helper, batch_paths, kg_skeleton, PROMPT_VERSION v7).
Also assert the three new scripts exist.

Protects against accidental rollback of spec 2026-04-17."
```

---

## Task 9: Manual smoke validation (one-time, documented here for the engineer)

**Not a code task — a runtime validation the engineer runs once after Tasks 1–8 are merged. No commit.**

- [ ] **Step 1: Pick a small test topic**

Invoke `/research-papers` with a narrow topic that will accept ~5–10 papers, e.g. `/research-papers "attention sinks in discrete diffusion language models"`. Run the full Phase A → B → C cycle.

- [ ] **Step 2: Verify first-run cache log**

Expected in A-3 stderr/output:
```
[A-3 cache] hits=0 stale=0 misses=N   # where N == accepted count
[A-3] chunked N papers into ceil(N/5) batches of ≤5
```

- [ ] **Step 3: Verify summaries carry the new frontmatter**

Pick one file from `papers/marp-summary/**/*.md` and confirm frontmatter has:

```
source_digest_sha256: "..."
prompt_version: "v7"
venue_class: "whitelist" | "etc"
kg_skeleton_used: true
```

- [ ] **Step 4: Re-run the same slug**

Invoke `/research-papers --slug <slug-from-step-1>`. Expected A-3 log:
```
[A-3 cache] hits=N stale=0 misses=0
[A-3] fully cached — no dispatch needed
```
0 Agent dispatches in A-3. Report.md/Report.slides.md should still be regenerated.

- [ ] **Step 5: Force a cache invalidation via manual PROMPT_VERSION bump**

Edit `.claude/skills/paper-summarize/scripts/gemini_digest.py` and set `PROMPT_VERSION = "v7.1"`. Re-run the same slug. Expected:
```
[A-3 cache] hits=0 stale=N misses=0
[A-3] chunked N papers into ceil(N/5) batches of ≤5
```

Revert the PROMPT_VERSION change back to `"v7"` after the validation — do not commit v7.1.

---

## Self-Review Results

**Spec coverage:**
- §1 Architecture (X — batch B=5 + cache_gate + kg_skeleton) → Tasks 1+3+2.
- §2.1 cache_gate.py → Task 3.
- §2.2 kg_skeleton.py → Task 2.
- §2.3 paper-summarizer agent → Task 5.
- §2.4 SKILL.md → Task 6.
- §2.5 gemini_digest.py v7 + entity fields → Task 4.
- §2.6 research-papers.md §Step 6 A-3 → Task 7.
- §2.7 chunk_helper.py → Task 1.
- §3 Data Flow — exercised by Tasks 1+3+5+6+7 collectively.
- §4 Error Handling — Tasks 2 (fallback), 3 (when-in-doubt stale), 7 (fail fast), 5 (per-paper try/except).
- §5 Testing — Task 1+2+3 tests, Task 8 regression, Task 9 smoke.
- §6 Quality axis impact — no code change, captured in spec.
- §7 Migration — Task 4's v6→v7 bump classifies all existing summaries as stale on next run, per spec §7.
- §8 Out-of-scope — correctly not implemented (parallel dispatch, `--no-refresh-stale`, token-delta measurement).

No gaps found.

**Placeholder scan:** no `TBD`/`TODO` tokens in plan body. Every task has exact file paths, exact code, exact commands.

**Type consistency:**
- `chunk_paths(paths, batch_size=5)` signature identical across Tasks 1 (creation), 7 (usage), 8 (assertion).
- `cache_gate.py --paths ... --out ...` signature identical across Tasks 3 (creation), 6 (SKILL.md Step 2.0), 7 (research-papers A-3), 8 (assertion).
- `kg_skeleton.py --digest ... --slug ... --out ...` signature identical across Tasks 2 (creation), 5 (agent), 6 (SKILL.md Step 2f), 8 (assertion).
- Frontmatter field names (`source_digest_sha256`, `prompt_version`, `kg_skeleton_used`, `venue_class`) identical across Tasks 3 (cache_gate reads), 5 (agent writes), 6 (SKILL.md checklist), 8 (assertion).
- PROMPT_VERSION = `"v7"` consistent across Tasks 4, 8, and the smoke validation.

No inconsistencies found.

---

## Execution Handoff

**Plan complete and saved to** `docs/superpowers/plans/2026-04-17-paper-summarizer-token-opt.md`.

Two execution options:

**1. Subagent-Driven (recommended)** — I dispatch a fresh subagent per task, two-stage review (spec compliance + code quality) between tasks, fast iteration. Uses superpowers:subagent-driven-development.

**2. Inline Execution** — Execute tasks in this session using superpowers:executing-plans, batch execution with checkpoints for your review.

Which approach?
