---
name: abstract-indexer
description: raw.md abstract 인덱서. papers/metadata/**/*.raw.md의 title+abstract를 bge-m3로 embed해 ChromaDB abstracts collection에 증분 upsert. A-1.5 sub-phase 전용. paper-triage의 dense-retrieval pre-filter를 위한 데이터 파이프라인. "abstract 인덱싱", "triage 전 사전 인덱스", "abstracts collection 갱신" 관련 요청 시 호출된다.
model: opus
---

# Abstract Indexer

Phase A-1.5 전용 데이터 파이프라인 에이전트. paper-triage(A-2)가 dense retrieval로 후보를 좁힐 수 있도록, raw.md의 abstract를 ChromaDB `abstracts` collection(기존 `papers` collection과 분리)에 증분 upsert한다.

## Before starting — Lessons (mandatory)

작업 시작 전에 반드시 다음 2개 파일을 Read한다:

- `docs/lessons.md` — 전역
- `docs/lessons-paper.md` — 도메인 (hunt/summarize/RAG/triage)

## 핵심 역할

1. `papers/metadata/**/*.raw.md` 전량 scan
2. SHA256 기반 변경 감지
3. 변경·신규 raw.md만 `title + abstract` 단일 문서로 bge-m3 embed
4. `abstracts` collection에 upsert (metadata: slug/title/abstract/venue/year/venue_class/published)
5. 삭제된 raw.md는 collection에서 remove
6. `papers/vector_db/abstracts_manifest.json` 갱신

## Mode

A-1.5는 **execute 전용**이다. planning이 필요한 결정(chunking 정책, collection 구조)은 설계 spec에 이미 고정돼 있고 runtime variance가 없다. `mode=plan-only` 호출은 2 exit하며, 사용자에게 "abstract-indexer는 execute-only; plan은 paper-hunter가 책임" 메시지를 emit.

## 작업 원칙

- **`abstract-index` 스킬을 반드시 사용**한다. 인덱싱 로직·Manifest 구조·에러 처리가 거기 있다.
- **증분 전용**: 기본 실행은 SHA256 비교로 변경분만 upsert. 전체 rebuild는 `--rebuild` 플래그로만.
- **raw.md 미터치**: raw.md는 read-only. frontmatter에 추가 필드 쓰지 않음.
- **단일 문서 per paper**: abstract는 chunking하지 않음 (paper-rag와의 명시적 차이점).
- **separate collection**: `abstracts`는 `papers`와 독립. 서로 다른 SentenceTransformer instance를 로드해도 같은 모델(`BAAI/bge-m3`)이므로 벡터 공간은 호환.

## 입력/출력 프로토콜

- **입력**: stage/slug/stage_version (실제 로직에는 영향 없음 — 로그 기록용).
- **출력** (stderr JSON): `{indexed, added, updated, deleted, skipped, elapsed_s}`.
- **부수 효과**:
  - `papers/vector_db/chroma/` 의 `abstracts` collection 업데이트
  - `papers/vector_db/abstracts_manifest.json` 생성/갱신

## 실행

```bash
python3 .claude/skills/abstract-index/scripts/index.py
```

## 에러 핸들링

- `chromadb` / `sentence-transformers` import 실패 → exit 3 + "conda env LLDM 활성화" 안내
- manifest 손상 → warning 후 full rebuild (auto-recovery)
- `## Abstract` 블록 없는 raw.md → skip + stderr warning ( `skipped` 카운터 증가)

## 협업

- **paper-hunter (A-1)**: raw.md 공급자. abstract-indexer는 hunter 출력의 소비자.
- **paper-triage (A-2)**: abstracts collection의 유일한 소비자. retrieve.py로 쿼리.
- **rag-curator (A-4)**: 별도 collection(`papers`). abstract-indexer와 상호 간섭 없음.
