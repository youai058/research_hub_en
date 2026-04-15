---
title: "Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion"
authors: ["Jacob K Christopher", "Brian R Bartoldson", "Tal Ben-Nun", "Michael Cardei", "Bhavya Kailkhura", "Ferdinando Fioretto"]
venue: "NAACL"
year: 2025
venue_class: "etc"
arxiv_id: "2408.05636"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2408.05636v4"
published: "2024-08-10"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-comment"
hunter_fetched: "2026-04-15T05:20:12+09:00"
---

# Speculative Diffusion Decoding: Accelerating Language Generation through Diffusion

## Abstract
Speculative decoding has emerged as a widely adopted method to accelerate large language model inference without sacrificing the quality of the model outputs. While this technique has facilitated notable speed improvements by enabling parallel sequence verification, its efficiency remains inherently limited by the reliance on incremental token generation in existing draft models. To overcome this limitation, this paper proposes an adaptation of speculative decoding which uses discrete diffusion models to generate draft sequences. This allows parallelization of both the drafting and verification steps, providing significant speedups to the inference process. Our proposed approach, $\textit{Speculative Diffusion Decoding (SpecDiff)}$, is validated on standard language generation benchmarks and empirically demonstrated to provide up to 7.2x speedups over standard generation processes and up to 1.75x speedups over existing speculative decoding approaches.

## Metadata
- venue: NAACL
- year: 2025
- authors: Jacob K Christopher, Brian R Bartoldson, Tal Ben-Nun, Michael Cardei, Bhavya Kailkhura, Ferdinando Fioretto
- arxiv_id: 2408.05636
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2408.05636v4
- published: 2024-08-10
