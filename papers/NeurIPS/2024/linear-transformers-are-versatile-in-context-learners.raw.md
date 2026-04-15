---
title: "Linear Transformers are Versatile In-Context Learners"
authors: ["Max Vladymyrov", "Johannes von Oswald", "Mark Sandler", "Rong Ge"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "p1ft33Mu3J"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f0bb66de2cdfa918523f8384547b5be538489651.pdf"
published: "2024"
categories: []
keywords: ["Linear Transformers", "In-Context Learning", "Noisy Linear Regression", "Model Selection", "Mesa-optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:05+09:00"
---

# Linear Transformers are Versatile In-Context Learners

## Abstract
Recent research has demonstrated that transformers, particularly linear attention models, implicitly execute gradient-descent-like algorithms on data provided in-context during their forward inference step. However, their capability in handling more complex problems remains unexplored. In this paper, we prove that each layer of a linear transformer maintains a weight vector for an implicit linear regression problem and can be interpreted as performing a variant of preconditioned gradient descent. We also investigate the use of linear transformers in a challenging scenario where the training data is corrupted with different levels of noise. Remarkably, we demonstrate that for this problem linear transformers discover an intricate and highly effective optimization algorithm, surpassing or matching in performance many reasonable baselines. We analyze this algorithm and show that it is a novel approach incorporating momentum and adaptive rescaling based on noise levels. Our findings show that even linear transformers possess the surprising ability to discover sophisticated optimization strategies.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Max Vladymyrov, Johannes von Oswald, Mark Sandler, Rong Ge
- arxiv_id: 
- openreview_id: p1ft33Mu3J
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f0bb66de2cdfa918523f8384547b5be538489651.pdf
- published: 2024
- keywords: Linear Transformers, In-Context Learning, Noisy Linear Regression, Model Selection, Mesa-optimization
