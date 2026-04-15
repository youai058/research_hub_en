---
title: "How Gradient descent balances features: A dynamical analysis for two-layer neural networks"
authors: ["Zhenyu Zhu", "Fanghui Liu", "Volkan Cevher"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "25j2ZEgwTj"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a230c85d0f3500fd0a0d1d8028d4beecebef1a6e.pdf"
published: "2025"
categories: []
keywords: ["learning theory", "over-parameterization", "learning dynamics"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:10+09:00"
---

# How Gradient descent balances features: A dynamical analysis for two-layer neural networks

## Abstract
This paper investigates the fundamental regression task of learning $k$ neurons (\emph{a.k.a.} teachers) from Gaussian input, using two-layer ReLU neural networks with width $m$ (\emph{a.k.a.} students) and $m, k= \mathcal{O}(1)$, trained via gradient descent under proper initialization and a small step-size. Our analysis follows a three-phase structure: \emph{alignment} after weak recovery, \emph{tangential growth}, and \emph{local convergence}, providing deeper insights into the learning dynamics of gradient descent (GD). We prove the global convergence at the rate of $\mathcal{O}(T^{-3})$ for the zero loss of excess risk. Additionally, our results show that GD automatically groups and balances student neurons, revealing an implicit bias toward achieving the minimum ``balanced'' $\ell_2$-norm in the solution. Our work extends beyond previous studies in exact-parameterization setting ($m = k = 1$, (Yehudai and Ohad, 2020)) and single-neuron setting ($m \geq k = 1$, (Xu and Du, 2023)). The key technical challenge lies in handling the interactions between multiple teachers and students during training, which we address by refining the alignment analysis in Phase 1 and introducing a new dynamic system analysis for tangential components in Phase 2. Our results pave the way for further research on optimizing neural network training dynamics and understanding implicit biases in more complex architectures.

## Metadata
- venue: ICLR
- year: 2025
- authors: Zhenyu Zhu, Fanghui Liu, Volkan Cevher
- arxiv_id: 
- openreview_id: 25j2ZEgwTj
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a230c85d0f3500fd0a0d1d8028d4beecebef1a6e.pdf
- published: 2025
- keywords: learning theory, over-parameterization, learning dynamics
