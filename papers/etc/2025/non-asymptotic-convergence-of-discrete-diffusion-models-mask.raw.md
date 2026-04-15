---
title: "Non-Asymptotic Convergence of Discrete Diffusion Models: Masked and Random Walk dynamics"
authors: ["Giovanni Conforti", "Alain Durmus", "Le-Tuyet-Nhi Pham", "Gael Raoul"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.00580"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.00580v3"
published: "2025-11-29"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:33+09:00"
---

# Non-Asymptotic Convergence of Discrete Diffusion Models: Masked and Random Walk dynamics

## Abstract
Diffusion models for continuous state spaces based on Gaussian noising processes are now relatively well understood from both practical and theoretical perspectives. In contrast, results for diffusion models on discrete state spaces remain far less explored and pose significant challenges, particularly due to their combinatorial structure and their more recent introduction in generative modelling. In this work, we establish new and sharp convergence guarantees for three popular discrete diffusion models (DDMs). Two of these models are designed for finite state spaces and are based respectively on the random walk and the masking process. The third DDM we consider is defined on the countably infinite space $\mathbb{N}^d$ and uses a drifted random walk as its forward process. For each of these models, the backward process can be characterized by a discrete score function that can, in principle, be estimated. However, even with perfect access to these scores, simulating the exact backward process is infeasible, and one must rely on time discretization. In this work, we study Euler-type approximations and establish convergence bounds in both Kullback-Leibler divergence and total variation distance for the resulting models, under minimal assumptions on the data distribution. To the best of our knowledge, this study provides the optimal non-asymptotic convergence guarantees for these noising processes that do not rely on boundedness assumptions on the estimated score. In particular, the computational complexity of each method scales only linearly in the dimension, up to logarithmic factors.

## Metadata
- venue: arXiv
- year: 2025
- authors: Giovanni Conforti, Alain Durmus, Le-Tuyet-Nhi Pham, Gael Raoul
- arxiv_id: 2512.00580
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.00580v3
- published: 2025-11-29
