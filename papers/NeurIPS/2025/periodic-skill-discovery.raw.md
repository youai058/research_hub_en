---
title: "Periodic Skill Discovery"
authors: ["Jonghae Park", "Daesol Cho", "Jusuk Lee", "Dongseok Shim", "Inkyu Jang", "H. Jin Kim"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BPSU46emit"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ed022476433f489ee250c4e34c0830545d57451a.pdf"
published: "2025"
categories: []
keywords: ["reinforcement learning", "unsupervised skill discovery", "periodicity"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:59+09:00"
---

# Periodic Skill Discovery

## Abstract
Unsupervised skill discovery in reinforcement learning (RL) aims to learn diverse behaviors without relying on external rewards. However, current methods often overlook the periodic nature of learned skills, focusing instead on increasing the mutual dependency between states and skills or maximizing the distance traveled in latent space. Considering that many robotic tasks—particularly those involving locomotion—require periodic behaviors across varying timescales, the ability to discover diverse periodic skills is essential. Motivated by this, we propose Periodic Skill Discovery (PSD), a framework that discovers periodic behaviors in an unsupervised manner. The key idea of PSD is to train an encoder that maps states to a circular latent space, thereby naturally encoding periodicity in the latent representation. By capturing temporal distance, PSD can effectively learn skills with diverse periods in complex robotic tasks, even with pixel-based observations. We further show that these learned skills achieve high performance on downstream tasks such as hurdling. Moreover, integrating PSD with an existing skill discovery method offers more diverse behaviors, thus broadening the agent’s repertoire.
Our code and demos are available at https://jonghaepark.github.io/psd

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jonghae Park, Daesol Cho, Jusuk Lee, Dongseok Shim, Inkyu Jang, H. Jin Kim
- arxiv_id: 
- openreview_id: BPSU46emit
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ed022476433f489ee250c4e34c0830545d57451a.pdf
- published: 2025
- keywords: reinforcement learning, unsupervised skill discovery, periodicity
