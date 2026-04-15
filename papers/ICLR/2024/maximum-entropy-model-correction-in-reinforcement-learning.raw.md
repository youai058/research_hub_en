---
title: "Maximum Entropy Model Correction in Reinforcement Learning"
authors: ["Amin Rakhsha", "Mete Kemertas", "Mohammad Ghavamzadeh", "Amir-massoud Farahmand"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kNpSUN0uCc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1f91adc5c8d10f07321994671b62ab5b8ced10cb.pdf"
published: "2024"
categories: []
keywords: ["reinforcement learning", "model-based reinforcement learning", "maximum entropy", "planning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:17+09:00"
---

# Maximum Entropy Model Correction in Reinforcement Learning

## Abstract
We propose and theoretically analyze an approach for planning with an approximate model in reinforcement learning that can reduce the adverse impact of model error. If the model is accurate enough, it accelerates the convergence to the true value function too. One of its key components is the MaxEnt Model Correction (MoCo) procedure that corrects the model’s next-state distributions based on a Maximum Entropy density estimation formulation. Based on MoCo, we introduce the Model Correcting Value Iteration (MoCoVI) algorithm, and its sampled-based variant MoCoDyna. We show that MoCoVI and MoCoDyna’s convergence can be much faster than the conventional model-free algorithms. Unlike traditional model-based algorithms, MoCoVI and MoCoDyna effectively utilize an approximate model and still converge to the correct value function.

## Metadata
- venue: ICLR
- year: 2024
- authors: Amin Rakhsha, Mete Kemertas, Mohammad Ghavamzadeh, Amir-massoud Farahmand
- arxiv_id: 
- openreview_id: kNpSUN0uCc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1f91adc5c8d10f07321994671b62ab5b8ced10cb.pdf
- published: 2024
- keywords: reinforcement learning, model-based reinforcement learning, maximum entropy, planning
