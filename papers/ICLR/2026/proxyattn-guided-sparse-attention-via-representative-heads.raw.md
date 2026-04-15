---
title: "ProxyAttn: Guided Sparse Attention via Representative Heads"
authors: ["Yixuan Wang", "Huang He", "Siqi Bao", "Hua Wu", "Haifeng Wang", "Qingfu Zhu", "Wanxiang Che"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "m3HXHQYmZu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6fad8703cb392000cfda3c10d663023352f67e89.pdf"
published: "2026"
categories: []
keywords: ["Efficient LLM", "Sparse Attention"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:30+09:00"
---

# ProxyAttn: Guided Sparse Attention via Representative Heads

## Abstract
The quadratic complexity of attention mechanisms limits the efficiency of Large Language Models (LLMs) on long-text tasks. Recently, methods that dynamically estimate block importance have enabled efficient block sparse attention, leading to significant acceleration in long-text pre-filling of LLMs. However, their block-level coarse-grained estimation inevitably leads to performance degradation at high sparsity ratios. In this work, we propose ProxyAttn, a training-free sparse attention algorithm that achieves token-level estimation by compressing the dimension of attention heads. Based on our observation of the similarity among multiple attention heads in long texts, we use the attention scores of pooled representative heads to approximate the scores for all heads. To account for the varying sparsity among heads, we also propose a block-aware dynamic budget estimation method. By combining the scores from a set of representative heads with a multi-head dynamic budget, we can achieve a more fine-grained block attention evaluation at a low computational cost. Experiments on a variety of mainstream models and extensive benchmarks confirm the underlying similarity among attention heads in long texts. Leveraging a token-level fine-grained estimation, the proposed method achieves substantial gains in performance and efficiency compared to existing methods. More precisely, ProxyAttn can achieve up to 10.3x attention acceleration and 2.4x prefilling acceleration without significant performance loss. Our code is available at https://github.com/wyxstriker/ProxyAttn.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yixuan Wang, Huang He, Siqi Bao, Hua Wu, Haifeng Wang, Qingfu Zhu, Wanxiang Che
- arxiv_id: 
- openreview_id: m3HXHQYmZu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6fad8703cb392000cfda3c10d663023352f67e89.pdf
- published: 2026
- keywords: Efficient LLM, Sparse Attention
