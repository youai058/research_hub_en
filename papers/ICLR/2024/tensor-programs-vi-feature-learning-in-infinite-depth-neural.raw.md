---
title: "Tensor Programs VI: Feature Learning in Infinite Depth Neural Networks"
authors: ["Greg Yang", "Dingli Yu", "Chen Zhu", "Soufiane Hayou"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "17pVDnpwwl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a2d69b77708b87f741baac0303581cfb7924d0b7.pdf"
published: "2024"
categories: []
keywords: ["Tensor Programs", "mup", "deep learning", "optimization", "optimal hyperparameter transfer"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:21+09:00"
---

# Tensor Programs VI: Feature Learning in Infinite Depth Neural Networks

## Abstract
Empirical studies have consistently demonstrated that increasing the size of neural networks often yields superior performance in practical applications. However, there is a lack of consensus regarding the appropriate scaling strategy, particularly when it comes to increasing the depth of neural networks. In practice, excessively large depths can lead to model performance degradation. In this paper, we introduce Depth-$\mu$P, a principled approach for depth scaling, allowing for the training of arbitrarily deep architectures while maximizing feature learning and diversity among nearby layers. Our method involves dividing the contribution of each residual block and the parameter update by the square root of the depth. Through the use of Tensor Programs, we rigorously establish the existence of a limit for infinitely deep neural networks under the proposed scaling scheme. This scaling strategy ensures more stable training for deep neural networks and guarantees the transferability of hyperparameters from shallow to deep models. To substantiate the efficacy of our scaling method, we conduct empirical validation on neural networks with depths up to $2^{10}$.

## Metadata
- venue: ICLR
- year: 2024
- authors: Greg Yang, Dingli Yu, Chen Zhu, Soufiane Hayou
- arxiv_id: 
- openreview_id: 17pVDnpwwl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a2d69b77708b87f741baac0303581cfb7924d0b7.pdf
- published: 2024
- keywords: Tensor Programs, mup, deep learning, optimization, optimal hyperparameter transfer
