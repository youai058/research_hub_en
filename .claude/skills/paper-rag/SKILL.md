---
name: paper-rag
description: "Paper RAG (ChromaDB + bge-m3). Per-section chunking with equation / table preservation, SHA256 incremental upsert, query.py, manifest. Used by rag-curator / answer-formulator / planner. Triggers: 'RAG indexing', 'vector query', 'paper search', 'chroma update'."
---

# Paper RAG Skill

Vector RAG pipeline over ChromaDB + bge-m3. Scripts are bundled under `scripts/` and invoked by rag-curator.

## Stack

- **Embedding**: `BAAI/bge-m3` via `sentence-transformers`
- **Store**: `chromadb.PersistentClient(path="papers/vector_db/chroma")`, collection=`"papers"`
- **Chunker**: per section (`##` heading), preserving equation blocks (`$$...$$`) and tables; chunk_size ≤ 1200 tokens
- **Hash**: `hashlib.sha256(file_bytes)` → stored in manifest

## File layout

```
.claude/skills/paper-rag/
├── SKILL.md
└── scripts/
    ├── index.py    full / incremental indexing
    ├── query.py    top-k query CLI
    └── status.py   manifest / collection status report
```

## Incremental indexing algorithm

```
1. Collect papers/marp-summary/**/*.md
2. Compute SHA256 per file
3. Compare with existing hashes in manifest.json
   - new file: chunk + embed + upsert (ID: slug_section_chunk)
   - changed: delete old chunk IDs → re-embed + upsert
   - removed: delete from collection
4. Update manifest.json
5. Append to chunks.jsonl (append-only)
```

## Query interface

CLI:
```bash
python3 .claude/skills/paper-rag/scripts/query.py "your question" --k 5 --filter venue=ICLR
```

Output (stdout JSON):
```json
[
  {
    "id": "attack-lldm_3_1",
    "score": 0.87,
    "source": "papers/marp-summary/ICLR/2026/attack-lldm.md",
    "section": "Methodology",
    "text": "...chunk text preview..."
  }
]
```

Programmatic call (Python):
```python
import subprocess, json
r = subprocess.run(
    ["python3", ".claude/skills/paper-rag/scripts/query.py", q, "--k", "5"],
    capture_output=True, text=True, check=True,
)
results = json.loads(r.stdout)
```

## Environment setup

```bash
conda activate LLDM
pip install chromadb sentence-transformers
# bge-m3 auto-downloads from HuggingFace on first use (~2.3 GB)
```

## Chunking rules

1. Split sections on `##` headings
2. If section text exceeds 1200 tokens, split further at paragraph boundaries
3. `$$...$$` equation blocks are **not split**
4. `|...|` table blocks are **not split**
5. Chunk metadata: `{slug, section_title, section_idx, chunk_idx, venue, year, authors}`

Token approximation: `len(text.split()) * 1.3` (English). If Korean / equations are mixed, use `tiktoken` for precision.

## manifest.json structure

```json
{
  "version": 1,
  "embed_model": "BAAI/bge-m3",
  "last_update": "2026-04-14T15:00:00+09:00",
  "files": {
    "papers/marp-summary/ICLR/2026/attack-lldm.md": {
      "sha256": "abc123...",
      "mtime": 1234567890,
      "chunks": 12,
      "chunk_ids": ["attack-lldm_0_0", "attack-lldm_1_0", ...]
    }
  },
  "cursors": {"arxiv:cs.CL:...": {...}}
}
```

## Failure modes

- bge-m3 download failure: use a HuggingFace mirror or offline cache
- OOM during embedding: reduce batch_size from 32 → 8
- ChromaDB corruption: back up `papers/vector_db/chroma/` and full-reindex (`index.py --rebuild`)
- Corrupt manifest: `index.py --rebuild-manifest` recomputes hashes

## Query quality tips

- Narrow with `--filter venue=ICLR year=2025` for quality
- For abstract questions (e.g., "relation between diffusion and jailbreak"), decompose into multiple keyword queries and issue each
- Recommended top-k 5–10. Too many → noise.

## Checklist

- [ ] `chromadb`, `sentence-transformers`, `pymupdf` installed
- [ ] `papers/vector_db/chroma/` directory exists
- [ ] `manifest.json` initialized or loaded
- [ ] Incremental indexing performed
- [ ] Query smoke test (≥ 1 result for an arbitrary query)
