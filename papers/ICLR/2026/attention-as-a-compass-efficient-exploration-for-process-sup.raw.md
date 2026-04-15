---
title: "Attention as a Compass: Efficient Exploration for Process-Supervised RL in Reasoning Models"
authors: ["Runze Liu", "Jiakang Wang", "Yuling Shi", "Zhihui Xie", "Chenxin An", "Kaiyan Zhang", "Jian Zhao", "Xiaodong Gu", "Lei Lin", "Wenping Hu", "Xiu Li", "Fuzheng Zhang", "Guorui Zhou", "Kun Gai"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "NCN8oUsiNf"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4b7c57c5da8e0b71a807cf5a7980a1f390c0daec.pdf"
published: "2026"
categories: []
keywords: ["Large Language Model", "Reinforcement Learning", "Process Supervision"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:37+09:00"
---

# Attention as a Compass: Efficient Exploration for Process-Supervised RL in Reasoning Models

## Abstract
Reinforcement Learning (RL) has shown remarkable success in enhancing the reasoning capabilities of Large Language Models (LLMs). Process-Supervised RL (PSRL) has emerged as a more effective paradigm compared to outcome-based RL. However, existing PSRL approaches suffer from limited exploration efficiency, both in terms of branching positions and sampling. In this paper, we introduce a novel PSRL framework (AttnRL), which enables efficient exploration for reasoning models. Motivated by preliminary observations that steps exhibiting high attention scores correlate with reasoning behaviors, we propose to branch from positions with high values. Furthermore, we develop an adaptive sampling strategy that accounts for problem difficulty and historical batch size, ensuring that the whole training batch maintains non-zero advantage values. To further improve sampling efficiency, we design a one-step off-policy training pipeline for PSRL. Extensive experiments on multiple challenging mathematical reasoning benchmarks demonstrate that our method consistently outperforms prior approaches in terms of performance and sampling and training efficiency. Our code is available at https://github.com/RyanLiu112/AttnRL.

## Metadata
- venue: ICLR
- year: 2026
- authors: Runze Liu, Jiakang Wang, Yuling Shi, Zhihui Xie, Chenxin An, Kaiyan Zhang, Jian Zhao, Xiaodong Gu, Lei Lin, Wenping Hu, Xiu Li, Fuzheng Zhang, Guorui Zhou, Kun Gai
- arxiv_id: 
- openreview_id: NCN8oUsiNf
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4b7c57c5da8e0b71a807cf5a7980a1f390c0daec.pdf
- published: 2026
- keywords: Large Language Model, Reinforcement Learning, Process Supervision
