---
name: paper-kg
description: "SQLite 지식 그래프. .kg.json 부산물 증분 ingest → papers/kg/kg.sqlite triplestore, Pydantic 검증 + 2-pass upsert (LLM 호출 없음), 쿼리 node/neighbors/lookup/sql + hybrid_query(RAG+KG). kg-curator + 모든 생성 에이전트. 트리거: 'KG 인덱싱', '지식 그래프 쿼리', '트리플 upsert', '하이브리드 쿼리'."
---

# Paper KG Skill

SQLite triplestore 기반 knowledge graph. 에이전트는 프로즈 파일 옆에 `.kg.json` 부산물을 쓰고, `kg-curator`가 이 파일을 LLM 없이 검증·ingest한다.

## 핵심 원칙

1. **추출은 부산물**: 별도 LLM 추출 패스 없음. `.kg.json`은 생성 에이전트(paper-summarizer 등)가 프로즈와 동시에 쓴다.
2. **1:1 sibling 규칙**: `<source>.md` ↔ `<source>.kg.json` 같은 디렉토리. 스크립트 emission(lesson.py, loop_state.py)은 per-entry append.
3. **Alias는 에이전트 판단**: 신규 canonical 노드(Method/Dataset/Model/Metric) 생성 전 `lookup --name-fuzzy`를 호출하고 결과를 `alias_check`에 기록.
4. **Curator는 LLM 없음**: Pydantic 검증, ID regex, 타입-prefix 일치, FK 존재성, alias_check 필수 여부만 체크.

## 스택

- **Store**: `sqlite3` — `papers/kg/kg.sqlite` (PRAGMA foreign_keys=ON, WAL mode)
- **Schema**: 3 tables — `nodes` (PK id) / `edges` (FK src·dst ON DELETE RESTRICT) / `aliases` (FK canonical_id)
- **Validation**: `pydantic>=2` via `scripts/schema.py`
- **Fuzzy lookup**: `rapidfuzz.fuzz.WRatio` ≥ 85 (결정론적)
- **Hybrid query**: `paper-rag/scripts/query.py`를 module import (subprocess 금지)

## 파일 구조

```
papers/kg/
├── kg.sqlite              SQLite triplestore
├── manifest.json          {file → sha256, last_upsert_at, counts}
├── extraction_log.jsonl   append-only audit
├── rejected.jsonl         validation fail 로그 (orchestrator가 소비)
└── schema.version         "1"

.claude/skills/paper-kg/
├── SKILL.md               (this file)
└── scripts/
    ├── schema.py          Pydantic models, ID regex, ALIAS_BOOTSTRAP_THRESHOLD
    ├── db.py              SQLite open/migrate helpers
    ├── index.py           incremental 2-pass upsert
    ├── query.py           node / neighbors / lookup / sql
    ├── hybrid_query.py    RAG + KG joint retrieval
    └── status.py          counts + by_type + manifest + rejected
```

## Sibling placement

| Source file | Sibling `.kg.json` | Author |
|---|---|---|
| `papers/<Venue>/<Year>/<slug>.md` | `papers/<Venue>/<Year>/<slug>.kg.json` | paper-summarizer |
| `research/answers/<date>_<slug>.md` | `research/answers/<date>_<slug>.kg.json` | answer-formulator |
| `research/critiques/<slug>.md` | `research/critiques/<slug>.kg.json` | critic |
| `research/plans/<slug>/PLAN.md` | `research/plans/<slug>/PLAN.kg.json` | experiment-planner |
| `experiments/<slug>/IMPL_MAP.md` | `experiments/<slug>/IMPL_MAP.kg.json` | code-implementer |
| `research/diagnoses/<slug>.md` | `research/diagnoses/<slug>.kg.json` | results-analyst |
| `docs/lessons-<domain>.md` | `docs/lessons-<domain>.kg.json` (append-only per entry) | `lesson.py` |
| `research/loop_state.json` | `research/loop_state.kg.json` (append-only per iteration) | `loop_state.py` |

## `.kg.json` envelope

```json
{
  "version": 1,
  "source_file": "papers/ICLR/2026/attack-lldm.md",
  "source_sha": "abc123...",
  "author_agent": "paper-summarizer",
  "extracted_at": "2026-04-14T17:30:00+09:00",
  "nodes": [...],
  "edges": [...]
}
```

**필수 필드**: `version`, `source_file`, `source_sha`, `author_agent`, `extracted_at`, `nodes`, `edges`.

## 증분 ingest 알고리즘

```
1. .kg.json 파일 모두 수집 (papers/, research/, experiments/, docs/)
2. 각 파일 SHA256 계산
3. manifest.json 과 비교
   - new/changed: Pydantic 검증 → 통과 시 upsert pipeline, 실패 시 rejected.jsonl append
   - removed: 이전 (source_file) 모든 nodes/edges DELETE
4. Upsert pipeline (트랜잭션):
   a. 기존 (source_file, source_sha') 노드/엣지 DELETE (source_sha 변경 시만)
   b. Pass 1: 모든 노드 INSERT (id 충돌 시 updated_at만 갱신)
   c. Pass 2: 모든 엣지 INSERT (src/dst 존재 확인 → dangling 시 rollback + reject)
   d. alias_merge 특수 엣지는 aliases 테이블로 라우팅
5. manifest.json 갱신 + extraction_log.jsonl append
```

## 쿼리 인터페이스

```bash
# 노드 조회 (quote 주의: # 포함 id는 반드시 quote)
python3 .claude/skills/paper-kg/scripts/query.py node "paper:iclr/2026/attack-lldm"

# 이웃 탐색
python3 .claude/skills/paper-kg/scripts/query.py neighbors "method:gcg" --hops 2 --edge-type PROPOSES

# fuzzy 검색 (alias check용)
python3 .claude/skills/paper-kg/scripts/query.py lookup --type Method --name-fuzzy "Greedy Coord" --k 5

# exact name 검색
python3 .claude/skills/paper-kg/scripts/query.py lookup --type Method --exact-name "GCG"

# raw SQL (디버깅 전용)
python3 .claude/skills/paper-kg/scripts/query.py sql "SELECT type, COUNT(*) FROM nodes GROUP BY type"
```

## Hybrid query 프로토콜 (answer-formulator·critic·planner)

```bash
python3 .claude/skills/paper-kg/scripts/hybrid_query.py "question" --k 5
```

출력 JSON 최상위 키: `query`, `rag`, `kg`, `hybrid`.
내부 구현은 `paper-rag.query` module import로 subprocess 없이 호출.

## Alias Check Protocol (에이전트 지침)

신규 `Method|Dataset|Model|Metric` 노드 생성 전:

1. `lookup --type <T> --name-fuzzy "<candidate>" --k 5` 호출
2. 결과를 보고 판단:
   - **재사용**: 매칭된 기존 id를 `edges[].dst`로 사용 (새 노드 생성 X)
   - **신규**: 새 id + `alias_check: {queried_existing: true, matched: null, rationale: "..."}` 기록
   - **alias 추가**: `type: "alias_merge"` 특수 엣지로 기존 노드에 alias 추가
3. Jaro-Winkler / WRatio 0.85+ AND 같은 도메인이면 재사용 권장
4. 약자 vs 풀네임 매치 → 재사용, 풀네임을 aliases에 append
5. 버전 차이(v1 vs v2) → 신규 + `DERIVED_FROM` 엣지

**Bootstrap softening**: KG nodes < 50인 상태에서는 `alias_check.queried_existing: false`도 허용. schema.py의 `ALIAS_BOOTSTRAP_THRESHOLD` 상수가 이 경계를 고정한다.

## Schema Enforcement (curator 체크리스트)

1. Pydantic validation (`KGFile`) 통과
2. ID regex 매치 (§schema.py ID_REGEX)
3. `nodes[].type` ↔ id prefix 일치
4. `Method|Dataset|Model|Metric` 신규 노드는 `alias_check` 필수 (bootstrap 조건부)
5. `EVIDENCED_BY` 엣지는 `meta.polarity ∈ {support, contradict, mixed}` 강제
6. edges[].src/dst 가 같은 파일 nodes[] 또는 DB의 기존 id에 존재
7. Provenance (source_file, source_sha, extracted_at) 필수
8. Post-ingest exact-name collision 감지 → `rejected.jsonl`에 수동 검토 플래그

Reject된 파일은 `papers/kg/rejected.jsonl`에 이유와 함께 append. orchestrator가 이걸 읽어 원작 에이전트에 재dispatch.

## 환경 준비

```bash
conda activate LLDM
pip install pydantic rapidfuzz
```

sqlite3는 Python stdlib이라 추가 설치 불필요.

## 실패 모드

- Pydantic 검증 실패: 해당 `.kg.json` 하나만 reject, 나머지는 정상 ingest
- Dangling edge (src/dst 부재): 파일 전체 reject (트랜잭션 롤백)
- `kg.sqlite` 손상: `extraction_log.jsonl` replay 또는 `index.py --rebuild`
- manifest 손상: `index.py --rebuild-manifest` 로 해시 재계산
- Post-ingest name collision: silent merge 금지, `rejected.jsonl` 수동 플래그

## 체크리스트

- [ ] `pydantic`, `rapidfuzz` 설치 확인
- [ ] `papers/kg/kg.sqlite` 존재 (없으면 `db.open_and_migrate`로 생성)
- [ ] `manifest.json` 초기화 또는 로드
- [ ] `.kg.json` 증분 수집
- [ ] 2-pass upsert (nodes → edges)
- [ ] 쿼리 스모크 테스트 (`query.py node <id>` 1건 이상)
