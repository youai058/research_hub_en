---
title: "Dream-Coder 7B: An Open Diffusion Language Model for Code"
authors: ["Zhihui Xie", "Jiacheng Ye", "Lin Zheng", "Jiahui Gao", "Jingwei Dong", "Zirui Wu", "Xueliang Zhao", "Shansan Gong", "Xin Jiang", "Zhenguo Li", "Lingpeng Kong"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.01142"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.01142v1"
published: "2025-09-01"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Dream-Coder 7B: An Open Diffusion Language Model for Code

## Abstract
We present Dream-Coder 7B, an open-source discrete diffusion language model for code generation that exhibits emergent any-order generation capabilities. Unlike traditional autoregressive (AR) models that decode strictly left-to-right, Dream-Coder 7B adaptively determines its decoding strategy based on the coding task: sketch-first generation for complex algorithms, left-to-right generation for straightforward completions, and interleaved reasoning generation for code understanding tasks. We adapt a pretrained AR checkpoint to a discrete diffusion frameworks with a continuous-time weighted cross-entropy objective. Our post-training recipe comprises (i) supervised fine-tuning, where we mitigate padding pathologies via random truncation and a padding penalty to improve sample efficiency and stabilize generation; and (ii) reinforcement learning with verifiable rewards over a curated high-quality prompt set drawn from open-source datasets, using a tailored reinforcement learning recipe for diffusion language models. The resulting Dream-Coder 7B Instruct attains 21.4\% pass@1 on LiveCodeBench (2410--2505) and demonstrates competitive performance on HumanEval, MBPP, BigCodeBench, and CRUXEval. We release Dream-Coder-7B and Dream-Coder-7B-Instruct checkpoints, training recipes, preprocessing pipelines, and inference code to facilitate reproducibility and further research.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zhihui Xie, Jiacheng Ye, Lin Zheng, Jiahui Gao, Jingwei Dong, Zirui Wu, Xueliang Zhao, Shansan Gong, Xin Jiang, Zhenguo Li, Lingpeng Kong
- arxiv_id: 2509.01142
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.01142v1
- published: 2025-09-01
