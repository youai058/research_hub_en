---
title: "Multi-Feature Quantized Self-Attention for Fair Large Language Models"
authors: ["Jaeil Park", "Sung-Bae Cho"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0UvgQxsi7S"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3a678c2076fde37f16069525ca66c4f1a70d0809.pdf"
published: "2026"
categories: []
keywords: ["Large language models", "multi-attribute social bias", "quantized adversarial autoencoder"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:37+09:00"
---

# Multi-Feature Quantized Self-Attention for Fair Large Language Models

## Abstract
Large language models (LLMs) often encode social biases tied to sensitive features such as race and gender, undermining fairness in downstream tasks even after instruction tuning. Conventional debiasing methods require expensive fine-tuning, are tied to specific architectures, or operate only at the input or decoding stage while neglecting attention-level representations, which can result in compromised task performance. Moreover, most approaches are tailored to single-attribute settings and do not explicitly address scenarios with multiple, overlapping protected attributes and their intersections. This paper proposes a novel method of multi-feature quantized attention regularization (MQAR) to mitigate multi-feature bias by injecting a structured quantization into frozen self-attention layers. MQAR disentangles attribute-specific activations through vector-quantized regularization and uses a discriminator-guided autoencoding regularizer to adversarially suppress protected-attribute information while preserving task-relevant semantics. Crucially, the proposed method operates without modifying the backbone parameters or accessing pre-training data, ensuring architecture-agnostic applicability and minimizing representation distortion. MQAR is evaluated on five diverse LLMs (BERT, T5, GPT-Neo, Mixtral, and LLaMA 3.2) using three standard bias benchmarks (WinoBias, StereoSet, and CrowS-Pairs). Across these models, MQAR consistently reduces bias for multiple protected attributes and their intersections while maintaining downstream accuracy within at most 0.4 \%, on average, of non-debiased baselines on sentiment analysis, abusive language detection, and text generation tasks. These findings highlight quantized attention regularization as a scalable and effective method for mitigating social bias in modern language models.

## Metadata
- venue: ICLR
- year: 2026
- authors: Jaeil Park, Sung-Bae Cho
- arxiv_id: 
- openreview_id: 0UvgQxsi7S
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3a678c2076fde37f16069525ca66c4f1a70d0809.pdf
- published: 2026
- keywords: Large language models, multi-attribute social bias, quantized adversarial autoencoder
