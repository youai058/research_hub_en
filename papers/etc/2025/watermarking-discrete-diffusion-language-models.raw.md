---
title: "Watermarking Discrete Diffusion Language Models"
authors: ["Avi Bagchi", "Akhil Bhimaraju", "Moulik Choraria", "Daniel Alabi", "Lav R. Varshney"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.02083"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.02083v2"
published: "2025-11-03"
categories: ["cs.CR", "cs.AI", "cs.CY"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# Watermarking Discrete Diffusion Language Models

## Abstract
Watermarking has emerged as a promising technique to track AI-generated content and differentiate it from authentic human creations. While prior work extensively studies watermarking for autoregressive large language models (LLMs) and image diffusion models, it remains comparatively underexplored for discrete diffusion language models (DDLMs), which are becoming popular due to their high inference throughput. In this paper, we introduce one of the first watermarking methods for DDLMs. Our approach applies a distribution-preserving Gumbel-max sampling trick at every diffusion step and seeds the randomness by sequence position to enable reliable detection. We empirically demonstrate reliable detectability on LLaDA, a state-of-the-art DDLM. We also analytically prove that the watermark is distortion-free, with a false detection probability that decays exponentially in the sequence length. A key practical advantage is that our method realizes desired watermarking properties with no expensive hyperparameter tuning, making it straightforward to deploy and scale across models and benchmarks.

## Metadata
- venue: arXiv
- year: 2025
- authors: Avi Bagchi, Akhil Bhimaraju, Moulik Choraria, Daniel Alabi, Lav R. Varshney
- arxiv_id: 2511.02083
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.02083v2
- published: 2025-11-03
