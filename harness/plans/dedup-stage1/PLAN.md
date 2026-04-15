# PLAN — Dedup Stage 1 (Low-Risk Duplicate Cleanup)

> Phase A (계획) 전용. 구현 금지. 사용자가 트리거 phrase(§4.3 CLAUDE.md whitelist)를 명시해야 Phase C로 전이.
>
> 목적: 이전 감사·검증에서 LOW/NEGLIGIBLE risk로 판정된 2개 중복만 우선 정리한다. MEDIUM risk 이상(Phase A/B/C 프로토콜 boilerplate 통합, experiment-design/experiment-plan 경계 명문화)은 Stage 2로 이월.

---

## 0. 한 줄 요약

- **범위**: (A) TRIGGER_WHITELIST 구(句) 목록을 `.claude/agents/orchestrator.md`·`.claude/skills/orchestrate/SKILL.md` 2곳에서 제거하고 loop_state.py SSOT 1줄 참조로 축약, (A-3) CLAUDE.md §4.3 말미에 "loop_state.py와 sync" 주석 1줄 append(본문 목록은 유지), (B) `test_loop_state.py`를 `.claude/scripts/` → `.claude/tests/` top-level로 이동.
- **무엇을 건드리지 않는가**: 에이전트·스킬·커맨드 자체 파일 수·계약·훅·loop_state.py runtime 로직. 이전 오판(orchestrator.md:75 C-1, experiment-plan/SKILL.md)은 drift가 아니었으므로 이 PLAN에서 제외.

---

## 1. 현재 확인된 사실 (검증 근거)

### 1.1 TRIGGER_WHITELIST 현황

| 파일 | 라인 | 내용 |
|---|---|---|
| `.claude/scripts/loop_state.py` | 85–92 | KO 7 + EN 6 (composite only). 주석(라인 83): "`해줘`·`그래`는 2026-04-15 codex M2에서 제거 — 너무 모호". **Canonical runtime SSOT**. |
| `.claude/agents/orchestrator.md` | 117–120 | 동일 KO 7 + EN 6 (문자 단위 identical). |
| `.claude/skills/orchestrate/SKILL.md` | 57–60 | 동일 KO 7 + EN 6. |
| `.claude/commands/research-*.md` | (예시 문구만) | "구현해줘" 등 한두 개 inline example 언급. 전체 목록 복붙 아님 → 축약 대상 아님. |

- Drift: **zero**. 완벽 동일.
- Runtime consumer: `loop_state.py is_trigger_phrase()` 하나. `.md`의 목록은 Claude가 판단 재료로 읽는 참고용.
- CLAUDE.md §4.3에도 동일 whitelist가 이미 있어 Claude는 항상 4중 중복 노출됨.

### 1.2 test_loop_state.py 현황

| 항목 | 값 |
|---|---|
| 경로 | `.claude/scripts/test_loop_state.py` |
| 라인 수 | 274 |
| Runtime consumer | **없음** (hook/command/skill grep 결과 zero) |
| CI/SessionStart 호출 | 없음 |
| Claude-read context 여부 | 아님 (`.md` 확장자 아니고 skill reference에도 미포함) |
| 용도 | loop_state v1→v3 migrate, stage-enter/advance/trigger-check 유닛 테스트 |

- 현재 `.claude/scripts/` 아래에 production 스크립트 3개(loop_state.py / report_builder.py / lesson.py)와 나란히 놓여 있어 "scripts = 전부 production"이라는 인상을 훼손.

---

## 2. 변경 상세 (2 items)

### Change A — TRIGGER_WHITELIST `.md` 2곳 축약

**원칙**: loop_state.py를 SSOT로 고정. `.md`는 "어디에 정의되어 있는지" + "판정 명령"만 언급.

**A-1. `.claude/agents/orchestrator.md` (lines 117–120)**
- Before:
  ```
  3. **명시 트리거 phrase whitelist** (대소문자 무관, trim 후 정확 매칭; `loop_state.py trigger-check "<phrase>"`로 판정):
     - 한국어: `구현해줘`, `실행해줘`, `진행해줘`, `ok 해`, `시작해`, `좋아 진행`, `ok 진행`
     - 영어: `proceed`, `go ahead`, `run it`, `execute`, `ok run it`, `ok proceed`
     - 이외 발화는 전부 피드백으로 간주 → Phase A의 (1)로 재진입.
  ```
- After (축약):
  ```
  3. **명시 트리거 phrase whitelist**: SSOT는 `.claude/scripts/loop_state.py` `TRIGGER_WHITELIST` 상수. 판정은 `python3 .claude/scripts/loop_state.py trigger-check "<phrase>"` (exit 0 + `is_trigger:true` = pass). 매칭 실패 발화는 전부 피드백으로 간주 → Phase A의 (1)로 재진입. 현재 수록된 구(句)의 요지만: 한국어 composite 7개("구현해줘" 계열) + 영어 composite 6개("proceed" 계열). **직접 목록은 코드에서 확인하며, 이 파일과 CLAUDE.md §4.3에 사본 두지 않는다.**
  ```
- 유지: `loop_state.py trigger-check` 호출 방법, "Hard stop: autonomous 분기 없음" 문구.
- 제거: 7+6 구 단위 목록.

**A-2. `.claude/skills/orchestrate/SKILL.md` (lines 57–61)**
- Before:
  ```
  3. **명시 트리거 phrase whitelist** (대소문자 무관, trim 후 정확 매칭):
     - 한국어: `구현해줘`, `실행해줘`, `진행해줘`, `ok 해`, `시작해`, `좋아 진행`, `ok 진행`
     - 영어: `proceed`, `go ahead`, `run it`, `execute`, `ok run it`, `ok proceed`
     - 판정은 `python3 .claude/scripts/loop_state.py trigger-check "<phrase>"` (exit 0 = pass).
     - 매칭 실패 발화는 전부 피드백으로 간주 → Phase A의 (1)로 재진입.
  ```
- After (축약):
  ```
  3. **명시 트리거 phrase whitelist**: SSOT = `.claude/scripts/loop_state.py` `TRIGGER_WHITELIST`. 판정은 `python3 .claude/scripts/loop_state.py trigger-check "<phrase>"` (exit 0 + `is_trigger:true` = pass; 대소문자 무관·trim 후 정확 매칭). 매칭 실패 발화는 전부 피드백으로 간주 → Phase A의 (1)로 재진입. 구(句) 추가/삭제는 loop_state.py만 편집.
  ```

**A-3. CLAUDE.md §4.3 (프로젝트 지침) — 유지 + sync 주석 추가**
- CLAUDE.md는 **사용자-지향 SSOT 계약 문서**이며 `.claude/agents`·`.claude/skills`는 **Claude-지향 prompt**. 목적이 다른 타깃이므로 "의도적 target-specific 복제"지 drift 유발 중복이 아니다. 목록은 그대로 유지한다.
- 단 CLAUDE.md §4.3 끝부분에 sync 책임 1줄 주석 추가:
  ```
  > 위 목록은 `.claude/scripts/loop_state.py` `TRIGGER_WHITELIST`와 동기 유지. 구 추가/삭제 시 두 곳 모두 갱신.
  ```
- Phase C에서 이 1줄만 추가하는 최소 편집.

### Change B — test_loop_state.py 재배치

**원칙**: production script dir과 test artifact 시각적 분리.

- Action: `git mv` (또는 `mv`) `.claude/scripts/test_loop_state.py` → `.claude/tests/test_loop_state.py`.
- 신규 디렉토리: `.claude/tests/` (scripts/ **하위가 아니라 top-level**). Python 관례(테스트는 숨김 대상 아님) + production script dir 순수성 + discoverability 동시 확보. 향후 hook·skill script 테스트도 같은 위치로 확장.
- 테스트 실행법을 README 대신 파일 상단 docstring에 1줄 남김: `# Run: python3 .claude/tests/test_loop_state.py` (이미 있으면 그대로).
- import 경로 수정 필요 여부: 현 파일은 `sys.path.insert(0, ...)`로 loop_state.py를 import하는 패턴이면 해당 경로 1개 변경만. 확인 후 수정 (loop_state.py가 형제 디렉토리 `.claude/scripts/`에 있으므로 `sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))` 형태로 조정).

**Verification (Phase C 마지막에 실행)**:
```bash
cd /home1/irteam/sw/research_hub
python3 .claude/tests/test_loop_state.py   # all tests pass
grep -rn "scripts/test_loop_state" .claude/ docs/   # 0 results expected
```

---

## 3. 명시적 비범위 (Non-goals)

이 PLAN은 다음을 **의도적으로 포함하지 않는다**. Stage 2 이후로 이월.

| 항목 | 이유 |
|---|---|
| Phase A/B/C 프로토콜 boilerplate 통합(orchestrator.md ↔ orchestrate/SKILL.md) | 두 파일이 관점이 다름(agent persona vs procedure). references/phase-abc-protocol.md 추출은 논리 일관성 diff 검토 필요 → 별도 설계. |
| STAGE_SUBPHASES 3곳 통합 | orchestrator.md:75의 C-1 포함 버전은 "개념적 구성"을 표현한 의도적 문서화. loop_state.py는 runtime sequence. drift가 아니며 주석이 이미 명시. 단, 독자 혼동 여지는 있어 Stage 2에서 명시적 분리 고려. |
| experiment-plan/SKILL.md deprecation | phase_advance_check.sh·code-implementer·implementation-verifier·results-analyst·paper-kg가 per-slug PLAN을 여전히 참조. active skill이므로 제거 금지. |
| MERGE 3건(paper-hunt+triage, paper-rag+kg, experiment-design+plan) | 구조적 재설계 — Stage 3 이상. |

---

## 4. Risk / Rollback

| 변경 | Risk | Rollback |
|---|---|---|
| A-1 orchestrator.md 축약 | LOW — Claude가 trigger 판정을 할 때 목록을 직접 읽는 대신 `loop_state.py trigger-check`를 호출하도록 이미 CLAUDE.md §4.3·orchestrate/SKILL.md가 유도함. 실행 경로 변화 없음. | `git checkout` (stage-split과 달리 단일 파일 2개). |
| A-2 orchestrate/SKILL.md 축약 | LOW — 동일 근거. | 동일. |
| A-3 CLAUDE.md sync 주석 추가 | NEGLIGIBLE — 본문 1줄 append, 계약 변경 없음. | `git checkout` |
| B `.claude/tests/` 이동 | NEGLIGIBLE — runtime 호출 없음. | `git mv` 역방향. |

**전체적 safety gate**: Phase C 실행 전 `grep -rn "구현해줘" .claude/`로 3→1(loop_state.py만) 축소 확인. 이외 잔존 시 Phase A 재진입.

---

## 5. Phase C 체크리스트 (사용자 트리거 후 실행 순서)

1. [ ] `.claude/agents/orchestrator.md` lines 117–120 → A-1 after 블록으로 치환.
2. [ ] `.claude/skills/orchestrate/SKILL.md` lines 57–61 → A-2 after 블록으로 치환.
3. [ ] `CLAUDE.md` §4.3 끝에 A-3 sync 주석 1줄(`> 위 목록은 loop_state.py TRIGGER_WHITELIST와 동기 유지 …`) append.
4. [ ] `mkdir -p .claude/tests`.
5. [ ] `mv .claude/scripts/test_loop_state.py .claude/tests/test_loop_state.py`.
6. [ ] test 파일 상단 import 경로 확인·수정 (형제 디렉토리 `.claude/scripts/` 참조로 조정).
7. [ ] `python3 .claude/tests/test_loop_state.py` 전체 통과 확인.
8. [ ] `grep -rn "구현해줘\|proceed" .claude/agents/orchestrator.md .claude/skills/orchestrate/SKILL.md` → 각 파일에 구(句) 목록 잔존하지 않음 확인(단일 요지 문구만).
9. [ ] `grep -rn "scripts/test_loop_state" .claude/ docs/ harness/` → 0 건.
10. [ ] `/research-status` 실행 → loop_state 계약 이상 없음.
11. [ ] **성공 시**: `/research-lesson global "Dedup Stage 1 — TRIGGER_WHITELIST SSOT 고정"` (Rule / Why / How to apply 3-line) append.
    - [ ] **실패 시 (대체)**: `/research-lesson global "Dedup Stage 1 실패 — <구체 원인 1줄>"` — 성공 lesson append 금지. 실패 원인·재현 명령·관측된 증상을 Rule/Why/How에 기록하여 동일 실수 재발 방지.
12. [ ] `harness/plans/dedup-stage1/IMPL_LOG.md` 생성 — 각 체크박스 결과·커밋 해시·검증 로그 기록(성공·실패 무관 항상 작성).

---

## 6. Phase B 결정 (확정됨 2026-04-15)

이전 Phase B 협의를 거쳐 3항목 확정:

1. **CLAUDE.md §4.3 유지** (✓): 사용자-지향 SSOT 계약 문서이므로 구(句) 목록 유지. `.claude/` 내 Claude-지향 prompt(orchestrator.md·orchestrate/SKILL.md)는 축약. 추가로 CLAUDE.md §4.3 끝에 "loop_state.py와 sync" 주석 1줄 append(Change A-3).
2. **`.claude/tests/` top-level 디렉토리 채택** (✓): scripts/ 하위(`.claude/scripts/tests/`)나 숨김(`.claude/scripts/.tests/`)이 아니라 top-level `.claude/tests/`. production scripts dir 순수성 + Python 관례 + discoverability 모두 확보. 미래 hook·skill script 테스트 확장 경로 동일.
3. **lessons append 시점** (✓): Phase C 마지막 단계. **성공 시** 성공 lesson 1건, **실패 시** 실패 원인 lesson 1건을 append(둘 중 하나만). 체크박스 11 참조.

사용자가 트리거 phrase를 발화해야 Phase C 전이. 예: "구현해줘", "proceed".

---

## 7. 예상 산출물

- `.claude/agents/orchestrator.md` (1 편집 — lines 117–120 축약)
- `.claude/skills/orchestrate/SKILL.md` (1 편집 — lines 57–61 축약)
- `CLAUDE.md` (1 편집 — §4.3 말미에 sync 주석 1줄 append)
- `.claude/tests/test_loop_state.py` (신규 위치; import 경로 1곳 조정)
- `.claude/scripts/test_loop_state.py` (삭제 — `git mv`로 흔적 남김)
- `docs/lessons.md` (성공 또는 실패 lesson append 1 entry — 둘 중 하나)
- `harness/plans/dedup-stage1/IMPL_LOG.md` (신규)

**총 diff 규모 예상**: ~40줄 순삭감 (.md 2곳 구(句) 목록 제거) + ~2줄 추가 (CLAUDE.md sync 주석, import 경로 조정) + 파일 이동 1건.
