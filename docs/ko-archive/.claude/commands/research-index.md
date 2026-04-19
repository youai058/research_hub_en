---
description: Run incremental (default) or full rebuild of the papers RAG index via paper-rag/scripts/index.py. Clears the stale flag on success.
argument-hint: "[--rebuild] [--rebuild-manifest]"
---

# /research-index

Trigger the RAG indexer. Incremental by default.

**Flags from user**: $ARGUMENTS

Steps:

1. If `--rebuild` is in `$ARGUMENTS`, confirm with the user first. Rebuild drops the `papers` collection and re-embeds every paper.

2. Run the indexer:
   ```bash
   python3 /home/irteam/sw/research_hub/.claude/skills/paper-rag/scripts/index.py $ARGUMENTS
   ```

3. On failure due to missing packages, tell the user to `conda activate LLDM && pip install chromadb sentence-transformers`. Do not install unilaterally.

4. On success, clear the stale flag:
   ```bash
   rm -f /home/irteam/sw/research_hub/papers/vector_db/rag.stale
   ```

5. Print the summary JSON (`changed`, `removed`, `files`, `chunks_written`, `elapsed_s`).

6. If `changed == 0` and there was no stale flag, remind the user no work was needed.

7. For a quick cross-check, you may also run `python3 /home/irteam/sw/research_hub/.claude/scripts/loop_state.py status` to confirm the new manifest counts are reflected.

Do not launch other agents. Do not modify `manifest.json` manually.
