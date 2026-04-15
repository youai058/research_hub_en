---
title: "MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation"
authors: ["Yang Liu", "Pengxiang Ding", "Tengyue Jiang", "Xudong Wang", "Wenxuan Song", "Minghui Lin", "Han Zhao", "Hongyin Zhang", "Zifeng Zhuang", "Wei Zhao", "Siteng Huang", "Jinkui Shi", "Donglin Wang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.25406"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.25406v2"
published: "2026-03-26"
categories: ["cs.RO"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:24+09:00"
---

# MMaDA-VLA: Large Diffusion Vision-Language-Action Model with Unified Multi-Modal Instruction and Generation

## Abstract
Vision-Language-Action (VLA) models aim to control robots for manipulation from visual observations and natural-language instructions. However, existing hierarchical and autoregressive paradigms often introduce architectural overhead, suffer from temporal inconsistency and long-horizon error accumulation, and lack a mechanism to capture environment dynamics without extra modules. To this end, we present MMaDA-VLA, a fully native pre-trained large diffusion VLA model that unifies multi-modal understanding and generation in a single framework. Our key idea is a native discrete diffusion formulation that embeds language, images, and continuous robot controls into one discrete token space and trains a single backbone with masked token denoising to jointly generate a future goal observation and an action chunk in parallel. Iterative denoising enables global, order-free refinement, improving long-horizon consistency while grounding actions in predicted future visual outcomes without auxiliary world models. Experiments across simulation benchmarks and real-world tasks show state-of-the-art performance, achieving 98.0% average success on LIBERO and 4.78 average length on CALVIN.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yang Liu, Pengxiang Ding, Tengyue Jiang, Xudong Wang, Wenxuan Song, Minghui Lin, Han Zhao, Hongyin Zhang, Zifeng Zhuang, Wei Zhao, Siteng Huang, Jinkui Shi, Donglin Wang
- arxiv_id: 2603.25406
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.25406v2
- published: 2026-03-26
