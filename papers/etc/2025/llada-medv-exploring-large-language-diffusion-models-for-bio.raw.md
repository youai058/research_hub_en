---
title: "LLaDA-MedV: Exploring Large Language Diffusion Models for Biomedical Image Understanding"
authors: ["Xuanzhao Dong", "Wenhui Zhu", "Xiwen Chen", "Zhipeng Wang", "Peijie Qiu", "Shao Tang", "Xin Li", "Yalin Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2508.01617"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2508.01617v2"
published: "2025-08-03"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# LLaDA-MedV: Exploring Large Language Diffusion Models for Biomedical Image Understanding

## Abstract
Autoregressive models (ARMs) have long dominated the landscape of biomedical vision-language models (VLMs). Recently, masked diffusion models such as LLaDA have emerged as promising alternatives, yet their application in the biomedical domain remains largely underexplored. To bridge this gap, we introduce LLaDA-MedV, the first large language diffusion model tailored for biomedical image understanding through vision instruction tuning. LLaDA-MedV achieves relative performance gains of 7.855% over LLaVA-Med and 1.867% over LLaDA-V in the open-ended biomedical visual conversation task, and sets new state-of-the-art accuracy on the closed-form subset of three VQA benchmarks: 84.93% on VQA-RAD, 92.31% on SLAKE, and 95.15% on PathVQA. Furthermore, a detailed comparison with LLaVA-Med suggests that LLaDA-MedV is capable of generating reasonably longer responses by explicitly controlling response length, which can lead to more informative outputs. We also conduct an in-depth analysis of both the training and inference stages, highlighting the critical roles of initialization weight selection, fine-tuning strategies, and the interplay between sampling steps and response repetition. The code and model weight is released at https://github.com/LLM-VLM-GSL/LLaDA-MedV.

## Metadata
- venue: arXiv
- year: 2025
- authors: Xuanzhao Dong, Wenhui Zhu, Xiwen Chen, Zhipeng Wang, Peijie Qiu, Shao Tang, Xin Li, Yalin Wang
- arxiv_id: 2508.01617
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2508.01617v2
- published: 2025-08-03
