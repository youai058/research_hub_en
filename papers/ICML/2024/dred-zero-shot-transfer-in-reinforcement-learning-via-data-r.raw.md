---
title: "DRED: Zero-Shot Transfer in Reinforcement Learning via Data-Regularised Environment Design"
authors: ["Samuel Garcin", "James Doran", "Shangmin Guo", "Christopher G. Lucas", "Stefano V Albrecht"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uku9r6RROl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f34fcc9854db1d72042056e9eefe23794f54cb3f.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:49+09:00"
---

# DRED: Zero-Shot Transfer in Reinforcement Learning via Data-Regularised Environment Design

## Abstract
Autonomous agents trained using deep reinforcement learning (RL) often lack the ability to successfully generalise to new environments, even when these environments share characteristics with the ones they have encountered during training. In this work, we investigate how the sampling of individual environment instances, or levels, affects the zero-shot generalisation (ZSG) ability of RL agents. We discover that, for deep actor-critic architectures sharing their base layers, prioritising levels according to their value loss minimises the mutual information between the agent's internal representation and the set of training levels in the generated training data. This provides a novel theoretical justification for the regularisation achieved by certain adaptive sampling strategies. We then turn our attention to unsupervised environment design (UED) methods, which assume control over level generation. We find that existing UED methods can significantly shift the training distribution, which translates to low ZSG performance. To prevent both overfitting and distributional shift, we introduce *data-regularised environment design* (DRED). DRED generates levels using a generative model trained to approximate the ground truth distribution of an initial set of level parameters. Through its grounding, DRED achieves significant improvements in ZSG over adaptive level sampling strategies and UED methods.

## Metadata
- venue: ICML
- year: 2024
- authors: Samuel Garcin, James Doran, Shangmin Guo, Christopher G. Lucas, Stefano V Albrecht
- arxiv_id: 
- openreview_id: uku9r6RROl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f34fcc9854db1d72042056e9eefe23794f54cb3f.pdf
- published: 2024
