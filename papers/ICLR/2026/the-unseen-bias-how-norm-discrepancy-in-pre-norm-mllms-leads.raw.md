---
title: "The Unseen Bias: How Norm Discrepancy in Pre-Norm MLLMs Leads to  Visual  Information Loss"
authors: ["Bozhou Li", "Xinda Xue", "Sihan Yang", "Yang Shi", "Xinlong Chen", "Yushuo Guan", "Yuanxing Zhang", "Wentao Zhang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GVVNG2EMQv"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cd2bcc8d97c7444d98fd22ee04529059d6e0641d.pdf"
published: "2026"
categories: []
keywords: ["MultiModal Large Language Model;Pre-Normlization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:21+09:00"
---

# The Unseen Bias: How Norm Discrepancy in Pre-Norm MLLMs Leads to  Visual  Information Loss

## Abstract
Multimodal Large Language Models (MLLMs), which couple pre-trained vision encoders and language models, have shown remarkable capabilities. However, their reliance on the ubiquitous Pre-Norm architecture introduces a subtle yet critical flaw: a severe norm disparity between the high-norm visual tokens and the low-norm text tokens. In this work, we present a formal theoretical analysis demonstrating that this imbalance is not a static issue. Instead, it induces an "asymmetric update dynamic", where high-norm visual tokens exhibit a ''representational inertia,'' causing them to transform semantically much slower than their textual counterparts. This fundamentally impairs effective cross-modal feature fusion. Our empirical validation across a range of mainstream MLLMs confirms that this theoretical dynamic---the persistence of norm disparity and the resulting asymmetric update rates---is a prevalent phenomenon. Based on this insight, we propose a remarkably simple yet effective solution: inserting a single, carefully initialized LayerNorm layer after the visual projector to enforce norm alignment. Experiments conducted on the LLaVA-1.5 architecture show that this intervention yields significant performance gains not only on a wide suite of multimodal benchmarks but also, notably, on text-only evaluations such as MMLU, suggesting that resolving the architectural imbalance leads to a more holistically capable model.

## Metadata
- venue: ICLR
- year: 2026
- authors: Bozhou Li, Xinda Xue, Sihan Yang, Yang Shi, Xinlong Chen, Yushuo Guan, Yuanxing Zhang, Wentao Zhang
- arxiv_id: 
- openreview_id: GVVNG2EMQv
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cd2bcc8d97c7444d98fd22ee04529059d6e0641d.pdf
- published: 2026
- keywords: MultiModal Large Language Model;Pre-Normlization
