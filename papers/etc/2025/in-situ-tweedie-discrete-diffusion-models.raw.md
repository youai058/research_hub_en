---
title: "In-Situ Tweedie Discrete Diffusion Models"
authors: ["Xiao Li", "Jiaqi Zhang", "Shuxiang Zhang", "Tianshui Chen", "Liang Lin", "Guangrun Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.01047"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.01047v2"
published: "2025-10-01"
categories: ["cs.CV", "cs.AI", "cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:40+09:00"
---

# In-Situ Tweedie Discrete Diffusion Models

## Abstract
While diffusion models excel at generating continuous data such as images, adapting them to discrete tasks has relied on indirect approaches that either operate in continuous embedding spaces or use token masking mechanisms, both of which deviate from modeling the true discrete data distribution that can be theoretically guaranteed by Tweedie's formula. We propose in-situ Tweedie Discrete Diffusion (TDD), a framework that performs diffusion guaranteed by Tweedie's formula directly within the discrete one-hot space, hence "in-situ." Unlike prior methods that diffuse continuous embeddings or mask tokens, TDD directly corrupts one-hot vectors with Gaussian noise and performs iterative denoising through a timestep-conditioned cross-entropy objective rather than mean-squared-error reconstruction. At each denoising step, the model predicts class probabilities, applies argmax to obtain discrete predictions, converts them to one-hot vectors, and feeds them into the next iteration with progressively reduced noise. This process naturally unifies discriminative classification and generative modeling under a single framework. Experiments demonstrate that TDD achieves strong performance on both image classification and text generation tasks, with extensive ablation studies confirming the effectiveness of each design component. Our work establishes a principled approach to discrete diffusion that preserves the core characteristics of diffusion models while operating natively in discrete space.

## Metadata
- venue: arXiv
- year: 2025
- authors: Xiao Li, Jiaqi Zhang, Shuxiang Zhang, Tianshui Chen, Liang Lin, Guangrun Wang
- arxiv_id: 2510.01047
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.01047v2
- published: 2025-10-01
