---
title: "FIRE: Frobenius-Isometry Reinitialization for Balancing the Stability–Plasticity Tradeoff"
authors: ["Isaac Han", "Sangyeon Park", "Seungwon Oh", "Donghu Kim", "Hojoon Lee", "KyungJoong Kim"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CfZLxT3zIZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0544dbe6129a410f81e3b6f56205708832cd664b.pdf"
published: "2026"
categories: []
keywords: ["stability-plasticity tradeoff", "continual learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:32+09:00"
---

# FIRE: Frobenius-Isometry Reinitialization for Balancing the Stability–Plasticity Tradeoff

## Abstract
Deep neural networks trained on nonstationary data must balance stability (i.e., retaining prior knowledge) and plasticity (i.e., adapting to new tasks). Standard reinitialization methods, which reinitialize weights toward their original values, are widely used but difficult to tune: conservative reinitializations fail to restore plasticity, while aggressive ones erase useful knowledge. We propose FIRE, a principled reinitialization method that explicitly balances the stability–plasticity tradeoff. FIRE quantifies stability through Squared Frobenius Error (SFE), measuring proximity to past weights, and plasticity through Deviation from Isometry (DfI), reflecting weight isotropy. The reinitialization point is obtained by solving a constrained optimization problem, minimizing SFE subject to DfI being zero, which is efficiently approximated by Newton–Schulz iteration. FIRE is evaluated on continual visual learning (CIFAR-10 with ResNet-18), language modeling (OpenWebText with GPT-0.1B), and reinforcement learning (HumanoidBench with SAC and Atari games with DQN). Across all domains, FIRE consistently outperforms both naive training without intervention and standard reinitialization methods, demonstrating effective balancing of the stability–plasticity tradeoff.

## Metadata
- venue: ICLR
- year: 2026
- authors: Isaac Han, Sangyeon Park, Seungwon Oh, Donghu Kim, Hojoon Lee, KyungJoong Kim
- arxiv_id: 
- openreview_id: CfZLxT3zIZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0544dbe6129a410f81e3b6f56205708832cd664b.pdf
- published: 2026
- keywords: stability-plasticity tradeoff, continual learning
