---
title: "DiffuMamba: High-Throughput Diffusion LMs with Mamba Backbone"
authors: ["Vaibhav Singh", "Oleksiy Ostapenko", "Pierre-André Noël", "Eugene Belilovsky", "Torsten Scholak"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.15927"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.15927v3"
published: "2025-11-19"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# DiffuMamba: High-Throughput Diffusion LMs with Mamba Backbone

## Abstract
Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive (AR) generation, yet their reliance on Transformer backbones limits inference efficiency due to quadratic attention or KV-cache overhead. We introduce DiffuMamba, a masked diffusion language model built on a bidirectional Mamba backbone that combines the diffusion objective with linear-time sequence modeling, and DiffuMamba-H, a hybrid variant with interleaved attention. Across scales up to 1.3B parameters, our models match Transformer-based diffusion in downstream performance while achieving up to 8.2x and 4.3x higher inference throughput, respectively, on long sequences. We further present a systematic analysis of inference efficiency across modern DLM variants combining asymptotic complexity with empirical measurements. Notably, cache-efficient block diffusion with Mamba mixers emerges as the only strategy that scales linearly with sequence length and achieves the strongest performance across all baselines, suggesting a promising direction for future diffusion-based generation systems.

## Metadata
- venue: arXiv
- year: 2025
- authors: Vaibhav Singh, Oleksiy Ostapenko, Pierre-André Noël, Eugene Belilovsky, Torsten Scholak
- arxiv_id: 2511.15927
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.15927v3
- published: 2025-11-19
