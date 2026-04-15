---
title: "MissHDD: Hybrid Deterministic Diffusion for Hetrogeneous Incomplete Data Imputation"
authors: ["Youran Zhou", "Mohamed Reda Bouadjenek", "Sunil Aryal"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.14543"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.14543v1"
published: "2025-11-18"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# MissHDD: Hybrid Deterministic Diffusion for Hetrogeneous Incomplete Data Imputation

## Abstract
Incomplete data are common in real-world tabular applications, where numerical, categorical, and discrete attributes coexist within a single dataset. This heterogeneous structure presents significant challenges for existing diffusion-based imputation models, which typically assume a homogeneous feature space and rely on stochastic denoising trajectories. Such assumptions make it difficult to maintain conditional consistency, and they often lead to information collapse for categorical variables or instability when numerical variables require deterministic updates. These limitations indicate that a single diffusion process is insufficient for mixed-type tabular imputation.
  We propose a hybrid deterministic diffusion framework that separates heterogeneous features into two complementary generative channels. A continuous DDIM-based channel provides efficient and stable deterministic denoising for numerical variables, while a discrete latent-path diffusion channel, inspired by loopholing-based discrete diffusion, models categorical and discrete features without leaving their valid sample manifolds. The two channels are trained under a unified conditional imputation objective, enabling coherent reconstruction of mixed-type incomplete data.
  Extensive experiments on multiple real-world datasets show that the proposed framework achieves higher imputation accuracy, more stable sampling trajectories, and improved robustness across MCAR, MAR, and MNAR settings compared with existing diffusion-based and classical methods. These results demonstrate the importance of structure-aware diffusion processes for advancing deep learning approaches to incomplete tabular data.

## Metadata
- venue: arXiv
- year: 2025
- authors: Youran Zhou, Mohamed Reda Bouadjenek, Sunil Aryal
- arxiv_id: 2511.14543
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.14543v1
- published: 2025-11-18
