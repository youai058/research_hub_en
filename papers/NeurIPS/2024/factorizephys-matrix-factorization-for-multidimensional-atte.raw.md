---
title: "FactorizePhys: Matrix Factorization for Multidimensional Attention in Remote Physiological Sensing"
authors: ["Jitesh Joshi", "Sos Agaian", "Youngjun Cho"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "qrfp4eeZ47"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9abd14b56c34451b8fc9ee44ba4395c988c4d34d.pdf"
published: "2024"
categories: []
keywords: ["Time-series estimation", "remote photo-plethysmography", "spatial-temporal attention", "non-negative matrix factorization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:29+09:00"
---

# FactorizePhys: Matrix Factorization for Multidimensional Attention in Remote Physiological Sensing

## Abstract
Remote photoplethysmography (rPPG) enables non-invasive extraction of blood volume pulse signals through imaging, transforming spatial-temporal data into time series signals. Advances in end-to-end rPPG approaches have focused on this transformation where attention mechanisms are crucial for feature extraction. However, existing methods compute attention disjointly across spatial, temporal, and channel dimensions. Here, we propose the Factorized Self-Attention Module (FSAM), which jointly computes multidimensional attention from voxel embeddings using nonnegative matrix factorization. To demonstrate FSAM's effectiveness, we developed FactorizePhys, an end-to-end 3D-CNN architecture for estimating blood volume pulse signals from raw video frames. Our approach adeptly factorizes voxel embeddings to achieve comprehensive spatial, temporal, and channel attention, enhancing performance of generic signal extraction tasks. Furthermore, we deploy FSAM within an existing 2D-CNN-based rPPG architecture to illustrate its versatility. FSAM and FactorizePhys are thoroughly evaluated against state-of-the-art rPPG methods, each representing different types of architecture and attention mechanism. We perform ablation studies to investigate the architectural decisions and hyperparameters of FSAM. Experiments on four publicly available datasets and intuitive visualization of learned spatial-temporal features substantiate the effectiveness of FSAM and enhanced cross-dataset generalization in estimating rPPG signals, suggesting its broader potential as a multidimensional attention mechanism. The code is accessible at https://github.com/PhysiologicAILab/FactorizePhys.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Jitesh Joshi, Sos Agaian, Youngjun Cho
- arxiv_id: 
- openreview_id: qrfp4eeZ47
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9abd14b56c34451b8fc9ee44ba4395c988c4d34d.pdf
- published: 2024
- keywords: Time-series estimation, remote photo-plethysmography, spatial-temporal attention, non-negative matrix factorization
