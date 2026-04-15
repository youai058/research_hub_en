---
description: Append a lesson entry to the appropriate docs/lessons*.md file via .claude/scripts/lesson.py. Append-only — never edit or delete prior entries.
argument-hint: <domain> "<rule title>" [--rule "..."] [--why "..."] [--when "..."]
---

# /research-lesson

Delegates to `.claude/scripts/lesson.py append`. The script owns dating,
frontmatter bump, and entry counting — do **not** hand-edit the lessons files.

**Args**: $ARGUMENTS

Expected form (first token = domain, second token = quoted title, rest = optional context):

```
/research-lesson <domain> "<rule title>" [Rule text — Why text — When-to-apply text]
```

Valid domains: `global`, `paper`, `research`, `impl`, `analysis`.

Steps:

1. Parse `$ARGUMENTS`. If domain is missing or invalid, print the valid list and abort — **do not guess**.
2. Extract Rule / Why / When-to-apply:
   - If the user provided them inline, use them verbatim.
   - Otherwise, infer from the immediately preceding conversation turn.
   - If inference is impossible, pass `TODO` for missing fields; the script will mark `has_placeholders: true` so the user can fix them.
3. Run:
   ```bash
   python3 /home/irteam/sw/research_hub/.claude/scripts/lesson.py append \
     --domain <domain> \
     --title "<rule title>" \
     --rule "<rule>" \
     --why "<why>" \
     --when "<when to apply>"
   ```
4. Print the JSON response and confirm the new `entry_count` plus the target file path.
5. If `has_placeholders` is true, warn the user explicitly so they can replace `TODO`s.

Do not launch agents. Do not touch other lesson files. Do not modify `CLAUDE.md`.
