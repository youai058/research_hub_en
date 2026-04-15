---
title: "RTop-K: Ultra-Fast Row-Wise Top-K Selection for Neural Network Acceleration on GPUs"
authors: ["Xi Xie", "Yuebo Luo", "Hongwu Peng", "Caiwen Ding"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "PHg4rAXFVH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dd458214d8ab9259ee817a3caa21a7cfb0180c33.pdf"
published: "2025"
categories: []
keywords: ["row-wise topk selection", "GPU", "CUDA"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:10+09:00"
---

# RTop-K: Ultra-Fast Row-Wise Top-K Selection for Neural Network Acceleration on GPUs

## Abstract
Abstract Top-k selection algorithms are fundamental in a wide range of applications, including high-performance computing, information retrieval, big data processing, and neural network model training. In this paper, we present RTop-K, a highly efficient parallel row-wise top-k selection algorithm specifically designed for GPUs. RTop-K leverages a binary search-based approach to optimize row-wise top-k selection, providing a scalable and accelerated solution.
We conduct a detailed analysis of early stopping in our algorithm, showing that it effectively maintains the testing accuracy of neural network models while substantially improving performance. Our GPU implementation of RTop-K demonstrates superior performance over state-of-the-art row-wise top-k GPU implementations, achieving an average speed-up of up to 11.49× with early stopping and 7.29× without early stopping. Moreover, RTop-K accelerates the overall training workflow of MaxK-GNNs, delivering speed-ups ranging from 11.97% to 33.29% across different models and datasets.

## Metadata
- venue: ICLR
- year: 2025
- authors: Xi Xie, Yuebo Luo, Hongwu Peng, Caiwen Ding
- arxiv_id: 
- openreview_id: PHg4rAXFVH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dd458214d8ab9259ee817a3caa21a7cfb0180c33.pdf
- published: 2025
- keywords: row-wise topk selection, GPU, CUDA
