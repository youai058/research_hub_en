---
name: harness-settings
description: "settings.json 편집·병합·검증. permissions(allow/deny/ask/defaultMode), env, statusLine, model, outputStyle, keybindings.json, output-styles 디렉토리. hooks 키는 harness-hooks 담당. 트리거: 'settings 수정', 'permission 추가', 'defaultMode 변경', 'statusline', '환경변수', 'output style', '키바인딩 변경'."
---

# Harness Settings Editor

settings.json은 하네스의 루트 설정이다. 잘못 쓰면 세션 전체가 동작하지 않으므로 **계층·스키마·병합 규칙**을 반드시 지킨다.

## 계층

| 파일 | 범위 | 언제 쓰는가 |
|---|---|---|
| `~/.claude/settings.json` | user global | 모든 프로젝트에 공통(재사용 가능한 설정만) |
| `{project}/.claude/settings.json` | project (commit 대상) | 프로젝트 특화 설정·훅 |
| `{project}/.claude/settings.local.json` | project local (gitignore) | 비밀, 개인 오버라이드 |

병합 우선순위: **local > project > user**. 배열 필드(`permissions.allow` 등)는 병합되고, 스칼라는 하위 레벨이 덮어쓴다. user global 수정은 다른 프로젝트에 영향을 주므로 **반드시 사용자 명시 승인**을 받는다.

## 주요 키

### permissions
```json
{
  "permissions": {
    "allow": ["Bash(ls:*)", "Read(*)"],
    "deny": ["Bash(rm -rf *)"],
    "ask": ["Bash(git push:*)"],
    "defaultMode": "bypassPermissions"
  }
}
```
- `defaultMode`: `plan` | `default` | `acceptEdits` | `bypassPermissions`
- 도구 매처 형식: `ToolName(pattern)` — Bash는 접두사 매칭, 다른 도구는 구체 문자열
- `skipDangerousModePermissionPrompt: true`는 `bypassPermissions`와 함께 쓸 때만 의미 있음

### env
```json
{"env": {"CLAUDE_BASH_DEFAULT_TIMEOUT_MS": "300000"}}
```
주로 모델 힌트, 프록시, 타임아웃 등 환경변수. 비밀은 `settings.local.json`에.

### statusLine
```json
{"statusLine": {"type": "command", "command": "/home/irteam/sw/.claude/hooks/statusline.sh"}}
```
셸 커맨드 출력을 상태바로 렌더링. 1초 이내 반환되도록 작성.

### model / outputStyle
```json
{"model": "opus", "outputStyle": "default"}
```
`outputStyle`은 `.claude/output-styles/{name}.md` 파일명을 지정. 페르소나 시스템 프롬프트 오버라이드.

### MCP 토글
```json
{
  "enableAllProjectMcpServers": false,
  "disabledMcpjsonServers": ["some-server"],
  "enabledMcpjsonServers": ["other-server"]
}
```
MCP 서버 등록은 `.mcp.json`에 하고, 토글만 여기서.

## 편집 절차

1. **Read로 현재 파일을 먼저 읽는다**. 공백·순서도 가능하면 보존.
2. JSON 파싱 — 파싱 실패 시 중단하고 원본 백업.
3. 키를 병합(배열은 중복 제거, 스칼라는 덮어쓰기).
4. 원자적 쓰기 — Write로 전체 파일 재기록.
5. 파싱 재검증: `python3 -c "import json,sys; json.load(open('...'))"`.

## Output styles

`.claude/output-styles/{name}.md`에 frontmatter + 시스템 프롬프트 본문. settings의 `outputStyle` 키로 활성화.

```markdown
---
name: terse-engineer
description: 한국어 간결 응답
---
모든 응답은 100자 이내. 코드 변경은 파일 경로 + 한 줄 요약.
```

## Keybindings

`~/.claude/keybindings.json`만 존재(프로젝트 범위 없음). 상세 작성법은 빌트인 `keybindings-help` 스킬 참조. 이 스킬에서는 포인터만 제공한다.

## 검증 체크

- 파일이 유효한 JSON인가 (`json.load` 통과)
- `defaultMode` 값이 4개 enum 중 하나인가
- `permissions.allow`/`deny`/`ask` 각 엔트리가 `ToolName(...)` 형식인가
- `statusLine.command` 경로가 실제 존재·실행 가능인가
- user global 편집이면 사용자 승인을 받았는가

## 실패 모드

- 잘못된 `defaultMode` 값 → 세션 시작 시 거부됨
- 권한 매처 오타 → 조용히 무시되어 권한이 안 걸림
- statusLine 스크립트 실패 → 상태바 비어있음, 세션은 동작
- JSON 구문 오류 → **세션 전체가 기동 실패**. 반드시 재검증할 것.
