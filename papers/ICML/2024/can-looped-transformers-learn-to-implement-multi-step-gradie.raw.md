---
title: "Can Looped Transformers Learn to Implement Multi-step Gradient Descent for In-context Learning?"
authors: ["Khashayar Gatmiry", "Nikunj Saunshi", "Sashank J. Reddi", "Stefanie Jegelka", "Sanjiv Kumar"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "o8AaRKbP9K"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/65f94d6355d2a69eaeabf88485e6104e8d041197.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:35+09:00"
---

# Can Looped Transformers Learn to Implement Multi-step Gradient Descent for In-context Learning?

## Abstract
Transformers to do reasoning and few-shot learning, without any fine-tuning, is widely conjectured to stem from their ability to implicitly simulate a multi-step algorithms -- such as gradient descent -- with their weights in a single forward pass. Recently, there has been progress in understanding this complex phenomenon from an expressivity point of view, by demonstrating that Transformers can express such multi-step algorithms. However, our knowledge about the more fundamental aspect of its learnability, beyond single layer models, is very limited. In particular, *can training Transformers enable convergence to algorithmic solutions*? In this work we resolve this for in context linear regression with linear looped Transformers -- a multi-layer model with weight sharing that is conjectured to have an inductive bias to learn fix-point iterative algorithms. More specifically, for this setting we show that the global minimizer of the population training loss implements multi-step preconditioned gradient descent, with a preconditioner that adapts to the data distribution. Furthermore, we show a fast convergence for gradient flow on the regression loss, despite the non-convexity of the landscape, by proving a novel gradient dominance condition. To our knowledge, this is the first theoretical analysis for multi-layer Transformer in this setting. We further validate our theoretical findings through synthetic experiments.

## Metadata
- venue: ICML
- year: 2024
- authors: Khashayar Gatmiry, Nikunj Saunshi, Sashank J. Reddi, Stefanie Jegelka, Sanjiv Kumar
- arxiv_id: 
- openreview_id: o8AaRKbP9K
- anthology_id: 
- pdf_url: https://openreview.net/pdf/65f94d6355d2a69eaeabf88485e6104e8d041197.pdf
- published: 2024
