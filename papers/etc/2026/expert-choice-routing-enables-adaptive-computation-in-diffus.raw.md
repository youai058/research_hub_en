---
title: "Expert-Choice Routing Enables Adaptive Computation in Diffusion Language Models"
authors: ["Shuibai Zhang", "Caspian Zhuang", "Chihan Cui", "Zhihan Yang", "Fred Zhangzhi Peng", "Yanxin Zhang", "Haoyue Bai", "Zack Jia", "Yang Zhou", "Guanhua Chen", "Ming Liu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.01622"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.01622v1"
published: "2026-04-02"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# Expert-Choice Routing Enables Adaptive Computation in Diffusion Language Models

## Abstract
Diffusion language models (DLMs) enable parallel, non-autoregressive text generation, yet existing DLM mixture-of-experts (MoE) models inherit token-choice (TC) routing from autoregressive systems, leading to load imbalance and rigid computation allocation. We show that expert-choice (EC) routing is a better fit for DLMs: it provides deterministic load balancing by design, yielding higher throughput and faster convergence than TC. Building on the property that EC capacity is externally controllable, we introduce timestep-dependent expert capacity, which varies expert allocation according to the denoising step. We find that allocating more capacity to low-mask-ratio steps consistently achieves the best performance under matched FLOPs, and provide a mechanistic explanation: tokens in low-mask-ratio contexts exhibit an order-of-magnitude higher learning efficiency, so concentrating compute on these steps yields the largest marginal return. Finally, we show that existing pretrained TC DLMs can be retrofitted to EC by replacing only the router, achieving faster convergence and improved accuracy across diverse downstream tasks. Together, these results establish EC routing as a superior paradigm for DLM MoE models and demonstrate that computation in DLMs can be treated as an adaptive policy rather than a fixed architectural constant. Code is available at https://github.com/zhangshuibai/EC-DLM.

## Metadata
- venue: arXiv
- year: 2026
- authors: Shuibai Zhang, Caspian Zhuang, Chihan Cui, Zhihan Yang, Fred Zhangzhi Peng, Yanxin Zhang, Haoyue Bai, Zack Jia, Yang Zhou, Guanhua Chen, Ming Liu
- arxiv_id: 2604.01622
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.01622v1
- published: 2026-04-02
