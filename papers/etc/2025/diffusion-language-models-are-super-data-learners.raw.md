---
title: "Diffusion Language Models are Super Data Learners"
authors: ["Jinjie Ni", "Qian Liu", "Longxu Dou", "Chao Du", "Zili Wang", "Hang Yan", "Tianyu Pang", "Michael Qizhe Shieh"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.03276"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.03276v1"
published: "2025-11-05"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# Diffusion Language Models are Super Data Learners

## Abstract
Under strictly controlled pre-training settings, we observe a Crossover: when unique data is limited, diffusion language models (DLMs) consistently surpass autoregressive (AR) models by training for more epochs. The crossover shifts later with more or higher-quality data, earlier with larger models, and persists across dense and sparse architectures. We attribute the gains to three compounding factors: (1) any-order modeling, (2) super-dense compute from iterative bidirectional denoising, and (3) built-in Monte Carlo augmentation; input or parameter noise improves AR under data constraint but cannot close the gap. At scale, a 1.7B DLM trained with a ~1.5T-token compute budget on 10B unique Python tokens overtakes an AR coder trained with strictly matched settings. In addition, a 1B-parameter DLM achieves > 56% accuracy on HellaSwag and > 33% on MMLU using only 1B tokens, without any special tricks, just by repeating standard pre-training data. We also show that rising validation cross-entropy does not imply degraded downstream performance in this regime.

## Metadata
- venue: arXiv
- year: 2025
- authors: Jinjie Ni, Qian Liu, Longxu Dou, Chao Du, Zili Wang, Hang Yan, Tianyu Pang, Michael Qizhe Shieh
- arxiv_id: 2511.03276
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.03276v1
- published: 2025-11-05
