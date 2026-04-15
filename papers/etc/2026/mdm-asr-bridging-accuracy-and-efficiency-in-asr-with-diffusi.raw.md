---
title: "MDM-ASR: Bridging Accuracy and Efficiency in ASR with Diffusion-Based Non-Autoregressive Decoding"
authors: ["Hao Yen", "Pin-Jui Ku", "Ante Jukić", "Sabato Marco Siniscalchi"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.18952"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.18952v2"
published: "2026-02-21"
categories: ["eess.AS"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# MDM-ASR: Bridging Accuracy and Efficiency in ASR with Diffusion-Based Non-Autoregressive Decoding

## Abstract
In sequence-to-sequence Transformer ASR, autoregressive (AR) models achieve strong accuracy but suffer from slow decoding, while non-autoregressive (NAR) models enable parallel decoding at the cost of degraded performance. We propose a principled NAR ASR framework based on Masked Diffusion Models to reduce this gap. A pre-trained speech encoder is coupled with a Transformer diffusion decoder conditioned on acoustic features and partially masked transcripts for parallel token prediction. To mitigate the training-inference mismatch, we introduce Iterative Self-Correction Training that exposes the model to its own intermediate predictions. We also design a Position-Biased Entropy-Bounded Confidence-based sampler with positional bias to further boost results. Experiments across multiple benchmarks demonstrate consistent gains over prior NAR models and competitive performance with strong AR baselines, while retaining parallel decoding efficiency.

## Metadata
- venue: arXiv
- year: 2026
- authors: Hao Yen, Pin-Jui Ku, Ante Jukić, Sabato Marco Siniscalchi
- arxiv_id: 2602.18952
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.18952v2
- published: 2026-02-21
