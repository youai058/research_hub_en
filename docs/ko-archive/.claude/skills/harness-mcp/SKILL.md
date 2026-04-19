---
name: harness-mcp
description: "MCP 서버 등록·토글·디버그. .mcp.json(repo) + ~/.claude.json(user), stdio/sse/http, settings.json enableAllProjectMcpServers/disabled/enabled 플래그. 트리거: 'MCP 서버 추가', '외부 도구 연결', '.mcp.json', 'MCP 비활성화', 'stdio 서버', 'http MCP'."
---

# Harness MCP Manager

MCP는 외부 도구 서버를 Claude Code에 **도구(tool)** 로 노출하는 프로토콜이다. 서버 등록과 토글을 분리해서 관리한다.

## 등록 위치

| 파일 | 범위 | 비고 |
|---|---|---|
| `{project}/.mcp.json` | project | git commit 대상. 팀 공유 서버 |
| `~/.claude.json` | user global | 개인용 서버 (프로젝트 무관) |

## 서버 타입

### stdio (로컬 프로세스)

```json
{
  "mcpServers": {
    "my-server": {
      "type": "stdio",
      "command": "/usr/bin/node",
      "args": ["/path/to/server.js"],
      "env": {"API_KEY": "xxx"}
    }
  }
}
```

- 가장 일반적. 서버가 stdin/stdout으로 JSON-RPC 통신.
- 비밀은 여기 쓰지 말고 `env`에 환경변수명만 두고 실제 값은 `settings.local.json`이나 호스트 환경변수로.

### SSE (원격)

```json
{
  "mcpServers": {
    "remote-sse": {
      "type": "sse",
      "url": "https://example.com/mcp"
    }
  }
}
```

### HTTP (원격)

```json
{
  "mcpServers": {
    "remote-http": {
      "type": "http",
      "url": "https://example.com/mcp"
    }
  }
}
```

## 토글 — settings.json

`.mcp.json`에 등록하는 것과 활성화하는 것은 별개. settings.json에서:

```json
{
  "enableAllProjectMcpServers": true,
  "disabledMcpjsonServers": ["my-server"],
  "enabledMcpjsonServers": []
}
```

- `enableAllProjectMcpServers`: `.mcp.json`의 모든 서버를 기본 허용. 보안 관점에서 **기본값은 false**로 두고 명시적으로 활성화.
- `disabledMcpjsonServers`/`enabledMcpjsonServers`: 개별 토글.

## 편집 절차

1. **비밀 스캔**: 추가할 서버 config에 평문 비밀이 있는지 확인, 있으면 환경변수로 분리
2. `.mcp.json` 읽기 → `mcpServers` 객체에 새 서버 추가 → JSON 재검증
3. 필요 시 `harness-settings` 스킬로 settings.json 토글 편집
4. git 상태 확인: `.mcp.json`이 이미 tracked면 commit 범위 확인, 비밀 누출 없는지 재검증
5. 사용자에게 "서버 등록 완료, 세션 재시작 후 `/mcp`로 확인" 안내

## 디버깅

- 서버가 리스트에 안 뜸 → `.mcp.json` JSON 파싱 확인, settings의 토글 확인
- 서버가 뜨지만 도구 호출 실패 → stdio 서버의 stderr 로그 확인, `env` 환경변수 전달 확인
- 권한 프롬프트 매번 뜸 → settings.json의 `permissions.allow`에 MCP 도구 추가

## 보안 원칙

- `.mcp.json`에는 **실행 가능한 커맨드 경로**가 들어간다. repo commit 시 팀원이 그대로 실행됨을 고려
- 신뢰 불명 MCP 서버는 `enableAllProjectMcpServers: false`로 두고 명시 허용
- API 키·토큰은 절대 `.mcp.json`에 평문으로 쓰지 말 것. `env` 경유 + `settings.local.json` 조합

## 체크리스트

- [ ] `.mcp.json` JSON 유효
- [ ] 서버 타입 명시 (`stdio`/`sse`/`http`)
- [ ] 평문 비밀 없음
- [ ] git 상태 확인 (commit 대상이면 사용자 공지)
- [ ] settings.json 토글 정책 결정
- [ ] 등록 후 `/mcp` 확인 안내
