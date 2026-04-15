---
title: "DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching"
authors: ["Jiayi Chen", "Wenxuan Song", "Shuai Chen", "Jingbo Wang", "Zhijun Li", "Haoang Li"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.26320"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.26320v3"
published: "2026-03-27"
categories: ["cs.RO", "cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# DFM-VLA: Iterative Action Refinement for Robot Manipulation via Discrete Flow Matching

## Abstract
Vision--Language--Action (VLA) models that encode actions using a discrete tokenization scheme are increasingly adopted for robotic manipulation, but existing decoding paradigms remain fundamentally limited. Whether actions are decoded sequentially by autoregressive VLAs or in parallel by discrete diffusion VLAs, once a token is generated, it is typically fixed and cannot be revised in subsequent iterations, so early token errors cannot be effectively corrected later. We propose DFM-VLA, a discrete flow matching VLA for iterative refinement of action tokens. DFM-VLA~models a token-level probability velocity field that dynamically updates the full action sequence across refinement iterations. We investigate two ways to construct the velocity field: an auxiliary velocity-head formulation and an action-embedding-guided formulation. Our framework further adopts a two-stage decoding strategy with an iterative refinement stage followed by deterministic validation for stable convergence. Extensive experiments on CALVIN, LIBERO, and real-world manipulation tasks show that DFM-VLA consistently outperforms strong autoregressive, discrete diffusion, and continuous diffusion baselines in manipulation performance while retaining high inference efficiency. In particular, DFM-VLA achieves an average success length of 4.44 on CALVIN and an average success rate of 95.7\% on LIBERO, highlighting the value of action refinement via discrete flow matching for robotic manipulation. Our project is available https://chris1220313648.github.io/DFM-VLA/

## Metadata
- venue: arXiv
- year: 2026
- authors: Jiayi Chen, Wenxuan Song, Shuai Chen, Jingbo Wang, Zhijun Li, Haoang Li
- arxiv_id: 2603.26320
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.26320v3
- published: 2026-03-27
