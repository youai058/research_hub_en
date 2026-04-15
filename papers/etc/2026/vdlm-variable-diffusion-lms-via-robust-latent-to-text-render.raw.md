---
title: "VDLM: Variable Diffusion LMs via Robust Latent-to-Text Rendering"
authors: ["Shuhui Qu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.15870"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.15870v1"
published: "2026-01-27"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# VDLM: Variable Diffusion LMs via Robust Latent-to-Text Rendering

## Abstract
Autoregressive language models decode left-to-right with irreversible commitments, limiting revision during multi-step reasoning. We propose \textbf{VDLM}, a modular variable diffusion language model that separates semantic planning from text rendering. VDLM applies LLaDA-style masked diffusion over semantic variable embeddings to enable iterative refinement in latent space, then post-trains the planner with trajectory-aware optimization using embedding-space rewards and values, avoiding text decoding inside the RL loop. To convert planned embeddings back to text, we use a \textbf{Vec2Text} renderer and introduce \textbf{embedding perturbations} to robustify decoding under planner noise. Across nine benchmarks spanning general reasoning, math, and code, VDLM is competitive in pre-training and yields substantial post-training improvements on long-form generation tasks, outperforming other baselines. These results highlight the effectiveness of embedding-space post-training and robust latent-to-text rendering for diffusion language modeling.

## Metadata
- venue: arXiv
- year: 2026
- authors: Shuhui Qu
- arxiv_id: 2602.15870
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.15870v1
- published: 2026-01-27
