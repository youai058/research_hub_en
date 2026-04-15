---
title: "dgMARK: Decoding-Guided Watermarking for Diffusion Language Models"
authors: ["Pyo Min Hong", "Albert No"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.22985"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.22985v1"
published: "2026-01-30"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# dgMARK: Decoding-Guided Watermarking for Diffusion Language Models

## Abstract
We propose dgMARK, a decoding-guided watermarking method for discrete diffusion language models (dLLMs). Unlike autoregressive models, dLLMs can generate tokens in arbitrary order. While an ideal conditional predictor would be invariant to this order, practical dLLMs exhibit strong sensitivity to the unmasking order, creating a new channel for watermarking. dgMARK steers the unmasking order toward positions whose high-reward candidate tokens satisfy a simple parity constraint induced by a binary hash, without explicitly reweighting the model's learned probabilities. The method is plug-and-play with common decoding strategies (e.g., confidence, entropy, and margin-based ordering) and can be strengthened with a one-step lookahead variant. Watermarks are detected via elevated parity-matching statistics, and a sliding-window detector ensures robustness under post-editing operations including insertion, deletion, substitution, and paraphrasing.

## Metadata
- venue: arXiv
- year: 2026
- authors: Pyo Min Hong, Albert No
- arxiv_id: 2601.22985
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.22985v1
- published: 2026-01-30
