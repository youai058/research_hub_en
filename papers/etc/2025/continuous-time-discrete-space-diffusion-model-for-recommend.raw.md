---
title: "Continuous-time Discrete-space Diffusion Model for Recommendation"
authors: ["Chengyi Liu", "Xiao Chen", "Shijie Wang", "Wenqi Fan", "Qing Li"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.12114"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.12114v1"
published: "2025-11-15"
categories: ["cs.IR"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# Continuous-time Discrete-space Diffusion Model for Recommendation

## Abstract
In the era of information explosion, Recommender Systems (RS) are essential for alleviating information overload and providing personalized user experiences. Recent advances in diffusion-based generative recommenders have shown promise in capturing the dynamic nature of user preferences. These approaches explore a broader range of user interests by progressively perturbing the distribution of user-item interactions and recovering potential preferences from noise, enabling nuanced behavioral understanding. However, existing diffusion-based approaches predominantly operate in continuous space through encoded graph-based historical interactions, which may compromise potential information loss and suffer from computational inefficiency. As such, we propose CDRec, a novel Continuous-time Discrete-space Diffusion Recommendation framework, which models user behavior patterns through discrete diffusion on historical interactions over continuous time. The discrete diffusion algorithm operates via discrete element operations (e.g., masking) while incorporating domain knowledge through transition matrices, producing more meaningful diffusion trajectories. Furthermore, the continuous-time formulation enables flexible adaptive sampling. To better adapt discrete diffusion models to recommendations, CDRec introduces: (1) a novel popularity-aware noise schedule that generates semantically meaningful diffusion trajectories, and (2) an efficient training framework combining consistency parameterization for fast sampling and a contrastive learning objective guided by multi-hop collaborative signals for personalized recommendation. Extensive experiments on real-world datasets demonstrate CDRec's superior performance in both recommendation accuracy and computational efficiency.

## Metadata
- venue: arXiv
- year: 2025
- authors: Chengyi Liu, Xiao Chen, Shijie Wang, Wenqi Fan, Qing Li
- arxiv_id: 2511.12114
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.12114v1
- published: 2025-11-15
