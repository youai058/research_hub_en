---
title: "µnit Scaling: Simple and Scalable FP8 LLM Training"
authors: ["Saaketh Narayan", "Abhay Gupta", "Mansheej Paul", "Davis Blalock"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "qOLjAhxZgm"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3f76dc52b247683c5b3a28300c98cd94347c9ead.pdf"
published: "2025"
categories: []
keywords: ["LLM", "FP8", "Transformer", "Model Training", "Attention"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:32+09:00"
---

# µnit Scaling: Simple and Scalable FP8 LLM Training

## Abstract
Large language model training with 8-bit floating point (FP8) formats promises significant efficiency improvements, but reduced numerical precision makes training challenging. It is currently possible to train in FP8 only if one is willing to tune various hyperparameters, reduce model scale, or accept the overhead of computing dynamic scale factors. We demonstrate simple, scalable FP8 training that requires no dynamic scaling factors or special hyperparameters, even at large model sizes. Our method, \textit{µnit Scaling (µS)}, also enables simple hyperparameter transfer across model widths, matched numerics across training and inference, and other desirable properties. µnit Scaling is straightforward to implement, consisting of a set of minimal interventions based on a first-principles analysis of transformer operations. We validate our method by training models with parameters ranging from 1B to 13B, performing all hidden linear layer computations in FP8. We achieve quality equal to higher-precision baselines while also training up to 33% faster.

## Metadata
- venue: ICML
- year: 2025
- authors: Saaketh Narayan, Abhay Gupta, Mansheej Paul, Davis Blalock
- arxiv_id: 
- openreview_id: qOLjAhxZgm
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3f76dc52b247683c5b3a28300c98cd94347c9ead.pdf
- published: 2025
- keywords: LLM, FP8, Transformer, Model Training, Attention
