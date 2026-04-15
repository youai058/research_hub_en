---
title: "Diffusion In Diffusion: Reclaiming Global Coherence in Semi-Autoregressive Diffusion"
authors: ["Linrui Ma", "Yufei Cui", "Kai Han", "Yunhe Wang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.13599"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.13599v2"
published: "2026-01-20"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# Diffusion In Diffusion: Reclaiming Global Coherence in Semi-Autoregressive Diffusion

## Abstract
One of the most compelling features of global discrete diffusion language models is their global bidirectional contextual capability. However, existing block-based diffusion studies tend to introduce autoregressive priors, which, while offering benefits, can cause models to lose this global coherence at the macro level. To regain global contextual understanding while preserving the advantages of the semi-autoregressive paradigm, we propose Diffusion in Diffusion, a 'draft-then-refine' framework designed to overcome the irreversibility and myopia problems inherent in block diffusion models. Our approach first employs block diffusion to generate rapid drafts using small blocks, then refines these drafts through global bidirectional diffusion with a larger bidirectional receptive field. We utilize snapshot confidence remasking to identify the most critical tokens that require modification, and apply mix-scale training to expand the block diffusion model's global capabilities. Empirical results demonstrate that our approach sets a new benchmark for discrete diffusion models on the OpenWebText dataset. Using only 26% of the fine-tuning budget of baseline models, we reduce generative perplexity from 25.7 to 21.9, significantly narrowing the performance gap with autoregressive models.

## Metadata
- venue: arXiv
- year: 2026
- authors: Linrui Ma, Yufei Cui, Kai Han, Yunhe Wang
- arxiv_id: 2601.13599
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.13599v2
- published: 2026-01-20
