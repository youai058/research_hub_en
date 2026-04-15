---
title: "CNN Kernels Can Be the Best Shapelets"
authors: ["Eric Qu", "Yansen Wang", "Xufang Luo", "Wenqiang He", "Kan Ren", "Dongsheng Li"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "O8ouVV8PjF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/69b308cc2c2320f9051d94361939bb8848074ab0.pdf"
published: "2024"
categories: []
keywords: ["Shapelet", "Covolutional Neural Network", "Time-series"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:20+09:00"
---

# CNN Kernels Can Be the Best Shapelets

## Abstract
Shapelets and CNN are two typical approaches to model time series. Shapelets aim at finding a set of sub-sequences that extract feature-based interpretable shapes, but may suffer from accuracy and efficiency issues. CNN performs well by encoding sequences with a series of hidden representations, but lacks interpretability. In this paper, we demonstrate that shapelets are essentially equivalent to a specific type of CNN kernel with a squared norm and pooling. Based on this finding, we propose ShapeConv, an interpretable CNN layer with its kernel serving as shapelets to conduct time-series modeling tasks in both supervised and unsupervised settings. By incorporating shaping regularization, we enforce the similarity for maximum interpretability. We also find human knowledge can be easily injected to ShapeConv by adjusting its initialization and model performance is boosted with it. Experiments show that ShapeConv can achieve state-of-the-art performance on time-series benchmarks without sacrificing interpretability and controllability.

## Metadata
- venue: ICLR
- year: 2024
- authors: Eric Qu, Yansen Wang, Xufang Luo, Wenqiang He, Kan Ren, Dongsheng Li
- arxiv_id: 
- openreview_id: O8ouVV8PjF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/69b308cc2c2320f9051d94361939bb8848074ab0.pdf
- published: 2024
- keywords: Shapelet, Covolutional Neural Network, Time-series
