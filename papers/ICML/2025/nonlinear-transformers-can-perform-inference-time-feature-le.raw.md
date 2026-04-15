---
title: "Nonlinear transformers can perform inference-time feature learning"
authors: ["Naoki Nishikawa", "Yujin Song", "Kazusato Oko", "Denny Wu", "Taiji Suzuki"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xQTSvP57C3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9e556ce75b5ed115579a27d1c9d09074582d393a.pdf"
published: "2025"
categories: []
keywords: ["transformers", "in-context learning", "feature learning", "single-index models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:17+09:00"
---

# Nonlinear transformers can perform inference-time feature learning

## Abstract
Pretrained transformers have demonstrated the ability to implement various algorithms at inference time without parameter updates. While theoretical works have established this capability through constructions and approximation guarantees, the optimization and statistical efficiency aspects remain understudied. In this work, we investigate how transformers learn features in-context -- a key mechanism underlying their inference-time adaptivity. We focus on the in-context learning of single-index models $y=\sigma_*(\langle \\boldsymbol{x},\\boldsymbol{\beta}\rangle)$, which are low-dimensional nonlinear functions parameterized by feature vector $\\boldsymbol\beta$. We prove that transformers pretrained by gradient-based optimization can perform *inference-time feature learning*, i.e., extract information of the target features $\\boldsymbol{\beta}$ solely from test prompts (despite $\\boldsymbol
{\beta}$ varying across different prompts), hence achieving an in-context statistical efficiency that surpasses any non-adaptive (fixed-basis) algorithms such as kernel methods. Moreover, we show that the inference-time sample complexity surpasses the Correlational Statistical Query (CSQ) lower bound, owing to nonlinear label transformations naturally induced by the Softmax self-attention mechanism.

## Metadata
- venue: ICML
- year: 2025
- authors: Naoki Nishikawa, Yujin Song, Kazusato Oko, Denny Wu, Taiji Suzuki
- arxiv_id: 
- openreview_id: xQTSvP57C3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9e556ce75b5ed115579a27d1c9d09074582d393a.pdf
- published: 2025
- keywords: transformers, in-context learning, feature learning, single-index models
