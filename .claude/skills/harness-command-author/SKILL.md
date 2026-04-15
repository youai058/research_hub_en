---
name: harness-command-author
description: "슬래시 프롬프트 템플릿(.claude/commands/{name}.md). $ARGUMENTS/$1../!셸/@파일 지시자 + description·argument-hint·allowed-tools·model 헤더. 트리거: '새 slash command', '/custom 프롬프트', '커맨드 템플릿'."
---

# Harness Command Author

Slash command는 **사용자가 `/name`으로 호출하는 프롬프트 템플릿**이다. 자동 실행이 아니라 사용자 주도 단축키이며, 반복되는 복합 프롬프트를 재사용 가능하게 만든다.

## 저장 위치

```
.claude/commands/{name}.md      (project scope, /name)
~/.claude/commands/{name}.md    (user global, /name)
```

project commands가 user global commands를 오버라이드한다. 서브디렉토리 구조로 네임스페이스도 가능: `.claude/commands/git/commit.md` → `/git:commit`.

## Frontmatter

```yaml
---
description: "이 커맨드가 하는 일 한 줄 요약 (`/help`에 표시)"
argument-hint: "<file> [--flag]"
allowed-tools: ["Bash", "Read", "Edit"]
model: opus
---
```

- `description`: `/help` 목록에 표시. 없어도 동작하지만 권장.
- `argument-hint`: 사용자에게 인자 힌트. 자동완성에 사용.
- `allowed-tools`: 이 커맨드 실행 컨텍스트에서 허용할 도구 목록. 생략 시 기본 세션 권한.
- `model`: 이 커맨드 실행 시 강제할 모델 (선택).

## 본문 지시자

| 지시자 | 의미 |
|---|---|
| `$ARGUMENTS` | 사용자가 `/name foo bar`로 호출 시 `foo bar` 전체 |
| `$1`, `$2`, … | 개별 위치 인자 |
| `!command` | 셸 커맨드를 **커맨드 작성 시점에** 실행하고 결과를 프롬프트에 인라인 |
| `@path/to/file` | 해당 파일 내용을 프롬프트에 인라인 |

### 예시: `/commit`

```markdown
---
description: 스테이징된 변경을 커밋
argument-hint: "[message]"
allowed-tools: ["Bash"]
---

다음 상태를 보고 커밋 메시지를 제안하거나 사용자가 준 메시지 "$ARGUMENTS"를 사용해 커밋해라.

현재 상태:
!git status --short

변경 요약:
!git diff --stat
```

### 예시: `/review-pr`

```markdown
---
description: GitHub PR 리뷰
argument-hint: "<pr-number>"
allowed-tools: ["Bash", "Read"]
---

PR #$1 의 변경사항을 검토해라.

!gh pr view $1
!gh pr diff $1
```

## 편집 절차

1. 기존 커맨드 스캔: `.claude/commands/**/*.md`의 name·description 충돌 확인
2. 파일 작성 (frontmatter + 본문)
3. `!` 셸 지시자가 있으면 커맨드 레벨에서 실행 권한 확인
4. 테스트: `/name [샘플 인자]` 로 실제 호출
5. harness-validate로 frontmatter 검증

## 커맨드 vs 스킬 vs 훅 — 어느 걸 선택할까

| 상황 | 선택 |
|---|---|
| 사용자가 명시 호출하는 재사용 프롬프트 | **command** |
| 키워드로 자동 트리거되는 복합 워크플로우 | **skill** |
| 이벤트(도구 호출·프롬프트 제출 등)에 자동 실행 | **hook** |

혼동하지 말 것: command는 능동(사용자 호출), hook은 수동(이벤트 반응), skill은 자동(description 매칭).

## 체크리스트

- [ ] 파일이 `.claude/commands/` 하위
- [ ] frontmatter 유효 (description 권장, argument-hint·allowed-tools 선택)
- [ ] `$ARGUMENTS` / `$1..$n` 사용 시 argument-hint도 함께
- [ ] `!` / `@` 지시자가 실제 실행 가능
- [ ] 기존 커맨드와 네임 충돌 없음
