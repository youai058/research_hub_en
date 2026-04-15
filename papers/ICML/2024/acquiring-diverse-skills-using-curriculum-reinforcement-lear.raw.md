---
title: "Acquiring Diverse Skills using Curriculum Reinforcement Learning with Mixture of Experts"
authors: ["Onur Celik", "Aleksandar Taranovic", "Gerhard Neumann"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9ZkUFSwlUH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9eab51ffd9ded49f98c8072baadbba0c43763cd4.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:37+09:00"
---

# Acquiring Diverse Skills using Curriculum Reinforcement Learning with Mixture of Experts

## Abstract
Reinforcement learning (RL) is a powerful approach for acquiring a good-performing policy. However, learning diverse skills is challenging in RL due to the commonly used Gaussian policy parameterization. We propose Diverse Skill Learning (Di-SkilL), an RL method for learning diverse skills using Mixture of Experts, where each expert formalizes a skill as a contextual motion primitive. Di-SkilL optimizes each expert and its associate context distribution to a maximum entropy objective that incentivizes learning diverse skills in similar contexts. The per-expert context distribution enables automatic curricula learning, allowing each expert to focus on its best-performing sub-region of the context space. To overcome hard discontinuities and multi-modalities without any prior knowledge of the environment's unknown context probability space, we leverage energy-based models to represent the per-expert context distributions and demonstrate how we can efficiently train them using the standard policy gradient objective. We show on challenging robot simulation tasks that Di-SkilL can learn diverse and performant skills.

## Metadata
- venue: ICML
- year: 2024
- authors: Onur Celik, Aleksandar Taranovic, Gerhard Neumann
- arxiv_id: 
- openreview_id: 9ZkUFSwlUH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9eab51ffd9ded49f98c8072baadbba0c43763cd4.pdf
- published: 2024
