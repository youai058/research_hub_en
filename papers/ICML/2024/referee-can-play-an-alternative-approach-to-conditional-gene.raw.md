---
title: "Referee Can Play: An Alternative Approach to Conditional Generation via Model Inversion"
authors: ["Xuantong LIU", "Tianyang Hu", "Wenjia Wang", "Kenji Kawaguchi", "Yuan Yao"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hZ0fWhgVch"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a24fa3e6f02bf1e75586a0204f1d38fd01d2c784.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:12+09:00"
---

# Referee Can Play: An Alternative Approach to Conditional Generation via Model Inversion

## Abstract
As a dominant force in text-to-image generation tasks, Diffusion Probabilistic Models (DPMs) face a critical challenge in controllability, struggling to adhere strictly to complex, multi-faceted instructions. In this work, we aim to address this alignment challenge for conditional generation tasks. First, we provide an alternative view of state-of-the-art DPMs as a way of inverting advanced Vision-Language Models (VLMs). With this formulation, we naturally propose a training-free approach that bypasses the conventional sampling process associated with DPMs. By directly optimizing images with the supervision of discriminative VLMs, the proposed method can potentially achieve a better text-image alignment. As proof of concept, we demonstrate the pipeline with the pre-trained BLIP-2 model and identify several key designs for improved image generation. To further enhance the image fidelity, a Score Distillation Sampling module of Stable Diffusion is incorporated. By carefully balancing the two components during optimization, our method can produce high-quality images with near state-of-the-art performance on T2I-Compbench. The code is available at https://github.com/Pepper-lll/VLMinv.

## Metadata
- venue: ICML
- year: 2024
- authors: Xuantong LIU, Tianyang Hu, Wenjia Wang, Kenji Kawaguchi, Yuan Yao
- arxiv_id: 
- openreview_id: hZ0fWhgVch
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a24fa3e6f02bf1e75586a0204f1d38fd01d2c784.pdf
- published: 2024
