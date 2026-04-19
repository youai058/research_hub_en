---
description: Score collected raw.md papers against a topic (Claude-native, runtime only), emit accepted path list, and append to research/topics/<slug>.md.
argument-hint: --topic "<string>" [--threshold 3.0 | --top-n N] [--format paths|json|table] [--topic-from <slug>] [--no-save-topic]
---

Trigger the paper-triage agent to run a relevance pass over `papers/metadata/**/*.raw.md`.

## Dispatch

이 커맨드는 **paper-triage 에이전트를 Task tool로 실제 dispatch** 한다. orchestrator/클로드는 다음을 수행한다:

1. `$ARGUMENTS`를 그대로 subagent 프롬프트에 전달.
2. `Task(subagent_type="paper-triage", description="Relevance triage over raw.md pool", prompt="<forwarded $ARGUMENTS + usage context>")` 호출.
3. 에이전트 stdout의 accepted path 목록과 stderr의 `scanned=N accepted=M threshold=F` stat을 회수해 호출자에 반환한다.
4. `--no-save-topic`이 없으면 에이전트가 `research/topics/<slug>.md`에 run 엔트리를 append했는지 확인한다.

에이전트 정의는 `.claude/agents/paper-triage.md`, 스킬 계약은 `.claude/skills/paper-triage/SKILL.md`.

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
