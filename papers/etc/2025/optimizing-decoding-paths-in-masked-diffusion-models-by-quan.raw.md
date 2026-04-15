---
title: "Optimizing Decoding Paths in Masked Diffusion Models by Quantifying Uncertainty"
authors: ["Ziyu Chen", "Xinbei Jiang", "Peng Sun", "Tao Lin"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.21336"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.21336v1"
published: "2025-12-24"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# Optimizing Decoding Paths in Masked Diffusion Models by Quantifying Uncertainty

## Abstract
Masked Diffusion Models (MDMs) offer flexible, non-autoregressive generation, but this freedom introduces a challenge: final output quality is highly sensitive to the decoding order. We are the first to formalize this issue, attributing the variability in output quality to the cumulative predictive uncertainty along a generative path. To quantify this uncertainty, we introduce Denoising Entropy, a computable metric that serves as an internal signal for evaluating generative process. Leveraging this metric, we propose two algorithms designed to optimize the decoding path: a post-hoc selection method and a real-time guidance strategy. Experiments demonstrate that our entropy-guided methods significantly improve generation quality, consistently boosting accuracy on challenging reasoning, planning, and code benchmarks. Our work establishes Denoising Entropy as a principled tool for understanding and controlling generation, effectively turning the uncertainty in MDMs from a liability into a key advantage for discovering high-quality solutions.

## Metadata
- venue: arXiv
- year: 2025
- authors: Ziyu Chen, Xinbei Jiang, Peng Sun, Tao Lin
- arxiv_id: 2512.21336
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.21336v1
- published: 2025-12-24
