---
title: "Activation by Interval-wise Dropout: A Simple Way to Prevent Neural Networks from Plasticity Loss"
authors: ["Sangyeon Park", "Isaac Han", "Seungwon Oh", "KyungJoong Kim"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Y0hjl4L1ve"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/95beb7633cf84695d507830aba0407601b117ca3.pdf"
published: "2025"
categories: []
keywords: ["loss of plasticity", "plasticity", "continual learning", "reinforcement learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:42+09:00"
---

# Activation by Interval-wise Dropout: A Simple Way to Prevent Neural Networks from Plasticity Loss

## Abstract
Plasticity loss, a critical challenge in neural network training, limits a model's ability to adapt to new tasks or shifts in data distribution. While widely used techniques like L2 regularization and Layer Normalization have proven effective in mitigating this issue, Dropout remains notably ineffective. This paper introduces AID (Activation by Interval-wise Dropout), a novel method inspired by Dropout, designed to address plasticity loss. Unlike Dropout, AID generates subnetworks by applying Dropout with different probabilities on each preactivation interval. Theoretical analysis reveals that AID regularizes the network, promoting behavior analogous to that of deep linear networks, which do not suffer from plasticity loss. We validate the effectiveness of AID in maintaining plasticity across various benchmarks, including continual learning tasks on standard image classification datasets such as CIFAR10, CIFAR100, and TinyImageNet. Furthermore, we show that AID enhances reinforcement learning performance in the Arcade Learning Environment benchmark.

## Metadata
- venue: ICML
- year: 2025
- authors: Sangyeon Park, Isaac Han, Seungwon Oh, KyungJoong Kim
- arxiv_id: 
- openreview_id: Y0hjl4L1ve
- anthology_id: 
- pdf_url: https://openreview.net/pdf/95beb7633cf84695d507830aba0407601b117ca3.pdf
- published: 2025
- keywords: loss of plasticity, plasticity, continual learning, reinforcement learning
