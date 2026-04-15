---
title: "Decoding quantum low density parity check codes with diffusion"
authors: ["Zejun Liu", "Anqi Gong", "Bryan K. Clark"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.22347"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.22347v1"
published: "2025-09-26"
categories: ["quant-ph"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:26+09:00"
---

# Decoding quantum low density parity check codes with diffusion

## Abstract
An efficient decoder is essential for quantum error correction, and data-driven neural decoders have emerged as promising, flexible solutions. Here, we introduce a diffusion model framework to infer logical errors from syndrome measurements in quantum low-density parity-check codes. Using the bivariate bicycle code with realistic circuit-level noise, we show that masked diffusion decoders are more accurate, often faster on average, and always faster in the worst case than other state-of-the-art decoders, including belief propagation with ordered statistics decoding (BP-OSD) and autoregressive neural decoders. We show that by using fewer diffusion steps during inference one can gain significant speed at minimal cost in accuracy. By examining the factored attention from our trained neural network we find that, despite being trained solely on paired samples of syndrome-logical errors, this diffusion decoder learns the structure of the quantum codes. We also compare both masked and continuous diffusion decoders on code-capacity noise models, finding that masked diffusion decoders scale better than continuous diffusion decoders.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zejun Liu, Anqi Gong, Bryan K. Clark
- arxiv_id: 2509.22347
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.22347v1
- published: 2025-09-26
