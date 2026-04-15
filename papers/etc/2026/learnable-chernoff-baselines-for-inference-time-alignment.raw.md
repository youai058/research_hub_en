---
title: "Learnable Chernoff Baselines for Inference-Time Alignment"
authors: ["Sunil Madhow", "Yuchen Liang", "Ness Shroff", "Yingbin Liang", "Yu-Xiang Wang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.07738"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.07738v2"
published: "2026-02-08"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:32+09:00"
---

# Learnable Chernoff Baselines for Inference-Time Alignment

## Abstract
We study inference-time reward-guided alignment for generative models. Existing methods often rely on either architecture-specific adaptations or computationally costly inference procedures. We introduce Learnable Chernoff Baselines (LCBs) as a method for efficiently and approximately sampling from the exponentially tilted kernels that arise from KL-regularized reward alignment. Using only black-box sampling access to the pretrained model, LCBs implement a form of rejection sampling with adaptively selected acceptance probabilities, which allows fine-grained control over inference-compute scaling. We establish total-variation guarantees to the ideal aligned model, and demonstrate in both continuous and discrete diffusion settings that LCB sampling closely matches ideal rejection sampling while using substantially fewer queries to the pretrained model.

## Metadata
- venue: arXiv
- year: 2026
- authors: Sunil Madhow, Yuchen Liang, Ness Shroff, Yingbin Liang, Yu-Xiang Wang
- arxiv_id: 2602.07738
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.07738v2
- published: 2026-02-08
