---
marp: true
theme: default
paginate: true
title: "Simple and Effective Masked Diffusion Language Models"
digest_source: gemini
venue: ICLR
venue_class: whitelist
year: 2025
---

<!--
PLANNING:
  SECTIONS:
    1. Lead (title / authors / venue / links)                              [no image]
    2. TL;DR (anchor)                                                      [no image]
    3. 왜 discrete diffusion이 AR에 뒤쳐져 왔는가 (motivation)                [no image]
    4. 핵심 관찰 — SUBS parameterization이 loss를 mask-only CE로 축약         [Figure 1]
    5. Method (anchor) — Rao-Blackwellized NELBO + 단순화                   [no image]
    6. Method (anchor, 연속) — Algorithm 1 + Semi-AR generation             [no image]
    7. Experiments Setup (baselines table)                                 [no image]
    8. Result (anchor) — Language Modeling PPL (LM1B / OWT / zero-shot)    [no image]
    9. Result (anchor, 연속) — Downstream / Semi-AR / DNA                   [no image]
    10. Result (anchor, 연속) — Ablation 핵심                                [no image]
    11. 노이즈 스케줄이 ELBO에 영향 없다는 것의 의미 (analysis)                [no image]
    12. Critical Reading (anchor)                                          [no image]
    13. Keywords (RAG용)                                                    [no image]
  IMAGE_SOURCES:
    - Figure 1: ./.figure_cache/simple-and-effective-masked-diffusion-language-models__fig1.png
                — MDLM objective가 per-token masked CE의 weighted mixture라는 점을 시각화
                  (Method 진입 맥락 anchor 역할).
-->

<!-- _class: lead -->

# Simple and Effective Masked Diffusion Language Models

**Subham Sekhar Sahoo, Marianne Arriola, Yair Schiff, Aaron Gokaslan, Edgar Marroquin, Justin T. Chiu, Alexander Rush, Volodymyr Kuleshov** — ICLR 2025

[arXiv](https://arxiv.org/abs/2406.07524) · [OpenReview](https://openreview.net/forum?id=mPMDVk3CKj)

---

## TL;DR

> **Simple한 masked discrete diffusion이 "원래 알려진 것보다" 훨씬 잘 동작함을 empirical하게 보여준 논문**. SUBS parameterization + continuous-time Rao-Blackwellized ELBO를 유도하니 loss가 **masked cross-entropy의 weighted mixture** 라는 단순한 형태가 되고, DiT+rotary+BERT tokenizer 같은 engineering recipe를 얹으면 LM1B에서는 AR과 근접(23.00 vs 20.86)한 PPL을 달성함. OWT·DNA에서는 AR과 gap 유지되나 SEDD·D3PM 계열 diffusion baseline은 전부 압도함.

---

## 왜 discrete diffusion이 AR에 뒤쳐져 왔는가

- **Problem**: continuous diffusion이 image에서 강한 반면, discrete(language)에서는 AR 대비 log-likelihood gap이 크다고 보고돼왔음. D3PM·SEDD는 diffusion을 discrete로 옮겼지만 complex objective + 작은 8k vocabulary + suboptimal architecture 때문에 AR에 크게 뒤쳐졌음.
- **기존 approach**:
  - **D3PM**: 일반 transition matrix $Q_t$ 기반 discrete forward process, 복잡한 KL objective.
  - **SEDD**: score entropy loss, 여전히 variance 크고 training 비효율.
  - **DiffusionBert**: BERT 위에 diffusion objective를 얹었으나 PPL 여전히 $\le 63.78$.
- **Limitation**:
  - 복잡한 variational objective → high variance, training efficiency 낮음.
  - zero-shot downstream evaluation 방법이 부재.
  - 공정한 engineering baseline(same architecture·vocab·budget)과의 비교가 없어 "정말 diffusion이 구조적으로 열등한가" 알 수 없었음.

---

## 핵심 관찰 — absorbing state diffusion의 forward marginal이 매우 단순함

- $\pi = m$ (special [MASK] one-hot)로 두면 forward marginal이:

$$q(z_t|x) = \mathrm{Cat}(z_t;\, \alpha_t x + (1-\alpha_t) m)$$

- 즉 시간 $t$에 각 token이 확률 $1-\alpha_t$로 [MASK]가 됨. reverse posterior도 두 case로 clean하게 split:

$$q(z_s|z_t,x) = \begin{cases} \mathrm{Cat}(z_s; z_t) & z_t \neq m \\ \mathrm{Cat}\!\left(z_s;\, \dfrac{(1-\alpha_s)m + (\alpha_s-\alpha_t)x}{1-\alpha_t}\right) & z_t = m \end{cases}$$

- **SUBS parameterization**: $p_\theta$를 위 posterior에 $x_\theta(z_t,t)$ 대입 형태로 define. 두 가지 structural constraint를 강제함:
  - **Zero masking**: $\langle x_\theta(z_t,t), m\rangle = 0$ (mask token logit = $-\infty$)
  - **Carry-over unmasking**: $z_t \neq m$이면 $x_\theta(z_t,t) = z_t$ (출력 그대로 복사)

---

## 핵심 관찰 — Figure 1

![w:650](./.figure_cache/simple-and-effective-masked-diffusion-language-models__fig1.png)

MDLM objective가 per-token masked cross-entropy의 weighted mixture임을 시각화 — Method 진입 맥락 anchor. SEDD·D3PM 계열 대비 단순한 loss 형태로 SOTA PPL을 달성함을 함께 요약.

---

## Method — Rao-Blackwellized ELBO + 단순화

- SUBS 위에서 2단계 Rao-Blackwellization(RB1: $z_t$가 mask인지에 대한 indicator 제거, RB2: KL에서 redundant term 제거)을 적용하면 discrete-time loss가 극적으로 단순해짐:

$$\mathcal{L}_\text{diffusion} = \sum_{i=1}^{T} \mathbb{E}_q\!\left[\frac{\alpha_{t(i)} - \alpha_{s(i)}}{1 - \alpha_{t(i)}} \log\langle x_\theta(z_{t(i)}), x\rangle\right]$$

- $T \to \infty$ continuous-time extension + $\gamma \equiv \log(1-\alpha_t)$ 치환으로 **loss가 $\alpha_t$ functional form에 invariant**함을 증명:

$$\mathcal{L}^{\infty}_\text{NELBO} = \mathbb{E}_q \int_{t=0}^{1} \frac{\alpha'_t}{1-\alpha_t} \sum_\ell \log\langle x^\ell_\theta(z^{1:L}_t,t),\, x^\ell\rangle\, dt$$

- Engineering recipe: DiT + rotary embeddings + `bert-base-uncased` tokenizer + log-linear schedule $\sigma(t) = -\log(1-t)$ + low-discrepancy time sampler.

---

## Method — Algorithm 1 (training) + Semi-AR generation

```
repeat
  x_{1:L} ~ q(x)
  t ~ U[0,1]
  z^ℓ_t ~ Cat(z^ℓ_t; α_t·x^ℓ + (1-α_t)·m)   for all ℓ
  step on ∇_θ (α'_t / (1-α_t)) · Σ_ℓ log ⟨x^ℓ_θ(z^{1:L}_t, t), x^ℓ⟩
until converged
```

- **Semi-autoregressive (SAR)**: 생성된 $\tilde x^{1:L}$ 뒤에 $L'$개 token을 더 만들 때, 앞 $L-L'$개를 prefix로 고정하고 나머지만 diffusion으로 채움. carry-over unmasking 덕분에 prefix는 sampling 중 변경되지 않음 — AR처럼 이어쓰기 가능.

---

## Experiments Setup — 비교 방법론별 조건

| Method | Architecture | Key HP | Training | 비고 |
|---|---|---|---|---|
| **MDLM (Proposed)** | DiT, 12L / 768H / 12-head, rotary, timestep emb 128 | LR=3e-4, batch=512, AdamW, dropout=0.1, warmup 2500, log-linear schedule | Scratch. LM1B 1M/10M steps (33B/327B tokens) · OWT 1M steps (262B) | Proposed |
| **AR (Retrained)** | Same transformer 12L/768H/12-head, no weight tying | LR=3e-4, batch=512, AdamW, dropout=0.1, warmup 2500 | Scratch. LM1B 0.5M/5M steps · OWT 0.5M steps | 재구현, 동일 token 예산 |
| **SEDD (Retrained)** | Same as MDLM | Same as MDLM | Scratch. OWT 1M steps (262B) | 재구현 |
| **MosaicBERT + MDLM-FT** | MosaicBERT 137M, ALiBi | Pretrain LR=5e-4 batch=4096 · FT LR=5e-5 batch=512 | Pretrain C4 70k steps (36B) · FT 5k steps (32M) | Downstream GLUE |
| **Caduceus (DNA)** | Mamba bi-dir, 467K params | LR=1e-3, no timestep emb | HG38 pretrain 10B · FT 50B tokens | 5 seeds |

> AR은 MDLM 대비 step 수가 절반(0.5M vs 1M)이나 동일 token 예산. MDLM은 평균 50% token이 masked이므로 effective gradient signal 양은 다를 수 있음 (Critical Reading 참고).

---

## Result — Language Modeling PPL

**LM1B** (Table 1, 110M params):

| Model | Tokens | PPL ↓ |
|---|---|---|
| Transformer-XL Base (0.46B) | — | 23.5 |
| AR Retrained | 33B | 22.32 |
| AR Retrained | 327B | **20.86** |
| D3PM (absorb) | — | $\le 76.90$ |
| DiffusionBert | — | $\le 63.78$ |
| SEDD | 33B | $\le 32.79$ |
| **MDLM (Ours)** | 33B | $\le 27.04$ |
| **MDLM (Ours)** | 327B | $\le$ **23.00** |

**OWT** (Table 2, 262B tokens): AR† 17.54 · SEDD† $\le 24.10$ · **MDLM $\le 23.21$**.

**Zero-shot on 7 domains** (Table 3, 524B OWT): MDLM이 SEDD 대비 7/7 domain에서 더 낮은 PPL (Lambada 47.52 vs 49.86, ArXiv 37.37 vs 38.48 등).

---

## Result — Downstream / Semi-AR / DNA

**GLUE** (Table 4, BERT+MDLM-FT vs baselines, ↑):

| | MNLI m/mm | QQP | QNLI | SST-2 | CoLA | STS-B | MRPC | RTE | Avg |
|---|---|---|---|---|---|---|---|---|---|
| AR | 80.94/80.78 | 86.98 | 86.16 | 90.14 | 33.43 | 84.32 | 83.88 | 47.29 | 74.88 |
| BERT | 84.43/85.35 | 88.41 | 90.46 | 92.20 | 54.81 | 88.41 | 89.16 | 61.37 | 81.62 |
| **+MDLM-FT** | **84.76**/85.07 | **88.49** | 90.30 | 92.20 | **57.69** | 87.48 | **90.53** | **62.09** | **82.06** |

**Semi-AR gen** (Table 5, seq=2048): MDLM Gen PPL **27.18** (89.3 sec/seq) vs SSD-LM 35.43 (2473.9 sec/seq) — PPL·속도 모두 우세.

**DNA** (Table 6, Caduceus 467K): AR Mamba 3.067 · Plaid $\le 3.240$ · SEDD $\le 3.216$ · **MDLM $\le 3.199$**. diffusion 중 SOTA이나 AR Mamba와 gap 잔존.

---

## Result — Ablation 핵심

**Component ablation** (Table 8, LM1B 33B tokens):

| Variant | PPL ≤ |
|---|---|
| MDLM (full) | 27.04 ± .01 |
| w/o continuous time (T=1000) | 27.19 ± .07 (+0.15) |
| & w/o carry-over | 28.56 ± .15 (+1.52) |
| & w/o zero masking | 28.51 ± .15 (+1.47) |

- **Discrete vs continuous** (Table 11): $T=10$ → 42.18 · $T=1000$ → 23.15 · $T=\infty$ → 23.05.
- **Time conditioning** (Table 12, OWT): w/ 23.21 vs w/o 23.05 — 제거가 오히려 약간 낫거나 동등.
- **Sampling speed** (Table 10, 64 samples, A5000): MDLM+caching 40.1min @ $T=5k$ vs SEDD 85.3min.

---

## 노이즈 스케줄이 ELBO에 영향 없다는 것의 의미

- $\gamma = \log(1-\alpha_t)$ 치환으로 continuous-time NELBO가 schedule functional form에 **invariant**함을 증명(§3.4).
- 실험 확인 (Table 9, OWT BPD): Log Linear / Cosine / Cosine Squared / Linear 모두 mean **3.30** 동일.
- 단 **variance**는 다름: Log Linear 1.81 · Cosine 3.30 · Cosine² 3.30 · Linear 7.57 → 그래서 log-linear 채택.
- 해석: schedule choice는 학습 variance 문제로 환원되고, 이전 continuous diffusion 연구의 schedule tuning 노력이 masked diffusion에서는 gradient noise 최적화로 재해석됨.

---

## Critical Reading

**논문의 부족한 부분**:
- **AR gap 과소표현**: Abstract의 "match or exceed" claim은 LM1B에서 PPL 23.00 vs 20.86으로 근접했을 뿐이고, OWT에서는 23.21 vs 17.54로 약 32% 열등. 제목의 "effective"가 AR 대비 gap 크기를 희석함.
- **Upper bound만 보고**: diffusion PPL이 모두 $\le$ 로만 보고됨. bound tightness에 대한 분석이 없어 true PPL이 얼마나 낮은지 불명 — SEDD와 MDLM의 bound tightness가 같은지조차 검증 안 됨.
- **1.1B 실험 미보고**: 본문 Table은 전부 110M. 1.1B parameter from-scratch 학습을 언급하지만 scaling law·수치가 appendix에도 체계적으로 등장하지 않음.
- **GLUE는 MDLM from-scratch가 아님**: GLUE 개선(82.06 > 81.62)은 pretrained BERT에 MDLM-FT만 얹은 결과. pure MDLM-from-scratch의 downstream 성능은 검증되지 않음.
- **Training compute fairness**: MDLM 1M steps vs AR 0.5M steps (동일 token 예산이지만 MDLM은 평균 50% token이 masked이므로 effective label signal이 상이할 수 있음). "same budget"이 unbiased인지 추가 검증 필요.
- **Generation quality 미평가**: human eval·distinct-n·reference-based metric 없이 PPL만 비교 — 실사용 품질 주장은 indirect.
- **Noise schedule invariance의 한계**: 이론은 continuous-time + infinite sample 가정. finite-step sampling에서 schedule 영향은 Table 10의 wall-clock만 보고, PPL 재생성 차이는 분리되지 않음.

---

## Keywords (RAG용)

`masked diffusion`, `discrete diffusion`, `language model`, `MDLM`, `Rao-Blackwellization`, `ELBO`, `SUBS parameterization`, `absorbing state`, `noise schedule invariance`, `semi-autoregressive`, `perplexity`, `cross-entropy loss`, `continuous-time`, `variational bound`, `DiT`
