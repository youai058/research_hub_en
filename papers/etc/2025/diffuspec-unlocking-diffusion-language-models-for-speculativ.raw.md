---
title: "DiffuSpec: Unlocking Diffusion Language Models for Speculative Decoding"
authors: ["Guanghao Li", "Zhihui Fu", "Min Fang", "Qibin Zhao", "Ming Tang", "Chun Yuan", "Jun Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.02358"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.02358v1"
published: "2025-09-28"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# DiffuSpec: Unlocking Diffusion Language Models for Speculative Decoding

## Abstract
As large language models (LLMs) scale up, accuracy improves, but the autoregressive (AR) nature of decoding increases latency since each token requires a serial forward pass. Speculative decoding addresses this by employing a fast drafter to propose multi-token drafts, which are then verified in parallel by the target model. However, many deployments still rely on AR drafters, where sequential passes limit wall-clock gains. We revisit the drafting stage and present DiffuSpec, a training-free drop-in framework that uses a pretrained diffusion language model (DLM) to produce multi-token drafts in a single forward pass, while remaining compatible with standard AR verifiers. Because DLM drafts are generated under bidirectional conditioning, parallel per-position candidates form a token lattice in which the locally highest-probability token at each position need not form a causal left-to-right path. Moreover, DLM drafting requires pre-specifying a draft length, inducing a speed-quality trade-off. To address these challenges, we introduce two practical components: (i) a causal-consistency path search (CPS) over this lattice that extracts a left-to-right path aligned with AR verification; and (ii) an adaptive draft-length (ADL) controller that adjusts next proposal size based on recent acceptance feedback and realized generated length. Across benchmarks, DiffuSpec yields up to 3x wall-clock speedup, establishing diffusion-based drafting as a robust alternative to autoregressive drafters for speculative decoding.

## Metadata
- venue: arXiv
- year: 2025
- authors: Guanghao Li, Zhihui Fu, Min Fang, Qibin Zhao, Ming Tang, Chun Yuan, Jun Wang
- arxiv_id: 2510.02358
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.02358v1
- published: 2025-09-28
