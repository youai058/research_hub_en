---
title: "Statistical Analysis of the Sinkhorn Iterations for Two-Sample Schr\\\"{o}dinger Bridge Estimation"
authors: ["Ibuki Maeda", "Rentian Yao", "Atsushi Nitanda"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DsGrLE9gqv"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/237eb7670a2bc845c53df1bbb0ad9b3646f2bc6b.pdf"
published: "2025"
categories: []
keywords: ["Schrödinger bridge", "Sinkhorn algorithm", "statistical analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:54+09:00"
---

# Statistical Analysis of the Sinkhorn Iterations for Two-Sample Schr\"{o}dinger Bridge Estimation

## Abstract
The Schrödinger bridge problem seeks the optimal stochastic process that connects two given probability distributions with minimal energy modification. While the Sinkhorn algorithm is widely used to solve the static optimal transport problem, a recent work (Pooladian and Niles-Weed, 2024)  proposed the *Sinkhorn bridge*, which estimates Schrödinger bridges by plugging optimal transport into the time-dependent drifts of SDEs, with statistical guarantees in the one-sample estimation setting where the true source distribution is fully accessible. In this work, to further justify this method, we study the statistical performance of intermediate Sinkhorn iterations in the two-sample estimation setting, where only finite samples from both source and target distributions are available. Specifically, we establish a statistical bound on the squared total variation error of Sinkhorn bridge iterations: $\mathcal{O}(1/m+1/n + r^{2k})~(r \in (0,1))$, where $m$ and $n$ are the sample sizes from the source and target distributions, respectively, and $k$ is the number of Sinkhorn iterations. This result provides a theoretical guarantee for the finite-sample performance of the Schrödinger bridge estimator and offers practical guidance for selecting sample sizes and the number of Sinkhorn iterations. Notably, our theoretical results apply to several representative methods such as [SF]$^2$M, DSBM-IMF, BM2, and lightSB(-M) under specific settings, through the previously unnoticed connection between these estimators.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Ibuki Maeda, Rentian Yao, Atsushi Nitanda
- arxiv_id: 
- openreview_id: DsGrLE9gqv
- anthology_id: 
- pdf_url: https://openreview.net/pdf/237eb7670a2bc845c53df1bbb0ad9b3646f2bc6b.pdf
- published: 2025
- keywords: Schrödinger bridge, Sinkhorn algorithm, statistical analysis
