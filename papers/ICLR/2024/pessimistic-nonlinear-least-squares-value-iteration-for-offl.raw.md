---
title: "Pessimistic Nonlinear Least-Squares Value Iteration for Offline Reinforcement Learning"
authors: ["Qiwei Di", "Heyang Zhao", "Jiafan He", "Quanquan Gu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4kLVvIh8cp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/eccb6a13ad39f4a83f32bd2e74f2359e20086e81.pdf"
published: "2024"
categories: []
keywords: ["Offline reinforcement learning", "instance-dependent", "least-squares value iteration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:04+09:00"
---

# Pessimistic Nonlinear Least-Squares Value Iteration for Offline Reinforcement Learning

## Abstract
Offline reinforcement learning (RL), where the agent aims to learn the optimal policy based on the data collected by a behavior policy, has attracted increasing attention in recent years. While offline RL with linear function approximation has been extensively studied with optimal results achieved under certain assumptions, many works shift their interest to offline RL with non-linear function approximation.
However, limited works on offline RL with non-linear function approximation have instance-dependent regret guarantees.
    In this paper, we propose an oracle-efficient algorithm, dubbed Pessimistic Nonlinear Least-Square Value Iteration (PNLSVI), for offline RL with non-linear function approximation. Our algorithmic design comprises three innovative components: (1) a variance-based weighted regression scheme that can be applied to a wide range of function classes, (2) a subroutine for variance estimation, and (3) a planning phase that utilizes a pessimistic value iteration approach. Our algorithm enjoys a regret bound that has a tight dependency on the function class complexity and achieves minimax optimal instance-dependent regret when specialized to linear function approximation. Our work extends the previous instance-dependent results within simpler function classes, such as linear and differentiable function to a more general framework. To the best of our knowledge, this is the first statistically optimal algorithm for nonlinear offline RL.

## Metadata
- venue: ICLR
- year: 2024
- authors: Qiwei Di, Heyang Zhao, Jiafan He, Quanquan Gu
- arxiv_id: 
- openreview_id: 4kLVvIh8cp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/eccb6a13ad39f4a83f32bd2e74f2359e20086e81.pdf
- published: 2024
- keywords: Offline reinforcement learning, instance-dependent, least-squares value iteration
