---
title: "MS$^3$D: A RG Flow-Based Regularization for GAN Training with Limited Data"
authors: ["Jian Wang", "Xin Lan", "Yuxin Tian", "Jiancheng Lv"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "TuALw8xVum"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/20e444c98a5feb3e3811ceb0edae45c113238cba.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:29+09:00"
---

# MS$^3$D: A RG Flow-Based Regularization for GAN Training with Limited Data

## Abstract
Generative adversarial networks (GANs) have made impressive advances in image generation, but they often require large-scale training data to avoid degradation caused by discriminator overfitting. To tackle this issue, we investigate the challenge of training GANs with limited data, and propose a novel regularization method based on the idea of renormalization group (RG) in physics.We observe that in the limited data setting, the gradient pattern that the generator obtains from the discriminator becomes more aggregated over time. In RG context, this aggregated pattern exhibits a high discrepancy from its coarse-grained versions, which implies a high-capacity and sensitive system, prone to overfitting and collapse. To address this problem, we introduce a **m**ulti-**s**cale **s**tructural **s**elf-**d**issimilarity (MS$^3$D) regularization, which constrains the gradient field to have a consistent pattern across different scales, thereby fostering a more redundant and robust system. We show that our method can effectively enhance the performance and stability of GANs under limited data scenarios, and even allow them to generate high-quality images with very few data.

## Metadata
- venue: ICML
- year: 2024
- authors: Jian Wang, Xin Lan, Yuxin Tian, Jiancheng Lv
- arxiv_id: 
- openreview_id: TuALw8xVum
- anthology_id: 
- pdf_url: https://openreview.net/pdf/20e444c98a5feb3e3811ceb0edae45c113238cba.pdf
- published: 2024
