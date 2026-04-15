---
title: "dVLM-AD: Enhance Diffusion Vision-Language-Model for Driving via Controllable Reasoning"
authors: ["Yingzi Ma", "Yulong Cao", "Wenhao Ding", "Shuibai Zhang", "Yan Wang", "Boris Ivanovic", "Ming Jiang", "Marco Pavone", "Chaowei Xiao"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.04459"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.04459v1"
published: "2025-12-04"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:33+09:00"
---

# dVLM-AD: Enhance Diffusion Vision-Language-Model for Driving via Controllable Reasoning

## Abstract
The autonomous driving community is increasingly focused on addressing the challenges posed by out-of-distribution (OOD) driving scenarios. A dominant research trend seeks to enhance end-to-end (E2E) driving systems by integrating vision-language models (VLMs), leveraging their rich world knowledge and reasoning abilities to improve generalization across diverse environments. However, most existing VLMs or vision-language agents (VLAs) are built upon autoregressive (AR) models. In this paper, we observe that existing AR-based VLMs -- limited by causal attention and sequential token generation -- often fail to maintain consistency and controllability between high-level reasoning and low-level planning. In contrast, recent discrete diffusion VLMs equipped with bidirectional attention exhibit superior controllability and reliability through iterative denoising. Building on these observations, we introduce dVLM-AD, a diffusion-based vision-language model that unifies perception, structured reasoning, and low-level planning for end-to-end driving. Evaluated on nuScenes and WOD-E2E, dVLM-AD yields more consistent reasoning-action pairs and achieves planning performance comparable to existing driving VLM/VLA systems despite a modest backbone, outperforming AR-based baselines with a 9 percent improvement in behavior-trajectory consistency and a 6 percent increase in RFS on long-tail WOD-E2E scenarios. These results suggest a controllable and reliable pathway for scalable end-to-end driving.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yingzi Ma, Yulong Cao, Wenhao Ding, Shuibai Zhang, Yan Wang, Boris Ivanovic, Ming Jiang, Marco Pavone, Chaowei Xiao
- arxiv_id: 2512.04459
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.04459v1
- published: 2025-12-04
