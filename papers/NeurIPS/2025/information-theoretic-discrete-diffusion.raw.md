---
title: "Information-Theoretic Discrete Diffusion"
authors: ["Moongyu Jeon", "Sangwoo Shin", "Dongjae Jeon", "Albert No"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "B2iPEX5A9c"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9b4e154703fd904ac9ee0a421f77a7013e3b4e1a.pdf"
published: "2025"
categories: []
keywords: ["Discrete Diffusion Models", "Information Theory", "Score Matching", "Denoising Score Entropy (DSE)", "Denoising Cross-Entropy (DCE)"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:23+09:00"
---

# Information-Theoretic Discrete Diffusion

## Abstract
We present an information-theoretic framework for discrete diffusion models 
that yields principled estimators of log-likelihood using score-matching losses.
Inspired by the I-MMSE identity for the Gaussian setup, we derive analogous results for the discrete setting.
Specifically, we introduce the Information–Minimum Denoising Score Entropy (I-MDSE) relation,
which links mutual information between data and its diffused version to the minimum denoising score entropy (DSE) loss.
We extend this theory to masked diffusion and establish the Information–Minimum Denoising Cross-Entropy (I-MDCE) relation,
connecting cross-entropy losses to mutual information in discrete masked processes.
These results provide a time-integral decomposition of the log-likelihood of the data in terms of optimal score-based losses,
showing that commonly used losses such as DSE and DCE are not merely variational bounds 
but tight and principled estimators of log-likelihood.
The I-MDCE decomposition further enables practical extensions, including time-free formula,
conditional likelihood estimation in prompt–response tasks, and coupled Monte Carlo estimation of likelihood ratios.
Experiments on synthetic and real-world data confirm the accuracy, variance stability, and utility of our estimators.
The code is publicly available at https://github.com/Dongjae0324/infodis.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Moongyu Jeon, Sangwoo Shin, Dongjae Jeon, Albert No
- arxiv_id: 
- openreview_id: B2iPEX5A9c
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9b4e154703fd904ac9ee0a421f77a7013e3b4e1a.pdf
- published: 2025
- keywords: Discrete Diffusion Models, Information Theory, Score Matching, Denoising Score Entropy (DSE), Denoising Cross-Entropy (DCE)
