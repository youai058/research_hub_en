---
title: "Optimal Transport for Time Series Imputation"
authors: ["Hao Wang", "zhengnan li", "Haoxuan Li", "Xu Chen", "Mingming Gong", "BinChen", "Zhichao Chen"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xPTzjpIQNp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b5211a0cc33b9c5316eb4545340830695d7cc21f.pdf"
published: "2025"
categories: []
keywords: ["Time series", "Imputation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:41+09:00"
---

# Optimal Transport for Time Series Imputation

## Abstract
Missing data imputation through distribution alignment has demonstrated advantages for non-temporal datasets but exhibits suboptimal performance in time-series applications. The primary obstacle is crafting a discrepancy measure that simultaneously (1) captures temporal patterns—accounting for periodicity and temporal dependencies inherent in time-series—and (2) accommodates non-stationarity, ensuring robustness amidst multiple coexisting temporal patterns. In response to these challenges, we introduce the Proximal Spectrum Wasserstein (PSW) discrepancy, a novel discrepancy tailored for comparing two \textit{sets} of time-series based on optimal transport. It incorporates a pairwise spectral distance to encapsulate temporal patterns, and a selective matching regularization to accommodate non-stationarity. Subsequently, we develop the PSW for Imputation (PSW-I) framework, which iteratively refines imputation results by minimizing the PSW discrepancy. Extensive experiments demonstrate that PSW-I effectively accommodates temporal patterns and non-stationarity, outperforming prevailing time-series imputation methods. Code is available at https://github.com/FMLYD/PSW-I.

## Metadata
- venue: ICLR
- year: 2025
- authors: Hao Wang, zhengnan li, Haoxuan Li, Xu Chen, Mingming Gong, BinChen, Zhichao Chen
- arxiv_id: 
- openreview_id: xPTzjpIQNp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b5211a0cc33b9c5316eb4545340830695d7cc21f.pdf
- published: 2025
- keywords: Time series, Imputation
