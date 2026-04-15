---
title: "Potentially Optimal Joint Actions Recognition for Cooperative Multi-Agent Reinforcement Learning"
authors: ["Chang Huang", "Shatong Zhu", "Junqiao Zhao", "Hongtu Zhou", "Hai Zhang", "Di Zhang", "Chen Ye", "Ziqiao Wang", "Guang Chen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "YQ1muQBDV4"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/987163834e0ac94a36fabbea5c4008b45d9ad83f.pdf"
published: "2026"
categories: []
keywords: ["Reinforcement Learning", "Value function factorization", "Multi-Agent"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:32+09:00"
---

# Potentially Optimal Joint Actions Recognition for Cooperative Multi-Agent Reinforcement Learning

## Abstract
Value function factorization is widely used in cooperative multi-agent reinforcement learning (MARL).
Existing approaches often impose monotonicity constraints between the joint action value and individual action values to enable decentralized execution.
However, such constraints limit the expressiveness of value factorization, restricting the range of joint action values that can be represented and hindering the learning of optimal policies.
To address this, we propose Potentially Optimal Joint Actions Weighting (POW), a method that ensures optimal policy recovery where existing approximate weighting strategies may fail.
POW iteratively identifies potentially optimal joint actions and assigns them higher training weights through a theoretically grounded iterative weighted training process. We prove that this mechanism guarantees recovery of the true optimal policy, overcoming the limitations of prior heuristic weighting strategies.
POW is architecture-agnostic and can be seamlessly integrated into existing value factorization algorithms.
Extensive experiments on matrix games, difficulty-enhanced predator-prey tasks, SMAC, SMACv2, and a highway-env intersection scenario show that POW substantially improves stability and consistently surpasses state-of-the-art value-based MARL methods.

## Metadata
- venue: ICLR
- year: 2026
- authors: Chang Huang, Shatong Zhu, Junqiao Zhao, Hongtu Zhou, Hai Zhang, Di Zhang, Chen Ye, Ziqiao Wang, Guang Chen
- arxiv_id: 
- openreview_id: YQ1muQBDV4
- anthology_id: 
- pdf_url: https://openreview.net/pdf/987163834e0ac94a36fabbea5c4008b45d9ad83f.pdf
- published: 2026
- keywords: Reinforcement Learning, Value function factorization, Multi-Agent
