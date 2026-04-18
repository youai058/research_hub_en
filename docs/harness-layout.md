# Harness Layout (CLAUDE.md §5·§7 분리본)

## Directory Structure

```
research_hub/
├── CLAUDE.md                 (이 파일)
├── docs/
│   ├── lessons.md            전역 lessons
│   ├── lessons-paper.md      논문 수집·요약·RAG
│   ├── lessons-research.md   답변 formulate·근거 비판·검증 계획
│   ├── lessons-impl.md       코드 구현·검증
│   └── lessons-analysis.md   결과 분석
├── .claude/
│   ├── settings.json
│   ├── agents/               14종 에이전트 정의 (+ harness-engineer, kg-curator, paper-triage, abstract-indexer, codex-reviewer)
│   ├── skills/               22종 스킬 (research 12 + paper-kg + harness-* 7 + experiments 3: experiment-design/impl/report)
│   ├── hooks/                8종 (session_start, mark_indices_stale, protect_chroma, protect_kg, protect_external_paths, guard_empty_rag advisory-only, phase_advance_check, inject_lessons)
│   ├── scripts/              유틸리티 (loop_state.py v3 + report_builder.py + lesson.py)
│   └── commands/             10종 (/research-papers, /research-qa, /research-experiments, /research-analyze, /research-status, /research-rag, /research-index, /research-lesson, /research-kg, /research-triage)
├── papers/
│   ├── metadata/<Venue>/<Year>/<slug>.raw.md   paper-hunter 원본 메타
│   ├── marp-summary/<Venue>/<Year>/<slug>.md   adaptive Marp 요약 (PLANNING-first, 4 앵커)
│   ├── digest/<Venue>/<Year>/
│   │   ├── <slug>.digest.md                    Gemini Stage-1 digest
│   │   └── .pdf_cache/<slug>.pdf               PDF 캐시
│   └── vector_db/
│       ├── chroma/                   ChromaDB persistent store (index.py가 자동 생성)
│       ├── manifest.json            RAG 해시·mtime 증분 상태
│       ├── kg.sqlite                SQLite triplestore
│       ├── kg-manifest.json         KG 해시·ingest 상태
│       ├── extraction_log.jsonl     KG audit log
│       ├── rejected.jsonl           KG validation fail log
│       ├── schema.version           KG schema version
│       ├── rag.stale                RAG stale marker
│       ├── kg.stale                 KG stale marker
│       └── kg-staging/              .kg.json 부산물 수집 대기
├── research/
│   ├── answers/YYYY-MM-DD_<slug>.md  answer-formulator 산출 (Direct Answer + Evidence Chain)
│   ├── critiques/<slug>.md           근거 체인 4축 비판
│   ├── diagnoses/<slug>.md           Evidence verification outcome + revision seed
│   ├── topics/<slug>.md              paper-triage run log (append-only, runtime only; A-2에서 생성)
│   ├── plans/
│   │   ├── <slug>/PLAN.md            experiment-level PLAN (code-implementer 소비, 기존 평탄 경로 유지)
│   │   └── <stage>/<slug>/v<N>/PLAN.md   stage-level PLAN (Phase A 산출, 버전링) — stage ∈ {papers, qa, experiments, analyze}
│   ├── reports/
│   │   └── <stage>/<slug>/v<N>/
│   │       ├── Report.md             stage Phase C 종료 산출 (md)
│   │       └── Report.slides.md      stage Phase C 종료 산출 (Marp 슬라이드)
│   └── loop_state.json               현재 루프 단계 (v3 schema)
├── experiments/
│   └── <slug>/
│       ├── code/
│       ├── configs/
│       ├── run.sh
│       └── IMPL_MAP.md               Evidence ↔ Experiment ↔ Code 3-way 매핑
├── harness/
│   └── plans/<name>/                 하네스 인프라 PLAN (루프와 직교; 예: stage-split)
└── results_<slug>/                   실험 산출물
```

> **단종 커맨드**: `/research-start`, `/research-autonomous` 두 커맨드는 v3 refactor에서 폐지됐다. 대체 경로: 새 사이클은 `/research-papers <topic>` (또는 필요한 stage 커맨드 직접 호출)로 시작. autonomous 모드 자체가 제거됐으므로 on/off 개념은 없다.

## 9 Configuration Surfaces

Claude Code 하네스는 9종 configuration surface를 노출한다. research_hub는 **6종을 적극 사용**하고 3종은 의도적으로 미사용이다.

### 사용 중 (6종)

| # | Surface | 경로 | 용도 |
|---|---|---|---|
| 1 | settings.json | `.claude/settings.json` | permissions, env, hooks 등록, statusLine |
| 2 | agents | `.claude/agents/*.md` | 14종 페르소나 정의 (paper-hunter, paper-triage, abstract-indexer, codex-reviewer, ...) |
| 3 | skills | `.claude/skills/*/SKILL.md` | 22종 절차적 스킬 (progressive disclosure) |
| 4 | commands | `.claude/commands/*.md` | 10종 slash command |
| 5 | hooks | `.claude/hooks/*` + settings.json `hooks` | 8종 (아래 표 참조) |
| 6 | CLAUDE.md / memory | `./CLAUDE.md`, `docs/lessons*.md` | 역할·워크플로우·자기개선 루프 SSOT |

### Commands 상세 (10종)

4개 stage 커맨드 + 6개 관리/조회 커맨드:

| # | 커맨드 | 종류 | 역할 |
|---|---|---|---|
| 1 | `/research-papers <topic>` | stage | `papers` stage Phase A→B→C. paper-hunter → paper-triage → paper-summarizer → rag-curator. |
| 2 | `/research-qa <slug> <question>` | stage | `qa` stage Phase A→B→C. answer-formulator → critic (+ codex-reviewer 병렬). |
| 3 | `/research-experiments <slug>` | stage | `experiments` stage Phase A→B→C. 내부 3 스킬 (experiment-design / experiment-impl / experiment-report). E-1 → E-2 → E-3 → report. |
| 4 | `/research-analyze <slug>` | stage | `analyze` stage Phase A→B→C. results-analyst (F-1) → codex-reviewer (F-2). diagnosis + revision seed. |
| 5 | `/research-status` | 조회 | `loop_state.json` v3 필드 + RAG 인덱스 + KG + lessons 카운트 요약. |
| 6 | `/research-rag <query>` | 조회 | RAG top-k ad-hoc 쿼리. 인덱싱 안 함. |
| 7 | `/research-index` | 관리 | RAG 증분(기본) 또는 `--rebuild` 전체 재인덱스. |
| 8 | `/research-lesson <domain> "<title>"` | 관리 | 해당 `docs/lessons*.md`에 3-line 엔트리 append (Rule/Why/When). |
| 9 | `/research-kg <build\|query\|node\|lookup\|stats>` | 관리 | SQLite KG 하위 커맨드 분배. |
| 10 | `/research-triage` | 관리 | raw.md 수집본을 주제 기준 Claude-native 점수화. |

### Hooks 상세 (8종)

| # | 파일 | 이벤트 | 역할 |
|---|---|---|---|
| 1 | `session_start.sh` | SessionStart | v3 스키마 (stage/inner_phase/sub_phase/slug/stage_version) + RAG/KG/lessons 카운트 주입. autonomous 블록 제거됨. |
| 2 | `mark_indices_stale.sh` | PostToolUse(Write\|Edit\|MultiEdit) | papers/ 수정 시 RAG·KG stale 마커 touch |
| 3 | `protect_chroma.sh` | PreToolUse(Write\|Edit) | `papers/vector_db/chroma/` 내부 파일 직접 수정 차단 |
| 4 | `protect_kg.sh` | PreToolUse(Write\|Edit) | `papers/vector_db/kg.sqlite` 직접 수정 차단 |
| 5 | `protect_external_paths.sh` | PreToolUse(Write\|Edit\|MultiEdit\|Bash) | research_hub 바깥(특히 LLM/LLDM/~/.claude) 쓰기 및 유료 API·HF 다운로드 차단 |
| 6 | `guard_empty_rag.sh` | PreToolUse(Bash) | **advisory-only (v3)**: RAG manifest가 비었을 때 `/answer-formulate`·`/critique`·`/research-qa` 등에 stderr 경고만 (차단 안 함). `RESEARCH_HUB_GUARD_QUIET=1`로 silencing 가능. |
| 7 | `phase_advance_check.sh` | Stop | v3 스키마 기반 stage × sub_phase 상태 보고 sub-phase advance 또는 `stage-complete` 시기 advisory 출력 (mutate 금지). |
| 8 | `inject_lessons.sh` | UserPromptSubmit | 전역 `lessons.md` 최근 3 엔트리 + 도메인 카운트를 프롬프트에 주입 |

### 의도적 미사용 (3종)

| # | Surface | 사유 |
|---|---|---|
| 7 | MCP servers (`.mcp.json`) | 모든 외부 I/O는 Python 스크립트(`.claude/scripts/`) + 훅 경로로 집행. MCP 도입 시 권한·감사 surface가 이중화되므로 보류. repo-level `.mcp.json`은 `{"mcpServers": {}}` 의도적 빈 스텁으로 유지. |
| 8 | output-styles (`.claude/output-styles/*.md`) | Marp 5-part 포맷이 이미 `paper-summarize` 스킬에 하드코딩되어 있어 전역 출력 스타일 변경이 불필요. |
| 9 | keybindings (`~/.claude/keybindings.json`) | user global 영역이고 머신/운영자별 선호이므로 repo에서 관리하지 않음. 필요 시 개별 사용자가 직접 편집. |

## 에이전트 팀 구성

| 에이전트 | 전문 영역 | 활성 Sub-phase | 소속 stage |
|---------|---------|-----------|---|
| paper-hunter | venue API 스캔·수집 | A-1 | papers |
| abstract-indexer | raw.md abstract를 bge-m3로 embed해 ChromaDB `abstracts` collection에 증분 upsert. A-2 triage의 dense-retrieval pre-filter용. | A-1.5 | papers |
| paper-triage | abstract 기반 Claude-native 관련도 점수화(0-5) + accepted 필터 | A-2 | papers |
| paper-summarizer | 5-part 비판적 요약 | A-3 | papers |
| rag-curator | 임베딩·벡터 스토어 유지 | A-4 (주), 모든 sub-phase 끝단 선택 호출 | papers |
| answer-formulator | hybrid_query → Direct Answer + Evidence Chain (divergent ideation 금지) | B-1 | qa |
| critic | 근거 체인 4축 독립 비판 (Grounding/Support/Counter-Evidence/Verifiability) | B-2, 실험 설계 검토 보조 | qa, experiments |
| experiment-planner | Evidence 1:1 verification 실험 설계 (Expected Under/If Wrong 사전 명시) | C-1 (experiments Phase A) | experiments |
| code-implementer | 코드 구현·외부 레포 통합 (3-way IMPL_MAP + decide_verdict) | E-1 | experiments |
| implementation-verifier | incremental QA + Evidence verification boundary 확인 | E-2 | experiments |
| results-analyst | Evidence 단위 verdict (CONFIRMED/REFUTED/INCONCLUSIVE/IMPL_BUG) + diagnosis·시각화 | F-1 | analyze |
| kg-curator | SQLite KG 증분 ingest·검증·쿼리 | 모든 sub-phase 끝단 (kg `.stale` 감지 시) | cross-stage |
| codex-reviewer | Codex CLI 기반 3rd-party adversarial review | B-2 (critic 병렬), E-3 (최종 게이트), F-2 (최종 게이트) | qa, experiments, analyze |
| harness-engineer | Claude Code 하네스(9 surface) 구성·수정 | out-of-loop | — |

## Stage × Phase 요약

| Stage | STAGE_SUBPHASES (Phase C 체인) | 산출물 |
|---|---|---|
| `papers` | A-1 → A-2 → A-3 → A-4 | `papers/marp-summary/<V>/<Y>/*.md`, `research/reports/papers/<slug>/v<N>/` |
| `qa` | B-1 → B-2 | `research/answers/`, `research/critiques/`, `research/reports/qa/<slug>/v<N>/` |
| `experiments` | (C-1 satisfied in Phase A) → E-1 → E-2 → E-3 + experiment-report skill | `experiments/<slug>/`, `research/reports/experiments/<slug>/v<N>/` |
| `analyze` | F-1 → F-2 | `research/diagnoses/`, `research/reports/analyze/<slug>/v<N>/` |

`STAGE_SUBPHASES`는 `loop_state.py` 단일 SSOT로 정의됨. **Stage 간 auto-chain 금지**.

## Versioning

- 동일 `<stage, slug>` 조합 재실행 시 `loop_state.py stage-enter`가 `research/plans/<stage>/<slug>/v*/` + `research/reports/<stage>/<slug>/v*/` 글롭 → `max(existing) + 1`을 `stage_version`에 할당.
- PLAN.md · Report.md · Report.slides.md는 `v<N>/` 하위. **이전 버전 수정·삭제 금지**.
- `latest` 심볼릭 링크는 선택적 편의 (실패해도 치명적 아님).
- 60일 이상 된 stage 버전 디렉토리는 수동 정리 권장.

## Phase B 트리거 whitelist

상세는 CLAUDE.md §4.3 + `.claude/scripts/loop_state.py` TRIGGER_WHITELIST 참조 (SSOT 2곳, Dedup Stage 1 lesson 2026-04-15).

자세한 워크플로우는 각 stage slash command (`.claude/commands/research-*.md`)와 `CLAUDE.md §4`에 정의되어 있다.

## Dispatch rules (2026-04-16 refactor)

- Phase A PLAN.md writers are the four specialist planners (`paper-hunter`, `answer-formulator`, `experiment-planner`, `results-analyst`) dispatched by the stage slash command with `mode=plan-only` and `run_in_background: true`.
- Phase C sub-phases are owned by the stage slash command, which dispatches each sub-phase as a separate `Agent(..., run_in_background=true)` call and verifies the artifact between dispatches.
- The only main-session (foreground) step is the `topic-refine` skill in `/research-papers`, which is interactive by nature.
- No agent delegates to another agent. Orchestration is a main-session responsibility.
