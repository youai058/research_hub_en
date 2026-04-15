---
title: "Plastic Learning with Deep Fourier Features"
authors: ["Alex Lewandowski", "Dale Schuurmans", "Marlos C. Machado"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "NIkfix2eDQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2ba80613704373b450ab7c2b997b3d70e9be3fbe.pdf"
published: "2025"
categories: []
keywords: ["Fourier", "plasticity", "neural networks", "continual learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:18+09:00"
---

# Plastic Learning with Deep Fourier Features

## Abstract
Deep neural networks can struggle to learn continually in the face of non-stationarity, a
  phenomenon known as loss of plasticity.
  In this paper, we identify underlying principles that lead to plastic algorithms.
  We provide theoretical results showing that linear function approximation, as well as a special case of deep linear networks, do not suffer from loss of plasticity.
  We then propose deep Fourier features, which are the concatenation of a sine and cosine in every layer, and we show that this combination provides a dynamic balance between the trainability obtained through linearity and the effectiveness obtained through the nonlinearity of neural networks.
  Deep networks composed entirely of deep Fourier features are highly trainable and sustain their trainability over the course of learning.
  Our empirical results show that continual learning performance can be improved by replacing ReLU activations with deep Fourier features combined with regularization.
  These results hold for different continual learning scenarios (e.g., label noise, class incremental learning, pixel permutations)
  on all major supervised learning datasets used for continual learning research, such as CIFAR10, CIFAR100, and tiny-ImageNet.

## Metadata
- venue: ICLR
- year: 2025
- authors: Alex Lewandowski, Dale Schuurmans, Marlos C. Machado
- arxiv_id: 
- openreview_id: NIkfix2eDQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2ba80613704373b450ab7c2b997b3d70e9be3fbe.pdf
- published: 2025
- keywords: Fourier, plasticity, neural networks, continual learning
