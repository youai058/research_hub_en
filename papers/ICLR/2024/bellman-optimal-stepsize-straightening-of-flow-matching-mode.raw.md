---
title: "Bellman Optimal Stepsize Straightening of Flow-Matching Models"
authors: ["Bao Nguyen", "Binh Nguyen", "Viet Anh Nguyen"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Iyve2ycvGZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/49149ffea0255c53a80d017478e79f91b0a6c402.pdf"
published: "2024"
categories: []
keywords: ["flow matching", "generative model", "efficient sampling", "distillation", "responsible ML"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:50+09:00"
---

# Bellman Optimal Stepsize Straightening of Flow-Matching Models

## Abstract
Flow matching is a powerful framework for generating high-quality samples in various applications, especially image synthesis. However, the intensive computational demands of these models, especially during the finetuning process and sampling processes, pose significant challenges for low-resource scenarios. This paper introduces Bellman Optimal Stepsize Straightening (BOSS) technique for distilling flow-matching generative models: it aims specifically for a few-step efficient image sampling while adhering to a computational budget constraint. First, this technique involves a dynamic programming algorithm that optimizes the stepsizes of the pretrained network. Then, it refines the velocity network to match the optimal step sizes, aiming to straighten the generation paths. Extensive experimental evaluations across image generation tasks demonstrate the efficacy of BOSS in terms of both resource utilization and image quality. Our results reveal that BOSS achieves substantial gains in efficiency while maintaining competitive sample quality, effectively bridging the gap between low-resource constraints and the demanding requirements of flow-matching generative models. Our paper also fortifies the responsible development of artificial intelligence, offering a more sustainable generative model that reduces computational costs and environmental footprints. Our code can be found at https://github.com/nguyenngocbaocmt02/BOSS.

## Metadata
- venue: ICLR
- year: 2024
- authors: Bao Nguyen, Binh Nguyen, Viet Anh Nguyen
- arxiv_id: 
- openreview_id: Iyve2ycvGZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/49149ffea0255c53a80d017478e79f91b0a6c402.pdf
- published: 2024
- keywords: flow matching, generative model, efficient sampling, distillation, responsible ML
