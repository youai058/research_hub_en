---
name: abstract-index
description: "raw.md abstract indexer for paper-triage dense-retrieval pre-filter. Incremental bge-m3 upsert into ChromaDB collection 'abstracts'. Trigger: 'index abstracts', 'pre-index before triage', 'refresh abstracts collection'."
---

# Abstract Index Skill

Dedicated skill that incrementally refreshes the `abstracts` ChromaDB collection used by paper-triage. Independent of `paper-rag` (which handles `papers/marp-summary/**/*.md`); the input is the abstract body of `papers/metadata/**/*.raw.md`.

## Philosophy
- **Incremental only**: re-embed only raw.md files that changed by SHA256.
- **Non-destructive**: do not touch raw.md.
- **Single document per paper**: abstracts are not chunked; upsert `title + "\n\n" + abstract` as one document.
- **Separate collection**: kept separate from the `papers` collection to avoid semantic drift from mixed queries.

## Stack
- Embedding: `BAAI/bge-m3` via `sentence-transformers`
- Store: `chromadb.PersistentClient(path="papers/vector_db/chroma")`, collection=`"abstracts"`
- Hash: `hashlib.sha256(file_bytes)`
- Manifest: `papers/vector_db/abstracts_manifest.json`

## File layout

```
.claude/skills/abstract-index/
├── SKILL.md
└── scripts/
    └── index.py    incremental / full indexing (CLI)
```

## Algorithm

```
1. Glob all papers/metadata/**/*.raw.md
2. Compute SHA256 for each file
3. Compare against existing hashes in abstracts_manifest.json:
   - new: collect_abstracts.extract() → title+abstract → embed → upsert
   - changed: delete existing id → re-embed + upsert
   - removed (present in manifest but file missing): delete id
4. Save manifest.json (last_update KST)
```

## Invocation examples

```bash
# Default run — incremental
python3 .claude/skills/abstract-index/scripts/index.py

# Rebuild manifest only (no Chroma upsert)
python3 .claude/skills/abstract-index/scripts/index.py --rebuild-manifest

# Rebuild both Chroma and manifest
python3 .claude/skills/abstract-index/scripts/index.py --rebuild
```

## Error handling
- `sentence-transformers` / `chromadb` not installed → exit 3, prompt to activate `conda env LLDM`
- Corrupt manifest (JSON parse failure) → warn and proceed with empty manifest (effectively full rebuild)
- raw.md without an `## Abstract` block → print `[warn]` and skip (not added to the collection)

## Checklist
- [ ] conda env LLDM active (`chromadb`, `sentence-transformers` importable)
- [ ] `papers/vector_db/chroma/` writable
- [ ] Manifest init or load succeeded
- [ ] Incremental indexing complete
- [ ] (On first run) abstracts collection count > 0

## Lessons hook
Before starting, Read `docs/lessons.md` + `docs/lessons-paper.md`.
