---
title: "Dependency-Guided Parallel Decoding in Discrete Diffusion Language Models"
authors: ["Liran Ringel", "Ameen Ali", "Yaniv Romano"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.02560"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.02560v1"
published: "2026-04-02"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# Dependency-Guided Parallel Decoding in Discrete Diffusion Language Models

## Abstract
Discrete diffusion language models (dLLMs) accelerate text generation by unmasking multiple tokens in parallel. However, parallel decoding introduces a distributional mismatch: it approximates the joint conditional using a fully factorized product of per-token marginals, which degrades output quality when selected tokens are strongly dependent.
  We propose DEMASK (DEpendency-guided unMASKing), a lightweight dependency predictor that attaches to the final hidden states of a dLLM. In a single forward pass, it estimates pairwise conditional influences between masked positions. Using these predictions, a greedy selection algorithm identifies positions with bounded cumulative dependency for simultaneous unmasking. Under a sub-additivity assumption, we prove this bounds the total variation distance between our parallel sampling and the model's joint. Empirically, DEMASK achieves 1.7-2.2$\times$ speedup on Dream-7B while matching or improving accuracy compared to confidence-based and KL-based baselines.

## Metadata
- venue: arXiv
- year: 2026
- authors: Liran Ringel, Ameen Ali, Yaniv Romano
- arxiv_id: 2604.02560
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.02560v1
- published: 2026-04-02
