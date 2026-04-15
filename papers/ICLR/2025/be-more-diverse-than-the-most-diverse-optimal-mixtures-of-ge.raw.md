---
title: "Be More Diverse than the Most Diverse: Optimal Mixtures of Generative Models via Mixture-UCB Bandit Algorithms"
authors: ["Parham Rezaei", "Farzan Farnia", "Cheuk Ting Li"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2Chkk5Ye2s"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/230cde0aea64ec293c3697666f813211ec3f5bfd.pdf"
published: "2025"
categories: []
keywords: ["Multi-Armed Bandits", "Evaluation of generative models", "Kernel-based evaluation scores", "Mixture-UCB", "Diversity in data generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:52+09:00"
---

# Be More Diverse than the Most Diverse: Optimal Mixtures of Generative Models via Mixture-UCB Bandit Algorithms

## Abstract
The availability of multiple training algorithms and architectures for generative models requires a selection mechanism to form a single model over a group of well-trained generation models. The selection task is commonly addressed by identifying the model that maximizes an evaluation score based on the diversity and quality of the generated data. However, such a best-model identification approach overlooks the possibility that a mixture of available models can outperform each individual model. In this work, we numerically show that a mixture of generative models on benchmark image datasets can indeed achieve a better evaluation score (based on FID and KID scores), compared to the individual models. This observation motivates the development of efficient algorithms for selecting the optimal mixture of the models. To address this, we formulate a quadratic optimization problem to find an optimal mixture model achieving the maximum of kernel-based evaluation scores including kernel inception distance (KID) and Rényi kernel entropy (RKE). To identify the optimal mixture of the models using the fewest possible sample queries, we view the selection task as a multi-armed bandit (MAB) problem and propose the *Mixture Upper Confidence Bound (Mixture-UCB)* algorithm that provably converges to the optimal mixture of the involved models. More broadly, the proposed Mixture-UCB can be extended to optimize every convex quadratic function of the mixture weights in a general MAB setting. We prove a regret bound for the  Mixture-UCB algorithm and perform several numerical experiments to show the success of Mixture-UCB in finding the optimal mixture of text and image generative models. The project code is available in the [Mixture-UCB Github repository](https://github.com/Rezaei-Parham/Mixture-UCB).

## Metadata
- venue: ICLR
- year: 2025
- authors: Parham Rezaei, Farzan Farnia, Cheuk Ting Li
- arxiv_id: 
- openreview_id: 2Chkk5Ye2s
- anthology_id: 
- pdf_url: https://openreview.net/pdf/230cde0aea64ec293c3697666f813211ec3f5bfd.pdf
- published: 2025
- keywords: Multi-Armed Bandits, Evaluation of generative models, Kernel-based evaluation scores, Mixture-UCB, Diversity in data generation
