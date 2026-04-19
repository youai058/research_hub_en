---
name: harness-agent-author
description: "Subagent persona file (.claude/agents/{name}.md). Header name·description·model·tools + sections (role / working principles / I/O / team comms / error handling / collaboration). Triggers: 'new subagent', 'agent persona', 'agent definition'."
---

# Harness Agent Author

An agent is an **expert persona file** defining "who does it". A skill is a procedural guide the agent references — the two concepts must not be mixed.

## Core principle

**Every agent must be defined as a `.claude/agents/{name}.md` file.** Even when using built-in types (`general-purpose`, `Explore`, `Plan`), create the agent definition file. Reasons:
- The file must exist to be reusable across sessions
- Team communication protocols must be spelled out to guarantee collaboration quality
- The harness's core value is separating "who (agent)" from "how (skill)"

## Frontmatter convention

```yaml
---
name: agent-name
description: "1–2 sentence role + list of trigger keywords. The orchestrator uses this for routing."
model: opus
---
```

- `name`: kebab-case, identical to the filename
- `description`: keyword-rich for triggering. Orchestrator or user decides to invoke based on this
- `model`: **always `opus`**. Harness quality depends on reasoning — opus delivers the best
- `tools`: (optional) restrict to specific tools. Omit to allow all

## Required body sections

```markdown
# {Agent Name} — one-line summary

You are the [role] expert in [domain].

## Core role
1. ...
2. ...

## Working principles
- principle 1 (include Why)
- principle 2

## Input / Output protocol
- Input: where what is received
- Output: where what is written
- Format: file format, structure

## Team communication protocol   ← required only in agent-team mode
- Message receive: from whom, what kind
- Message send: to whom
- Work request: what kinds from the shared work list

## Error handling
- behavior on failure
- behavior on timeout

## Collaboration
- boundaries / relations with other agents
```

## Special rules for QA agents

When authoring a QA agent:
- **Type is `general-purpose`** (Explore is read-only and cannot run verification scripts)
- Focus is not "existence check" but **"cross-boundary comparison"** — e.g., read API response shape and frontend hook shape simultaneously and compare
- Run **incrementally after each module completes**, not once at the end (incremental QA)

## Agent-split criteria

| Criterion | Split | Combine |
|---|---|---|
| Expertise | Different domains → split | Overlapping domains → combine |
| Parallelism | Independently executable → split | Sequentially dependent → consider combining |
| Context | Heavy context load → split | Lightweight and fast → consider combining |
| Reuse | Used by other teams → split | Used only by this team → consider combining |

## Skill-linkage patterns

Three ways an agent can leverage a skill:

| Pattern | Implementation | Fit |
|---|---|---|
| **Skill tool call** | Prompt states "invoke /skill-name via Skill tool" | Independent workflow, user-invocable |
| **Inline** | Include the procedure directly in the agent definition | Short (≤ 50 lines) and agent-specific |
| **Reference load** | Conditionally `Read` files from the skill's `references/` | Bulky, conditionally needed |

## Authoring steps

1. Scan existing agents: check `.claude/agents/*.md` for name/description collisions
2. Write `.claude/agents/{name}.md` (frontmatter + sections)
3. If linking a skill, reference it explicitly in the body
4. Validate frontmatter / sections via harness-validate

## Checklist

- [ ] Filename is kebab-case and matches frontmatter `name`
- [ ] `model: opus` specified
- [ ] `description` is keyword-rich for triggering
- [ ] All 6 required sections present (Role / Principles / I/O / Comms / Errors / Collaboration)
- [ ] Boundaries (Collaboration section) with other agents are clear
- [ ] No description collision with existing agents
