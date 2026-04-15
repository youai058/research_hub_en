---
title: "Fast-dLLM v2: Efficient Block-Diffusion LLM"
authors: ["Chengyue Wu", "Hao Zhang", "Shuchen Xue", "Shizhe Diao", "Yonggan Fu", "Zhijian Liu", "Pavlo Molchanov", "Ping Luo", "Song Han", "Enze Xie"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.26328"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.26328v1"
published: "2025-09-30"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# Fast-dLLM v2: Efficient Block-Diffusion LLM

## Abstract
Autoregressive (AR) large language models (LLMs) have achieved remarkable performance across a wide range of natural language tasks, yet their inherent sequential decoding limits inference efficiency. In this work, we propose Fast-dLLM v2, a carefully designed block diffusion language model (dLLM) that efficiently adapts pretrained AR models into dLLMs for parallel text generation, requiring only approximately 1B tokens of fine-tuning. This represents a 500x reduction in training data compared to full-attention diffusion LLMs such as Dream (580B tokens), while preserving the original model's performance. Our approach introduces a novel training recipe that combines a block diffusion mechanism with a complementary attention mask, enabling blockwise bidirectional context modeling without sacrificing AR training objectives. To further accelerate decoding, we design a hierarchical caching mechanism: a block-level cache that stores historical context representations across blocks, and a sub-block cache that enables efficient parallel generation within partially decoded blocks. Coupled with our parallel decoding pipeline, Fast-dLLM v2 achieves up to 2.5x speedup over standard AR decoding without compromising generation quality. Extensive experiments across diverse benchmarks demonstrate that Fast-dLLM v2 matches or surpasses AR baselines in accuracy, while delivering state-of-the-art efficiency among dLLMs - marking a significant step toward the practical deployment of fast and accurate LLMs. Code and model will be publicly released.

## Metadata
- venue: arXiv
- year: 2025
- authors: Chengyue Wu, Hao Zhang, Shuchen Xue, Shizhe Diao, Yonggan Fu, Zhijian Liu, Pavlo Molchanov, Ping Luo, Song Han, Enze Xie
- arxiv_id: 2509.26328
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.26328v1
- published: 2025-09-30
