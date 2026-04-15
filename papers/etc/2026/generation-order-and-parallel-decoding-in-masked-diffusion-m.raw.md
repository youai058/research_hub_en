---
title: "Generation Order and Parallel Decoding in Masked Diffusion Models: An Information-Theoretic Perspective"
authors: ["Shaorong Zhang", "Longxuan Yu", "Rob Brekelmans", "Luhan Tang", "Salman Asif", "Greg Ver Steeg"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.00286"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.00286v1"
published: "2026-01-30"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# Generation Order and Parallel Decoding in Masked Diffusion Models: An Information-Theoretic Perspective

## Abstract
Masked Diffusion Models (MDMs) significantly accelerate inference by trading off sequential determinism. However, the theoretical mechanisms governing generation order and the risks inherent in parallelization remain under-explored. In this work, we provide a unified information-theoretic framework to decouple and analyze two fundamental sources of failure: order sensitivity and parallelization bias. Our analysis yields three key insights: (1) The benefits of Easy-First decoding (prioritizing low-entropy tokens) are magnified as model error increases; (2) factorized parallel decoding introduces intrinsic sampling errors that can lead to arbitrary large Reverse KL divergence, capturing "incoherence" failures that standard Forward KL metrics overlook; and (3) while verification can eliminate sampling error, it incurs an exponential cost governed by the total correlation within a block. Conversely, heuristics like remasking, though computationally efficient, cannot guarantee distributional correctness. Experiments on a controlled Block-HMM and large-scale MDMs (LLaDA) for arithmetic reasoning validate our theoretical framework.

## Metadata
- venue: arXiv
- year: 2026
- authors: Shaorong Zhang, Longxuan Yu, Rob Brekelmans, Luhan Tang, Salman Asif, Greg Ver Steeg
- arxiv_id: 2602.00286
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.00286v1
- published: 2026-01-30
