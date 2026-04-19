---
name: harness-skill-author
description: "Procedure bundle (.claude/skills/{name}/SKILL.md). YAML header + 3-stage progressive disclosure + 500-line ceiling + references/ split + scripts/ bundling. Triggers: 'new skill', 'write SKILL.md', 'tune description', 'skill refactor'."
---

# Harness Skill Author

A skill is a procedural-knowledge bundle describing "how". Quality is determined by **description-trigger accuracy + Why-first prose**.

## Directory layout

```
.claude/skills/{name}/
├── SKILL.md         (required: frontmatter + body)
├── references/      (optional: conditionally loaded detail docs)
├── scripts/         (optional: executable code for repeated work)
└── assets/          (optional: templates / images)
```

## Frontmatter rules

```yaml
---
name: skill-name
description: "Specific actions + trigger situations + boundary conditions. Be pushy."
---
```

- `name`: matches the directory name. kebab-case.
- `description`: **the sole trigger mechanism**. At metadata-load time, Claude decides invocation based solely on this.

### Writing descriptions — aggressively

Claude errs conservatively on triggers. To compensate:
1. **Enumerate** what the skill does (verb + noun)
2. State **trigger situations** explicitly ("when X is requested, MUST use this skill")
3. **Disambiguate near-misses** — "but Y requests are handled by skill Z"

**Bad:** `"PDF processing skill"`
**Good:** `"Handles all PDF operations — read PDF, extract text / tables, merge, split, rotate, watermark, OCR. When a .pdf file is mentioned or a PDF deliverable is requested, MUST use this skill. For image-conversion-only requests, use the imaging skill."`

## Body principles

| Principle | Rule |
|---|---|
| **Why-first** | Explain reasons instead of "ALWAYS / NEVER". When an LLM understands why, it judges edge cases correctly. |
| **Lean** | Target body ≤ 500 lines. Ask whether each sentence justifies its token cost. |
| **Generalize** | Describe principles, not specific examples. No overfitting. |
| **Imperative** | Command-form voice. |
| **Bundle repeated code** | Helpers repeated 3+ times go into `scripts/`. |

## Progressive disclosure

Skills manage context via 3-stage loading:

| Stage | When | Size |
|---|---|---|
| metadata (name + description) | Always | ~100 words |
| SKILL.md body | On trigger | < 500 lines |
| references/ | On demand only | unbounded |

**Size management:**
- As the body approaches 500 lines, move details to `references/` and keep pointers in the body
- Reference files > 300 lines should include a ToC at the top
- If there are domain variants, split into `references/{domain}.md` (loaded only for that domain)

## Authoring steps

1. **Scan existing skills**: read every `.claude/skills/*/SKILL.md` frontmatter to check name / description duplication / conflict
2. Create the directory: `.claude/skills/{name}/`
3. Write SKILL.md (frontmatter + body)
4. Create `references/`, `scripts/` if needed
5. Check line count: split if > 500 lines
6. Validate structure via the harness-validate skill

## Trigger-conflict check

If a new skill's description semantically overlaps an existing skill's, Claude routes wrong. Before creating:

1. List every existing description
2. Check whether the new skill's trigger keywords overlap
3. On overlap, either add a **"but X is handled by skill Y"** boundary clause to the description, or merge the skills

## Do NOT put in a skill

- README.md, CHANGELOG.md, other ancillary docs
- Meta-information about the authoring process (test history)
- User-facing manuals (skills target AI agents)
- General knowledge Claude already possesses

## Checklist

- [ ] `{name}/` directory created, kebab-case
- [ ] Frontmatter has name + description
- [ ] Description is specific, pushy, with boundary conditions
- [ ] Body ≤ 500 lines, imperative, Why-first
- [ ] No trigger conflict with existing skills
- [ ] Split into `references/` where appropriate
- [ ] harness-validate passes
