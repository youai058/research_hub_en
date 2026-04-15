---
title: "Low-Rank Optimal Transport through Factor Relaxation with Latent Coupling"
authors: ["Peter Halmos", "Xinhao Liu", "Julian Gold", "Benjamin Raphael"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hGgkdFF2hR"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/23f1d7dffdae60ab713fe33b0148a4e9d4a9dd36.pdf"
published: "2024"
categories: []
keywords: ["Optimal Transport", "Sinkhorn", "Low-Rank", "Matrix Factorization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:40+09:00"
---

# Low-Rank Optimal Transport through Factor Relaxation with Latent Coupling

## Abstract
Optimal transport (OT) is a general framework for finding a minimum-cost transport plan, or coupling, between probability distributions, and has many applications in machine learning. A key challenge in applying OT to massive datasets is the quadratic scaling of the coupling matrix with the size of the dataset. [Forrow et al. 2019] introduced a factored coupling for the k-Wasserstein barycenter problem, which [Scetbon et al. 2021] adapted to solve the primal low-rank OT problem. We derive an alternative parameterization of the low-rank problem based on the _latent coupling_ (LC) factorization previously introduced by [Lin et al. 2021] generalizing [Forrow et al. 2019]. The LC factorization has multiple  advantages for low-rank OT including decoupling the problem into three OT problems and greater flexibility and interpretability. We leverage these advantages to derive a new algorithm _Factor Relaxation with Latent Coupling_ (FRLC), which uses _coordinate_ mirror descent to compute the LC factorization. FRLC handles multiple OT objectives (Wasserstein, Gromov-Wasserstein, Fused Gromov-Wasserstein), and marginal constraints (balanced, unbalanced, and semi-relaxed) with linear space complexity. We provide theoretical results on FRLC, and demonstrate superior performance on diverse applications -- including graph clustering and spatial transcriptomics --  while demonstrating its interpretability.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Peter Halmos, Xinhao Liu, Julian Gold, Benjamin Raphael
- arxiv_id: 
- openreview_id: hGgkdFF2hR
- anthology_id: 
- pdf_url: https://openreview.net/pdf/23f1d7dffdae60ab713fe33b0148a4e9d4a9dd36.pdf
- published: 2024
- keywords: Optimal Transport, Sinkhorn, Low-Rank, Matrix Factorization
