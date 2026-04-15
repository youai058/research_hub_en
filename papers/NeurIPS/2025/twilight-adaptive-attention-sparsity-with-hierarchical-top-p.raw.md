---
title: "Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$  Pruning"
authors: ["Chaofan Lin", "Jiaming Tang", "Shuo Yang", "Hanshuo Wang", "Tian Tang", "Boyu Tian", "Ion Stoica", "Song Han", "Mingyu Gao"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Ve693NkzcU"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d63b27c7918827915ee716011ba51753540879dd.pdf"
published: "2025"
categories: []
keywords: ["Large Language Model", "Sparse Attention", "Decode", "KV Cache"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:25+09:00"
---

# Twilight: Adaptive Attention Sparsity with Hierarchical Top-$p$  Pruning

## Abstract
Leveraging attention sparsity to accelerate long-context large language models (LLMs) has been of great importance recently. However, most existing sparse attention algorithms use a fixed budget of how many tokens to use in their computations. This simple static decision raises critical issues in real-world deployment because it fails to account for the dynamic nature of real-world scenarios, where the optimal balance between accuracy and efficiency can vary greatly. 
In this paper, we reveal a key insight that leveraging the idea of top-$p$ sampling (a.k.a., nucleus sampling) in sparse attention could enable efficient and adaptive budget decisions. Based on this, we propose Twilight, a framework that enhances any existing sparse attention algorithm with adaptive budget decision capabilities without sacrificing accuracy. 
Empirical results show that Twilight can adaptively prune up to 98% tokens with nearly no accuracy loss in both mid- and long-context scenarios, leading to a $1.4\times$ speedup over state-of-the-art sparse attention mechanisms.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Chaofan Lin, Jiaming Tang, Shuo Yang, Hanshuo Wang, Tian Tang, Boyu Tian, Ion Stoica, Song Han, Mingyu Gao
- arxiv_id: 
- openreview_id: Ve693NkzcU
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d63b27c7918827915ee716011ba51753540879dd.pdf
- published: 2025
- keywords: Large Language Model, Sparse Attention, Decode, KV Cache
