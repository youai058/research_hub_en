---
title: "Transformer-VQ: Linear-Time Transformers via Vector Quantization"
authors: ["Lucas Dax Lingle"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "oDdzXQzP2F"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9dfab016ded80c8754b4868d9dc2a054a8f347b6.pdf"
published: "2024"
categories: []
keywords: ["Transformer", "Transformer Decoder", "Decoder-Only Transformer", "Natural Language Processing", "NLP", "Vector Quantization", "VQ", "K-Means", "Clustering", "Causal Attention", "Autoregressive Attention", "Efficient Attention", "Linear-Time Attention", "Autoregressive Modeling", "Generative Modeling", "Gated Attention", "Compressive Attention", "Kernelized Attention", "Kernelizable Attention", "Hierarchical Attention", "Segment-Level Recurrent Attention", "Long-Context Modeling", "Long-Range Modeling", "Long-Range Dependencies", "Long-Term Dependencies", "Cached Attention", "Shift-Equivariant Attention"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:14+09:00"
---

# Transformer-VQ: Linear-Time Transformers via Vector Quantization

## Abstract
We introduce Transformer-VQ, a decoder-only transformer computing softmax-based dense self-attention in linear time.  Transformer-VQ's efficient attention is enabled by vector-quantized keys and a novel caching mechanism. 
In our large-scale experiments, Transformer-VQ is shown highly competitive in quality, obtaining 0.99 bpb on Enwik8, 26.6 ppl on PG-19, and 3.16 bpb on ImageNet64. In addition, the optimized implementation of Transformer-VQ is over 3x faster than a comparable quadratic-time transformer at sequence length 8k, is over 12x faster at 32k, and can scale to 131k with similar throughput. Code available: \url{https://github.com/transformer-vq/transformer_vq}

## Metadata
- venue: ICLR
- year: 2024
- authors: Lucas Dax Lingle
- arxiv_id: 
- openreview_id: oDdzXQzP2F
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9dfab016ded80c8754b4868d9dc2a054a8f347b6.pdf
- published: 2024
- keywords: Transformer, Transformer Decoder, Decoder-Only Transformer, Natural Language Processing, NLP, Vector Quantization, VQ, K-Means, Clustering, Causal Attention, Autoregressive Attention, Efficient Attention, Linear-Time Attention, Autoregressive Modeling, Generative Modeling, Gated Attention, Compressive Attention, Kernelized Attention, Kernelizable Attention, Hierarchical Attention, Segment-Level Recurrent Attention, Long-Context Modeling, Long-Range Modeling, Long-Range Dependencies, Long-Term Dependencies, Cached Attention, Shift-Equivariant Attention
