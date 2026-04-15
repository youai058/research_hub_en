---
title: "DODO: Discrete OCR Diffusion Models"
authors: ["Sean Man", "Roy Ganz", "Roi Ronen", "Shahar Tsiper", "Shai Mazor", "Niv Nayman"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.16872"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.16872v1"
published: "2026-02-18"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# DODO: Discrete OCR Diffusion Models

## Abstract
Optical Character Recognition (OCR) is a fundamental task for digitizing information, serving as a critical bridge between visual data and textual understanding. While modern Vision-Language Models (VLM) have achieved high accuracy in this domain, they predominantly rely on autoregressive decoding, which becomes computationally expensive and slow for long documents as it requires a sequential forward pass for every generated token. We identify a key opportunity to overcome this bottleneck: unlike open-ended generation, OCR is a highly deterministic task where the visual input strictly dictates a unique output sequence, theoretically enabling efficient, parallel decoding via diffusion models. However, we show that existing masked diffusion models fail to harness this potential; those introduce structural instabilities that are benign in flexible tasks, like captioning, but catastrophic for the rigid, exact-match requirements of OCR. To bridge this gap, we introduce DODO, the first VLM to utilize block discrete diffusion and unlock its speedup potential for OCR. By decomposing generation into blocks, DODO mitigates the synchronization errors of global diffusion. Empirically, our method achieves near state-of-the-art accuracy while enabling up to 3x faster inference compared to autoregressive baselines.

## Metadata
- venue: arXiv
- year: 2026
- authors: Sean Man, Roy Ganz, Roi Ronen, Shahar Tsiper, Shai Mazor, Niv Nayman
- arxiv_id: 2602.16872
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.16872v1
- published: 2026-02-18
