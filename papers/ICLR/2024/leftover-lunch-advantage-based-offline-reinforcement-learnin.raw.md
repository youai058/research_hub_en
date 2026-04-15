---
title: "Leftover Lunch: Advantage-based Offline Reinforcement Learning for Language Models"
authors: ["Ashutosh Baheti", "Ximing Lu", "Faeze Brahman", "Ronan Le Bras", "Maarten Sap", "Mark Riedl"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ZDGKPbF0VQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/12ee80d1f10cff1b285c1198d93c7a1190f0dac3.pdf"
published: "2024"
categories: []
keywords: ["Reinforcement Learning", "Natural Language Generation", "Offline Policy Gradients"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:05+09:00"
---

# Leftover Lunch: Advantage-based Offline Reinforcement Learning for Language Models

## Abstract
Reinforcement Learning with Human Feedback (RLHF) is the most prominent method for Language Model (LM) alignment. However, RLHF is an unstable and data-hungry process that continually requires new high-quality LM-generated data for finetuning. We introduce Advantage-Leftover Lunch RL (A-LoL), a new class of offline policy gradient algorithms that enable RL training on any pre-existing data. By assuming the entire LM output sequence as a single action, A-LoL allows incorporating sequence-level classifiers or human-designed scoring functions as
rewards. Subsequently, by using LM’s value estimate, A-LoL only trains on positive advantage (leftover) data points, making it resilient to noise. Overall, A-LoL is an easy-to-implement, sample-efficient, and stable LM training recipe.

We demonstrate the effectiveness of A-LoL and its variants with a set of four different language generation tasks. We compare against both online RL (PPO) and recent preference-based (DPO, PRO) and reward-based (GOLD) offline RL baselines. On the commonly-used RLHF benchmark, Helpful and Harmless Assistant (HHA), LMs trained with A-LoL methods achieve the highest diversity while also being rated more safe and helpful than the baselines according to humans. Additionally, in the remaining three tasks, A-LoL could optimize multiple distinct reward functions even when using noisy or suboptimal training data.

## Metadata
- venue: ICLR
- year: 2024
- authors: Ashutosh Baheti, Ximing Lu, Faeze Brahman, Ronan Le Bras, Maarten Sap, Mark Riedl
- arxiv_id: 
- openreview_id: ZDGKPbF0VQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/12ee80d1f10cff1b285c1198d93c7a1190f0dac3.pdf
- published: 2024
- keywords: Reinforcement Learning, Natural Language Generation, Offline Policy Gradients
