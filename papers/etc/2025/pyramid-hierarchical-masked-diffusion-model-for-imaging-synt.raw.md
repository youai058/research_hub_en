---
title: "Pyramid Hierarchical Masked Diffusion Model for Imaging Synthesis"
authors: ["Xiaojiao Xiao", "Qinmin Vivian Hu", "Guanghui Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2507.16579"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2507.16579v1"
published: "2025-07-22"
categories: ["eess.IV", "cs.AI", "cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# Pyramid Hierarchical Masked Diffusion Model for Imaging Synthesis

## Abstract
Medical image synthesis plays a crucial role in clinical workflows, addressing the common issue of missing imaging modalities due to factors such as extended scan times, scan corruption, artifacts, patient motion, and intolerance to contrast agents. The paper presents a novel image synthesis network, the Pyramid Hierarchical Masked Diffusion Model (PHMDiff), which employs a multi-scale hierarchical approach for more detailed control over synthesizing high-quality images across different resolutions and layers. Specifically, this model utilizes randomly multi-scale high-proportion masks to speed up diffusion model training, and balances detail fidelity and overall structure. The integration of a Transformer-based Diffusion model process incorporates cross-granularity regularization, modeling the mutual information consistency across each granularity's latent spaces, thereby enhancing pixel-level perceptual accuracy. Comprehensive experiments on two challenging datasets demonstrate that PHMDiff achieves superior performance in both the Peak Signal-to-Noise Ratio (PSNR) and Structural Similarity Index Measure (SSIM), highlighting its capability to produce high-quality synthesized images with excellent structural integrity. Ablation studies further confirm the contributions of each component. Furthermore, the PHMDiff model, a multi-scale image synthesis framework across and within medical imaging modalities, shows significant advantages over other methods. The source code is available at https://github.com/xiaojiao929/PHMDiff

## Metadata
- venue: arXiv
- year: 2025
- authors: Xiaojiao Xiao, Qinmin Vivian Hu, Guanghui Wang
- arxiv_id: 2507.16579
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2507.16579v1
- published: 2025-07-22
