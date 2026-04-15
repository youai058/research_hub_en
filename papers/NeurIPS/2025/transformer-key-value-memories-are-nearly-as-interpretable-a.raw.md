---
title: "Transformer Key-Value Memories Are Nearly as Interpretable as Sparse Autoencoders"
authors: ["Mengyu Ye", "Jun Suzuki", "Tatsuro Inaba", "Tatsuki Kuribayashi"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2TKEGTfQBd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/adec8dec1b058f333782bd49d8e0eb087317ba82.pdf"
published: "2025"
categories: []
keywords: ["interpretability", "key-value memories", "sparse autoencoders"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:36+09:00"
---

# Transformer Key-Value Memories Are Nearly as Interpretable as Sparse Autoencoders

## Abstract
Recent interpretability work on large language models (LLMs) has been increasingly dominated by a feature-discovery approach with the help of proxy modules. Then, the quality of features learned by, e.g., sparse auto-encoders (SAEs), is evaluated.
This paradigm naturally raises a critical question: do such learned features have better properties than those already represented within the original model parameters, and unfortunately, only a few studies have made such comparisons systematically so far.
In this work, we revisit the interpretability of feature vectors stored in feed-forward (FF) layers, given the perspective of FF as key-value memories, with modern interpretability benchmarks.
Our extensive evaluation revealed that SAE and FFs exhibits a similar range of interpretability, although SAEs displayed an observable but minimal improvement in some aspects. 
Furthermore, in certain aspects, surprisingly, even vanilla FFs yielded better interpretability than the SAEs, and features discovered in SAEs and FFs diverged.
These bring questions about the advantage of SAEs from both perspectives of feature quality and faithfulness, compared to directly interpreting FF feature vectors, and FF key-value parameters serve as a strong baseline in modern interpretability research.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Mengyu Ye, Jun Suzuki, Tatsuro Inaba, Tatsuki Kuribayashi
- arxiv_id: 
- openreview_id: 2TKEGTfQBd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/adec8dec1b058f333782bd49d8e0eb087317ba82.pdf
- published: 2025
- keywords: interpretability, key-value memories, sparse autoencoders
