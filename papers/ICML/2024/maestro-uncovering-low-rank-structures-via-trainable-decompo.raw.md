---
title: "Maestro: Uncovering Low-Rank Structures via Trainable Decomposition"
authors: ["Samuel Horváth", "Stefanos Laskaridis", "Shashank Rajput", "Hongyi Wang"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "7bjyambg4x"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/303660dd43c880c9fd381ccbd592ac368124e991.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:18+09:00"
---

# Maestro: Uncovering Low-Rank Structures via Trainable Decomposition

## Abstract
Deep Neural Networks (DNNs) have been a large driver for AI breakthroughs in recent years, ranging from self-driving cars to intelligent assistants. However, these models have been getting increasingly large as they become more accurate and safe. This means that their training becomes increasingly costly and time-consuming, and typically yields a single model to fit all targets. To mitigate this, various techniques have been proposed in the literature, including pruning, sparsification or quantization of the model weights and updates. While achieving high compression rates, they often incur significant computational overheads at training or lead to non-negligible accuracy penalty. Alternatively, factorization methods have been leveraged for low-rank compression of DNNs. Similarly, such techniques (e.g., SVD) frequently rely on heavy iterative decompositions of layers and are potentially sub-optimal for non-linear models, such as DNNs. We take a further step in designing efficient low-rank models and propose Maestro, a framework for trainable low-rank layers. Instead of iteratively applying a priori decompositions, the low-rank structure is baked into the training process through LoD, a low-rank ordered decomposition. Not only is this the first time importance ordering via sampling is applied on the decomposed DNN structure, but it also allows selecting ranks at a layer granularity. Our theoretical analysis demonstrates that LoD recovers the SVD decomposition of linear mapping on uniformly distributed data and PCA for linear autoencoders. Applied to DNNs, Maestro enables the extraction of lower footprint models that preserve performance. Simultaneously, it enables the graceful tradeoff between accuracy-latency for deployment to even more constrained devices, without retraining.

## Metadata
- venue: ICML
- year: 2024
- authors: Samuel Horváth, Stefanos Laskaridis, Shashank Rajput, Hongyi Wang
- arxiv_id: 
- openreview_id: 7bjyambg4x
- anthology_id: 
- pdf_url: https://openreview.net/pdf/303660dd43c880c9fd381ccbd592ac368124e991.pdf
- published: 2024
