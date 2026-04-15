---
title: "Robot-Gated Interactive Imitation Learning with Adaptive Intervention Mechanism"
authors: ["Haoyuan Cai", "Zhenghao Peng", "Bolei Zhou"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "TC1sQg5z0T"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2d69f8e47d89e3b4def482200fa47dd038d8586f.pdf"
published: "2025"
categories: []
keywords: ["Imitation Learning", "Human-in-the-loop Reinforcement Learning", "Shared Autonomy"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:34+09:00"
---

# Robot-Gated Interactive Imitation Learning with Adaptive Intervention Mechanism

## Abstract
Interactive Imitation Learning (IIL) allows agents to acquire desired behaviors through human interventions, but current methods impose high cognitive demands on human supervisors. We propose the Adaptive Intervention Mechanism (AIM), a novel robot-gated IIL algorithm that learns an adaptive criterion for requesting human demonstrations. AIM utilizes a proxy Q-function to mimic the human intervention rule and adjusts intervention requests based on the alignment between agent and human actions. By assigning high Q-values when the agent deviates from the expert and decreasing these values as the agent becomes proficient, the proxy Q-function enables the agent to assess the real-time alignment with the expert and request assistance when needed. Our expert-in-the-loop experiments reveal that AIM significantly reduces expert monitoring efforts in both continuous and discrete control tasks. Compared to the uncertainty-based baseline Thrifty-DAgger, our method achieves a 40% improvement in terms of human take-over cost and learning efficiency.
Furthermore, AIM effectively identifies safety-critical states for expert assistance, thereby collecting higher-quality expert demonstrations and reducing overall expert data and environment interactions needed. Code and demo video are available at https://github.com/metadriverse/AIM.

## Metadata
- venue: ICML
- year: 2025
- authors: Haoyuan Cai, Zhenghao Peng, Bolei Zhou
- arxiv_id: 
- openreview_id: TC1sQg5z0T
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2d69f8e47d89e3b4def482200fa47dd038d8586f.pdf
- published: 2025
- keywords: Imitation Learning, Human-in-the-loop Reinforcement Learning, Shared Autonomy
