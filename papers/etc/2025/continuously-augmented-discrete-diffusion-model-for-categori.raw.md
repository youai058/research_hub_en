---
title: "Continuously Augmented Discrete Diffusion model for Categorical Generative Modeling"
authors: ["Huangjie Zheng", "Shansan Gong", "Ruixiang Zhang", "Tianrong Chen", "Jiatao Gu", "Mingyuan Zhou", "Navdeep Jaitly", "Yizhe Zhang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.01329"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.01329v1"
published: "2025-10-01"
categories: ["stat.ML", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:40+09:00"
---

# Continuously Augmented Discrete Diffusion model for Categorical Generative Modeling

## Abstract
Standard discrete diffusion models treat all unobserved states identically by mapping them to an absorbing [MASK] token. This creates an 'information void' where semantic information that could be inferred from unmasked tokens is lost between denoising steps. We introduce Continuously Augmented Discrete Diffusion (CADD), a framework that augments the discrete state space with a paired diffusion in a continuous latent space. This yields graded, gradually corrupted states in which masked tokens are represented by noisy yet informative latent vectors rather than collapsed 'information voids'. At each reverse step, CADD may leverage the continuous latent as a semantic hint to guide discrete denoising. The design is clean and compatible with existing discrete diffusion training. At sampling time, the strength and choice of estimator for the continuous latent vector enables a controlled trade-off between mode-coverage (generating diverse outputs) and mode-seeking (generating contextually precise outputs) behaviors. Empirically, we demonstrate CADD improves generative quality over mask-based diffusion across text generation, image synthesis, and code modeling, with consistent gains on both qualitative and quantitative metrics against strong discrete baselines.

## Metadata
- venue: arXiv
- year: 2025
- authors: Huangjie Zheng, Shansan Gong, Ruixiang Zhang, Tianrong Chen, Jiatao Gu, Mingyuan Zhou, Navdeep Jaitly, Yizhe Zhang
- arxiv_id: 2510.01329
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.01329v1
- published: 2025-10-01
