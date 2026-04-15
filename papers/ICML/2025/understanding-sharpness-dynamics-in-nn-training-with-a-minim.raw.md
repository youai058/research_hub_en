---
title: "Understanding Sharpness Dynamics in NN Training with a Minimalist Example: The Effects of Dataset Difficulty, Depth, Stochasticity, and More"
authors: ["Geonhui Yoo", "Minhak Song", "Chulhee Yun"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XfjrLEPOQV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0d04785b006743d2b5f7fff340b0372cfa1904f0.pdf"
published: "2025"
categories: []
keywords: ["progressive sharpening", "sharpness"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:15+09:00"
---

# Understanding Sharpness Dynamics in NN Training with a Minimalist Example: The Effects of Dataset Difficulty, Depth, Stochasticity, and More

## Abstract
When training deep neural networks with gradient descent, sharpness often increases---a phenomenon known as *progressive sharpening*---before saturating at the *edge of stability*. Although commonly observed in practice, the underlying mechanisms behind progressive sharpening remain poorly understood. In this work, we study this phenomenon using a minimalist model: a deep linear network with a single neuron per layer. We show that this simple model effectively captures the sharpness dynamics observed in recent empirical studies, offering a simple testbed to better understand neural network training. Moreover, we theoretically analyze how dataset properties, network depth, stochasticity of optimizers, and step size affect the degree of progressive sharpening in the minimalist model. We then empirically demonstrate how these theoretical insights extend to practical scenarios. This study offers a deeper understanding of sharpness dynamics in neural network training, highlighting the interplay between depth, training data, and optimizers.

## Metadata
- venue: ICML
- year: 2025
- authors: Geonhui Yoo, Minhak Song, Chulhee Yun
- arxiv_id: 
- openreview_id: XfjrLEPOQV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0d04785b006743d2b5f7fff340b0372cfa1904f0.pdf
- published: 2025
- keywords: progressive sharpening, sharpness
