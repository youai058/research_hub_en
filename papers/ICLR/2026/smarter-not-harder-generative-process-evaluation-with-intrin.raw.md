---
title: "Smarter Not Harder: Generative Process Evaluation with Intrinsic-Signal Driving and Ability‑Adaptive Reward Shaping"
authors: ["Tao He", "Rongchuan Mu", "Lizi Liao", "Yixin Cao", "Yang Li", "Yijia Luo", "Weixun Wang", "Ming Liu", "Bing Qin"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LZZENDlZt9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/bdaf86ddfadfffafab5c3375607b7c7b339e003f.pdf"
published: "2026"
categories: []
keywords: ["Generative Process Reward Model", "Math Reasoning", "Large Reasoning Model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:40+09:00"
---

# Smarter Not Harder: Generative Process Evaluation with Intrinsic-Signal Driving and Ability‑Adaptive Reward Shaping

## Abstract
Large reasoning models (LRMs) have shown strong performance in complex mathematical reasoning when optimized via reinforcement learning (RL). However, conventional outcome-only reward provides sparse feedback, leading to inefficient optimization. In this work, we investigate whether generative process reward models (GenPRMs) can accelerate RL training of LRMs by improving the utilization of reasoning trajectories. We first analyze critical limitations in existing GenPRMs, including their heavy reliance on reasoning ability during correctness judgment, and suppression of exploration as well as vulnerability to reward hacking during reward assignment. To address these limitations, we first propose a novel \textbf{intrinsic-signal-driven evaluation} mechanism, which judges reasoning steps using semantic cues from the solution, thus mitigating extensive dependence on GenPRM. Furthermore, we (i) adopt \textbf{thought-level rewarding granularity} to alleviate over-dense step rewards, and (ii) design a \textbf{difficulty-aware reward formulation} that dynamically balances exploration and exploitation and keeping the optimization target of key tokens to mitigate reward hacking. We integrate these innovations into the process reward-based GRPO, resulting in the proposed \textbf{TP-GRPO} algorithm. Experiments on LRMs with 1.5B and 7B parameters show that TP-GRPO achieves higher improvements while using significantly fewer training samples, and more analyses further confirm the effectiveness of our proposed process evaluation mechanism.

## Metadata
- venue: ICLR
- year: 2026
- authors: Tao He, Rongchuan Mu, Lizi Liao, Yixin Cao, Yang Li, Yijia Luo, Weixun Wang, Ming Liu, Bing Qin
- arxiv_id: 
- openreview_id: LZZENDlZt9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/bdaf86ddfadfffafab5c3375607b7c7b339e003f.pdf
- published: 2026
- keywords: Generative Process Reward Model, Math Reasoning, Large Reasoning Model
