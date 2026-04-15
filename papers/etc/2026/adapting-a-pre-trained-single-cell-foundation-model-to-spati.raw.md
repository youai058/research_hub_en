---
title: "Adapting a Pre-trained Single-Cell Foundation Model to Spatial Gene Expression Generation from Histology Images"
authors: ["Donghai Fang", "Yongheng Li", "Zhen Wang", "Yuansong Zeng", "Wenwen Min"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.19766"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.19766v1"
published: "2026-03-20"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:09+09:00"
---

# Adapting a Pre-trained Single-Cell Foundation Model to Spatial Gene Expression Generation from Histology Images

## Abstract
Spatial transcriptomics (ST) enables spot-level in situ expression profiling, but its high cost and limited throughput motivate predicting expression directly from HE-stained histology. Recent advances explore using score- or flow-based generative models to estimate the conditional distribution of gene expression from histology, offering a flexible alternative to deterministic regression approaches. However, most existing generative approaches omit explicit modeling of gene-gene dependencies, undermining biological coherence. Single-cell foundation models (sc-FMs), pre-trained across diverse cell populations, capture these critical gene relationships that histology alone cannot reveal. Yet, applying expression-only sc-FMs to histology-conditioned expression modeling is nontrivial due to the absence of a visual pathway, a mismatch between their pre-training and conditional ST objectives, and the scarcity of mixed-cell ST supervision. To address these challenges, we propose HINGE (HIstology-coNditioned GEneration), which retrofits a pre-trained sc-FM into a conditional expression generator while mostly preserving its learned gene relationships. We achieve this by introducing SoftAdaLN, a lightweight, identity-initialized modulation that injects layer-wise visual context into the backbone, coupled with an expression-space masked diffusion objective and a warm-start curriculum to ensure objective alignment and training stability. Evaluated on three ST datasets, ours outperforms state-of-the-art baselines on mean Pearson correlation and yields more accurate spatial marker expression patterns and higher pairwise co-expression consistency, establishing a practical route to adapt pre-trained sc-FMs for histology-conditioned spatial expression generation.

## Metadata
- venue: arXiv
- year: 2026
- authors: Donghai Fang, Yongheng Li, Zhen Wang, Yuansong Zeng, Wenwen Min
- arxiv_id: 2603.19766
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.19766v1
- published: 2026-03-20
