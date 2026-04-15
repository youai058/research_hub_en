---
title: "Count Counts: Motivating Exploration in LLM Reasoning with Count-based Intrinsic Rewards"
authors: ["Xuan Zhang", "Ruixiao Li", "Zhijian Zhou", "Long Li", "Yulei Qin", "Ke Li", "Xing Sun", "Xiaoyu Tan", "Chao Qu", "Yuan Qi"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9xIBbfItGP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2772f03dcb5a597e116e66e419e7d288b6af3d99.pdf"
published: "2026"
categories: []
keywords: ["Large Language Models", "Reinforcement Learning", "Natural Language Reasoning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:38+09:00"
---

# Count Counts: Motivating Exploration in LLM Reasoning with Count-based Intrinsic Rewards

## Abstract
Reinforcement Learning (RL) has become a compelling way to strengthen the multi step reasoning ability of Large Language Models (LLMs). However, prevalent RL paradigms still lean on sparse outcome-based rewards and limited exploration, which often drives LLMs toward repetitive and suboptimal reasoning patterns. In this paper, we study the central question of how to design exploration for LLM reasoning and introduce MERCI (Motivating Exploration in LLM Reasoning with Count-based Intrinsic Rewards), a novel RL algorithm that augments policy optimization with a principled intrinsic reward. Building on the idea of count-based exploration, MERCI leverages a lightweight Coin Flipping Network (CFN) to estimate the pseudo count and further epistemic uncertainty over reasoning trajectories, and converts them into an intrinsic reward that values novelty while preserving the learning signal from task rewards. We integrate MERCI into some advanced RL frameworks like Group Relative Policy Optimization (GRPO). Experiments on complex reasoning benchmarks demonstrate that MERCI encourages richer and more varied chains of thought, significantly improves performance over strong baselines, and helps the policy escape local routines to discover better solutions. It indicates that our targeted intrinsic motivation can make exploration reliable for language model reasoning.

## Metadata
- venue: ICLR
- year: 2026
- authors: Xuan Zhang, Ruixiao Li, Zhijian Zhou, Long Li, Yulei Qin, Ke Li, Xing Sun, Xiaoyu Tan, Chao Qu, Yuan Qi
- arxiv_id: 
- openreview_id: 9xIBbfItGP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2772f03dcb5a597e116e66e419e7d288b6af3d99.pdf
- published: 2026
- keywords: Large Language Models, Reinforcement Learning, Natural Language Reasoning
