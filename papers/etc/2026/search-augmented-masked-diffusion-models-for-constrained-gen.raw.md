---
title: "Search-Augmented Masked Diffusion Models for Constrained Generation"
authors: ["Huu Binh Ta", "Michael Cardei", "Alvaro Velasquez", "Ferdinando Fioretto"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.02727"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.02727v1"
published: "2026-02-02"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:17+09:00"
---

# Search-Augmented Masked Diffusion Models for Constrained Generation

## Abstract
Discrete diffusion models generate sequences by iteratively denoising samples corrupted by categorical noise, offering an appealing alternative to autoregressive decoding for structured and symbolic generation. However, standard training targets a likelihood-based objective that primarily matches the data distribution and provides no native mechanism for enforcing hard constraints or optimizing non-differentiable properties at inference time. This work addresses this limitation and introduces Search-Augmented Masked Diffusion (SearchDiff), a training-free neurosymbolic inference framework that integrates informed search directly into the reverse denoising process. At each denoising step, the model predictions define a proposal set that is optimized under a user-specified property satisfaction, yielding a modified reverse transition that steers sampling toward probable and feasible solutions. Experiments in biological design and symbolic reasoning illustrate that SearchDiff substantially improves constraint satisfaction and property adherence, while consistently outperforming discrete diffusion and autoregressive baselines.

## Metadata
- venue: arXiv
- year: 2026
- authors: Huu Binh Ta, Michael Cardei, Alvaro Velasquez, Ferdinando Fioretto
- arxiv_id: 2602.02727
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.02727v1
- published: 2026-02-02
