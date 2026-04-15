---
title: "Rethinking Benign Overfitting in Two-Layer Neural Networks"
authors: ["Ruichen Xu", "Kexin Chen"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Uc0dTE2Wox"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e247731b079ecaf0aa651c2e0e2d51d26f854d7f.pdf"
published: "2025"
categories: []
keywords: ["Benign overfitting", "long-tailed data", "two-layer neural networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:05+09:00"
---

# Rethinking Benign Overfitting in Two-Layer Neural Networks

## Abstract
Recent theoretical studies (Kou et al., 2023; Cao et al., 2022) revealed a sharp phase transition from benign to harmful overfitting when the
noise-to-feature ratio exceeds a threshold—a situation common in long-tailed data distributions where atypical data is prevalent. However, such harmful overfitting rarely happens in overparameterized neural networks. Further experimental results suggested that memorization is necessary for achieving near-optimal generalization error in long-tailed data distributions (Feldman & Zhang, 2020). We argue that this discrepancy between theoretical predictions and empirical observations arises because previous feature-noise data models overlook the heterogeneous nature of noise across different data classes. In this paper, we refine the feature-noise data model by incorporating class-dependent heterogeneous noise and re-examine the overfitting phenomenon in neural networks. Through a comprehensive analysis of the training dynamics, we establish test loss bounds for the refined model. Our findings reveal that neural networks can leverage "data noise" to learn implicit features that improve the classification accuracy for long-tailed data. Our analysis also provides a training-free metric for evaluating data influence on test performance. Experimental validation on both synthetic and real-world datasets supports our theoretical results.

## Metadata
- venue: ICML
- year: 2025
- authors: Ruichen Xu, Kexin Chen
- arxiv_id: 
- openreview_id: Uc0dTE2Wox
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e247731b079ecaf0aa651c2e0e2d51d26f854d7f.pdf
- published: 2025
- keywords: Benign overfitting, long-tailed data, two-layer neural networks
