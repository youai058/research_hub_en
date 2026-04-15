---
title: "$S^3$: Stratified Scaling Search for Test-Time in Diffusion Language Models"
authors: ["Ahsan Bilal", "Muhammad Ahmed Mohsin", "Muhammad Umer", "Asad Aali", "Muhammad Usman Khanzada", "Muhammad Usman Rafique", "Zihao He", "Emily Fox", "Dean F. Hougen"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.06260"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.06260v1"
published: "2026-04-07"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# $S^3$: Stratified Scaling Search for Test-Time in Diffusion Language Models

## Abstract
Test-time scaling investigates whether a fixed diffusion language model (DLM) can generate better outputs when given more inference compute, without additional training. However, naive best-of-$K$ sampling is fundamentally limited because it repeatedly draws from the same base diffusion distribution, whose high-probability regions are often misaligned with high-quality outputs. We propose $S^3$ (Stratified Scaling Search), a classical verifier-guided search method that improves generation by reallocating compute during the denoising process rather than only at the final output stage. At each denoising step, $S^3$ expands multiple candidate trajectories, evaluates them with a lightweight reference-free verifier, and selectively resamples promising candidates while preserving diversity within the search frontier. This procedure effectively approximates a reward-tilted sampling distribution that favors higher-quality outputs while remaining anchored to the model prior. Experiments with LLaDA-8B-Instruct on MATH-500, GSM8K, ARC-Challenge, and TruthfulQA demonstrate that $S^3$ consistently improves performance across benchmarks, achieving the largest gains on mathematical reasoning tasks while leaving the underlying model and decoding schedule unchanged. These results show that classical search over denoising trajectories provides a practical mechanism for test-time scaling in DLMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Ahsan Bilal, Muhammad Ahmed Mohsin, Muhammad Umer, Asad Aali, Muhammad Usman Khanzada, Muhammad Usman Rafique, Zihao He, Emily Fox, Dean F. Hougen
- arxiv_id: 2604.06260
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.06260v1
- published: 2026-04-07
