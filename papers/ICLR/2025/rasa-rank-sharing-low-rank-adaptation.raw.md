---
title: "RaSA: Rank-Sharing Low-Rank Adaptation"
authors: ["Zhiwei He", "Zhaopeng Tu", "Xing Wang", "Xingyu Chen", "Zhijie Wang", "Jiahao Xu", "Tian Liang", "Wenxiang Jiao", "Zhuosheng Zhang", "Rui Wang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "GdXI5zCoAt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/26347c818217d5c434c3eab6d9f6aea95413ae38.pdf"
published: "2025"
categories: []
keywords: ["parameter-efficient fine-tuning", "large language model", "low-rank adaptation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:42+09:00"
---

# RaSA: Rank-Sharing Low-Rank Adaptation

## Abstract
Low-rank adaptation (LoRA) has been prominently employed for parameter-efficient fine-tuning of large language models (LLMs). However, the limited expressive capacity of LoRA, stemming from the low-rank constraint, has been recognized as a bottleneck, particularly in rigorous tasks like code generation and mathematical reasoning. To address this limitation, we introduce Rank-Sharing Low-Rank Adaptation (RaSA), an innovative extension that enhances the expressive capacity of LoRA by leveraging partial rank sharing across layers. By forming a shared rank pool and applying layer-specific weighting, RaSA effectively increases the number of ranks without augmenting parameter overhead. Our theoretically grounded and empirically validated approach demonstrates that RaSA not only maintains the core advantages of LoRA but also significantly boosts performance in challenging code and math tasks. Code, data and scripts are available at: https://github.com/zwhe99/RaSA.

## Metadata
- venue: ICLR
- year: 2025
- authors: Zhiwei He, Zhaopeng Tu, Xing Wang, Xingyu Chen, Zhijie Wang, Jiahao Xu, Tian Liang, Wenxiang Jiao, Zhuosheng Zhang, Rui Wang
- arxiv_id: 
- openreview_id: GdXI5zCoAt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/26347c818217d5c434c3eab6d9f6aea95413ae38.pdf
- published: 2025
- keywords: parameter-efficient fine-tuning, large language model, low-rank adaptation
