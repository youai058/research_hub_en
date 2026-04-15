---
description: Umbrella command for the papers KG. Dispatches build|query|node|lookup|stats subcommands to .claude/skills/paper-kg/scripts/*.py. Read-only by default; build triggers incremental ingest.
argument-hint: <subcmd> [subcmd args...]
---

# /research-kg

Single entry-point for the papers knowledge graph. First token of `$ARGUMENTS` is the subcommand; remaining tokens are forwarded to the corresponding script.

**Arguments**: $ARGUMENTS

## Subcommands

| Subcmd | Dispatch | Purpose |
|---|---|---|
| `build` | `paper-kg/scripts/index.py <flags>` | Incremental ingest (`--rebuild`, `--rebuild-manifest`, `--dry-run`, `--file` supported). Clears `.stale` on success. |
| `query` | `paper-kg/scripts/hybrid_query.py <question> <flags>` | Hybrid RAG+KG joint retrieval. Returns `{rag, kg, hybrid}`. |
| `node` | `paper-kg/scripts/query.py node "<id>"` | Fetch a single node by pinned id. Always quote ids that contain `#`. |
| `lookup` | `paper-kg/scripts/query.py lookup <flags>` | `--type T (--exact-name X \| --name-fuzzy Y) [--k N]`. Used for alias checks. |
| `stats` | `paper-kg/scripts/status.py` | Counts, by_type breakdown, manifest summary, rejected count. |

## Steps

1. Parse `$ARGUMENTS`. If empty, print the subcommand table above and exit.

2. If first token is `build`:
   - If `--rebuild` is in the remaining args, confirm with the user before proceeding (rebuild drops the KG tables and re-ingests every `.kg.json` byproduct).
   - Run:
     ```bash
     python3 /home/irteam/sw/research_hub/.claude/skills/paper-kg/scripts/index.py <rest>
     ```
   - On success, the script itself clears `papers/kg/.stale`.
   - Print the summary JSON (`scanned`, `changed`, `unchanged`, `rejected`, `total_nodes_seen`, `total_edges_seen`).
   - If `rejected > 0`, remind the user that `papers/kg/rejected.jsonl` holds the detail and that orchestrator should re-dispatch the listed `author_agent`s.

3. If first token is `query`:
   - Remaining args form the question (quote them if they contain spaces) plus optional `--k N` / `--no-rag` / `--no-kg`.
   - Run:
     ```bash
     python3 /home/irteam/sw/research_hub/.claude/skills/paper-kg/scripts/hybrid_query.py <rest>
     ```
   - Summarize the result: top-k RAG chunks (slug/section/score) + top matched KG nodes (id/type) + `hybrid.joint_rank`.

4. If first token is `node`:
   - Pass the remaining argument verbatim to `query.py node`. The shell will quote-preserve if the user wraps it; if not, remind them to quote ids with `#`.
   - Run:
     ```bash
     python3 /home/irteam/sw/research_hub/.claude/skills/paper-kg/scripts/query.py node "<id>"
     ```

5. If first token is `lookup`:
   - Forward remaining args:
     ```bash
     python3 /home/irteam/sw/research_hub/.claude/skills/paper-kg/scripts/query.py lookup <rest>
     ```
   - Both `--exact-name` and `--name-fuzzy` are supported.

6. If first token is `stats`:
   - Run:
     ```bash
     python3 /home/irteam/sw/research_hub/.claude/skills/paper-kg/scripts/status.py
     ```
   - Pretty-print the JSON; also cross-reference `by_type` counts against the PLAN minimum (Paper + Claim expected after bootstrap).

7. For any unknown subcommand: print the table and return.

## Failure handling

- Missing `pydantic`/`rapidfuzz`: ask the user to `conda activate LLDM && pip install pydantic rapidfuzz` rather than installing automatically.
- Missing `papers/kg/kg.sqlite`: run `build` first (the script will auto-create it).
- Ingest errors are surfaced via `rejected.jsonl`; do not try to fix rejected files here — re-dispatch the original `author_agent` through orchestrator.

This command is read-only except for the `build` subcommand. Do not launch other agents.
