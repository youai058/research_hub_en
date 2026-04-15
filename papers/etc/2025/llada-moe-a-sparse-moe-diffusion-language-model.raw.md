---
title: "LLaDA-MoE: A Sparse MoE Diffusion Language Model"
authors: ["Fengqi Zhu", "Zebin You", "Yipeng Xing", "Zenan Huang", "Lin Liu", "Yihong Zhuang", "Guoshan Lu", "Kangyu Wang", "Xudong Wang", "Lanning Wei", "Hongrui Guo", "Jiaqi Hu", "Wentao Ye", "Tieyuan Chen", "Chenchen Li", "Chengfu Tang", "Haibo Feng", "Jun Hu", "Jun Zhou", "Xiaolu Zhang", "Zhenzhong Lan", "Junbo Zhao", "Da Zheng", "Chongxuan Li", "Jianguo Li", "Ji-Rong Wen"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.24389"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.24389v1"
published: "2025-09-29"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# LLaDA-MoE: A Sparse MoE Diffusion Language Model

## Abstract
We introduce LLaDA-MoE, a large language diffusion model with the Mixture-of-Experts (MoE) architecture, trained from scratch on approximately 20T tokens. LLaDA-MoE achieves competitive performance with significantly reduced computational overhead by maintaining a 7B-parameter capacity while activating only 1.4B parameters during inference. Our empirical evaluation reveals that LLaDA-MoE achieves state-of-the-art performance among diffusion language models with larger parameters, surpassing previous diffusion language models LLaDA, LLaDA 1.5, and Dream across multiple benchmarks. The instruct-tuned model LLaDA-MoE-7B-A1B-Instruct demonstrates capabilities comparable to Qwen2.5-3B-Instruct in knowledge understanding, code generation, mathematical reasoning, agent and alignment tasks, despite using fewer active parameters. Our results show that integrating a sparse MoE architecture into the training objective of masked diffusion language models still brings out MoE's strengths under efficient inference with few active parameters, and opens ample room for further exploration of diffusion language models. LLaDA-MoE models are available at Huggingface.

## Metadata
- venue: arXiv
- year: 2025
- authors: Fengqi Zhu, Zebin You, Yipeng Xing, Zenan Huang, Lin Liu, Yihong Zhuang, Guoshan Lu, Kangyu Wang, Xudong Wang, Lanning Wei, Hongrui Guo, Jiaqi Hu, Wentao Ye, Tieyuan Chen, Chenchen Li, Chengfu Tang, Haibo Feng, Jun Hu, Jun Zhou, Xiaolu Zhang, Zhenzhong Lan, Junbo Zhao, Da Zheng, Chongxuan Li, Jianguo Li, Ji-Rong Wen
- arxiv_id: 2509.24389
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.24389v1
- published: 2025-09-29
