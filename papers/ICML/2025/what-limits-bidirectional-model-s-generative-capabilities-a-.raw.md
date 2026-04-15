---
title: "What Limits Bidirectional Model's Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning"
authors: ["Zuchao Li", "Yonghua Hei", "Qiwei Li", "Lefei Zhang", "Ping Wang", "hai zhao", "Baoyuan Qi", "Liu Guoming"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kPqvx2mvec"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9155144240c8efce67103a9c3e8f02a319b25da9.pdf"
published: "2025"
categories: []
keywords: ["Large Language Model", "Bidirectional Modeling", "Causal Attention"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:31+09:00"
---

# What Limits Bidirectional Model's Generative Capabilities? A Uni-Bi-Directional Mixture-of-Expert Method For Bidirectional Fine-tuning

## Abstract
Large Language Models (LLMs) excel in generation tasks, yet their causal attention mechanisms limit performance in embedding tasks. While bidirectional modeling may enhance embeddings, naively fine-tuning unidirectional models bidirectionally severely degrades generative performance.
To investigate this trade-off, we analyze attention weights as dependence indicators and find that bidirectional fine-tuning increases subsequent dependence, impairing unidirectional generation. Through systematic Transformer module evaluations, we discover the FFN layer is least affected by such dependence.  Leveraging this discovery, we propose UBMoE-LLM, a novel Uni-Bi-directional Mixture-of-Experts LLM, which integrates the original unidirectional FFN with a bidirectionally fine-tuned FFN via unsupervised contrastive learning.  This MoE-based approach enhances embedding performance while preserving robust generation.
Extensive experiments across diverse datasets and model scales validate our attention dependence metric and demonstrate UBMoE-LLM’s superior generative quality and reduced hallucination. Code is available at: https://github.com/heiyonghua/ubmoe_llm.

## Metadata
- venue: ICML
- year: 2025
- authors: Zuchao Li, Yonghua Hei, Qiwei Li, Lefei Zhang, Ping Wang, hai zhao, Baoyuan Qi, Liu Guoming
- arxiv_id: 
- openreview_id: kPqvx2mvec
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9155144240c8efce67103a9c3e8f02a319b25da9.pdf
- published: 2025
- keywords: Large Language Model, Bidirectional Modeling, Causal Attention
