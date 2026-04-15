---
title: "Watermarking Diffusion Language Models"
authors: ["Thibaud Gloaguen", "Robin Staab", "Nikola Jovanović", "Martin Vechev"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.24368"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.24368v2"
published: "2025-09-29"
categories: ["cs.LG", "cs.AI", "cs.CR"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# Watermarking Diffusion Language Models

## Abstract
We introduce the first watermark tailored for diffusion language models (DLMs), an emergent LLM paradigm able to generate tokens in arbitrary order, in contrast to standard autoregressive language models (ARLMs) which generate tokens sequentially. While there has been much work in ARLM watermarking, a key challenge when attempting to apply these schemes directly to the DLM setting is that they rely on previously generated tokens, which are not always available with DLM generation. In this work we address this challenge by: (i) applying the watermark in expectation over the context even when some context tokens are yet to be determined, and (ii) promoting tokens which increase the watermark strength when used as context for other tokens. This is accomplished while keeping the watermark detector unchanged. Our experimental evaluation demonstrates that the DLM watermark leads to a >99% true positive rate with minimal quality impact and achieves similar robustness to existing ARLM watermarks, enabling for the first time reliable DLM watermarking.

## Metadata
- venue: arXiv
- year: 2025
- authors: Thibaud Gloaguen, Robin Staab, Nikola Jovanović, Martin Vechev
- arxiv_id: 2509.24368
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.24368v2
- published: 2025-09-29
