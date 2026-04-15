---
title: "Planned Diffusion"
authors: ["Daniel Israel", "Tian Jin", "Ellie Cheng", "Guy Van den Broeck", "Aditya Grover", "Suvinay Subramanian", "Michael Carbin"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.18087"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.18087v2"
published: "2025-10-20"
categories: ["cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# Planned Diffusion

## Abstract
Most large language models are autoregressive: they generate tokens one at a time. Discrete diffusion language models can generate multiple tokens in parallel, but sampling from them requires a denoising order: a strategy for deciding which tokens to decode at each step. Determining a good denoising order is difficult, and existing approaches use heuristics that create a steep trade-off between quality and latency. We propose planned diffusion, a system that trains the model to determine its own denoising order. Planned diffusion uses a single model that transitions between autoregressive and diffusion-based generation: first, the model autoregressively generates a plan that partitions the response into semantically independent chunks; second, the model denoises all chunks in parallel. The autoregressive plan enables the model to define the denoising order itself. On AlpacaEval, planned diffusion achieves 1.27x to 1.81x speedup over autoregressive generation with only 0.87% to 5.4% drop in win rate, establishing a new Pareto frontier for parallel generation with discrete diffusion. Additionally, planned diffusion's instruction following quality continues to improve with more finetuning compute, while the autoregressive baseline plateaus. Our implementation provides simple runtime knobs that offer tunable control over the quality-latency trade-off.

## Metadata
- venue: arXiv
- year: 2025
- authors: Daniel Israel, Tian Jin, Ellie Cheng, Guy Van den Broeck, Aditya Grover, Suvinay Subramanian, Michael Carbin
- arxiv_id: 2510.18087
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.18087v2
- published: 2025-10-20
