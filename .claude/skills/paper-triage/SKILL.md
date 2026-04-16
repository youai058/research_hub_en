---
name: paper-triage
description: 논문 관련도 선별. raw.md의 abstract를 주제 대비 0-5로 Claude가 직접 점수화(LLM-native, 외부 API 없음). 점수는 runtime only — raw.md frontmatter 미터치, 매 실행 독립. summarizer 입력 큐를 추려 Gemini digest 낭비를 줄인다. 부수 효과로 research/topics/<slug>.md에 토픽 이력 로그 append. 트리거 '논문 선별', '관련도 triage', 'relevance filter', 'abstract 점수화'.
---

# Paper Triage Skill

paper-hunter가 수집한 `raw.md` 풀을 현재 연구 주제 대비 관련도로 점수화하여 `paper-summarize`에 넘길 subset만 추린다. 점수는 **runtime only**. raw.md 파일을 미터치하고, 매 실행 독립이다. orchestrator Phase A-2 (paper-triage) 루프 단계로, A-1(paper-hunter)와 A-3(paper-summarizer) 사이에 위치한다.

## 철학

- **Claude-native**: 외부 judge(Gemini/OpenAI) 호출 없음. agent가 직접 abstract를 읽고 자기 추론으로 점수 부여.
- **Stateless**: triage_status 필드, manifest, hash 다 없음.
- **Non-destructive**: raw.md 미터치.
- **Summarizer-agnostic**: summarizer는 게이트 없이 호출받은 path를 처리. 필터링 책임은 orchestrator.
- **Log-but-don't-load**: 매 실행 `--topic "..."`이 canonical. 별도로 `research/topics/<slug>.md`에 이력 append. 재사용은 `--topic-from <slug>`로.

## 호출 예시

```bash
# 기본 실행
python3 .claude/skills/paper-triage/scripts/collect_abstracts.py \
    --glob "papers/metadata/**/*.raw.md" > /tmp/triage_input.json

# agent가 /tmp/triage_input.json을 Read해서 스코어링
# → threshold 3.0 이상 path 목록을 stdout에 한 줄씩 출력
# → topic_log.py append로 research/topics/<slug>.md 갱신
```

## 워크플로우 (agent 책임)

### Step 1 — Topic 확정

우선순위 (셋 중 정확히 하나):
1. `--topic-spec <path>` 주어짐 → `topic.json` 경로. `topic_spec.py validate <path>` 통과 필수. `refined_topic` + `triage_context`를 추출해 canonical topic으로 사용 (flat string 모드보다 **우선**).
2. `--topic-from <slug>` 주어짐 → `python3 topic_log.py load <slug>`로 텍스트 로드
3. `--topic "<string>"` 주어짐 → 그대로 사용
4. 아무것도 없음 → exit 2

`--topic-spec`과 `--topic`/`--topic-from`은 **mutually exclusive**.

Agent는 topic 텍스트와 함께 slug를 계산:

```bash
# --topic-spec 모드:
python3 .claude/skills/topic-refine/scripts/topic_spec.py get <path> refined_topic
# → slug는 스펙 파일명(<slug>.topic.json)에서 직접 파싱

# --topic 또는 --topic-from 모드:
python3 .claude/skills/paper-triage/scripts/topic_log.py slug --topic "<string>"
# → 예: lldm-late-step-<8hex>
```

### Step 2 — Abstract 수집

```bash
python3 .claude/skills/paper-triage/scripts/collect_abstracts.py \
    --glob "papers/metadata/**/*.raw.md"
```

stdout에 JSON 배열: `[{path, slug, title, abstract, venue, year, venue_class, published, categories}, ...]`

Agent는 이 JSON을 Read한다. 대량(≫150)이면 `--chunk 50`으로 분할 emit해 컨텍스트 관리.

### Step 3 — Claude-native scoring

Agent가 JSON 배열을 순회하며 **각 항목마다** topic 대비 0-5 점수와 1줄 사유를 부여한다. **모든 입력을 빠짐없이 처리, hallucinate 금지**.

**Rubric** (엄격히 적용):

- **5** — 주제의 핵심 기여와 직접 겹침. 방법·데이터셋·실험 설정까지 일치.
- **4** — 주제에서 쓰는 방법·데이터셋·모델과 직접 연결. 핵심 reference.
- **3** — 같은 서브필드, indirect 관련. 배경지식으로 유용.
- **2** — 주변부. 참고 가능하지만 핵심 아님.
- **1** — 무관한 주제. 표면적 키워드 겹침만.
- **0** — off-topic / noise. Out-of-scope와 겹침.

점수 판단 기준:
- **abstract 전체를 읽는다**. 제목·venue만 보고 판단 금지.
- 애매하면 **낮은 쪽**으로. 주제와 방향이 다른데 키워드만 겹치면 2 이하.
- 주제 텍스트에 명시적 "out of scope" 항목이 있으면 해당 논문은 즉시 0-1.

**`--topic-spec` 모드 추가 규칙** (구조화된 `triage_context` 입력일 때):

- `core_question`: 이 질문에 "yes, 이 논문이 답한다"고 말할 수 있는가가 primary judgment. Yes → 3+, No → 2 이하.
- `include`: 각 항목은 positive signal. 매치되면 baseline 3.
- `exclude`: 각 항목은 hard veto. 매치되면 **강제로 0–1**. abstract에서 exclude 근거가 보이면 다른 include 신호를 무시한다.
- `signal_methods`: 이 method명이 abstract에 언급되면 +1 bonus (단 core_question 실패면 무효).

`--topic` / `--topic-from` 모드(문자열 topic)에서는 rubric만 적용, 위 구조화 규칙은 무시.

### Step 4 — 필터링

- `--threshold F` (기본 **3.0**): score ≥ F만 accepted. 3.0은 rubric의 "같은 서브필드, indirect 관련" 이상을 통과시키는 기본값이다.
- `--top-n N`: 점수 내림차순 top N (threshold와 상호배타)
- 동점 시 `published` 최신 우선

### Step 5 — 출력

기본 포맷 `paths`: stdout에 한 줄당 accepted path (project-relative).
```
papers/metadata/etc/2026/foo.raw.md
papers/metadata/etc/2026/bar.raw.md
```

`--format json`: `[{path, score, reason}]` (orchestrator 파싱 용).
`--format table`: 사람 리뷰용 정렬 테이블 (stderr에 stat 포함).

### Step 6 — 이력 append

Agent는 결과 확정 후:
```bash
python3 .claude/skills/paper-triage/scripts/topic_log.py append \
    --slug <slug> --topic "<string>" \
    --stats-json '{"scanned":N,"accepted":M,"threshold":3.0,"accepted_slugs":["slug1",...]}'
```
→ `research/topics/<slug>.md` 생성 또는 기존 파일에 `## Runs` bullet append. `--no-save-topic` 플래그 있으면 이 단계 건너뛴다.

### Step 7 — Orchestrator에 반환

stdout의 accepted path 목록을 orchestrator가 캡처해 각 path를 `paper-summarize`에 전달한다. 점수는 여기서 버려진다.

## 토픽 파일 포맷 (`research/topics/<slug>.md`)

```markdown
---
slug: lldm-late-step-abcd1234
created_at: 2026-04-15T15:30:00+09:00
last_run_at: 2026-04-15T15:30:00+09:00
run_count: 1
---

# Topic
<토픽 원문 그대로>

## Runs
- 2026-04-15T15:30:00+09:00 — scanned 130, accepted 18 (threshold 3.0) [foo, bar, ...]
```

Append-only: 파일이 이미 있으면 `last_run_at`/`run_count` 갱신 + `## Runs`에 bullet 추가. 사용자가 수동 삭제하면 다음 실행이 `run_count=1`로 새로 생성.

## 체크리스트

- [ ] `--topic-spec` / `--topic` / `--topic-from` 중 정확히 하나
- [ ] `--topic-spec`이면 `topic_spec.py validate` 사전 통과
- [ ] `collect_abstracts.py` exit 0, JSON 파싱 성공
- [ ] 모든 입력 논문에 score 부여 (누락 0건)
- [ ] threshold/top-n 필터 적용, 동점 시 published 최신 우선
- [ ] 출력의 각 path가 실제 파일로 존재
- [ ] raw.md **미터치** (점수를 frontmatter에 쓰지 않음)
- [ ] `topic_log.py append` 호출 (`--no-save-topic` 없을 때)
- [ ] KST ISO8601 시간 사용

## 실패 처리

- `--topic`과 `--topic-from` 둘 다 / 둘 다 없음 → exit 2
- `collect_abstracts.py` 실패 → 에러 전파, triage 중단
- JSON 파싱 실패 → 스크립트 버그 보고, 중단
- scoring 중 입력 길이 불일치 → 잘못된 동작, 재실행 필요
- `topic_log.py append` 실패는 **fatal 아님** → 경고만, accepted path는 정상 출력

## Lessons 연결

작업 시작 전 `docs/lessons.md` + `docs/lessons-paper.md` Read.
