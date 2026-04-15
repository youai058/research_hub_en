---
title: "TDGNet: Hallucination Detection in Diffusion Language Models via Temporal Dynamic Graphs"
authors: ["Arshia Hemmat", "Philip Torr", "Yongqiang Chen", "Junchi Yu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.08048"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.08048v1"
published: "2026-02-08"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# TDGNet: Hallucination Detection in Diffusion Language Models via Temporal Dynamic Graphs

## Abstract
Diffusion language models (D-LLMs) offer parallel denoising and bidirectional context, but hallucination detection for D-LLMs remains underexplored. Prior detectors developed for auto-regressive LLMs typically rely on single-pass cues and do not directly transfer to diffusion generation, where factuality evidence is distributed across the denoising trajectory and may appear, drift, or be self-corrected over time. We introduce TDGNet, a temporal dynamic graph framework that formulates hallucination detection as learning over evolving token-level attention graphs. At each denoising step, we sparsify the attention graph and update per-token memories via message passing, then apply temporal attention to aggregate trajectory-wide evidence for final prediction. Experiments on LLaDA-8B and Dream-7B across QA benchmarks show consistent AUROC improvements over output-based, latent-based, and static-graph baselines, with single-pass inference and modest overhead. These results highlight the importance of temporal reasoning on attention graphs for robust hallucination detection in diffusion language models.

## Metadata
- venue: arXiv
- year: 2026
- authors: Arshia Hemmat, Philip Torr, Yongqiang Chen, Junchi Yu
- arxiv_id: 2602.08048
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.08048v1
- published: 2026-02-08
