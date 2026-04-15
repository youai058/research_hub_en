---
title: "When Will Gradient Regularization Be Harmful?"
authors: ["Yang Zhao", "Hao Zhang", "Xiuyuan Hu"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "60vC1FY0dZ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c9d36d02b49f47ef4263bc76d1cd028f1655c02a.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:11+09:00"
---

# When Will Gradient Regularization Be Harmful?

## Abstract
Gradient regularization (GR), which aims to penalize the gradient norm atop the loss function, has shown promising results in training modern over-parameterized deep neural networks. However, can we trust this powerful technique? This paper reveals that GR can cause performance degeneration in adaptive optimization scenarios, particularly with learning rate warmup. Our empirical and theoretical analyses suggest this is due to GR inducing instability and divergence in gradient statistics of adaptive optimizers at the initial training stage. Inspired by the warmup heuristic, we propose three GR warmup strategies, each relaxing the regularization effect to a certain extent during the warmup course to ensure the accurate and stable accumulation of gradients. With experiments on Vision Transformer family, we confirm the three GR warmup strategies can effectively circumvent these issues, thereby largely improving the model performance. Meanwhile, we note that scalable models tend to rely more on the GR warmup, where the performance can be improved by up to 3% on Cifar10 compared to baseline GR. Code is available at https://github.com/zhaoyang-0204/gnp.

## Metadata
- venue: ICML
- year: 2024
- authors: Yang Zhao, Hao Zhang, Xiuyuan Hu
- arxiv_id: 
- openreview_id: 60vC1FY0dZ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c9d36d02b49f47ef4263bc76d1cd028f1655c02a.pdf
- published: 2024
