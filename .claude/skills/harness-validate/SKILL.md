---
name: harness-validate
description: "하네스 전체 구조 검증. settings.json JSON 유효성, agents/skills/commands frontmatter, 훅 스크립트 +x, MCP 등록, description 트리거 충돌, 네이밍 규약. harness-engineer 편집 직후 필수. 트리거: '하네스 검증', '구조 체크', '하네스 헬스체크', '설정 유효성'."
---

# Harness Validator

하네스 수정 후 반드시 실행하는 구조 검증 스킬. 실패는 즉시 중단하고 사용자에게 보고한다.

## 검증 항목

### 1. settings.json 구문

- `.claude/settings.json`, `.claude/settings.local.json`, `~/.claude/settings.json` 각각 존재하면 JSON parse
- `python3 -c "import json; json.load(open('PATH'))"` 로 검사
- 실패 시 **즉시 중단** — 파싱 실패한 settings는 세션을 망가뜨린다

### 2. settings.json 스키마

- `permissions.defaultMode` ∈ {`plan`, `default`, `acceptEdits`, `bypassPermissions`}
- `permissions.allow`/`deny`/`ask` 엔트리가 `ToolName(pattern)` 형식
- `statusLine.type == "command"`이면 `command` 키 존재 + 경로 실제 존재
- `hooks.{Event}` 배열 각 항목에 `matcher`(선택)와 `hooks[]` 존재
- `hooks[].command` 경로가 실제 파일로 존재, 실행 권한(`os.access(path, os.X_OK)`)

### 3. Agents (`.claude/agents/*.md`)

- frontmatter parse (YAML)
- 필수 키: `name`, `description`
- 권장 키: `model: opus` (opus 아니면 경고)
- `name`이 파일명(확장자 제외)과 일치
- 본문에 6개 섹션(핵심 역할/작업 원칙/입출력 프로토콜/팀 통신 프로토콜/에러 핸들링/협업) 헤딩 존재 (경고 레벨)

### 4. Skills (`.claude/skills/*/SKILL.md`)

- frontmatter parse
- 필수: `name`, `description`
- `name`이 디렉토리명과 일치
- 본문 줄 수 ≤500 (경고, 초과 시 references 분리 제안)
- 300줄 이상 `references/*.md` 파일에 목차 존재 여부 (경고)

### 5. Slash commands (`.claude/commands/**/*.md`)

- frontmatter parse (선택이지만 있으면 유효해야 함)
- `allowed-tools` 있으면 배열이어야 함
- 본문에 `$ARGUMENTS`/`$1..9` 있으면 `argument-hint` frontmatter 권장

### 6. Hooks

- settings.json의 `hooks` 키에 등록된 커맨드 경로가 실제 존재
- `.claude/hooks/*.py`/`*.sh` 실행 권한 확인
- Python 스크립트는 `python3 -c "import ast; ast.parse(open('PATH').read())"`로 구문 검사

### 7. MCP

- `.mcp.json` 존재 시 JSON parse
- `mcpServers.{name}.type` ∈ {`stdio`, `sse`, `http`}
- stdio 서버의 `command` 경로 존재 확인 (절대 경로인 경우)

### 8. Trigger 충돌

- 모든 skill description을 수집
- 페어 단위로 의미적 중복 검사 (단순 키워드 overlap 기반 1차 필터)
- 중복 후보를 경고로 출력

## 실행 방식

검증 스크립트는 `.claude/skills/harness-validate/scripts/validate.py`로 번들링(아래 템플릿 참고)하고 다음과 같이 호출한다:

```bash
python3 .claude/skills/harness-validate/scripts/validate.py /home/irteam/sw
```

종료 코드:
- `0`: 모든 검사 통과
- `1`: 경고만 존재 (수정 권장)
- `2`: 치명적 오류 (세션 위험, 즉시 중단)

## 보고 형식

```
== Harness Validation Report ==
[OK]    settings.json syntax
[OK]    7 agents frontmatter
[WARN]  skills/foo/SKILL.md: 523 lines (exceeds 500)
[ERROR] settings.json: hooks.PreToolUse[0].command → path not executable
```

치명적 오류(`[ERROR]`)가 하나라도 있으면 harness-engineer는 롤백하거나 사용자에게 수정 요청.

## 호출 시점

1. harness-settings / harness-hooks / harness-agent-author / harness-skill-author / harness-command-author / harness-mcp 스킬이 편집 완료한 **직후**
2. 사용자가 "하네스 체크"를 명시 요청할 때
3. 세션 시작 직후 hook(`SessionStart`)에서 자동 실행 (선택)

## 체크리스트

- [ ] settings.json 3개 계층 모두 유효
- [ ] 모든 agents frontmatter 유효, name==파일명
- [ ] 모든 skills frontmatter 유효, 500줄 룰
- [ ] hooks 경로 존재 + 실행 권한
- [ ] MCP JSON 유효 + type 올바름
- [ ] trigger 중복 검사 수행
- [ ] 보고서 출력, ERROR면 중단
