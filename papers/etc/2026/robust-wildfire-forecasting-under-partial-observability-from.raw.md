---
title: "Robust Wildfire Forecasting under Partial Observability: From Reconstruction to Prediction"
authors: ["Chen Yang", "Mehdi Zafari", "Ziheng Duan", "A. Lee Swindlehurst"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.09042"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.09042v1"
published: "2026-03-10"
categories: ["eess.IV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:28+09:00"
---

# Robust Wildfire Forecasting under Partial Observability: From Reconstruction to Prediction

## Abstract
Satellite-derived fire observations are the primary input for learning-based wildfire spread prediction, yet they are inherently incomplete due to cloud cover, smoke obscuration, and sensor artifacts. This partial observability introduces a domain gap between the clean data used to train forecasting models and the degraded inputs encountered during deployment, often leading to unreliable predictions. To address this challenge, we formulate wildfire forecasting under partial observability using a two-stage probabilistic framework that decouples observation recovery from spatiotemporal prediction. Stage-I reconstructs plausible fire maps from corrupted observations via conditional inpainting, while Stage-II models wildfire dynamics on the recovered sequences using a spatiotemporal forecasting network. We consider four network architectures for the reconstruction module-a Residual U-Net (MaskUNet), a Conditional VAE (MaskCVAE), a cross-attention Vision Transformer (MaskViT), and a discrete diffusion model (MaskD3PM)-spanning CNN-based, latent-variable, attention-based, and diffusion-based approaches. We evaluate the performance of the two-stage approach on the WildfireSpreadTS (WSTS) dataset under various settings, including pixel-wise and block-wise masking, eight corruption levels (10%-80%), four fire scenarios, and leave-one-year-out cross-validation. Results show that all learning-based recovery models substantially outperform non-learning baselines, with MaskCVAE and MaskUNet achieving the strongest overall performance. Importantly, inserting the reconstruction stage before forecasting significantly mitigates the domain gap, restoring next-day prediction accuracy to near-clean-input levels even under severe information loss.

## Metadata
- venue: arXiv
- year: 2026
- authors: Chen Yang, Mehdi Zafari, Ziheng Duan, A. Lee Swindlehurst
- arxiv_id: 2603.09042
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.09042v1
- published: 2026-03-10
