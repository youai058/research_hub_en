---
title: "The Noisy Laplacian: a Threshold Phenomenon for Non-Linear Dimension Reduction"
authors: ["Alex Kokot", "Octavian-Vlad Murad", "Marina Meila"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GK6q2SFNHm"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c0fed3319c27fa28d7061a937db372103bb85ac9.pdf"
published: "2025"
categories: []
keywords: ["Dimension Reduction", "Denoising", "Diffusion Maps", "Laplacian", "VAE", "LTSA"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:32+09:00"
---

# The Noisy Laplacian: a Threshold Phenomenon for Non-Linear Dimension Reduction

## Abstract
In this paper, we clarify the effect of noise on common spectrally
motivated algorithms such as Diffusion Maps (DM) for dimension
reduction. Empirically, these methods are much more robust to noise
than current work suggests. Specifically, existing consistency results
require that either the noise amplitude or dimensionality must vary
with the sample size $n$.  We provide new theoretical results
demonstrating that low-frequency eigenpairs reliably capture the
geometry of the underlying manifold under a constant noise level, up to a dimension independent threshold $O(r^{-2})$, where $r$ is the noise amplitude. Our results rely on a decomposition of the manifold Laplacian in the Sasaki
metric, a technique not used before in this area, to our knowledge. 
We experimentally validate our theoretical predictions. Additionally, we observe
similar robust behavior for other manifold learning algorithms which 
are not based on computing the Laplacian, namely LTSA and VAE.

## Metadata
- venue: ICML
- year: 2025
- authors: Alex Kokot, Octavian-Vlad Murad, Marina Meila
- arxiv_id: 
- openreview_id: GK6q2SFNHm
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c0fed3319c27fa28d7061a937db372103bb85ac9.pdf
- published: 2025
- keywords: Dimension Reduction, Denoising, Diffusion Maps, Laplacian, VAE, LTSA
