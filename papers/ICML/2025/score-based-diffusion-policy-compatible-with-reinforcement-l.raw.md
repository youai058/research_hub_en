---
title: "Score-Based Diffusion Policy Compatible with Reinforcement Learning via Optimal Transport"
authors: ["Mingyang Sun", "Pengxiang Ding", "Weinan Zhang", "Donglin Wang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2dqiqST8ZJ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/042a98250460febe9fae9f9da4096061b506dbf1.pdf"
published: "2025"
categories: []
keywords: ["Diffusion Policy", "Reinforcement Learning", "Optimal Transport"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:16+09:00"
---

# Score-Based Diffusion Policy Compatible with Reinforcement Learning via Optimal Transport

## Abstract
Diffusion policies have shown promise in learning complex behaviors from demonstrations, particularly for tasks requiring precise control and long-term planning. However, they face challenges in robustness when encountering distribution shifts. This paper explores improving diffusion-based imitation learning models through online interactions with the environment. We propose OTPR (Optimal Transport-guided score-based diffusion Policy for Reinforcement learning fine-tuning), a novel method that integrates diffusion policies with RL using optimal transport theory. OTPR leverages the Q-function as a transport cost and views the policy as an optimal transport map, enabling efficient and stable fine-tuning. Moreover, we introduce masked optimal transport to guide state-action matching using expert keypoints and a compatibility-based resampling strategy to enhance training stability. Experiments on three simulation tasks demonstrate OTPR's superior performance and robustness compared to existing methods, especially in complex and sparse-reward environments. In sum, OTPR provides an effective framework for combining IL and RL, achieving versatile and reliable policy learning.

## Metadata
- venue: ICML
- year: 2025
- authors: Mingyang Sun, Pengxiang Ding, Weinan Zhang, Donglin Wang
- arxiv_id: 
- openreview_id: 2dqiqST8ZJ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/042a98250460febe9fae9f9da4096061b506dbf1.pdf
- published: 2025
- keywords: Diffusion Policy, Reinforcement Learning, Optimal Transport
