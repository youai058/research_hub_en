---
title: "Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning"
authors: ["Lang Feng", "Weihao Tan", "Zhiyi Lyu", "Longtao Zheng", "Haiyang Xu", "Ming Yan", "Fei Huang", "Bo An"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "H76PMm7hf2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/79d7c13badf6250286deb9e558c99bb7b0f69a20.pdf"
published: "2025"
categories: []
keywords: ["vision-language model", "agent", "reinforcement learning", "online fine-tuning", "counterfactual"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:12+09:00"
---

# Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning

## Abstract
Online fine-tuning vision-language model (VLM) agents with reinforcement learning (RL) has shown promise for equipping agents with multi-step, goal-oriented capabilities in dynamic environments. However, their open-ended textual action space and non-end-to-end nature of action generation present significant challenges to effective online exploration in RL, e.g., explosion of the exploration space. We propose a novel online fine-tuning method, Counterfactual Soft Reinforcement Learning (CoSo), better suited to the textual output space of VLM agents. Compared to prior methods that assign uniform uncertainty to all tokens, CoSo leverages counterfactual reasoning to dynamically assess the causal influence of individual tokens on post-processed actions. By prioritizing the exploration of action-critical tokens while reducing the impact of semantically redundant or low-impact tokens, CoSo enables a more targeted and efficient online rollout process. We provide theoretical analysis proving CoSo's convergence and policy improvement guarantees, and extensive empirical evaluations supporting CoSo's effectiveness. Our results across a diverse set of agent tasks, including Android device control, card gaming, and embodied AI, highlight its remarkable ability to enhance exploration efficiency and deliver consistent performance gains. The code is available at https://github.com/langfengQ/CoSo.

## Metadata
- venue: ICML
- year: 2025
- authors: Lang Feng, Weihao Tan, Zhiyi Lyu, Longtao Zheng, Haiyang Xu, Ming Yan, Fei Huang, Bo An
- arxiv_id: 
- openreview_id: H76PMm7hf2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/79d7c13badf6250286deb9e558c99bb7b0f69a20.pdf
- published: 2025
- keywords: vision-language model, agent, reinforcement learning, online fine-tuning, counterfactual
