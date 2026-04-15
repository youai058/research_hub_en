---
title: "Improved Sampling Schedules for Discrete Diffusion Models"
authors: ["Alberto Foresti", "Mustapha Bounoua", "Giulio Franzese", "Luca Ambrogioni", "Pietro Michiardi"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.06849"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.06849v2"
published: "2026-02-06"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:32+09:00"
---

# Improved Sampling Schedules for Discrete Diffusion Models

## Abstract
Discrete diffusion models have emerged as a powerful paradigm for generative modeling on sequence data; however, the information-theoretic principles governing their reverse processes remain significantly less understood than those of their continuous counterparts. In this work, we bridge this gap by analyzing the reverse process dynamics through the lens of thermodynamic entropy production. We propose the entropy production rate as a rigorous proxy for quantifying information generation, deriving as a byproduct a bound on the Wasserstein distance between intermediate states and the data distribution. Leveraging these insights, we introduce two novel sampling schedules that are uniformly spaced with respect to their corresponding physics-inspired metrics: the Entropic Discrete Schedule (EDS), which is defined by maintaining a constant rate of information gain, and the Wasserstein Discrete Schedule (WDS), which is defined by taking equal steps in terms of the Wasserstein distance. We empirically demonstrate that our proposed schedules significantly outperform state-of-the-art strategies across diverse application domains, including synthetic data, music notation, vision and language modeling, consistently achieving superior performance at a lower computational budget.

## Metadata
- venue: arXiv
- year: 2026
- authors: Alberto Foresti, Mustapha Bounoua, Giulio Franzese, Luca Ambrogioni, Pietro Michiardi
- arxiv_id: 2602.06849
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.06849v2
- published: 2026-02-06
