---
name: abstract-index
description: "raw.md abstract indexer for paper-triage dense-retrieval pre-filter. Incremental bge-m3 upsert into ChromaDB collection 'abstracts'. Trigger: 'abstract 인덱싱', 'triage 전 사전 인덱스', 'abstracts collection 갱신'."
---

# Abstract Index Skill

paper-triage가 쓰는 `abstracts` ChromaDB 컬렉션을 증분 갱신하는 전용 스킬. `papers/marp-summary/**/*.md`를 다루는 `paper-rag`와 독립이고, 입력은 `papers/metadata/**/*.raw.md`의 abstract 본문이다.

## 철학
- **증분 전용**: SHA256 기반으로 변경된 raw.md만 re-embed.
- **Non-destructive**: raw.md 미터치.
- **Single document per paper**: abstract는 chunking하지 않고 `title + "\n\n" + abstract` 한 문서로 upsert.
- **Separate collection**: `papers` 컬렉션과 분리. 혼합 쿼리 의미 훼손 방지.

## 스택
- Embedding: `BAAI/bge-m3` via `sentence-transformers`
- Store: `chromadb.PersistentClient(path="papers/vector_db/chroma")`, collection=`"abstracts"`
- 해시: `hashlib.sha256(file_bytes)`
- Manifest: `papers/vector_db/abstracts_manifest.json`

## 파일 구조

```
.claude/skills/abstract-index/
├── SKILL.md
└── scripts/
    └── index.py    증분/전체 인덱싱 (CLI)
```

## 알고리즘

```
1. papers/metadata/**/*.raw.md 전량 glob
2. 각 파일 SHA256 계산
3. abstracts_manifest.json의 기존 해시와 비교:
   - new: collect_abstracts.extract() → title+abstract → embed → upsert
   - changed: 기존 id를 delete → 새로 embed+upsert
   - removed (manifest에 있는데 파일 없음): id를 delete
4. manifest.json 저장 (last_update KST)
```

## 호출 예시

```bash
# 기본 실행 — 증분
python3 .claude/skills/abstract-index/scripts/index.py

# 매니페스트만 재계산 (Chroma upsert 안 함)
python3 .claude/skills/abstract-index/scripts/index.py --rebuild-manifest

# Chroma + manifest 전체 재구축
python3 .claude/skills/abstract-index/scripts/index.py --rebuild
```

## 에러 처리
- `sentence-transformers` / `chromadb` 미설치 → exit 3, `conda env LLDM` 활성화 요청
- manifest 손상 (JSON parse 실패) → warning 후 빈 manifest로 진행 (사실상 full rebuild)
- `## Abstract` 블록 없는 raw.md → `[warn]` 표시 후 skip (collection에 넣지 않음)

## 체크리스트
- [ ] conda env LLDM 활성 (`chromadb`, `sentence-transformers` import 가능)
- [ ] `papers/vector_db/chroma/` 쓰기 가능
- [ ] manifest init or load 성공
- [ ] 증분 인덱싱 완료
- [ ] (최초 실행 시) abstracts 컬렉션 count > 0

## Lessons 연결
작업 시작 전 `docs/lessons.md` + `docs/lessons-paper.md` Read.
