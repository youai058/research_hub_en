---
title: "Balancing Understanding and Generation in Discrete Diffusion Models"
authors: ["Yue Liu", "Yuzhong Zhao", "Zheyong Xie", "Qixiang Ye", "Jianbin Jiao", "Yao Hu", "Shaosheng Cao", "Yunfan Liu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.01362"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.01362v1"
published: "2026-02-01"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# Balancing Understanding and Generation in Discrete Diffusion Models

## Abstract
In discrete generative modeling, two dominant paradigms demonstrate divergent capabilities: Masked Diffusion Language Models (MDLM) excel at semantic understanding and zero-shot generalization, whereas Uniform-noise Diffusion Language Models (UDLM) achieve strong few-step generation quality, yet neither attains balanced performance across both dimensions. To address this, we propose XDLM, which bridges the two paradigms via a stationary noise kernel. XDLM offers two key contributions: (1) it provides a principled theoretical unification of MDLM and UDLM, recovering each paradigm as a special case; and (2) an alleviated memory bottleneck enabled by an algebraic simplification of the posterior probabilities. Experiments demonstrate that XDLM advances the Pareto frontier between understanding capability and generation quality. Quantitatively, XDLM surpasses UDLM by 5.4 points on zero-shot text benchmarks and outperforms MDLM in few-step image generation (FID 54.1 vs. 80.8). When scaled to tune an 8B-parameter large language model, XDLM achieves 15.0 MBPP in just 32 steps, effectively doubling the baseline performance. Finally, analysis of training dynamics reveals XDLM's superior potential for long-term scaling. Code is available at https://github.com/MzeroMiko/XDLM

## Metadata
- venue: arXiv
- year: 2026
- authors: Yue Liu, Yuzhong Zhao, Zheyong Xie, Qixiang Ye, Jianbin Jiao, Yao Hu, Shaosheng Cao, Yunfan Liu
- arxiv_id: 2602.01362
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.01362v1
- published: 2026-02-01
