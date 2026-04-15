---
title: "PolySketchFormer: Fast Transformers via Sketching Polynomial Kernels"
authors: ["Praneeth Kacham", "Vahab Mirrokni", "Peilin Zhong"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ghYrfdJfjK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c31152c57f5f0f721f79f67c58c9cd9607e5b509.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:31+09:00"
---

# PolySketchFormer: Fast Transformers via Sketching Polynomial Kernels

## Abstract
The quadratic time and memory complexity inherent to self-attention mechanisms, with respect to sequence length, presents a critical computational bottleneck in the training and deployment of large-scale Transformer-based language models. Recent theoretical results indicate the intractability of sub-quadratic softmax attention approximation under reasonable complexity assumptions. This paper addresses this challenge by first demonstrating that polynomial attention with high degree can effectively replace softmax without sacrificing model quality. Next, we develop polynomial sketching techniques from numerical linear algebra to achieve linear-time polynomial attention with approximation guarantees. Crucially, our approach achieves this speedup without requiring the sparsification of attention matrices. We also present a block-based algorithm to apply causal masking efficiently. Combining these techniques, we provide *PolySketchFormer*, a practical linear-time Transformer architecture for language modeling that offers provable guarantees. We validate PolySketchFormer empirically by training language models capable of handling long contexts. These experiments utilize both synthetic and real-world datasets (PG19, Wikipedia and C4) on Google Cloud TPUs. For context lengths of 32k and GPT-2 style models, our model achieves 2x speedup in training compared to FlashAttention of the fastest configuration, with no observed degradation in quality across our experiments.

## Metadata
- venue: ICML
- year: 2024
- authors: Praneeth Kacham, Vahab Mirrokni, Peilin Zhong
- arxiv_id: 
- openreview_id: ghYrfdJfjK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c31152c57f5f0f721f79f67c58c9cd9607e5b509.pdf
- published: 2024
