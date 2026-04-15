---
title: "Categorical Reparameterization with Denoising Diffusion models"
authors: ["Samson Gourevitch", "Alain Durmus", "Eric Moulines", "Jimmy Olsson", "Yazid Janati"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.00781"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.00781v2"
published: "2026-01-02"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# Categorical Reparameterization with Denoising Diffusion models

## Abstract
Learning models with categorical variables requires optimizing expectations over discrete distributions, a setting in which stochastic gradient-based optimization is challenging due to the non-differentiability of categorical sampling. A common workaround is to replace the discrete distribution with a continuous relaxation, yielding a smooth surrogate that admits reparameterized gradient estimates via the reparameterization trick. Building on this idea, we introduce ReDGE, a novel and efficient diffusion-based soft reparameterization method for categorical distributions. Our approach defines a flexible class of gradient estimators that includes the Straight-Through estimator as a special case. Experiments spanning latent variable models and inference-time reward guidance in discrete diffusion models demonstrate that ReDGE consistently matches or outperforms existing gradient-based methods. The code will be made available at https://github.com/samsongourevitch/redge.

## Metadata
- venue: arXiv
- year: 2026
- authors: Samson Gourevitch, Alain Durmus, Eric Moulines, Jimmy Olsson, Yazid Janati
- arxiv_id: 2601.00781
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.00781v2
- published: 2026-01-02
