---
title: "Masked Diffusion Models are Secretly Learned-Order Autoregressive Models"
authors: ["Prateek Garg", "Bhavya Kohli", "Sunita Sarawagi"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.19152"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.19152v1"
published: "2025-11-24"
categories: ["cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:19+09:00"
---

# Masked Diffusion Models are Secretly Learned-Order Autoregressive Models

## Abstract
Masked Diffusion Models (MDMs) have emerged as one of the most promising paradigms for generative modeling over discrete domains. It is known that MDMs effectively train to decode tokens in a random order, and that this ordering has significant performance implications in practice. This observation raises a fundamental question: can we design a training framework that optimizes for a favorable decoding order? We answer this in the affirmative, showing that the continuous-time variational objective of MDMs, when equipped with multivariate noise schedules, can identify and optimize for a decoding order during training. We establish a direct correspondence between decoding order and the multivariate noise schedule and show that this setting breaks invariance of the MDM objective to the noise schedule. Furthermore, we prove that the MDM objective decomposes precisely into a weighted auto-regressive losses over these orders, which establishes them as auto-regressive models with learnable orders.

## Metadata
- venue: arXiv
- year: 2025
- authors: Prateek Garg, Bhavya Kohli, Sunita Sarawagi
- arxiv_id: 2511.19152
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.19152v1
- published: 2025-11-24
