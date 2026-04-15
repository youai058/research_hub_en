---
title: "PipeOffload: Improving Scalability of Pipeline Parallelism with Memory Optimization"
authors: ["Xinyi Wan", "Penghui Qi", "Guangxing Huang", "Min Lin", "Jialin Li"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "O0lxLP4ABD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ef566bb5803ddb4e559eb45149494fdbf75a85d2.pdf"
published: "2025"
categories: []
keywords: ["LLM Training", "Pipeline Parallelism", "Offloading", "Memory Optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:19+09:00"
---

# PipeOffload: Improving Scalability of Pipeline Parallelism with Memory Optimization

## Abstract
Pipeline parallelism (PP) is widely used for training large language models (LLMs), yet its scalability is often constrained by high activation memory consumption as the number of in-flight microbatches grows with the degree of PP. In this paper, we focus on addressing this challenge by leveraging the under-explored memory offload strategy in PP. With empirical study, we discover that in the majority of standard configurations, at least half, and potentially all, of the activations can be offloaded with negligible overhead. In the cases where full overload is not possible, we introduce a novel selective offload strategy that decreases peak activation memory in a better-than-linear manner. Furthermore, we integrate memory offload with other techniques to jointly consider overall throughput and memory limitation. Our experiments proves that the per-device activation memory effectively reduces with the total number of stages, making PP a stronger alternative than TP, offering up to a 19\% acceleration with even lower memory consumption.

## Metadata
- venue: ICML
- year: 2025
- authors: Xinyi Wan, Penghui Qi, Guangxing Huang, Min Lin, Jialin Li
- arxiv_id: 
- openreview_id: O0lxLP4ABD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ef566bb5803ddb4e559eb45149494fdbf75a85d2.pdf
- published: 2025
- keywords: LLM Training, Pipeline Parallelism, Offloading, Memory Optimization
