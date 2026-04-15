---
title: "Adversarial Robustness via Deformable Convolution with Stochasticity"
authors: ["Yanxiang Ma", "Zixuan Huang", "Minjing Dong", "Shan You", "Chang Xu"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "vISiVCssVg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c6ee161c913f2e70e35bd649ff8beba9eb20f72c.pdf"
published: "2025"
categories: []
keywords: ["Adversarial Robustness; Mechine Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:25+09:00"
---

# Adversarial Robustness via Deformable Convolution with Stochasticity

## Abstract
Random defense represents a promising strategy to protect neural networks from adversarial attacks. Most of these methods enhance robustness by injecting randomness into the data, increasing uncertainty for attackers.
However, this randomness could reduce the generalization capacity of defense, as defense performance could be sensitive to the hyperparameters of noise added to the data, making it difficult to generalize across different datasets. 
Additionally, the involvement of randomness always comes with a reduction of natural accuracy, which leads to a delicate trade-off between them, which is seldom studied in random defense. In this work, we propose incorporating randomness into the network structure instead of data input by designing stochastic deformable convolution, where a random mask replaces the convolutional offset. This process promotes data independence, enhancing generalization across datasets. To study the trade-off, we conduct a theoretical analysis of both robust and clean accuracy, from a perspective of gradient cosine similarity and natural inference. Based on the analysis, we reformulate the adversarial training in our random defense framework. Extensive experiments show that our method achieves SOTA adversarial robustness and clean accuracy compared with other random defense methods.

## Metadata
- venue: ICML
- year: 2025
- authors: Yanxiang Ma, Zixuan Huang, Minjing Dong, Shan You, Chang Xu
- arxiv_id: 
- openreview_id: vISiVCssVg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c6ee161c913f2e70e35bd649ff8beba9eb20f72c.pdf
- published: 2025
- keywords: Adversarial Robustness; Mechine Learning
