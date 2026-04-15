---
title: "PairUni: Pairwise Training for Unified Multimodal Language Models"
authors: ["Jiani Zheng", "Zhiyang Teng", "Kunpeng Qiu", "Xiangtai Li", "Anran Wang", "Yu Tian", "Ye Tian", "Haochen Wang", "Zhuochen Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.25682"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.25682v3"
published: "2025-10-29"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# PairUni: Pairwise Training for Unified Multimodal Language Models

## Abstract
Unified Vision-Language Models (UVLMs) perform both understanding and generation within a single architecture. Since these models rely on heterogeneous data and supervision, balancing both generation and understanding in reinforcement learning (RL) is challenging. To address this challenge, we propose PairUni, a unified framework that reorganizes data into understanding-generation (UG) pairs and aligns optimization accordingly. Specifically, we construct a unified paired dataset by synthesizing aligned instances via cross-modal semantic completion and retrieving semantically related samples. These paired structures expose cross-task semantic correspondences and support consistent policy learning. To leverage this structure, we present PairGRPO, a pair-aware variant based on Group Relative Policy Optimization. It assigns a similarity score to each pair to modulate the advantage, strengthening learning from well-aligned examples and reducing task interference. Extensive experiments across diverse UVLM architectures (Autoregressive and Discrete Diffusion) and scales (1B to 14B) demonstrate that PairUni yields consistent improvements over strong baselines. Notably, our method also demonstrates strong generalization by improving performance on image editing tasks without using any editing-specific data. Codes are available at https://github.com/Haochen-Wang409/PairUni.

## Metadata
- venue: arXiv
- year: 2025
- authors: Jiani Zheng, Zhiyang Teng, Kunpeng Qiu, Xiangtai Li, Anran Wang, Yu Tian, Ye Tian, Haochen Wang, Zhuochen Wang
- arxiv_id: 2510.25682
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.25682v3
- published: 2025-10-29
