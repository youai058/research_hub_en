---
title: "Test-Time Anchoring for Discrete Diffusion Posterior Sampling"
authors: ["Litu Rout", "Andreas Lugmayr", "Yasamin Jafarian", "Srivatsan Varadharajan", "Constantine Caramanis", "Sanjay Shakkottai", "Ira Kemelmacher-Shlizerman"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.02291"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.02291v2"
published: "2025-10-02"
categories: ["cs.LG", "cs.CV", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# Test-Time Anchoring for Discrete Diffusion Posterior Sampling

## Abstract
While continuous diffusion models have achieved remarkable success, discrete diffusion offers a unified framework for jointly modeling text and images. Beyond unification, discrete diffusion provides faster inference, finer control, and principled training-free guidance, making it well-suited for posterior sampling. Existing approaches to posterior sampling using discrete diffusion face severe challenges: derivative-free guidance yields sparse signals, continuous relaxations limit applicability, and split Gibbs samplers suffer from the curse of dimensionality. To overcome these limitations, we introduce Anchored Posterior Sampling (APS), built on two key innovations: quantized expectation for gradient-like guidance in discrete embedding space, and anchored remasking for adaptive decoding. APS achieves state-of-the-art performance among discrete diffusion samplers on both linear and nonlinear inverse problems across the standard image benchmarks. We demonstrate the generality of APS through training-free stylization and text-guided editing. We further apply APS to a large-scale diffusion language model, showing consistent improvement in question answering.

## Metadata
- venue: arXiv
- year: 2025
- authors: Litu Rout, Andreas Lugmayr, Yasamin Jafarian, Srivatsan Varadharajan, Constantine Caramanis, Sanjay Shakkottai, Ira Kemelmacher-Shlizerman
- arxiv_id: 2510.02291
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.02291v2
- published: 2025-10-02
