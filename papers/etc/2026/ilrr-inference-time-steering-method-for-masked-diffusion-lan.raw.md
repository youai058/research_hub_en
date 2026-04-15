---
title: "ILRR: Inference-Time Steering Method for Masked Diffusion Language Models"
authors: ["Eden Avrahami", "Eliya Nachmani"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.21647"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.21647v1"
published: "2026-01-29"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# ILRR: Inference-Time Steering Method for Masked Diffusion Language Models

## Abstract
Discrete Diffusion Language Models (DLMs) offer a promising non-autoregressive alternative for text generation, yet effective mechanisms for inference-time control remain relatively underexplored. Existing approaches include sampling-level guidance procedures or trajectory optimization mechanisms. In this work, we introduce Iterative Latent Representation Refinement (ILRR), a learning-free framework for steering DLMs using a single reference sequence. ILRR guides generation by dynamically aligning the internal activations of the generated sequence with those of a given reference throughout the denoising process. This approach captures and transfers high-level semantic properties, with a tunable steering scale enabling flexible control over attributes such as sentiment. We further introduce Spatially Modulated Steering, an extension that enables steering long texts using shorter references by regulating guidance intensity across the sequence. Empirically, we demonstrate that ILRR achieves effective attribute steering on LLaDA and MDLM architectures with a minor computational overhead, requiring only one additional parallel forward pass per denoising step. Under the same compute budget, ILRR improves attribute accuracy over comparable baselines by 10$\%$ to 60$\%$ points, while maintaining high generation quality.

## Metadata
- venue: arXiv
- year: 2026
- authors: Eden Avrahami, Eliya Nachmani
- arxiv_id: 2601.21647
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.21647v1
- published: 2026-01-29
