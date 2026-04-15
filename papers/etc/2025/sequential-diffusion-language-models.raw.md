---
title: "Sequential Diffusion Language Models"
authors: ["Yangzhou Liu", "Yue Cao", "Hao Li", "Gen Luo", "Zhe Chen", "Weiyun Wang", "Xiaobo Liang", "Biqing Qi", "Lijun Wu", "Changyao Tian", "Yanting Zhang", "Yuqiang Li", "Tong Lu", "Yu Qiao", "Jifeng Dai", "Wenhai Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.24007"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.24007v1"
published: "2025-09-28"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Sequential Diffusion Language Models

## Abstract
Diffusion language models (DLMs) have strong theoretical efficiency but are limited by fixed-length decoding and incompatibility with key-value (KV) caches. Block diffusion mitigates these issues, yet still enforces a fixed block size and requires expensive training. We introduce Next Sequence Prediction (NSP), which unifies next-token and next-block prediction, enabling the model to adaptively determine the generation length at each step. When the length is fixed to 1, NSP reduces to standard next-token prediction. Building on NSP, we propose Sequential Diffusion Language Model (SDLM), which can retrofit pre-trained autoregressive language models (ALMs) at minimal cost. Specifically, SDLM performs diffusion inference within fixed-size mask blocks, but dynamically decodes consecutive subsequences based on model confidence, thereby preserving KV-cache compatibility and improving robustness to varying uncertainty and semantics across the sequence. Experiments show that SDLM matches or surpasses strong autoregressive baselines using only 3.5M training samples, while achieving 2.1 higher throughput than Qwen-2.5. Notably, the SDLM-32B model delivers even more pronounced efficiency gains, demonstrating the strong scalability potential of our modeling paradigm. Project page and codes: https://github.com/OpenGVLab/SDLM

## Metadata
- venue: arXiv
- year: 2025
- authors: Yangzhou Liu, Yue Cao, Hao Li, Gen Luo, Zhe Chen, Weiyun Wang, Xiaobo Liang, Biqing Qi, Lijun Wu, Changyao Tian, Yanting Zhang, Yuqiang Li, Tong Lu, Yu Qiao, Jifeng Dai, Wenhai Wang
- arxiv_id: 2509.24007
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.24007v1
- published: 2025-09-28
