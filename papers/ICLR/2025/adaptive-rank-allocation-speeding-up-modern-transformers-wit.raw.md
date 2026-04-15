---
title: "Adaptive Rank Allocation: Speeding Up Modern Transformers with RaNA Adapters"
authors: ["Roberto Garcia", "Jerry Weihong Liu", "Daniel Sorvisto", "Sabri Eyuboglu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uAtDga3q0r"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8b7c7c6efc3f832655b5c2d2a9c5a4305d89d61d.pdf"
published: "2025"
categories: []
keywords: ["Large Language Models", "Adaptive compute", "Rank adapters", "Neuron adapters"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:12+09:00"
---

# Adaptive Rank Allocation: Speeding Up Modern Transformers with RaNA Adapters

## Abstract
Large Language Models (LLMs) are computationally intensive, particularly during inference. Neuron-adaptive techniques, which selectively activate neurons in Multi-Layer Perceptron (MLP) layers, offer some speedups but suffer from limitations in modern Transformers. These include reliance on sparse activations, incompatibility with attention layers, and the use of costly neuron masking techniques. To address these issues, we propose the Adaptive Rank Allocation framework and introduce the Rank and Neuron Allocator (RaNA) adapter. RaNA adapters leverage rank adapters, which operate on linear layers by applying both low-rank matrix decompositions and adaptive masking to efficiently allocate compute without depending on activation sparsity. This enables RaNA to be generally applied to MLPs and linear components of attention modules, while eliminating the need for expensive maskers found in neuron-adaptive methods. Notably, when compared to neuron adapters, RaNA improves perplexity by up to 7 points and increases accuracy by up to 8 percentage-points when reducing FLOPs by $\sim$44\% in state-of-the-art Transformer architectures. These results position RaNA as a robust solution for improving inference efficiency in  modern Transformer architectures.

## Metadata
- venue: ICLR
- year: 2025
- authors: Roberto Garcia, Jerry Weihong Liu, Daniel Sorvisto, Sabri Eyuboglu
- arxiv_id: 
- openreview_id: uAtDga3q0r
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8b7c7c6efc3f832655b5c2d2a9c5a4305d89d61d.pdf
- published: 2025
- keywords: Large Language Models, Adaptive compute, Rank adapters, Neuron adapters
