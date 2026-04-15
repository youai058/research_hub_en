---
title: "Hyperbolic Active Learning for Semantic Segmentation under Domain Shift"
authors: ["Luca Franco", "Paolo Mandica", "Konstantinos Kallidromitis", "Devin Guillory", "Yu-Teng Li", "Trevor Darrell", "Fabio Galasso"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hKdJPMQvew"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ac704a67f5d23e6fbea960ffbcf0e6d2e9211655.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:37+09:00"
---

# Hyperbolic Active Learning for Semantic Segmentation under Domain Shift

## Abstract
We introduce a hyperbolic neural network approach to pixel-level active learning for semantic segmentation. Analysis of the data statistics leads to a novel interpretation of the hyperbolic radius as an indicator of data scarcity. In HALO (Hyperbolic Active Learning Optimization), for the first time, we propose the use of epistemic uncertainty as a data acquisition strategy, following the intuition of selecting data points that are the least known. The hyperbolic radius, complemented by the widely-adopted prediction entropy, effectively approximates epistemic uncertainty. We perform extensive experimental analysis based on two established synthetic-to-real benchmarks, i.e. GTAV $\rightarrow$ Cityscapes and SYNTHIA $\rightarrow$ Cityscapes. Additionally, we test HALO on Cityscape $\rightarrow$ ACDC for domain adaptation under adverse weather conditions, and we benchmark both convolutional and attention-based backbones. HALO sets a new state-of-the-art in active learning for semantic segmentation under domain shift and it is the first active learning approach that surpasses the performance of supervised domain adaptation while using only a small portion of labels (i.e., 1%).

## Metadata
- venue: ICML
- year: 2024
- authors: Luca Franco, Paolo Mandica, Konstantinos Kallidromitis, Devin Guillory, Yu-Teng Li, Trevor Darrell, Fabio Galasso
- arxiv_id: 
- openreview_id: hKdJPMQvew
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ac704a67f5d23e6fbea960ffbcf0e6d2e9211655.pdf
- published: 2024
