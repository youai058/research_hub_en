---
title: "Bayesian Coreset Optimization for Personalized Federated Learning"
authors: ["Prateek Chanda", "Shrey Modi", "Ganesh Ramakrishnan"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uz7d2N2zul"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cd650d7bda1c2da0c78084f2b993c15c2ec0925f.pdf"
published: "2024"
categories: []
keywords: ["federated learning", "personalized federated learning", "bayesian coreset", "submodularity", "variational inference", "coresets", "optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:56+09:00"
---

# Bayesian Coreset Optimization for Personalized Federated Learning

## Abstract
In a distributed machine learning setting like Federated Learning where there are multiple clients involved which update their individual weights to a single central server, often training on the entire individual client's dataset for each client becomes cumbersome. To address this issue we propose CORESET-PFEDBAYES : a personalized coreset weighted federated learning setup where the training updates for each individual clients are forwarded to the central server based on only individual client coreset based representative data points instead of the entire client data. Through theoretical analysis we present how the average generalization error is minimax optimal up to logarithm bounds (upper bounded by $\mathcal{O}(n_k^{-\frac{2 \beta}{2 \beta+\boldsymbol{\Lambda}}} \log ^{2 \delta^{\prime}}(n_k))$) and lower bounds of $\mathcal{O}(n_k^{-\frac{2 \beta}{2 \beta+\boldsymbol{\Lambda}}})$, and how the overall generalization error on the data likelihood differs from a vanilla Federated Learning setup as a closed form function ${\boldsymbol{\Im}}(\boldsymbol{w}, n_k)$ of the coreset weights $\boldsymbol{w}$ and coreset sample size $n_k$. 
Our experiments on different benchmark datasets based on a variety of recent personalized federated learning architectures show significant gains as compared to random sampling on the training data followed by federated learning, thereby indicating how intelligently selecting such training samples can help in performance. Additionally, through experiments on medical datasets our proposed method showcases some gains as compared to  other submodular optimization based approaches used for subset selection on client's data.

## Metadata
- venue: ICLR
- year: 2024
- authors: Prateek Chanda, Shrey Modi, Ganesh Ramakrishnan
- arxiv_id: 
- openreview_id: uz7d2N2zul
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cd650d7bda1c2da0c78084f2b993c15c2ec0925f.pdf
- published: 2024
- keywords: federated learning, personalized federated learning, bayesian coreset, submodularity, variational inference, coresets, optimization
