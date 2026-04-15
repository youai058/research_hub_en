# PLAN — Intent Router (`/research` natural-language entry → agent pick → auto stage-enter)

> Phase A (계획) 전용. 구현 금지. 사용자가 `§7 Phase B` 트리거 phrase를 명시해야 Phase C(실제 파일 편집)로 이행한다.
>
> 확정된 설계 방향 (사용자 O4 해석 1): **orchestrator가 14 agent description 기반 분류로 best agent 1개를 고르면 그 agent의 소속 stage로 자동 진입하여 표준 Phase A/B/C를 탄다**. B→C 트리거 게이트는 각 stage 내부 규칙 그대로. Router는 "어느 stage로 들어갈지"만 자동화.

---

## 1. Summary (1 문단)

사용자가 `/research "DPO reward hacking 관련 최근 논문 좀 모아줘"` 같은 자연어를 입력하면, 새 슬래시 커맨드 `/research`가 (a) plain text를 받아 (b) orchestrator 에이전트에게 "분류 전용 모드"로 dispatch하고, (c) orchestrator는 `.claude/agents/*.md` frontmatter description만을 판단 재료로 써서 12개 research-loop 에이전트(papers: paper-hunter/triage/summarizer/rag-curator, qa: answer-formulator/critic, experiments: experiment-planner/code-implementer/implementation-verifier, analyze: results-analyst, + codex-reviewer/kg-curator는 예외 경로) 중 best 1개를 고른다. (d) 선택된 agent의 소속 stage는 orchestrator.md §2 표의 "소속 stage" 컬럼을 SSOT로 쓰며, 해당 stage에 대해 `loop_state.py stage-enter --stage <S> --slug <slug-or-derived>`를 호출한 뒤 기존 `/research-<stage>` 커맨드와 **동일한 Phase A/B/C 프로토콜**로 넘어간다. Slug는 자연어에서 topic-like 경우 자동 파생(papers), qa/experiments/analyze는 필수 인자로 재질문. Ambiguous·out-of-scope·cross-cutting(kg-curator / harness-engineer / codex-reviewer 단독) 요청은 bail-out해서 기존 4 stage 커맨드 중 어느 것을 써야 하는지 3개 예시와 함께 안내. SSOT는 agent frontmatter 단일 — 복사본은 만들지 않으며 (Dedup Stage 1 lesson), stage 매핑은 **이미 존재하는** orchestrator.md §2 표를 참조한다.

---

## 2. Facts (조사 결과)

### 2.1 현재 하네스 상태

- **Agents (14)**: `.claude/agents/` 아래 14 파일 전부 frontmatter에 `name`·`description`·`model: opus` 3필드. `stage:` 필드는 **없음**. 각 description은 한국어 120–250자 + "xxx 관련 요청 시 호출된다" trigger 문구 + (일부) 배제 경계("LLDM 범위 아님" 등)로 구성.
- **Agent→stage 매핑 SSOT (현행)**: `.claude/agents/orchestrator.md` §2 표 (lines 36–48, 12행 컬럼 = 에이전트 / 전문 영역 / 활성 Sub-phase / **소속 stage**). 값은 `papers / qa / experiments / analyze / cross-stage / out-of-loop` 6종. `docs/harness-layout.md`는 authoritative dup 문서로 명시.
- **Commands (10)**: `research-papers / -qa / -experiments / -analyze / -status / -index / -rag / -lesson / -kg / -triage`. 전부 `.claude/commands/<name>.md` 1파일. `/research` (no suffix)는 **없음**.
- **Command 구조**: `/research-papers` = "Step 1 Preflight → Step 2 `loop_state.py stage-enter --stage papers --topic "$ARGUMENTS"` → Step 3 Phase A(orchestrator dispatch) → Step 4 제시 → Step 5 trigger 대기 → Step 6 Phase C". `/research-qa`/`/research-experiments`/`/research-analyze`는 동일 골격에 `--slug $1` 필수가 다름.
- **loop_state.py stage-enter 시그니처**: `--stage <papers|qa|experiments|analyze>` 필수, `--slug <explicit>` 또는 `--topic <free-text>` 하나 필수 (둘 다 없으면 SystemExit). topic 제공 시 내부에서 `YYYY-MM-DD_<slugified>` 파생. busy 상태면 `status: "busy"` 반환.
- **Trigger whitelist SSOT**: `loop_state.py TRIGGER_WHITELIST` + CLAUDE.md §4.3 (Dedup Stage 1 lesson). `.claude/agents`·`.claude/skills`에 사본 금지.
- **기존 lessons**: "Stage-split refactor" — 4 stage 독립 / B→C 사용자 트리거 필수 / autonomous 전면 폐기. 이 PLAN은 이 조항을 훼손하지 않음 (router는 **stage 진입만 자동화**, B→C는 stage 내부 규칙 그대로).

### 2.2 Agent description 분류가능성 실측

14개 description 읽은 결과:

| 에이전트 | description trigger 문구 | 소속 stage (orchestrator.md §2) | 분류 난이도 |
|---|---|---|---|
| paper-hunter | "논문 수집", "arxiv 검색", "OpenReview 논문", "venue 스캔", "새 논문 찾기" | papers | 쉬움 (venue·arxiv 키워드 강함) |
| paper-triage | "논문 triage", "relevance 선별", "accepted subset", "abstract 점수화" | papers | 쉬움 |
| paper-summarizer | "논문 요약", "paper summary", "Marp 변환", "5-part 정리", "비판적 독해" | papers | 쉬움 |
| rag-curator | "RAG 갱신", "벡터 인덱싱", "논문 검색", "chroma 쿼리", "임베딩 업데이트" | papers | 중간 (단독 RAG 쿼리는 `/research-rag`와 겹침 — 아래 참조) |
| answer-formulator | "답변 작성", "근거 체인", "evidence chain", "direct answer", "사용자 질문 답변" | qa | 쉬움 |
| critic | "답변 비판", "근거 검증", "counter-evidence", "grounding 검토" | qa (+ experiments) | 중간 (2 stage 소속이라 answer 문맥 요구) |
| experiment-planner | "evidence 검증 실험", "PLAN.md 작성", "verification plan" | experiments (Phase A) | 쉬움 |
| code-implementer | "실험 구현", "코드 구현", "PLAN 따라 구현", "외부 레포 통합" | experiments | 쉬움 |
| implementation-verifier | "구현 검증", "QA", "boundary check", "smoke test" | experiments | 쉬움 |
| results-analyst | "evidence 검증 결과", "diagnosis", "verification outcome", "답변 수정 제안" | analyze | 쉬움 |
| kg-curator | "KG 갱신", "트리플 upsert", "KG 쿼리", "지식 그래프 검증" | **cross-stage** | 특수 — stage 없음 |
| codex-reviewer | 리뷰 요청, E-3/F-2 게이트 | **multi-stage (qa/experiments/analyze)** | 특수 — 단독 불가 |
| harness-engineer | "하네스 수정", "settings 편집", "훅 추가", "skill/agent/command 생성", "MCP 등록" | **out-of-loop** | 특수 — stage 아님 |
| orchestrator | "stage A 진행", "실험 설계 Phase A", "analyze 결과 정리" (본인) | N/A | 본인이 분류자라 제외 |

**결론**: 12개 research-loop 에이전트 중 **11개는 description이 충분히 disjoint**해서 Claude-native 판단으로 best 1 pick 가능. rag-curator 단독 query("최근 DPO 논문 검색")만 약간 모호(기존 `/research-rag` 커맨드와 경합). critic 단독("이 답변 비판해줘")도 가능하지만 선행 answer 파일이 필요.

### 2.3 기존 PLAN 포맷 선행 연구

- `harness/plans/stage-split/PLAN.md`: 0 한줄 / 1 현재 / 2 새 구조 / 3+ checklist 순. 풍부하지만 이번 범위(1 커맨드 + 3–4 파일 변경)에는 과함.
- `harness/plans/dedup-stage1/PLAN.md`: 0 한줄 / 1 현재 확인 사실 / 2 변경 상세 / 3 비범위 / 4 risk 구조. **본 PLAN은 이 포맷을 7-section 프로토콜에 매핑해 따른다**.

---

## 3. Changes (파일·라인·추정 LOC)

### 3.1 신규 파일 (1개)

**C-1. `.claude/commands/research.md` (신규, ≈110 LOC)**
- Frontmatter: `description: Natural-language entry point. Routes free-text intent to one of 12 research-loop agents and auto-enters that agent's stage (Phase A/B/C).` + `argument-hint: <free-text intent>`.
- Step 1 — Parse: `$ARGUMENTS` 비어있으면 "자연어 의도를 입력해주세요 (예: 'DPO 논문 모아줘', '...에 대한 답변 만들어줘', '실험 구현해줘', '결과 분석해줘')" 안내 후 종료.
- Step 2 — Dispatch orchestrator in **classify-only mode**: input = raw text. Output JSON = `{"agent": "<name>", "stage": "papers|qa|experiments|analyze", "slug_hint": "...|null", "topic_hint": "...|null", "confidence": "high|medium|low", "reasoning": "2줄"}`. 부작용 금지 — stage-enter 호출·에이전트 dispatch·파일 편집 어느 것도 수행하지 않는다.
- Step 3 — Route by confidence:
  - `high` + stage ∈ {papers, qa, experiments, analyze} → Step 4로.
  - `medium` → 사용자에게 "`<agent>` 로 가려 하는데 맞으신가요? 아니면 `/research-papers`·`/research-qa`·`/research-experiments`·`/research-analyze` 중 직접 선택해주세요" 재확인, 명시 동의 없으면 중단.
  - `low` 또는 특수 agent(kg-curator / harness-engineer / codex-reviewer 단독 / orchestrator 자기선택) → bail-out: 4 stage 커맨드 리스트 + 3 구체 예시("`/research-papers DPO reward hacking`" 등) 출력 후 종료. `/research-kg`·harness-engineer·codex-reviewer는 **router 범위 외**라고 명시.
- Step 4 — Derive slug/topic and stage-enter:
  - `papers`: `$ARGUMENTS` 전체를 `--topic`으로 넘겨 `loop_state.py stage-enter --stage papers --topic "$ARGUMENTS"` (기존 `/research-papers` 그대로).
  - `qa/experiments/analyze`: slug hint가 있으면 `--slug <hint>` + 남은 텍스트를 `--topic`으로, slug hint 없으면 "이 stage는 기존 slug가 필요합니다. `/research-<stage> <slug> ...` 형태로 직접 호출해주세요"라고 bail-out. Router가 slug를 **추측 생성하지 않는다** (재현성 원칙).
- Step 5 — Delegate to canonical stage command: `/research-<stage>` 커맨드와 **동일한 Phase A(orchestrator dispatch) → Step 4 PLAN 제시 → Step 5 트리거 대기 → Step 6 Phase C** 흐름을 그대로 재사용. 구현상으로는 `research.md` Step 5가 4개 기존 커맨드의 Step 3–6을 `include` 하는 방식 대신 **해당 커맨드 전체를 사용자 입장에서 재호출하도록 안내**하거나, stage-enter 이후 orchestrator dispatch 블록을 `research.md` 안에 복제. **이 PLAN은 두 방안 중 어느 것이 lesson "SSOT 단일화"에 더 맞는지 Phase B에서 사용자 결정**을 받는다. 기본안: 복제 (슬래시 커맨드는 템플릿이라 include 메커니즘이 빈약).

### 3.2 수정 파일 (3–4개)

**M-1. `.claude/agents/orchestrator.md` — §3 라우팅 규칙 확장 (≈25 LOC 증가)**
- 현 §3 (lines 55–64)은 "하네스 수정 / 연구 루프 / stage 외" 3분류. 여기에 **새 라우팅 4번: "자연어 intent 분류 모드"** 항목 추가.
- 내용: classify-only dispatch 계약(input·output JSON schema·부작용 금지) + confidence 판정 규칙(high=agent trigger 문구가 input에 직접 등장 / medium=semantic overlap 존재하되 2+ agent가 경합 / low=trigger 문구 fuzzy + cross-stage/harness 경로) + bail-out 조건.
- stage-agent 매핑은 **§2 표를 참조**한다고만 명시 — 목록 복사 금지.

**M-2. `.claude/agents/orchestrator.md` — description 확장 (≈1 LOC 증가)**
- Frontmatter description 말미에 `"자연어 intent 라우팅", "어떤 agent/stage로 갈지 분류"` trigger 문구 추가. `/research` 커맨드가 `orchestrator` agent를 classify 모드로 dispatch할 때 description match에 걸리도록.

**M-3. `.claude/skills/orchestrate/SKILL.md` — classify 모드 섹션 신규 (≈40 LOC 증가)**
- 기존 SKILL은 Phase A/B/C 관리 절차. 여기에 **"Intent Classification Mode"** 섹션 추가: input text → agent pick → stage 추론 → JSON return 절차를 명세. 4-axis judgment rubric(explicit trigger / semantic overlap / scope fit / stage membership)과 confidence threshold 결정 규칙을 여기서 정의. `references/agent-triggers.md` 같은 복사본 파일은 **만들지 않는다** (SSOT는 agent frontmatter).

**M-4. `docs/lessons.md` — 이 리팩터 자체 lesson 1건 append (≈4 LOC)**
- Phase C 종료 시점에 append. Rule: "자연어 intent 라우팅은 orchestrator classify 모드 단일 경로, SSOT는 agent frontmatter description, stage 매핑은 orchestrator.md §2 표". Why+When 2줄.

### 3.3 명시적 비변경 (Non-edit)

- `.claude/agents/*.md` 14개 파일의 description 본문 (M-2 orchestrator 제외). 14개에 `stage:` 필드 신규 도입하지 **않는다** (D2 참조).
- `.claude/scripts/loop_state.py`: stage-enter 시그니처 그대로. 신규 플래그 없음.
- `.claude/commands/research-{papers,qa,experiments,analyze}.md` 4개: 인자·Step·trigger gate 전부 불변. `/research` 는 이들의 **상위 dispatcher**일 뿐.
- `CLAUDE.md`: §4 standard workflow 문단 불변 (4 stage 커맨드가 여전히 canonical entry, `/research`는 "편의 진입" 위치).

### 3.4 LOC 추정 합계

| 파일 | 신규/수정 | LOC |
|---|---|---|
| `.claude/commands/research.md` | 신규 | ~110 |
| `.claude/agents/orchestrator.md` §3 | 수정 | +25 |
| `.claude/agents/orchestrator.md` frontmatter | 수정 | +1 |
| `.claude/skills/orchestrate/SKILL.md` classify 섹션 | 수정 | +40 |
| `docs/lessons.md` | append | +4 |
| **총** | | **≈180 LOC, 4–5 파일** |

---

## 4. Non-goals (명시 금지)

- **D2 옵션 a 금지**: `.claude/agents/*.md` 14개 frontmatter에 `stage:` 필드 신규 도입하지 않는다. 기존 orchestrator.md §2 표가 이미 SSOT이며 Dedup Stage 1 lesson에 따라 복제를 피한다.
- **Agent description 목록 복사 금지**: orchestrate/SKILL.md에 14 agent의 trigger 문구를 복사하지 않는다. classify 모드는 Claude가 `.claude/agents/*.md` 파일을 직접 읽어 판단.
- **autonomous 부활 금지**: `/research`가 이름으로 autonomous를 연상시키지만, B→C 트리거 게이트는 각 stage 내부 규칙 그대로. Router는 stage-enter **만** 자동화.
- **Slug 추측 금지 (qa/experiments/analyze)**: 선행 stage의 slug를 재사용하거나 사용자가 명시해야 함. router가 새 slug를 만들면 재현성·버전링이 깨진다.
- **4 stage 커맨드 deprecate 금지**: `/research-papers` 등은 canonical entry로 유지. `/research`는 편의 진입이며 자신이 없으면 항상 4 canonical을 제안.
- **Command 간 include 메커니즘 구현 금지**: 슬래시 커맨드는 템플릿이므로, `/research` 안에서 `/research-papers` 본문을 재사용해야 한다면 복제로 처리. `include`·`source` 같은 신규 처리기 도입하지 않는다.
- **실제 파일 생성·편집**: 이 PLAN.md 외 금지. Phase B 트리거 phrase 받은 후에만 Phase C.

---

## 5. Risk / 완화

| # | Risk | 확률 | 영향 | 완화 |
|---|---|---|---|---|
| R1 | Classification confidence 오판 (medium을 high로 → 엉뚱한 stage-enter) | 중 | 큼 (busy 상태에 멀쩡한 stage 진입 후 실패) | confidence 판정을 orchestrator가 JSON으로 명시 return하도록 강제. `medium` 이하는 반드시 사용자 재확인. stage-enter는 확인 통과 후에만 실행. |
| R2 | rag-curator 단독 쿼리와 `/research-rag` 경합 | 낮 | 중 (쿼리가 papers stage full 진입으로 확대) | classify 출력에서 "단독 RAG 쿼리"로 판단되면 `/research-rag "<q>"` 사용을 권장하며 bail-out. agent rag-curator 픽해도 stage=papers로 진입하지 않음. |
| R3 | kg-curator / harness-engineer / codex-reviewer 단독 요청이 4 stage 중 하나로 오분류 | 중 | 큼 (잘못된 Phase A/B/C 진입) | classify 단계에서 cross-stage/out-of-loop agent를 먼저 필터. 해당 시 즉시 bail-out + 대응 경로(`harness-engineer`는 별도 dispatch 안내, `/research-kg` 커맨드, codex는 기존 게이트 내부) 안내. |
| R4 | Slug hint 자동 추출 실패 (qa/experiments/analyze) | 높 | 낮 (bail-out으로 resolve) | 이 PLAN은 slug 자동 생성을 금지하고 **필수 인자 재질문**으로 명시. 실패는 bail-out이지 잘못 실행 아님. |
| R5 | orchestrator.md description에 trigger 추가 시 기존 routing rule과 충돌 (기존 §3 "연구 루프 요청"과 "intent 분류 모드" 트리거 fuzzy overlap) | 낮 | 중 | §3 경계를 "커맨드 컨텍스트 있는 stage 요청" vs "`/research` 커맨드에서 classify-only 호출" 2가지로 명시 구분. classify 모드는 `/research` 커맨드에서만 dispatch됨. |
| R6 | 14 agent description이 향후 변경돼 drift 발생 | 중 | 낮 | SSOT 단일이므로 drift가 자동 해소. classify 로직은 파일을 매번 읽어 판단하므로 stale 캐시 없음. |
| R7 | busy state (이전 stage 미완) 상태에서 `/research` 호출 | 중 | 중 | Step 4 stage-enter 이후 `status: "busy"` 반환 시 기존 `/research-papers` Step 2 busy handling 로직 복제 — 사용자에게 `stage-complete --force` vs abort 질문. |

---

## 6. 설계 결정 (D1–D5) 권장 + 근거

### D1 — Entry command: **(a) 신규 `/research <자연어>` 커맨드 채택** (권장)

- (a) 기존 4 stage 커맨드와 parallel 수준의 slash entry. 사용자가 typo로 `/research-` 멈칫할 때 `/research`가 fallback. 복잡도 최저.
- (b) `/research-status` 확장은 의미 오용 — status는 현재 상태 조회이지 entry 생성이 아님.
- (c) UserPromptSubmit 훅은 훅 실행 side-effect가 많아 디버그 어려움. 또 idle 상태 탐지 후 orchestrator dispatch는 훅 외부에서 커맨드로 해도 동등. complexity/benefit 대비 reject.

### D2 — Agent→Stage 매핑 저장 위치: **(d) 이미 존재하는 orchestrator.md §2 표를 SSOT로 계속 사용** (권장)

- 14 agent frontmatter는 domain description 용도이고 stage membership은 **orchestration 관심사**. 소속이 변경되면 orchestrator.md 한 파일만 수정하면 됨.
- (a) frontmatter `stage:` 필드: 14 파일 touch + 파싱 훅·검증 훅 추가 필요 + critic/codex-reviewer multi-stage를 단일 값으로 표현 불가 (`"qa,experiments"` 같은 꼼수 회피).
- (b) orchestrator.md 본문 static lookup: 이미 §2 표가 그 역할. **그러니 신규 lookup table을 만드는 대신 §2 표를 명시적으로 "router SSOT"라고 §3에서 참조**.
- (c) 별도 references 파일: Dedup Stage 1 lesson ("SSOT 단일화") 위반.

### D3 — Cross-cutting / multi-stage agent 처리: **(i) + (ii) 혼합** (권장)

- Router는 **11개 research-loop 에이전트(paper-hunter/triage/summarizer/rag-curator, answer-formulator/critic, experiment-planner/code-implementer/implementation-verifier, results-analyst)** 만을 classify 대상으로 삼는다. classify 출력에 kg-curator·harness-engineer·codex-reviewer·orchestrator가 등장하면 **low confidence로 강제 하향** + bail-out.
- bail-out 안내 문구: "KG 관련은 `/research-kg`, 하네스 수정은 harness-engineer agent 직접 호출, 리뷰는 기존 stage 내부 E-3/F-2 게이트"로 redirect.
- critic 단독("이 답변 비판해줘")은 선행 answer 파일 존재 시에만 qa stage 재진입으로 해석 — 대응은 **qa stage re-entry prompt** (실제 B-2만 재실행하는 서브 엔트리는 스코프 외).

### D4 — Ambiguous / unknown input 처리: **Confidence tier 3단계 + bail-out 포맷 확정** (권장)

- Claude-native 판정이므로 numeric score 대신 **JSON enum 3단계**: `high` / `medium` / `low`.
  - `high`: input에 해당 agent description의 trigger 문구가 **substring 또는 근접 번역** 수준으로 등장 + 다른 agent와 경합 없음.
  - `medium`: trigger 문구 semantic overlap 존재하되 2개 이상 agent가 후보. 사용자 재확인 필요.
  - `low`: trigger 문구 매치 빈약 / cross-stage·out-of-loop agent 의심 / fuzzy intent. 즉시 bail-out.
- Bail-out 출력 포맷: "무엇을 하려는지 명확치 않습니다. 다음 중 하나로 시도해주세요:\n 1. `/research-papers <topic>` — 논문 수집·triage·요약·RAG 인덱싱\n 2. `/research-qa <slug> <question>` — 질문에 대한 답변과 근거 비판\n 3. `/research-experiments <slug>` — Evidence 검증 실험 계획·구현\n 4. `/research-analyze <slug>` — 실험 결과 분석·diagnosis\n 자연어를 다시 구체화해서 `/research`에 재시도해도 됩니다."

### D5 — Slug 정책: **papers는 auto, qa/experiments/analyze는 재질문** (권장)

- `papers`: topic → `YYYY-MM-DD_<slugified-topic>` 자동 (기존 `/research-papers` 동작과 동일).
- `qa/experiments/analyze`: 선행 stage의 slug 재사용이 설계 의도(Stage-split lesson). router가 자연어에서 slug 추출하려면 fuzzy match가 필요하고 **이는 재현성·버전링에 치명적**. 따라서 slug를 **필수 인자로 재질문** — `/research` 내부에서 prompt로 "어느 slug에 대한 요청인가요? 현재 `research/plans/<stage>/` 아래 존재하는 slug: ..." 목록 제시 후 사용자 응답 대기. 응답 받으면 그때 stage-enter.
- 대안(slug hint 무조건 생성)은 R4와 "Stage-split refactor" lesson("v<N> 버전링으로 재현성 확보") 모두 위반.

---

## 7. Checklist (Phase C 실행 시 수행)

Phase B 트리거 받으면 이 순서대로 진행:

1. **C-1**: `.claude/commands/research.md` 신규 작성 (Step 1–5 본문 + frontmatter).
2. **M-1**: `.claude/agents/orchestrator.md` §3 라우팅 규칙에 4번 "Intent classification mode" 항목 추가 + classify 모드 dispatch 계약 명시.
3. **M-2**: `.claude/agents/orchestrator.md` frontmatter description에 `"자연어 intent 라우팅"` 트리거 phrase 1개 추가.
4. **M-3**: `.claude/skills/orchestrate/SKILL.md` 에 "Intent Classification Mode" 섹션 추가 (judgment rubric + confidence tier + bail-out 포맷).
5. **harness-validate 스킬 실행**: frontmatter·description trigger 충돌·파일 존재 검증.
6. **스모크 테스트 (5건)**:
   - `/research "DPO 논문 모아줘"` → paper-hunter → papers stage Phase A 진입.
   - `/research "reward hacking 실험 결과 분석해"` → results-analyst → analyze stage + slug 재질문.
   - `/research "하네스에 훅 추가해"` → bail-out (harness-engineer는 router 범위 외).
   - `/research "KG 갱신"` → bail-out (`/research-kg` 안내).
   - `/research "음 뭐 해볼까"` → low confidence bail-out (4 stage 안내 + 예시 3개).
7. **M-4**: `docs/lessons.md` append — 이 리팩터 자체 lesson (3-line Rule/Why/When to apply).
8. **codex-reviewer 최종 검토** (선택): 하네스 변경이므로 권장.

---

## 8. Phase B — 승인 요청

- 이 PLAN은 `/research` 자연어 entry + classify-only orchestrator 모드를 도입하며, 기존 4 stage 커맨드·14 agent frontmatter·loop_state.py를 건드리지 않는 **최소 침습 변경(≈180 LOC, 4–5 파일)** 이다.
- 핵심 설계 결정 D1–D5 권장을 **§6에 명시** — 각 결정에 대해 수정·반대 의견 환영.
- 특히 확인 요청:
  1. **D2 결정**: orchestrator.md §2 표를 SSOT로 계속 사용(권장) vs 14 frontmatter에 `stage:` 필드 신규 도입. 권장이 맞나요?
  2. **D5 결정**: qa/experiments/analyze에서 slug 재질문(권장) vs router가 최근 stage의 slug를 auto-pick. 재질문이 맞나요?
  3. **C-1 Step 5 구현 방식**: `/research` 안에 각 stage 커맨드 Step 3–6을 복제(권장) vs 사용자에게 canonical `/research-<stage>` 재호출 안내. 복제가 맞나요?
- 수정사항이 없으면 `구현해줘` / `proceed` / `go ahead` 등 `.claude/scripts/loop_state.py TRIGGER_WHITELIST` 소속 phrase로 응답해주세요.
- 수정사항이 있으면 이 문서에 직접 편집해주시거나 피드백으로 말해주시면 harness-engineer가 **동일 PLAN.md를 제자리 갱신** 후 재제시합니다.

*Hard stop. 트리거 phrase 없이는 Phase C 실행 절대 금지.*
