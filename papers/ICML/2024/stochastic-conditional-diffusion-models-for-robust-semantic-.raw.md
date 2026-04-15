---
title: "Stochastic Conditional Diffusion Models for Robust Semantic Image Synthesis"
authors: ["Juyeon Ko", "Inho Kong", "Dogyun Park", "Hyunwoo J. Kim"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rMV86cAOh6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1f193a9499d8778ecbfc6abed41d7501451f7d83.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:48+09:00"
---

# Stochastic Conditional Diffusion Models for Robust Semantic Image Synthesis

## Abstract
Semantic image synthesis (SIS) is a task to generate realistic images corresponding to semantic maps (labels). However, in real-world applications, SIS often encounters noisy user inputs. To address this, we propose Stochastic Conditional Diffusion Model (SCDM), which is a robust conditional diffusion model that features novel forward and generation processes tailored for SIS with noisy labels. It enhances robustness by stochastically perturbing the semantic label maps through Label Diffusion, which diffuses the labels with discrete diffusion. Through the diffusion of labels, the noisy and clean semantic maps become similar as the timestep increases, eventually becoming identical at $t=T$. This facilitates the generation of an image close to a clean image, enabling robust generation. Furthermore, we propose a class-wise noise schedule to differentially diffuse the labels depending on the class. We demonstrate that the proposed method generates high-quality samples through extensive experiments and analyses on benchmark datasets, including a novel experimental setup simulating human errors during real-world applications. Code is available at https://github.com/mlvlab/SCDM.

## Metadata
- venue: ICML
- year: 2024
- authors: Juyeon Ko, Inho Kong, Dogyun Park, Hyunwoo J. Kim
- arxiv_id: 
- openreview_id: rMV86cAOh6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1f193a9499d8778ecbfc6abed41d7501451f7d83.pdf
- published: 2024
