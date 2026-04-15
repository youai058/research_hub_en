---
title: "TRAC: Tensor-Train based Across-layer Compression for Parameter-Efficient Fine-Tuning"
authors: ["Bangguo Ye", "Yuanwei Zhang", "Xiaoqun Zhang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tz5yPWZp9W"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e3dffe696fb4ca7ad56c5a441f9d5d88aaa8d6b9.pdf"
published: "2026"
categories: []
keywords: ["Parameter-efficient fine-tuning", "Low-rank adaptation", "Tensor decomposition"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:30+09:00"
---

# TRAC: Tensor-Train based Across-layer Compression for Parameter-Efficient Fine-Tuning

## Abstract
Fine-tuning large pre-trained models under resource constraints remains challenging due to the massive number of parameters involved. Existing parameter-efficient tuning methods, such as low-rank adaptation (LoRA) and its variants, rely heavily on matrix factorization and often struggle in extremely low-parameter regimes. In this work, we propose TRAC, a novel fine-tuning framework that leverages Tensor-Train decomposition with Across-layer Compression. Specifically, TRAC represents each adaptation module as a compact sequence of tensor-train cores and allows certain cores to be frozen or shared across layers, thereby exploiting the inherent similarity and redundancy among layer weight matrices. To retain layer-specific flexibility, lightweight controllers are introduced, enabling shared tensor cores to adaptively modulate representations. We evaluate TRAC on diverse architectures, including Qwen, LLaMA, GPT, BERT, and ViT, across benchmarks covering text classification, text generation, and image classification. Experimental results demonstrate that TRAC achieves performance comparable to or better than LoRA and its variants, while substantially reducing trainable parameters and storage requirements.

## Metadata
- venue: ICLR
- year: 2026
- authors: Bangguo Ye, Yuanwei Zhang, Xiaoqun Zhang
- arxiv_id: 
- openreview_id: tz5yPWZp9W
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e3dffe696fb4ca7ad56c5a441f9d5d88aaa8d6b9.pdf
- published: 2026
- keywords: Parameter-efficient fine-tuning, Low-rank adaptation, Tensor decomposition
