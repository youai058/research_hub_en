---
title: "LeFusion: Controllable Pathology Synthesis via Lesion-Focused Diffusion Models"
authors: ["Hantao Zhang", "Yuhe Liu", "Jiancheng Yang", "Shouhong Wan", "Xinyuan Wang", "Wei Peng", "Pascal Fua"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2403.14066"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2403.14066v2"
published: "2024-03-21"
categories: ["eess.IV", "cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# LeFusion: Controllable Pathology Synthesis via Lesion-Focused Diffusion Models

## Abstract
Patient data from real-world clinical practice often suffers from data scarcity and long-tail imbalances, leading to biased outcomes or algorithmic unfairness. This study addresses these challenges by generating lesion-containing image-segmentation pairs from lesion-free images. Previous efforts in medical imaging synthesis have struggled with separating lesion information from background, resulting in low-quality backgrounds and limited control over the synthetic output. Inspired by diffusion-based image inpainting, we propose LeFusion, a lesion-focused diffusion model. By redesigning the diffusion learning objectives to focus on lesion areas, we simplify the learning process and improve control over the output while preserving high-fidelity backgrounds by integrating forward-diffused background contexts into the reverse diffusion process. Additionally, we tackle two major challenges in lesion texture synthesis: 1) multi-peak and 2) multi-class lesions. We introduce two effective strategies: histogram-based texture control and multi-channel decomposition, enabling the controlled generation of high-quality lesions in difficult scenarios. Furthermore, we incorporate lesion mask diffusion, allowing control over lesion size, location, and boundary, thus increasing lesion diversity. Validated on 3D cardiac lesion MRI and lung nodule CT datasets, LeFusion-generated data significantly improves the performance of state-of-the-art segmentation models, including nnUNet and SwinUNETR. Code and model are available at https://github.com/M3DV/LeFusion.

## Metadata
- venue: arXiv
- year: 2024
- authors: Hantao Zhang, Yuhe Liu, Jiancheng Yang, Shouhong Wan, Xinyuan Wang, Wei Peng, Pascal Fua
- arxiv_id: 2403.14066
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2403.14066v2
- published: 2024-03-21
