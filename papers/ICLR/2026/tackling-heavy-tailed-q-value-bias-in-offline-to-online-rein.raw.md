---
title: "Tackling Heavy-Tailed Q-Value Bias in Offline-to-Online Reinforcement Learning with Laplace-Robust Modeling"
authors: ["Ruibo Guo", "Lei Liu", "Rui Yang", "Junjie Shen", "Guoping Wu", "Jie Wang", "Bin Li"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "I7UK5qHNBL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/478f6c5bdf2901be124811958e0f59d51b15a793.pdf"
published: "2026"
categories: []
keywords: ["Reinforcement Learning", "Offline-to-Online", "Q-value Estimation", "Laplace Distribution"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:43+09:00"
---

# Tackling Heavy-Tailed Q-Value Bias in Offline-to-Online Reinforcement Learning with Laplace-Robust Modeling

## Abstract
Offline-to-online reinforcement learning (O2O RL) aims to improve the performance of offline pretrained agents through online fine-tuning. Existing O2O RL methods have achieved advances in mitigating the overestimation of Q-value biases (i.e., biases of cumulative rewards), improving the performance. However, in this paper, we are the first to reveal that Q-value biases of these methods often follow a heavy-tailed distribution during online fine-tuning. Such biases induce high estimation variance and hinder performance improvement.
To address this challenge, we propose a Laplace-based robust offline-to-online RL (LAROO) approach. LAROO introduces a parameterized Laplace-distributed noise and transfers the heavy-tailed nature of Q-value biases into this noise, alleviating heavy tailedness of biases for training stability and performance improvement. Specifically, (1) since Laplace distribution is well-suited for modeling heavy-tailed data, LAROO introduces a parameterized Laplace-distributed noise that can adaptively capture heavy tailedness of any data. (2) By combining estimated Q-values with the noise to approximate true Q-values, LAROO transfers the heavy-tailed nature of biases into the noise, reducing estimation variance. (3) LAROO employs conservative ensemble-based estimates to re-center Q-value biases, shifting their mean towards zero. Based on (2) and (3), LAROO promotes heavy-tailed Q-value biases into a standardized form, improving training stability and performance. Extensive experiments demonstrate that LAROO achieves significant performance improvement, outperforming several state-of-the-art O2O RL baselines.

## Metadata
- venue: ICLR
- year: 2026
- authors: Ruibo Guo, Lei Liu, Rui Yang, Junjie Shen, Guoping Wu, Jie Wang, Bin Li
- arxiv_id: 
- openreview_id: I7UK5qHNBL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/478f6c5bdf2901be124811958e0f59d51b15a793.pdf
- published: 2026
- keywords: Reinforcement Learning, Offline-to-Online, Q-value Estimation, Laplace Distribution
