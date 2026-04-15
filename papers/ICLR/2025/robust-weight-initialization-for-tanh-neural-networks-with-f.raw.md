---
title: "Robust Weight Initialization for Tanh Neural Networks with Fixed Point Analysis"
authors: ["Hyun woo Lee", "Hayoung Choi", "Hyunju Kim"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Es4RPNDtmq"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/98a97d928200d2a62876799c0c7fd6a5cbe062cb.pdf"
published: "2025"
categories: []
keywords: ["Weight initialization", "Signal propagation", "Physics informed neural networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:06+09:00"
---

# Robust Weight Initialization for Tanh Neural Networks with Fixed Point Analysis

## Abstract
As a neural network's depth increases, it can improve generalization performance. However, training deep networks is challenging due to gradient and signal propagation issues. To address these challenges, extensive theoretical research and various methods have been introduced. Despite these advances, effective weight initialization methods for tanh neural networks remain insufficiently investigated. This paper presents a novel weight initialization method for neural networks with tanh activation function. Based on an analysis of the fixed points of the function $\tanh(ax)$, the proposed method aims to determine values of $a$ that mitigate activation saturation. A series of experiments on various classification datasets and physics-informed neural networks demonstrates that the proposed method outperforms Xavier initialization methods (with or without normalization) in terms of robustness across different network sizes, data efficiency, and convergence speed. Code is available at https://github.com/1HyunwooLee/Tanh-Init.

## Metadata
- venue: ICLR
- year: 2025
- authors: Hyun woo Lee, Hayoung Choi, Hyunju Kim
- arxiv_id: 
- openreview_id: Es4RPNDtmq
- anthology_id: 
- pdf_url: https://openreview.net/pdf/98a97d928200d2a62876799c0c7fd6a5cbe062cb.pdf
- published: 2025
- keywords: Weight initialization, Signal propagation, Physics informed neural networks
