---
title: "Relaxing Positional Alignment in Masked Diffusion Language Models"
authors: ["Mengyu Ye", "Ryosuke Takahashi", "Keito Kudo", "Jun Suzuki"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.22947"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.22947v1"
published: "2026-01-30"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Relaxing Positional Alignment in Masked Diffusion Language Models

## Abstract
Masked diffusion language models (MDLMs) have emerged as a promising alternative to dominant autoregressive approaches. Although they achieve competitive performance on several tasks, a substantial gap remains in open-ended text generation. We hypothesize that one cause of this gap is that strict positional prediction makes MDLM decoding highly sensitive to token misalignment, and we show through controlled interventions that a one-position shift can severely disrupt semantics. This observation suggests that enforcing strict positional supervision during training is misaligned with the irreversible denoising dynamics of MDLM decoding. Motivated by this mismatch, we adopt an alignment-flexible supervision strategy during fine-tuning. Specifically, we introduce a special token <slack> via the connectionist temporal classification objective. We apply this approach to the widely used MDLM model and conduct experiments on five open-ended text generation benchmarks. Our method consistently outperforms the original model and improves robustness to positional shifts, indicating that relaxing strict positional supervision is an important factor in improving generation quality in MDLMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Mengyu Ye, Ryosuke Takahashi, Keito Kudo, Jun Suzuki
- arxiv_id: 2601.22947
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.22947v1
- published: 2026-01-30
