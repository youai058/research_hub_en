---
title: "Sharp Convergence Rates for Masked Diffusion Models"
authors: ["Yuchen Liang", "Zhiheng Tan", "Ness Shroff", "Yingbin Liang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.22505"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.22505v1"
published: "2026-02-26"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# Sharp Convergence Rates for Masked Diffusion Models

## Abstract
Discrete diffusion models have achieved strong empirical performance in text and other symbolic domains, with masked (absorbing-rate) variants emerging as competitive alternatives to autoregressive models. Among existing samplers, the Euler method remains the standard choice in many applications, and more recently, the First-Hitting Sampler (FHS) has shown considerable promise for masked diffusion models. Despite their practical success, the theoretical understanding of these samplers remains limited. Existing analyses are conducted in Kullback-Leibler (KL) divergence, which often yields loose parameter dependencies and requires strong assumptions on score estimation. Moreover, these guarantees do not cover recently developed high-performance sampler of FHS. In this work, we first develop a direct total-variation (TV) based analysis for the Euler method that overcomes these limitations. Our results relax assumptions on score estimation, improve parameter dependencies, and establish convergence guarantees without requiring any surrogate initialization. Also for this setting, we provide the first convergence lower bound for the Euler sampler, establishing tightness with respect to both the data dimension $d$ and the target accuracy $\varepsilon$. Finally, we analyze the FHS sampler and show that it incurs no sampling error beyond that induced by score estimation, which we show to be tight with a matching lower error bound. Overall, our analysis introduces a direct TV-based error decomposition along the CTMC trajectory and a decoupling-based path-wise analysis for FHS, which may be of independent interest.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yuchen Liang, Zhiheng Tan, Ness Shroff, Yingbin Liang
- arxiv_id: 2602.22505
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.22505v1
- published: 2026-02-26
