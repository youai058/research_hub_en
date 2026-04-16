---
name: paper-rag
description: "논문 RAG (ChromaDB + bge-m3). 섹션 단위 chunking + 수식/표 보존, SHA256 증분 upsert, query.py, manifest. rag-curator·answer-formulator·planner 사용. 트리거: 'RAG 인덱싱', '벡터 쿼리', '논문 검색', 'chroma 업데이트'."
---

# Paper RAG Skill

ChromaDB + bge-m3 벡터 RAG 파이프라인. 스크립트는 `scripts/`에 번들링되어 있고, rag-curator가 호출한다.

## 스택

- **Embedding**: `BAAI/bge-m3` via `sentence-transformers`
- **Store**: `chromadb.PersistentClient(path="papers/vector_db/chroma")`, collection=`"papers"`
- **Chunker**: 섹션 단위(`##` 헤딩), 수식 블록(`$$...$$`)과 테이블 보존, chunk_size ≤1200 tokens
- **해시**: `hashlib.sha256(file_bytes)` → manifest에 저장

## 파일 구조

```
.claude/skills/paper-rag/
├── SKILL.md
└── scripts/
    ├── index.py    전체/증분 인덱싱
    ├── query.py    top-k 쿼리 CLI
    └── status.py   manifest·collection 상태 보고
```

## 증분 인덱싱 알고리즘

```
1. papers/marp-summary/**/*.md 리스트 수집
2. 각 파일의 SHA256 계산
3. manifest.json의 기존 해시와 비교
   - new 파일: chunk + embed + upsert (ID: slug_section_chunk)
   - changed: 기존 chunk ID들을 delete → 새로 embed + upsert
   - removed: collection에서 delete
4. manifest.json 갱신
5. chunks.jsonl에 로그 추가 (append-only)
```

## 쿼리 인터페이스

CLI:
```bash
python3 .claude/skills/paper-rag/scripts/query.py "your question" --k 5 --filter venue=ICLR
```

출력 (stdout JSON):
```json
[
  {
    "id": "attack-lldm_3_1",
    "score": 0.87,
    "source": "papers/marp-summary/ICLR/2026/attack-lldm.md",
    "section": "Methodology",
    "text": "...chunk text preview..."
  }
]
```

프로그램 호출 (Python):
```python
import subprocess, json
r = subprocess.run(
    ["python3", ".claude/skills/paper-rag/scripts/query.py", q, "--k", "5"],
    capture_output=True, text=True, check=True,
)
results = json.loads(r.stdout)
```

## 환경 준비

```bash
conda activate LLDM
pip install chromadb sentence-transformers
# bge-m3는 첫 실행 시 HuggingFace에서 자동 다운로드 (~2.3GB)
```

## Chunking 규칙

1. `##` 헤딩으로 섹션 분리
2. 섹션 텍스트가 1200 tokens 초과 시 문단 단위로 재분할
3. `$$...$$` 수식 블록은 **자르지 않음**
4. `|...|` 테이블 블록도 **자르지 않음**
5. chunk metadata: `{slug, section_title, section_idx, chunk_idx, venue, year, authors}`

Token 근사: `len(text.split()) * 1.3` (영어 기준). 한국어/수식이 섞이면 `tiktoken`로 정확히.

## manifest.json 구조

```json
{
  "version": 1,
  "embed_model": "BAAI/bge-m3",
  "last_update": "2026-04-14T15:00:00+09:00",
  "files": {
    "papers/marp-summary/ICLR/2026/attack-lldm.md": {
      "sha256": "abc123...",
      "mtime": 1234567890,
      "chunks": 12,
      "chunk_ids": ["attack-lldm_0_0", "attack-lldm_1_0", ...]
    }
  },
  "cursors": {"arxiv:cs.CL:...": {...}}
}
```

## 실패 모드

- bge-m3 다운로드 실패: HuggingFace mirror 대체 또는 오프라인 캐시 사용
- OOM during embedding: batch_size를 32→8로 줄임
- ChromaDB 손상: `papers/vector_db/chroma/` 백업 후 전체 reindex (`index.py --rebuild`)
- manifest 손상: `index.py --rebuild-manifest`로 해시 재계산

## 쿼리 품질 팁

- `--filter venue=ICLR year=2025` 로 좁히면 품질 향상
- 추상적 질문(예: "diffusion과 jailbreak 관계")은 키워드 여러 개로 분해 후 각각 쿼리
- top-k 5~10 권장. 너무 많으면 노이즈.

## 체크리스트

- [ ] `chromadb`, `sentence-transformers`, `pymupdf` 설치 확인
- [ ] `papers/vector_db/chroma/` 디렉토리 존재
- [ ] `manifest.json` 초기화 또는 로드
- [ ] 증분 인덱싱 수행
- [ ] 쿼리 스모크 테스트 (임의 쿼리로 1개 이상 결과 확인)
