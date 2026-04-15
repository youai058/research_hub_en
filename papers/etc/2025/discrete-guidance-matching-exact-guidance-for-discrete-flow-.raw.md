---
title: "Discrete Guidance Matching: Exact Guidance for Discrete Flow Matching"
authors: ["Zhengyan Wan", "Yidong Ouyang", "Liyan Xie", "Fang Fang", "Hongyuan Zha", "Guang Cheng"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.21912"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.21912v1"
published: "2025-09-26"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:26+09:00"
---

# Discrete Guidance Matching: Exact Guidance for Discrete Flow Matching

## Abstract
Guidance provides a simple and effective framework for posterior sampling by steering the generation process towards the desired distribution. When modeling discrete data, existing approaches mostly focus on guidance with the first-order Taylor approximation to improve the sampling efficiency. However, such an approximation is inappropriate in discrete state spaces since the approximation error could be large. A novel guidance framework for discrete data is proposed to address this problem: We derive the exact transition rate for the desired distribution given a learned discrete flow matching model, leading to guidance that only requires a single forward pass in each sampling step, significantly improving efficiency. This unified novel framework is general enough, encompassing existing guidance methods as special cases, and it can also be seamlessly applied to the masked diffusion model. We demonstrate the effectiveness of our proposed guidance on energy-guided simulations and preference alignment on text-to-image generation and multimodal understanding tasks. The code is available through https://github.com/WanZhengyan/Discrete-Guidance-Matching/tree/main.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zhengyan Wan, Yidong Ouyang, Liyan Xie, Fang Fang, Hongyuan Zha, Guang Cheng
- arxiv_id: 2509.21912
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.21912v1
- published: 2025-09-26
