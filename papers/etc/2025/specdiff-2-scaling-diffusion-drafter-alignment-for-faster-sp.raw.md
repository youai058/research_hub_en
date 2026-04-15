---
title: "SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding"
authors: ["Jameson Sandler", "Jacob K. Christopher", "Thomas Hartvigsen", "Ferdinando Fioretto"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.00606"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.00606v2"
published: "2025-11-01"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# SpecDiff-2: Scaling Diffusion Drafter Alignment For Faster Speculative Decoding

## Abstract
Speculative decoding has become the standard approach for accelerating Large Language Model (LLM) inference. It exploits a lossless draft-then-verify procedure to circumvent the latency of autoregressive decoding, achieving impressive speed-ups. Yet, current speculative decoding approaches remain limited by two fundamental bottlenecks: (1) the autoregressive dependency during drafting which limits parallelism, and (2) frequent rejections of draft tokens caused by misalignment between the draft and verify models. This paper proposes SpecDiff-2, a novel framework to jointly address these two bottlenecks. It leverages discrete diffusion as a non-autoregressive drafter to address bottleneck (1) and develops novel techniques to calibrate discrete diffusion drafters with autoregressive verifiers, addressing bottleneck (2). Experimental results across a comprehensive benchmark suite show that SpecDiff-2 achieves a new state-of-the-art across reasoning, coding, and mathematical benchmarks, improving tokens-per-second by up to an average of +55% over previous baselines and obtaining up to 5.5x average speed-up over standard decoding, without any loss of accuracy.

## Metadata
- venue: arXiv
- year: 2025
- authors: Jameson Sandler, Jacob K. Christopher, Thomas Hartvigsen, Ferdinando Fioretto
- arxiv_id: 2511.00606
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.00606v2
- published: 2025-11-01
