---
title: "F-scheduler: illuminating the free-lunch design space for fast sampling of diffusion models"
authors: ["Zilai Li", "Lujia Bai"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.02390"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.02390v3"
published: "2025-09-30"
categories: ["cs.GR", "cs.AI", "eess.IV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:40+09:00"
---

# F-scheduler: illuminating the free-lunch design space for fast sampling of diffusion models

## Abstract
Diffusion models are the state-of-the-art generative models for high-resolution images, but sampling from pretrained models is computationally expensive, motivating interest in fast sampling. Although Free-U Net is a training-free enhancement for improving image quality, we find it ineffective under few-step ($<10$) sampling. We analyze the discrete diffusion ODE and propose F-scheduler, a scheduler designed for ODE solvers with Free-U Net. Our proposed scheduler consists of a special time schedule that does not fully denoise the feature to enable the use of the KL-term in the $β$-VAE decoder, and the schedule of a proper inference stage for modifying the U-Net skip-connection via Free-U Net. Via information theory, we provide insights into how the better scheduled ODE solvers for the diffusion model can outperform the training-based diffusion distillation model. The newly proposed scheduler is compatible with most of the few-step ODE solvers and can sample a 1024 x 1024-resolution image in 6 steps and a 512 x 512-resolution image in 5 steps when it applies to DPM++ 2m and UniPC, with an FID result that outperforms the SOTA distillation models and the 20-step DPM++ 2m solver, respectively. Codebase: https://github.com/TheLovesOfLadyPurple/F-scheduler

## Metadata
- venue: arXiv
- year: 2025
- authors: Zilai Li, Lujia Bai
- arxiv_id: 2510.02390
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.02390v3
- published: 2025-09-30
