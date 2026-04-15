---
title: "Understanding the Reversal Curse Mitigation in Masked Diffusion Models through Attention and Training Dynamics"
authors: ["Sangwoo Shin", "BumJun Kim", "Kyelim Lee", "Moongyu Jeon", "Albert No"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.02133"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.02133v1"
published: "2026-02-02"
categories: ["cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Understanding the Reversal Curse Mitigation in Masked Diffusion Models through Attention and Training Dynamics

## Abstract
Autoregressive language models (ARMs) suffer from the reversal curse: after learning that "$A$ is $B$", they often fail on the reverse query "$B$ is $A$". Masked diffusion-based language models (MDMs) exhibit this failure in a much weaker form, but the underlying reason has remained unclear. A common explanation attributes this mitigation to the any-order training objective. However, observing "[MASK] is $B$" during training does not necessarily teach the model to handle the reverse prompt "$B$ is [MASK]". We show that the mitigation arises from architectural structure and its interaction with training. In a one-layer Transformer encoder, weight sharing couples the two directions by making forward and reverse attention scores positively correlated. In the same setting, we further show that the corresponding gradients are aligned, so minimizing the forward loss also reduces the reverse loss. Experiments on both controlled toy tasks and large-scale diffusion language models support these mechanisms, explaining why MDMs partially overcome a failure mode that persists in strong ARMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Sangwoo Shin, BumJun Kim, Kyelim Lee, Moongyu Jeon, Albert No
- arxiv_id: 2602.02133
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.02133v1
- published: 2026-02-02
