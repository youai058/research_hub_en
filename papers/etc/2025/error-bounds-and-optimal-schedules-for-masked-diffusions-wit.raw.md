---
title: "Error Bounds and Optimal Schedules for Masked Diffusions with Factorized Approximations"
authors: ["Hugo Lavenant", "Giacomo Zanella"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.25544"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.25544v2"
published: "2025-10-29"
categories: ["stat.ML", "cs.IT", "cs.LG", "stat.CO"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:22+09:00"
---

# Error Bounds and Optimal Schedules for Masked Diffusions with Factorized Approximations

## Abstract
Recently proposed generative models for discrete data, such as Masked Diffusion Models (MDMs), exploit conditional independence approximations to reduce the computational cost of popular Auto-Regressive Models (ARMs), at the price of some bias in the sampling distribution. We study the resulting computation-vs-accuracy trade-off, providing general error bounds (in relative entropy) that depend only on the average number of tokens generated per iteration and are independent of the data dimensionality (i.e. sequence length), thus supporting the empirical success of MDMs. We then investigate the gain obtained by using non-constant schedule sizes (i.e. varying the number of unmasked tokens during the generation process) and identify the optimal schedule as a function of a so-called information profile of the data distribution, thus allowing for a principled optimization of schedule sizes. We define methods directly as sampling algorithms and do not use classical derivations as time-reversed diffusion processes, leading us to simple and transparent proofs.

## Metadata
- venue: arXiv
- year: 2025
- authors: Hugo Lavenant, Giacomo Zanella
- arxiv_id: 2510.25544
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.25544v2
- published: 2025-10-29
