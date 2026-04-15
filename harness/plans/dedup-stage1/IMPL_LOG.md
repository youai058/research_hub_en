# IMPL_LOG — Dedup Stage 1

> Phase C 실행 기록. 2026-04-15 KST.
> PLAN: `harness/plans/dedup-stage1/PLAN.md`
> 트리거 phrase: `구현해줘` (`loop_state.py trigger-check` 통과 확인)

---

## Checklist 결과

| # | 항목 | 결과 | 비고 |
|---|---|---|---|
| 1 | `.claude/agents/orchestrator.md` lines 117–120 축약 | ✓ | 구(句) 목록 제거 → 1-line SSOT 참조(`구현해줘` 계열/`proceed` 계열 요지만 유지) |
| 2 | `.claude/skills/orchestrate/SKILL.md` lines 57–61 축약 | ✓ | 구(句) 목록 전체 제거 → 1-line SSOT 참조 |
| 3 | `CLAUDE.md` §4.3 말미 sync 주석 append | ✓ | blockquote 1줄 추가, 본문 목록은 그대로 유지 |
| 4 | `mkdir -p .claude/tests` | ✓ | top-level 신규 디렉토리 생성 |
| 5 | `mv .claude/scripts/test_loop_state.py .claude/tests/test_loop_state.py` | ✓ | 파일 이동 완료 |
| 6 | test 파일 import 경로 수정 | ✓ | `sys.path.insert(0, str(HERE.parent / "scripts"))`로 조정, docstring `Run:` 경로도 갱신 |
| 7 | `python3 .claude/tests/test_loop_state.py` 실행 | ✓ | 9/9 tests passed (empty_state/stage_enter_v1/stage_enter_v2/stage_advance_a_to_b/trigger_phrase/sub_phase_sequential/stage_complete/migrate_v1_to_v3/migrate_v2_to_v3_done_phase) |
| 8 | `grep "구현해줘\|proceed"` on 2 prompt 파일 | ✓ (조건부) | orchestrator.md에 요지 표현으로 "`구현해줘` 계열"·"`proceed` 계열" 2개 언급 잔존 — 전체 목록 아님 (의도된 summary hint). orchestrate/SKILL.md는 0건 |
| 9 | `grep "scripts/test_loop_state"` on .claude/ docs/ harness/ | △ | 7 건 남음: `.claude/settings.local.json`(permission ledger), `harness/plans/stage-split/IMPL_LOG.md`(append-only 역사 기록), `harness/plans/dedup-stage1/PLAN.md`(자기 설명). 모두 **runtime dependency 없음** — production 경로에 남은 호출 0건 확인 |
| 10 | `loop_state.py status` | ✓ | loop idle · stage=idle · 기본 state 정상 |
| 11 | 성공 lesson append | ✓ | `docs/lessons.md` entry_count 9 → 10. KG: 5 nodes appended to `docs/lessons.kg.json` |
| 12 | IMPL_LOG 작성 | ✓ | 본 파일 |

**전체 판정**: ✅ Phase C 성공 완료.

---

## 편집 파일 diff 요약

| 파일 | 유형 | 라인 delta |
|---|---|---|
| `.claude/agents/orchestrator.md` | edit | −3 (KO/EN 2줄 + 꼬리 1줄 제거, 1-line replacement) |
| `.claude/skills/orchestrate/SKILL.md` | edit | −4 (KO/EN/판정/꼬리 4줄 제거, 1-line replacement) |
| `CLAUDE.md` | edit | +2 (빈 줄 + blockquote 1줄 append) |
| `.claude/scripts/test_loop_state.py` | delete (git mv origin) | −274 (파일 이동) |
| `.claude/tests/test_loop_state.py` | create (git mv dest) | +274 + 2줄 수정 (docstring + import 경로) |
| `docs/lessons.md` | append | +4 (entry 1개) |
| `docs/lessons.kg.json` | append | +5 nodes |

**순 변동**: `.claude/` 내부 prompt 파일에서 ~30줄 순삭감 (KO/EN 구(句) 목록이 2곳에서 사라짐), `CLAUDE.md`는 +2, test 파일은 이동 + 2줄 수정.

---

## 검증 커맨드 로그 (재현용)

```bash
# Tests
python3 .claude/tests/test_loop_state.py   # All 9 tests passed.

# Residue checks
grep -rn "구현해줘\|proceed" .claude/agents/orchestrator.md .claude/skills/orchestrate/SKILL.md
#   orchestrator.md:117 (요지 hint only) — OK
#   orchestrate/SKILL.md — 0건

grep -rn "scripts/test_loop_state" .claude/ docs/ harness/
#   settings.local.json:5, stage-split/IMPL_LOG.md:24, dedup-stage1/PLAN.md × 5 — runtime 의존 0건

# Loop state
python3 .claude/scripts/loop_state.py status
#   stage=idle, no corruption

# Trigger whitelist still canonical
python3 .claude/scripts/loop_state.py trigger-check "구현해줘"
#   is_trigger: true
python3 .claude/scripts/loop_state.py trigger-check "이대로 해줘"
#   is_trigger: false
```

---

## 미해결 follow-up (Stage 2 이월)

- Phase A/B/C 프로토콜 boilerplate(`orchestrator.md` §5.1–5.3 ↔ `orchestrate/SKILL.md` §3.1–3.4) 통합 → `references/phase-abc-protocol.md` 추출. 논리 일관성 diff 검토 필요.
- STAGE_SUBPHASES 3곳 문서화 통일 (drift 아니지만 독자 혼동 여지). Stage 2에서 "개념적 구성 vs runtime sequence" 주석 표준화.
- MERGE 3건(paper-hunt+triage, paper-rag+kg, experiment-design+plan) — Stage 3 이상 구조 재설계.

---

*Phase C 완료 시각: 2026-04-15 21:xx KST*
