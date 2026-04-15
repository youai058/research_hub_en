---
title: "Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards"
authors: ["Hieu Trung Nguyen", "Bao Nguyen", "Wenao Ma", "Yuzhi Zhao", "Ruifeng She", "Viet Anh Nguyen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Z5sWYACAop"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6ee2f705eef5b4d7169297beb7748db19ab85413.pdf"
published: "2026"
categories: []
keywords: ["Reinforcement Learning", "Reinforcement Learning from Verifiable Rewards", "Resource Allocation", "Large Language model post training"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:33+09:00"
---

# Adaptive Rollout Allocation for Online Reinforcement Learning with Verifiable Rewards

## Abstract
Sampling efficiency is a key bottleneck in reinforcement learning with verifiable rewards. Existing group-based policy optimization methods, such as GRPO, allocate a fixed number of rollouts for all training prompts. This uniform allocation implicitly treats all prompts as equally informative, and could lead to inefficient computational budget usage and impede training progress. We introduce VIP, a Variance-Informed Predictive allocation strategy that allocates a given rollout budget to the prompts in the incumbent batch to minimize the expected gradient variance of the policy update. At each iteration, VIP uses a lightweight Gaussian process model to predict per-prompt success probabilities based on recent rollouts. These probability predictions are translated into variance estimates, which are then fed into a convex optimization problem to determine the optimal rollout allocations under a hard compute budget constraint. Empirical results show that VIP consistently improves sampling efficiency and achieves higher performance than uniform or heuristic allocation strategies in multiple benchmarks.

## Metadata
- venue: ICLR
- year: 2026
- authors: Hieu Trung Nguyen, Bao Nguyen, Wenao Ma, Yuzhi Zhao, Ruifeng She, Viet Anh Nguyen
- arxiv_id: 
- openreview_id: Z5sWYACAop
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6ee2f705eef5b4d7169297beb7748db19ab85413.pdf
- published: 2026
- keywords: Reinforcement Learning, Reinforcement Learning from Verifiable Rewards, Resource Allocation, Large Language model post training
