---
name: harness-hooks
description: "hooks 등록·편집·검증. PreToolUse/PostToolUse/UserPromptSubmit/Stop/SubagentStop/SessionStart/SessionEnd/PreCompact/Notification. \"X할 때마다 Y\" 류 자동 행동은 반드시 훅으로. 트리거: '훅 추가', 'PreToolUse', 'lint 강제', '도구 호출 차단', '자동 포맷팅', '세션 시작 자동 실행'."
---

# Harness Hooks Editor

훅은 하네스의 **실제 집행자**다. 본체 모델은 매 세션 잊기 쉬우므로 강제해야 하는 행동은 훅으로 구현한다.

## 훅 이벤트

| 이벤트 | 실행 시점 | 차단 가능? |
|---|---|---|
| `PreToolUse` | 도구 호출 직전 | **Yes** (non-zero exit → 차단, stderr가 모델에 전달) |
| `PostToolUse` | 도구 호출 직후 | No (로깅·후처리용) |
| `UserPromptSubmit` | 사용자 메시지 전송 직후 | Yes (프롬프트 변조/거부) |
| `SessionStart` | 세션 시작 | No (초기 컨텍스트 주입) |
| `SessionEnd` | 세션 종료 | No (정리) |
| `Stop` | 모델 응답 종료 직전 | Yes (응답 거부·재시작) |
| `SubagentStop` | 서브에이전트 종료 | No |
| `PreCompact` | 컨텍스트 압축 직전 | No (중요 정보 저장 기회) |
| `Notification` | 사용자 알림 발생 | No |

## 등록 위치

settings.json의 `hooks` 키:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {"type": "command", "command": "/home/irteam/sw/.claude/hooks/block-rm-rf.sh"}
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {"type": "command", "command": "/home/irteam/sw/.claude/hooks/format.sh"}
        ]
      }
    ]
  }
}
```

- `matcher`: 도구 이름 정규식. 도구가 없는 이벤트(`SessionStart` 등)는 matcher 생략.
- `hooks[]`: 각 항목은 하나의 셸 커맨드. 여러 개 등록 가능.
- 커맨드 경로는 **절대 경로**를 사용한다(작업 디렉토리 변동 방지).

## 훅 스크립트 작성 규약

스크립트는 `.claude/hooks/`에 둔다. 입력은 stdin으로 JSON이 들어오고, 출력은:
- **exit 0**: 통과, stdout은 로그로만 기록
- **exit non-zero (PreToolUse/UserPromptSubmit/Stop)**: 차단, stderr가 모델에 전달되어 다음 판단에 사용됨

### 최소 템플릿 (Python)

```python
#!/usr/bin/env python3
import json, sys

payload = json.load(sys.stdin)
# payload 예: {"tool_name": "Bash", "tool_input": {"command": "..."}}

cmd = payload.get("tool_input", {}).get("command", "")
if "rm -rf /" in cmd:
    print("blocked: rm -rf /", file=sys.stderr)
    sys.exit(1)
sys.exit(0)
```

### 최소 템플릿 (Bash)

```bash
#!/usr/bin/env bash
payload=$(cat)
echo "$payload" | jq -e '.tool_input.command | test("rm -rf /")' >/dev/null \
  && { echo "blocked" >&2; exit 1; }
exit 0
```

스크립트는 반드시 실행 권한(`chmod +x`) 부여.

## 편집 절차

1. 훅 스크립트를 `.claude/hooks/{name}.py`에 작성하고 `chmod +x`
2. stdin JSON payload 샘플로 **로컬 dry-run**: `echo '{"tool_name":"Bash","tool_input":{"command":"ls"}}' | python3 .claude/hooks/{name}.py`
3. settings.json의 `hooks.{Event}` 배열에 등록 (harness-settings 스킬 위임)
4. 같은 이벤트+매처에 중복 등록이 없는지 확인
5. PreToolUse 훅은 **차단 영향 범위**를 사용자에게 명시 보고

## 일반적 패턴

### 커밋 전 lint 강제
`PreToolUse` + `matcher: "Bash"` + payload에서 `git commit` 감지 시 `npm run lint`/`ruff` 실행, 실패 시 exit 1.

### 자동 포맷팅
`PostToolUse` + `matcher: "Write|Edit"` + 파일 확장자 보고 `ruff format` / `prettier`.

### 위험 경로 보호
`PreToolUse` + `matcher: "Write|Edit"` + `tool_input.file_path`가 `LLM/`, `LLDM/` 하위면 차단.

### 세션 시작 시 컨텍스트 주입
`SessionStart` → 현재 브랜치·최근 커밋·실험 상태를 stdout으로 출력하면 모델 초기 컨텍스트에 들어감.

## 실패 모드 & 디버깅

- PreToolUse 훅이 실수로 항상 non-zero → **모든 도구 호출 차단됨**. 되돌리려면 settings.json에서 해당 훅 제거.
- 경로 상대화 → cwd 변경 시 훅 스크립트를 못 찾음. 절대 경로 사용.
- 스크립트 퍼미션 누락 → 실행 실패, 조용히 무시될 수 있음.
- 느린 훅 → 모든 도구 호출이 느려짐. 1초 이내 목표.

## 안전 원칙

- **PreToolUse는 최소한으로**: 본체 모델의 판단을 과하게 오버라이드하면 유연성 상실
- **새 훅은 항상 dry-run**: 로컬에서 여러 payload로 테스트 후 등록
- **롤백 계획**: 등록 전 원본 settings.json 내용을 기억하고, 문제 시 즉시 되돌릴 수 있어야 함
- **사용자 공지**: 도구 차단성 훅(PreToolUse, UserPromptSubmit, Stop)은 등록 시 사용자에게 영향 범위 보고 필수
