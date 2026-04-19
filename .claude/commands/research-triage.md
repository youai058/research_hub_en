---
description: Score collected raw.md papers against a topic (Claude-native, runtime only), emit accepted path list, and append to research/topics/<slug>.md.
argument-hint: --topic "<string>" [--threshold 3.0 | --top-n N] [--format paths|json|table] [--topic-from <slug>] [--no-save-topic]
---

Trigger the paper-triage agent to run a relevance pass over `papers/metadata/**/*.raw.md`.

## Dispatch

This command **actually dispatches the paper-triage agent via the Task tool**. The orchestrator / Claude does the following:

1. Forward `$ARGUMENTS` verbatim into the subagent prompt.
2. Call `Task(subagent_type="paper-triage", description="Relevance triage over raw.md pool", prompt="<forwarded $ARGUMENTS + usage context>")`.
3. Collect the accepted-path list from the agent's stdout and the `scanned=N accepted=M threshold=F` stats from stderr, and return them to the caller.
4. Unless `--no-save-topic` is given, verify that the agent appended a run entry to `research/topics/<slug>.md`.

Agent definition: `.claude/agents/paper-triage.md`. Skill contract: `.claude/skills/paper-triage/SKILL.md`.

## Usage

```
/research-triage --topic "LLDM late-step generation order" --threshold 3.0   # default
/research-triage --topic "masked diffusion inference acceleration" --top-n 20
/research-triage --topic-from lldm-late-step-abcd1234
/research-triage --topic "..." --format table      # human review
/research-triage --topic "..." --no-save-topic     # skip history log
```

## Behavior

1. Loads topic from `--topic` or `--topic-from <slug>` (mutually exclusive).
2. Runs `.claude/skills/paper-triage/scripts/collect_abstracts.py` to bundle abstracts into a single JSON payload.
3. The agent scores each paper 0-5 using the rubric in `.claude/skills/paper-triage/SKILL.md` (Claude-native, no external LLM calls).
4. Applies threshold or top-n filter.
5. Writes a new run entry to `research/topics/<slug>.md` via `topic_log.py append` (unless `--no-save-topic`).
6. Emits accepted `papers/.../*.raw.md` paths on stdout for the orchestrator to pipe into `paper-summarize`.

## Notes

- Score is **runtime only** — `raw.md` frontmatter is never mutated.
- Topic history lives in `research/topics/<slug>.md` (KST timestamps, append-only).
- The agent should read `docs/lessons.md` + `docs/lessons-paper.md` before starting.

## Arguments

`$ARGUMENTS` are forwarded verbatim to the paper-triage agent.
