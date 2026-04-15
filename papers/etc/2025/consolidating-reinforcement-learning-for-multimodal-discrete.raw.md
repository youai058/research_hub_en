---
title: "Consolidating Reinforcement Learning for Multimodal Discrete Diffusion Models"
authors: ["Tianren Ma", "Mu Zhang", "Yibing Wang", "Qixiang Ye"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.02880"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.02880v1"
published: "2025-10-03"
categories: ["cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:40+09:00"
---

# Consolidating Reinforcement Learning for Multimodal Discrete Diffusion Models

## Abstract
Optimizing discrete diffusion model (DDM) with rewards remains a challenge: the non-autoregressive paradigm makes importance sampling intractable and rollout complex, puzzling reinforcement learning methods such as Group Relative Policy Optimization (GRPO). In this study, we introduce MaskGRPO, the first viable approach to enable scalable multimodal reinforcement learning in discrete diffusion with effective importance sampling and modality-specific adaptations. To this end, we first clarify the theoretical foundation for DDMs, which facilitates building an importance estimator that captures valuable token fluctuation for gradient updates. We then delicately tailored the rollout method for visual sequences, which yields diverse completions and reliable optimization gradients. Upon math reasoning, coding, and visual generation benchmarks, MaskGRPO brings more stable and efficient updates, leading to stronger reasoning performance and better generation quality. This study establishes MaskGRPO as a systematic policy optimization approach and the first practical way for discretized visual diffusion.

## Metadata
- venue: arXiv
- year: 2025
- authors: Tianren Ma, Mu Zhang, Yibing Wang, Qixiang Ye
- arxiv_id: 2510.02880
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.02880v1
- published: 2025-10-03
