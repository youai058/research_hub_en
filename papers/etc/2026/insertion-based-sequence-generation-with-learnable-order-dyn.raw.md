---
title: "Insertion Based Sequence Generation with Learnable Order Dynamics"
authors: ["Dhruvesh Patel", "Benjamin Rozonoyer", "Gaurav Pandey", "Tahira Naseem", "Ramón Fernandez Astudillo", "Andrew McCallum"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.18695"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.18695v1"
published: "2026-02-21"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# Insertion Based Sequence Generation with Learnable Order Dynamics

## Abstract
In many domains generating variable length sequences through insertions provides greater flexibility over autoregressive models. However, the action space of insertion models is much larger than that of autoregressive models (ARMs) making the learning challenging. To address this, we incorporate trainable order dynamics into the target rates for discrete flow matching, and show that with suitable choices of parameterizations, joint training of the target order dynamics and the generator is tractable without the need for numerical simulation. As the generative insertion model, we use a variable length masked diffusion model, which generates by inserting and filling mask tokens. On graph traversal tasks for which a locally optimal insertion order is known, we explore the choices of parameterization empirically and demonstrate the trade-offs between flexibility, training stability and generation quality. On de novo small molecule generation, we find that the learned order dynamics leads to an increase in the number of valid molecules generated and improved quality, when compared to uniform order dynamics.

## Metadata
- venue: arXiv
- year: 2026
- authors: Dhruvesh Patel, Benjamin Rozonoyer, Gaurav Pandey, Tahira Naseem, Ramón Fernandez Astudillo, Andrew McCallum
- arxiv_id: 2602.18695
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.18695v1
- published: 2026-02-21
