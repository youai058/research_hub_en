---
title: "Towards Robust Model-Based Reinforcement Learning Against Adversarial Corruption"
authors: ["Chenlu Ye", "Jiafan He", "Quanquan Gu", "Tong Zhang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Z0S6fUdW68"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1940f283c26aa0f48f467412305f45e8ace706c4.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:15+09:00"
---

# Towards Robust Model-Based Reinforcement Learning Against Adversarial Corruption

## Abstract
This study tackles the challenges of adversarial corruption in model-based reinforcement learning (RL), where the transition dynamics can be corrupted by an adversary. Existing studies on corruption-robust RL mostly focus on the setting of model-free RL, where robust least-square regression is often employed for value function estimation. However, these techniques cannot be directly applied to model-based RL. In this paper, we focus on model-based RL and take the maximum likelihood estimation (MLE) approach to learn transition model. Our work encompasses both online and offline settings. In the online setting, we introduce an algorithm called corruption-robust optimistic MLE (CR-OMLE), which leverages total-variation (TV)-based information ratios as uncertainty weights for MLE. We prove that CR-OMLE achieves a regret of $\tilde{\mathcal{O}}(\sqrt{T} + C)$, where $C$ denotes the cumulative corruption level after $T$ episodes. We also prove a lower bound to show that the additive dependence on $C$ is optimal. We extend our weighting technique to the offline setting, and propose an algorithm named corruption-robust pessimistic MLE (CR-PMLE). Under a uniform coverage condition, CR-PMLE exhibits suboptimality worsened by $\mathcal{O}(C/n)$, nearly matching the lower bound. To the best of our knowledge, this is the first work on corruption-robust model-based RL algorithms with provable guarantees.

## Metadata
- venue: ICML
- year: 2024
- authors: Chenlu Ye, Jiafan He, Quanquan Gu, Tong Zhang
- arxiv_id: 
- openreview_id: Z0S6fUdW68
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1940f283c26aa0f48f467412305f45e8ace706c4.pdf
- published: 2024
