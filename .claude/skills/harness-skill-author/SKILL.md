---
name: harness-skill-author
description: "절차 번들(.claude/skills/{name}/SKILL.md). YAML 헤더 + progressive disclosure 3단계 + 500줄 상한 + references/ 분리 + scripts/ 번들링. 트리거: '새 skill', 'SKILL.md 작성', 'description 튜닝', '스킬 리팩터'."
---

# Harness Skill Author

스킬은 "어떻게 하는가"를 담는 절차적 지식 번들이다. 품질은 **description 트리거 정확도 + 본문의 Why-first 서술**에서 결정된다.

## 디렉토리 구조

```
.claude/skills/{name}/
├── SKILL.md         (필수: frontmatter + 본문)
├── references/      (선택: 조건부 로드 상세 문서)
├── scripts/         (선택: 반복 작업용 실행 코드)
└── assets/          (선택: 템플릿·이미지)
```

## Frontmatter 규칙

```yaml
---
name: skill-name
description: "구체적 동작 + 트리거 상황 + 경계 조건. pushy 하게."
---
```

- `name`: 디렉토리명과 일치. kebab-case.
- `description`: **유일한 트리거 메커니즘**. metadata 로드 시 Claude가 이것만 보고 트리거 여부를 판단한다.

### Description 작성 — 적극적으로

Claude는 트리거를 보수적으로 판단한다. 이를 보상하려면:
1. 스킬이 하는 일을 **구체적으로 나열** (동사 + 명사)
2. **트리거 상황**을 명시 ("X를 요청하면 반드시 이 스킬을 사용할 것")
3. near-miss 구분 — "단, Y 요청은 다른 스킬 Z가 담당한다"

**나쁜 예:** `"PDF 처리 스킬"`
**좋은 예:** `"PDF 읽기, 텍스트/테이블 추출, 병합, 분할, 회전, 워터마크, OCR 등 모든 PDF 작업 수행. .pdf 파일 언급 또는 PDF 산출물 요청 시 반드시 이 스킬을 사용할 것. 단, 이미지 변환만 필요하면 imaging 스킬이 담당."`

## 본문 작성 원칙

| 원칙 | 규칙 |
|---|---|
| **Why-first** | "ALWAYS/NEVER" 대신 이유 설명. LLM은 이유를 이해하면 엣지 케이스에서도 올바르게 판단한다. |
| **Lean** | 본문 ≤500줄 목표. 매 문장이 토큰 비용을 정당화하는지 자문. |
| **일반화** | 특정 예시가 아닌 원리를 서술. 오버피팅 금지. |
| **명령형** | "~한다", "~하라" 어조. |
| **반복 코드는 번들링** | 3회 이상 반복되는 헬퍼는 `scripts/`에 수록. |

## Progressive Disclosure

스킬은 3단계 로딩으로 컨텍스트를 관리한다:

| 단계 | 시점 | 크기 |
|---|---|---|
| metadata (name+description) | 항상 | ~100단어 |
| SKILL.md 본문 | 트리거 시 | <500줄 |
| references/ | 필요할 때만 | 무제한 |

**크기 관리:**
- 본문이 500줄에 근접하면 상세를 `references/`로 분리하고 본문에 포인터 남김
- 300줄 이상 reference 파일은 상단에 ToC 포함
- 도메인별 변형이 있으면 `references/{domain}.md`로 분리 (해당 도메인 작업 시만 로드)

## 편집 절차

1. **기존 스킬 스캔**: `.claude/skills/*/SKILL.md`의 frontmatter를 모두 읽어 name·description 중복/충돌 확인
2. 디렉토리 생성: `.claude/skills/{name}/`
3. SKILL.md 작성 (frontmatter + 본문)
4. 필요 시 `references/`, `scripts/` 생성
5. 줄 수 확인: 500줄 초과 시 분리
6. harness-validate 스킬로 구조 검증

## 트리거 충돌 검사

새 스킬 description이 기존 스킬 description과 의미적으로 겹치면 Claude가 잘못 라우팅한다. 생성 전에:

1. 모든 기존 description을 나열
2. 새 스킬의 트리거 키워드가 겹치는지 확인
3. 겹치면 description에 **"단, X는 Y 스킬이 담당"** 경계 문구를 추가하거나 스킬을 병합

## 스킬에 넣지 말 것

- README.md, CHANGELOG.md 등 부가 문서
- 생성 과정의 메타 정보(테스트 이력)
- 사용자 대상 설명서 (스킬은 AI 에이전트용)
- Claude가 이미 아는 일반 지식

## 체크리스트

- [ ] `{name}/` 디렉토리 생성, kebab-case
- [ ] frontmatter에 name + description
- [ ] description이 구체적·pushy·경계조건 포함
- [ ] 본문 ≤500줄, 명령형 어조, Why-first
- [ ] 기존 스킬과 트리거 충돌 없음
- [ ] 필요 시 `references/`로 분리
- [ ] harness-validate 통과
