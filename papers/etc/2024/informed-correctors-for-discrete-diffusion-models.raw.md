---
title: "Informed Correctors for Discrete Diffusion Models"
authors: ["Yixiu Zhao", "Jiaxin Shi", "Feng Chen", "Shaul Druckmann", "Lester Mackey", "Scott Linderman"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2407.21243"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2407.21243v5"
published: "2024-07-30"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:12+09:00"
---

# Informed Correctors for Discrete Diffusion Models

## Abstract
Discrete diffusion has emerged as a powerful framework for generative modeling in discrete domains, yet efficiently sampling from these models remains challenging. Existing sampling strategies often struggle to balance computation and sample quality when the number of sampling steps is reduced, even when the model has learned the data distribution well. To address these limitations, we propose a predictor-corrector sampling scheme where the corrector is informed by the diffusion model to more reliably counter the accumulating approximation errors. To further enhance the effectiveness of our informed corrector, we introduce complementary architectural modifications based on hollow transformers and a simple tailored training objective that leverages more training signal. We use a synthetic example to illustrate the failure modes of existing samplers and show how informed correctors alleviate these problems. On the text8 and tokenized ImageNet 256x256 datasets, our informed corrector consistently produces superior samples with fewer errors or improved FID scores for discrete diffusion models. These results underscore the potential of informed correctors for fast and high-fidelity generation using discrete diffusion. Our code is available at https://github.com/lindermanlab/informed-correctors.

## Metadata
- venue: arXiv
- year: 2024
- authors: Yixiu Zhao, Jiaxin Shi, Feng Chen, Shaul Druckmann, Lester Mackey, Scott Linderman
- arxiv_id: 2407.21243
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2407.21243v5
- published: 2024-07-30
