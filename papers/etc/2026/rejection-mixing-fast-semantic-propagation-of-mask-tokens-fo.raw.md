---
title: "Rejection Mixing: Fast Semantic Propagation of Mask Tokens for Efficient DLLM Inference"
authors: ["Yushi Ye", "Feng Hong", "Huangjie Zheng", "Xu Chen", "Zhiyong Chen", "Yanfeng Wang", "Jiangchao Yao"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.22868"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.22868v1"
published: "2026-02-26"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:28+09:00"
---

# Rejection Mixing: Fast Semantic Propagation of Mask Tokens for Efficient DLLM Inference

## Abstract
Diffusion Large Language Models (DLLMs) promise fast non-autoregressive inference but suffer a severe quality-speed trade-off in parallel decoding. This stems from the ''combinatorial contradiction'' phenomenon, where parallel tokens form semantically inconsistent combinations. We address this by integrating continuous representations into the discrete decoding process, as they preserve rich inter-position dependency. We propose ReMix (Rejection Mixing), a framework that introduces a novel Continuous Mixing State as an intermediate between the initial masked state and the final decoded token state. This intermediate state allows a token's representation to be iteratively refined in a continuous space, resolving mutual conflicts with other tokens before collapsing into a final discrete sample. Furthermore, a rejection rule reverts uncertain representations from the continuous state back to the masked state for reprocessing, ensuring stability and preventing error propagation. ReMix thus mitigates combinatorial contradictions by enabling continuous-space refinement during discrete diffusion decoding. Extensive experiments demonstrate that ReMix, as a training-free method, achieves a $2-8 \times$ inference speedup without any quality degradation.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yushi Ye, Feng Hong, Huangjie Zheng, Xu Chen, Zhiyong Chen, Yanfeng Wang, Jiangchao Yao
- arxiv_id: 2602.22868
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.22868v1
- published: 2026-02-26
