---
title: "Co-GRPO: Co-Optimized Group Relative Policy Optimization for Masked Diffusion Model"
authors: ["Renping Zhou", "Zanlin Ni", "Tianyi Chen", "Zeyu Liu", "Yang Yue", "Yulin Wang", "Yuxuan Wang", "Jingshu Liu", "Gao Huang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.22288"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.22288v1"
published: "2025-12-25"
categories: ["cs.LG", "cs.AI", "cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# Co-GRPO: Co-Optimized Group Relative Policy Optimization for Masked Diffusion Model

## Abstract
Recently, Masked Diffusion Models (MDMs) have shown promising potential across vision, language, and cross-modal generation. However, a notable discrepancy exists between their training and inference procedures. In particular, MDM inference is a multi-step, iterative process governed not only by the model itself but also by various schedules that dictate the token-decoding trajectory (e.g., how many tokens to decode at each step). In contrast, MDMs are typically trained using a simplified, single-step BERT-style objective that masks a subset of tokens and predicts all of them simultaneously. This step-level simplification fundamentally disconnects the training paradigm from the trajectory-level nature of inference, leaving the inference schedules never optimized during training. In this paper, we introduce Co-GRPO, which reformulates MDM generation as a unified Markov Decision Process (MDP) that jointly incorporates both the model and the inference schedule. By applying Group Relative Policy Optimization at the trajectory level, Co-GRPO cooperatively optimizes model parameters and schedule parameters under a shared reward, without requiring costly backpropagation through the multi-step generation process. This holistic optimization aligns training with inference more thoroughly and substantially improves generation quality. Empirical results across four benchmarks-ImageReward, HPS, GenEval, and DPG-Bench-demonstrate the effectiveness of our approach. For more details, please refer to our project page: https://co-grpo.github.io/ .

## Metadata
- venue: arXiv
- year: 2025
- authors: Renping Zhou, Zanlin Ni, Tianyi Chen, Zeyu Liu, Yang Yue, Yulin Wang, Yuxuan Wang, Jingshu Liu, Gao Huang
- arxiv_id: 2512.22288
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.22288v1
- published: 2025-12-25
