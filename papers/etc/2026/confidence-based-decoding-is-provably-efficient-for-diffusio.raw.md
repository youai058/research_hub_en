---
title: "Confidence-Based Decoding is Provably Efficient for Diffusion Language Models"
authors: ["Changxiao Cai", "Gen Li"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.22248"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.22248v1"
published: "2026-03-23"
categories: ["cs.LG", "cs.AI", "cs.IT", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# Confidence-Based Decoding is Provably Efficient for Diffusion Language Models

## Abstract
Diffusion language models (DLMs) have emerged as a promising alternative to autoregressive (AR) models for language modeling, allowing flexible generation order and parallel generation of multiple tokens. However, this flexibility introduces a challenge absent in AR models: the \emph{decoding strategy} -- which determines the order and number of tokens generated at each iteration -- critically affects sampling efficiency. Among decoding strategies explored in practice, confidence-based methods, which adaptively select which and how many tokens to unmask based on prediction confidence, have shown strong empirical performance. Despite this success, our theoretical understanding of confidence-based decoding remains limited.
  In this work, we develop the first theoretical analysis framework for confidence-based decoding in DLMs. We focus on an entropy sum-based strategy that continues unmasking tokens within each iteration until the cumulative entropy exceeds a threshold, and show that it achieves $\varepsilon$-accurate sampling in KL divergence with an expected number of iterations $\widetilde O(H(X_0)/\varepsilon)$, where $H(X_0)$ denotes the entropy of the target data distribution. Notably, this strategy yields substantial sampling acceleration when the data distribution has low entropy relative to the sequence length, while automatically adapting to the intrinsic complexity of data without requiring prior knowledge or hyperparameter tuning. Overall, our results provide a theoretical foundation for confidence-based decoding and may inform the design of more efficient decoding strategies for DLMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Changxiao Cai, Gen Li
- arxiv_id: 2603.22248
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.22248v1
- published: 2026-03-23
