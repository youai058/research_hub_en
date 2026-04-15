---
title: "Why DPO is a Misspecified Estimator and How to Fix It"
authors: ["Aditya Gopalan", "Sayak Ray Chowdhury", "Debangshu Banerjee"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "btEiAfnLsX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5c45c14f190e28a365715ec84148dede578815e9.pdf"
published: "2026"
categories: []
keywords: ["Direct Preference Optimization", "Reinforcement Learning", "Reinforcement learning with human feedback"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:37+09:00"
---

# Why DPO is a Misspecified Estimator and How to Fix It

## Abstract
Direct alignment algorithms such as Direct Preference Optimization (DPO) fine-tune models based on preference data, using only supervised learning instead of two-stage reinforcement learning with human feedback (RLHF). We show that DPO encodes a statistical estimation problem over reward functions induced by a parametric policy class. When the true reward function that generates preferences cannot be realized via the policy class, DPO becomes misspecified, resulting in failure modes such as preference order reversal, worsening of policy reward, and high sensitivity to the input preference data distribution. On the other hand, we study the local behavior of two-stage RLHF for a parametric class and relate it to a natural gradient step in policy space.  Our fine-grained geometric characterization allows us to propose AuxDPO, which introduces additional auxiliary variables in the DPO loss function to help move towards the RLHF solution in a principled manner and mitigate the misspecification in DPO. We empirically demonstrate the superior performance of AuxDPO on didactic bandit settings as well as LLM alignment tasks.

## Metadata
- venue: ICLR
- year: 2026
- authors: Aditya Gopalan, Sayak Ray Chowdhury, Debangshu Banerjee
- arxiv_id: 
- openreview_id: btEiAfnLsX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5c45c14f190e28a365715ec84148dede578815e9.pdf
- published: 2026
- keywords: Direct Preference Optimization, Reinforcement Learning, Reinforcement learning with human feedback
