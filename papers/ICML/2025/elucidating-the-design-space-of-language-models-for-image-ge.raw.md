---
title: "Elucidating the design space of language models for image generation"
authors: ["Xuantong LIU", "Shaozhe Hao", "Xianbiao Qi", "Tianyang Hu", "Jun Wang", "Rong Xiao", "Yuan Yao"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "EIfCH9OgjR"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/28a2edcfdf09690ba809b2a17b0348b56fda2f4d.pdf"
published: "2025"
categories: []
keywords: ["Image generation", "Large language model", "Generative model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:18+09:00"
---

# Elucidating the design space of language models for image generation

## Abstract
The success of large language models (LLMs) in text generation has inspired their application to image generation. However, existing methods either rely on specialized designs with inductive biases or adopt LLMs without fully exploring their potential in vision tasks. In this work, we systematically investigate the design space of LLMs for image generation and demonstrate that LLMs can achieve near state-of-the-art performance without domain-specific designs, simply by making proper choices in tokenization methods, modeling approaches, scan patterns, vocabulary design, and sampling strategies. We further analyze autoregressive models' learning and scaling behavior, revealing how larger models effectively capture more useful information than the smaller ones. Additionally, we explore the inherent differences between text and image modalities, highlighting the potential of LLMs across domains. The exploration provides valuable insights to inspire more effective designs when applying LLMs to other domains. With extensive experiments, our proposed model, **ELM** achieves an FID of 1.54 on 256$\times$256 ImageNet and an FID of 3.29 on 512$\times$512 ImageNet, demonstrating the powerful generative potential of LLMs in vision tasks.

## Metadata
- venue: ICML
- year: 2025
- authors: Xuantong LIU, Shaozhe Hao, Xianbiao Qi, Tianyang Hu, Jun Wang, Rong Xiao, Yuan Yao
- arxiv_id: 
- openreview_id: EIfCH9OgjR
- anthology_id: 
- pdf_url: https://openreview.net/pdf/28a2edcfdf09690ba809b2a17b0348b56fda2f4d.pdf
- published: 2025
- keywords: Image generation, Large language model, Generative model
