---
title: "Stratified Hazard Sampling: Minimal-Variance Event Scheduling for CTMC/DTMC Discrete Diffusion and Flow Models"
authors: ["Seunghwan Jang", "SooJean Han"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.02799"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.02799v2"
published: "2026-01-06"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# Stratified Hazard Sampling: Minimal-Variance Event Scheduling for CTMC/DTMC Discrete Diffusion and Flow Models

## Abstract
Uniform-noise discrete diffusion and flow models (e.g., D3PM, SEDD, UDLM, DFM) generate sequences non-autoregressively by iteratively refining randomly initialized vocabulary tokens through multiple context-dependent replacements. These models are typically formulated as time-inhomogeneous CTMC/DTMC processes and sampled using independent Bernoulli change decisions at each discretization step. This induces Poisson-binomial variance in per-position jump counts that grows with the number of required edits, leading to the characteristic under-editing (residual noise) and over-editing (cascading substitutions) failure modes that degrade sample quality, especially under tight discretization budgets. In contrast, absorbing-state (mask-start) models avoid this instability by allowing each position to jump at most once. We propose Stratified Hazard Sampling (SHS), a training-free, drop-in, and hyperparameter-free inference principle for any sampler that admits a stay-vs.-replace decomposition. SHS models per-token edits as events driven by cumulative hazard (CTMC) or cumulative jump mass (DTMC) and places events by stratifying this cumulative quantity: with a single random phase per position, a token is updated whenever its accumulated hazard crosses unit-spaced thresholds. This preserves the expected number of jumps while achieving the minimum possible conditional variance among unbiased integer estimators (bounded by 1/4 for any fixed cumulative mass), without altering per-jump destination sampling and thus retaining multimodality. Experiments on uniform-noise discrete diffusion language models show that SHS consistently improves sample quality. We further show that SHS improves robustness under token-level blacklist filtering, with benefits increasing as lexical constraints grow more severe.

## Metadata
- venue: arXiv
- year: 2026
- authors: Seunghwan Jang, SooJean Han
- arxiv_id: 2601.02799
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.02799v2
- published: 2026-01-06
