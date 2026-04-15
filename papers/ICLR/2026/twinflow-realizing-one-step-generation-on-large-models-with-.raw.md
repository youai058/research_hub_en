---
title: "TwinFlow: Realizing One-step Generation on Large Models with Self-adversarial Flows"
authors: ["Zhenglin Cheng", "Peng Sun", "Jianguo Li", "Tao Lin"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fBc9v8CVvm"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b65362604a23bf3ea79543a882c67f8d49b1343e.pdf"
published: "2026"
categories: []
keywords: ["few-step generation", "text-to-image generation", "multi-modal generative models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:47+09:00"
---

# TwinFlow: Realizing One-step Generation on Large Models with Self-adversarial Flows

## Abstract
Recent advances in large multi-modal generative models have demonstrated impressive capabilities in multi-modal generation, including image and video generation.
These models are typically built upon multi-step frameworks like diffusion and flow matching, which inherently limits their inference efficiency (requiring 40-100 Number of Function Evaluations (NFEs)).
While various few-step methods aim to accelerate the inference, existing solutions have clear limitations.
Prominent distillation-based methods, such as progressive and consistency distillation, either require an iterative distillation procedure or show significant degradation at very few steps (< 4-NFE).
Meanwhile, integrating adversarial training into distillation (e.g., DMD/DMD2 and SANA-Sprint) to enhance performance introduces training instability, added complexity, and high GPU memory overhead due to the auxiliary trained models.
To this end, we propose TwinFlow, a simple yet effective framework for training 1-step generative models that bypasses the need for distillation from pre-trained models and avoids standard adversarial training, making  it ideal for building large-scale, efficient models.
On text-to-image tasks, our method achieves a GenEval score of 0.83 in 1-NFE, outperforming strong baselines like SANA-Sprint (a GAN loss-based framework) and RCGM (a consistency-based framework).
**Notably, we demonstrate the scalability of TwinFlow by transforming Qwen-Image-20B---the current largest open-source multi-modal generative model---into an efficient few-step generator**. With just 1-NFE, our approach matches the performance of the original 100-NFE model on both the GenEval and DPG-Bench benchmarks, reducing computational cost by $100\times$ with minor quality degradation.
Our code and models will be made publicly available.

## Metadata
- venue: ICLR
- year: 2026
- authors: Zhenglin Cheng, Peng Sun, Jianguo Li, Tao Lin
- arxiv_id: 
- openreview_id: fBc9v8CVvm
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b65362604a23bf3ea79543a882c67f8d49b1343e.pdf
- published: 2026
- keywords: few-step generation, text-to-image generation, multi-modal generative models
