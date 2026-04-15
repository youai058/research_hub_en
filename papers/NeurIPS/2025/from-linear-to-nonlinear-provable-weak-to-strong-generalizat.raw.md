---
title: "From Linear to Nonlinear: Provable Weak-to-Strong Generalization through Feature Learning"
authors: ["Junsoo Oh", "Jerry Song", "Chulhee Yun"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xMiKDqxEE8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/10df99a0eca17f39bdcb4e527c55f41736146a02.pdf"
published: "2025"
categories: []
keywords: ["weak-to-strong generalization", "theory", "feature learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:44+09:00"
---

# From Linear to Nonlinear: Provable Weak-to-Strong Generalization through Feature Learning

## Abstract
Weak-to-strong generalization refers to the phenomenon where a stronger model trained under supervision from a weaker one can outperform its teacher. While prior studies aim to explain this effect, most theoretical insights are limited to abstract frameworks or linear/random feature models. In this paper, we provide a formal analysis of weak-to-strong generalization from a linear CNN (weak) to a two-layer ReLU CNN (strong). We consider structured data composed of label-dependent signals of varying difficulty and label-independent noise, and analyze gradient descent dynamics when the strong model is trained on data labeled by the pretrained weak model. Our analysis identifies two regimes—data-scarce and data-abundant—based on the signal-to-noise characteristics of the dataset, and reveals distinct mechanisms of weak-to-strong generalization. In the data-scarce regime, generalization occurs via benign overfitting or fails via harmful overfitting, depending on the amount of data, and we characterize the transition boundary. In the data-abundant regime, generalization emerges in the early phase through label correction, but we observe that overtraining can subsequently degrade performance.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Junsoo Oh, Jerry Song, Chulhee Yun
- arxiv_id: 
- openreview_id: xMiKDqxEE8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/10df99a0eca17f39bdcb4e527c55f41736146a02.pdf
- published: 2025
- keywords: weak-to-strong generalization, theory, feature learning
