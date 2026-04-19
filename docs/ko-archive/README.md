---
archived: 2026-04-19
status: frozen-snapshot
---

# Korean Archive — Pre-Translation Snapshot

This directory is a **frozen snapshot** of the Korean-primary harness taken on 2026-04-19, immediately before the English translation pass.

## Purpose

The active harness files at their runtime paths (`CLAUDE.md`, `docs/*.md`, `.claude/agents/*.md`, `.claude/skills/*/SKILL.md`, `.claude/commands/*.md`) are being translated to English as the new primary. Claude Code loads runtime files by fixed path, so there can only be one active version — this archive preserves the Korean text for reference, recovery, and diff.

## Contents (mirror of runtime paths)

- `CLAUDE.md` — root harness contract
- `docs/` — lessons*.md + harness-layout.md
- `.claude/agents/` — 14 agent personas
- `.claude/skills/` — 25 skill bundles (SKILL.md + scripts)
- `.claude/commands/` — 10 slash commands

## Editing policy

**DO NOT EDIT** files inside `ko-archive/`. This is append-only / frozen. If a Korean-language rule needs updating, update the English runtime file and append a note to `lessons.md` (English). The archive is not a live copy.

## Recovery

To restore any file from this archive to its runtime location:

```bash
cp docs/ko-archive/<path> <path>    # e.g. docs/ko-archive/CLAUDE.md → CLAUDE.md
```

## Why not keep Korean as runtime?

Single SSOT. Two parallel runtime trees would drift (cf. `docs/lessons.md` 2026-04-15 TRIGGER_WHITELIST SSOT lesson). Archive = reference only.
