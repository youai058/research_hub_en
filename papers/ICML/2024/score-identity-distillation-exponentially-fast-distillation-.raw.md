---
title: "Score identity Distillation: Exponentially Fast Distillation of Pretrained Diffusion Models for One-Step Generation"
authors: ["Mingyuan Zhou", "Huangjie Zheng", "Zhendong Wang", "Mingzhang Yin", "Hai Huang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "QhqQJqe0Wq"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/722f66081ab5933b5ca43310101c50d837c36ddd.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:46+09:00"
---

# Score identity Distillation: Exponentially Fast Distillation of Pretrained Diffusion Models for One-Step Generation

## Abstract
We introduce Score identity Distillation (SiD), an innovative data-free method that distills the generative capabilities of pretrained diffusion models into a single-step generator. SiD not only facilitates an exponentially fast reduction in Fréchet inception distance (FID) during distillation but also approaches or even exceeds the FID performance of the original teacher diffusion models. By reformulating forward diffusion processes as semi-implicit distributions, we leverage three score-related identities to create an innovative loss mechanism. This mechanism achieves rapid FID reduction by training the generator using its own synthesized images, eliminating the need for real data or reverse-diffusion-based generation, all accomplished within significantly shortened generation time. Upon evaluation across four benchmark datasets, the SiD algorithm demonstrates high iteration efficiency during distillation and surpasses competing distillation approaches, whether they are one-step or few-step, data-free, or dependent on training data, in terms of generation quality. This achievement not only redefines the benchmarks for efficiency and effectiveness in diffusion distillation but also in the broader field of diffusion-based generation. The PyTorch implementation is available at https://github.com/mingyuanzhou/SiD.

## Metadata
- venue: ICML
- year: 2024
- authors: Mingyuan Zhou, Huangjie Zheng, Zhendong Wang, Mingzhang Yin, Hai Huang
- arxiv_id: 
- openreview_id: QhqQJqe0Wq
- anthology_id: 
- pdf_url: https://openreview.net/pdf/722f66081ab5933b5ca43310101c50d837c36ddd.pdf
- published: 2024
