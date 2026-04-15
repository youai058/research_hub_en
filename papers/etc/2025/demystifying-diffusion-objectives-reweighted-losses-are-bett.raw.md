---
title: "Demystifying Diffusion Objectives: Reweighted Losses are Better Variational Bounds"
authors: ["Jiaxin Shi", "Michalis K. Titsias"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.19664"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.19664v1"
published: "2025-11-24"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# Demystifying Diffusion Objectives: Reweighted Losses are Better Variational Bounds

## Abstract
We derive a new theoretical interpretation of the reweighted losses that are widely used for training diffusion models. Our method is based on constructing a cascade of time-dependent variational lower bounds on the data log-likelihood, that provably improves upon the standard evidence lower bound and results in reduced data-model KL-divergences. Combining such bounds gives rise to reweighted objectives that can be applied to any generative diffusion model including both continuous Gaussian diffusion and masked (discrete) diffusion models. Then, we showcase this framework in masked diffusion and report significant improvements over previous training losses in pixel-space image modeling, approaching sample quality comparable to continuous diffusion models. Our results also provide a theoretical justification for the simple weighting scheme widely used in masked image models.

## Metadata
- venue: arXiv
- year: 2025
- authors: Jiaxin Shi, Michalis K. Titsias
- arxiv_id: 2511.19664
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.19664v1
- published: 2025-11-24
