---
title: "Generalized Discrete Diffusion with Self-Correction"
authors: ["Linxuan Wang", "Ziyi Wang", "Yikun Bai", "Wei Deng", "Guang Lin", "Qifan Song"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.02230"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.02230v1"
published: "2026-02-13"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:32+09:00"
---

# Generalized Discrete Diffusion with Self-Correction

## Abstract
Self-correction is an effective technique for maintaining parallel sampling in discrete diffusion models with minimal performance degradation. Prior work has explored self-correction at inference time or during post-training; however, such approaches often suffer from limited generalization and may impair reasoning performance. GIDD pioneers pretraining-based self-correction via a multi-step BERT-style uniform-absorbing objective. However, GIDD relies on a continuous interpolation-based pipeline with opaque interactions between uniform transitions and absorbing masks, which complicates hyperparameter tuning and hinders practical performance. In this work, we propose a Self-Correcting Discrete Diffusion (SCDD) model to reformulate pretrained self-correction with explicit state transitions and learn directly in discrete time. Our framework also simplifies the training noise schedule, eliminates a redundant remasking step, and relies exclusively on uniform transitions to learn self-correction. Experiments at the GPT-2 scale demonstrate that our method enables more efficient parallel decoding while preserving generation quality.

## Metadata
- venue: arXiv
- year: 2026
- authors: Linxuan Wang, Ziyi Wang, Yikun Bai, Wei Deng, Guang Lin, Qifan Song
- arxiv_id: 2603.02230
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.02230v1
- published: 2026-02-13
