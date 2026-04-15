---
title: "Distillation of Discrete Diffusion by Exact Conditional Distribution Matching"
authors: ["Yansong Gao", "Yu Sun"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.12889"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.12889v1"
published: "2025-12-15"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:33+09:00"
---

# Distillation of Discrete Diffusion by Exact Conditional Distribution Matching

## Abstract
Discrete diffusion models (DDMs) are a powerful class of generative models for categorical data, but they typically require many function evaluations for a single sample, making inference expensive. Existing acceleration methods either rely on approximate simulators, such as $τ$-leaping, or on distillation schemes that train new student models and auxiliary networks with proxy objectives. We propose a simple and principled distillation alternative based on \emph{conditional distribution matching}. Our key observation is that the reverse conditional distribution of clean data given a noisy state, $p_{0\mid t}(x_0 \mid x_t)$, admits a Markov decomposition through intermediate times and can be recovered from marginal density ratios and the known forward CTMC kernel. We exploit this structure to define distillation objectives that directly match conditional distributions between a pre-trained teacher and a low-NFE student, both for one-step and few-step samplers.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yansong Gao, Yu Sun
- arxiv_id: 2512.12889
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.12889v1
- published: 2025-12-15
