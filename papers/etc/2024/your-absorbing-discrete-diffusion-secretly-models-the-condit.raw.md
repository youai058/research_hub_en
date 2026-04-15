---
title: "Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data"
authors: ["Jingyang Ou", "Shen Nie", "Kaiwen Xue", "Fengqi Zhu", "Jiacheng Sun", "Zhenguo Li", "Chongxuan Li"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2406.03736"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2406.03736v4"
published: "2024-06-06"
categories: ["cs.LG", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:17+09:00"
---

# Your Absorbing Discrete Diffusion Secretly Models the Conditional Distributions of Clean Data

## Abstract
Discrete diffusion models with absorbing processes have shown promise in language modeling. The key quantities to be estimated are the ratios between the marginal probabilities of two transitive states at all timesteps, called the concrete score. In this paper, we reveal that the concrete score in absorbing diffusion can be expressed as conditional probabilities of clean data, multiplied by a time-dependent scalar in an analytic form. Motivated by this finding, we propose reparameterized absorbing discrete diffusion (RADD), a dedicated diffusion model without time-condition that characterizes the time-independent conditional probabilities. Besides its simplicity, RADD can reduce the number of function evaluations (NFEs) by caching the output of the time-independent network when the noisy sample remains unchanged in a sampling interval, which enables sampling acceleration. Built upon the new perspective of conditional distributions, we further unify absorbing discrete diffusion and any-order autoregressive models (AO-ARMs), showing that the upper bound on the negative log-likelihood for the diffusion model can be interpreted as an expected negative log-likelihood for AO-ARMs. Further, our RADD models achieve SOTA performance among diffusion models on 5 zero-shot language modeling benchmarks (measured by perplexity) at the GPT-2 scale. Our code is available at https://github.com/ML-GSAI/RADD.

## Metadata
- venue: arXiv
- year: 2024
- authors: Jingyang Ou, Shen Nie, Kaiwen Xue, Fengqi Zhu, Jiacheng Sun, Zhenguo Li, Chongxuan Li
- arxiv_id: 2406.03736
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2406.03736v4
- published: 2024-06-06
