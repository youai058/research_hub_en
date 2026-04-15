---
title: "Diffusion Language Model Inference with Monte Carlo Tree Search"
authors: ["Zheng Huang", "Kiran Ramnath", "Yueyan Chen", "Aosong Feng", "Sangmin Woo", "Balasubramaniam Srinivasan", "Zhichao Xu", "Kang Zhou", "Shuai Wang", "Haibo Ding", "Lin Lee Cheong"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.12168"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.12168v2"
published: "2025-12-13"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# Diffusion Language Model Inference with Monte Carlo Tree Search

## Abstract
Diffusion language models (DLMs) have recently emerged as a compelling alternative to autoregressive generation, offering parallel generation and improved global coherence. During inference, DLMs generate text by iteratively denoising masked sequences in parallel; however, determining which positions to unmask and which tokens to commit forms a large combinatorial search problem. Existing inference methods approximate this search using heuristics, which often yield suboptimal decoding paths; other approaches instead rely on additional training to guide token selection. To introduce a principled search mechanism for DLMs inference, we introduce MEDAL, an inference-time scaling framework that integrates Monte Carlo Tree SEarch initialization for Diffusion LAnguage Model inference. We employ Monte Carlo Tree Search at the initialization stage to explore promising unmasking trajectories, providing a robust starting point for subsequent refinement. This design enables efficient inference-time scaling, allowing generation quality to improve as the search budget increases, without additional training. Across multiple benchmarks, MEDAL achieves up to 22.0% improvement over existing inference strategies, establishing a new paradigm for search-based inference in DLMs.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zheng Huang, Kiran Ramnath, Yueyan Chen, Aosong Feng, Sangmin Woo, Balasubramaniam Srinivasan, Zhichao Xu, Kang Zhou, Shuai Wang, Haibo Ding, Lin Lee Cheong
- arxiv_id: 2512.12168
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.12168v2
- published: 2025-12-13
