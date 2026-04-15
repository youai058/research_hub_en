---
title: "Unifying Masked Diffusion Models with Various Generation Orders and Beyond"
authors: ["Chunsan Hong", "Sanghyun Lee", "Jong Chul Ye"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.02112"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.02112v1"
published: "2026-02-02"
categories: ["cs.LG", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# Unifying Masked Diffusion Models with Various Generation Orders and Beyond

## Abstract
Masked diffusion models (MDMs) are a potential alternative to autoregressive models (ARMs) for language generation, but generation quality depends critically on the generation order. Prior work either hard-codes an ordering (e.g., blockwise left-to-right) or learns an ordering policy for a pretrained MDM, which incurs extra cost and can yield suboptimal solutions due to the two-stage optimization. Motivated by this, we propose order-expressive masked diffusion model (OeMDM) for a broad class of diffusion generative processes with various generation orders, enabling the interpretation of MDM, ARM, and block diffusion in a single framework. Furthermore, building on OeMDM, we introduce learnable-order masked diffusion model (LoMDM), which jointly learns the generation ordering and diffusion backbone through a single objective from scratch, enabling the diffusion model to generate text in context-dependent ordering. Empirically, we confirm that LoMDM outperforms various discrete diffusion models across multiple language modeling benchmarks.

## Metadata
- venue: arXiv
- year: 2026
- authors: Chunsan Hong, Sanghyun Lee, Jong Chul Ye
- arxiv_id: 2602.02112
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.02112v1
- published: 2026-02-02
