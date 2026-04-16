---
description: Run an ad-hoc RAG top-k query against the papers collection. Does not trigger reindexing.
argument-hint: <query text> [--k N] [--filter key=value ...]
---

# /research-rag

Direct top-k query against the `papers` ChromaDB collection (bge-m3 embeddings).

**Query**: $ARGUMENTS

Steps:

1. If `/home/irteam/sw/research_hub/papers/vector_db/rag.stale` exists, warn the user that the index is stale but proceed anyway (reading cached vectors).

2. Run:
   ```bash
   python3 /home/irteam/sw/research_hub/.claude/skills/paper-rag/scripts/query.py $ARGUMENTS
   ```
   If `--k` is absent in arguments, default to `--k 5`.

3. If the script fails because `chromadb` or `sentence-transformers` is not installed, tell the user to run `conda activate LLDM && pip install chromadb sentence-transformers` — do not try to install automatically.

4. If the collection is empty, suggest `/research-index` first.

5. Summarize the top results: `slug`, `section`, `score`, and a 1-line preview each. Do not dump full chunk texts unless the user asks.

This command is read-only. Do not modify any files or launch agents.
