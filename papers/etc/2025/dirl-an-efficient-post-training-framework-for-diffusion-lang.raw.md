---
title: "DiRL: An Efficient Post-Training Framework for Diffusion Language Models"
authors: ["Ying Zhu", "Jiaxin Wan", "Xiaoran Liu", "Siyang He", "Qiqi Wang", "Xu Guo", "Tianyi Liang", "Zengfeng Huang", "Ziwei He", "Xipeng Qiu"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.22234"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.22234v2"
published: "2025-12-23"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# DiRL: An Efficient Post-Training Framework for Diffusion Language Models

## Abstract
Diffusion Language Models (dLLMs) have emerged as promising alternatives to Auto-Regressive (AR) models. While recent efforts have validated their pre-training potential and accelerated inference speeds, the post-training landscape for dLLMs remains underdeveloped. Existing methods suffer from computational inefficiency and objective mismatches between training and inference, severely limiting performance on complex reasoning tasks such as mathematics. To address this, we introduce DiRL, an efficient post-training framework that tightly integrates FlexAttention-accelerated blockwise training with LMDeploy-optimized inference. This architecture enables a streamlined online model update loop, facilitating efficient two-stage post-training (Supervised Fine-Tuning followed by Reinforcement Learning). Building on this framework, we propose DiPO, the first unbiased Group Relative Policy Optimization (GRPO) implementation tailored for dLLMs. We validate our approach by training DiRL-8B-Instruct on high-quality math data. Our model achieves state-of-the-art math performance among dLLMs and surpasses comparable models in the Qwen2.5 series on several benchmarks.

## Metadata
- venue: arXiv
- year: 2025
- authors: Ying Zhu, Jiaxin Wan, Xiaoran Liu, Siyang He, Qiqi Wang, Xu Guo, Tianyi Liang, Zengfeng Huang, Ziwei He, Xipeng Qiu
- arxiv_id: 2512.22234
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.22234v2
- published: 2025-12-23
