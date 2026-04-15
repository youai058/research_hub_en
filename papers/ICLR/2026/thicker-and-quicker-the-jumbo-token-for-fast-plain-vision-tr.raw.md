---
title: "Thicker and Quicker: The Jumbo Token for Fast Plain Vision Transformers"
authors: ["Anthony Fuller", "Yousef Yassin", "Daniel Kyrollos", "Evan Shelhamer", "James R Green"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nxcevynv08"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1887c8ded7f8497fa64fc93eb58c0ae40ae28351.pdf"
published: "2026"
categories: []
keywords: ["efficient deep learning", "computer vision", "vision transformers"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:36+09:00"
---

# Thicker and Quicker: The Jumbo Token for Fast Plain Vision Transformers

## Abstract
ViTs are general and accurate, and address many tasks, but ViTs are slow, and are not always practical when efficiency is key. Existing methods for faster ViTs design hybrid non-ViT architectures, losing generality, or shrink their tokens, sacrificing accuracy. Many non-ViT architectures are both fast and accurate. Yet, without significant modifications, they cannot do what ViTs can: process other input shapes, pre-train by SOTA self-supervised learning, reduce computation by dropping tokens, and more. We make ViTs faster by reducing patch token width while increasing global token width by adding a new Jumbo token. Our wider Jumbo token is processed by its own wider FFN to increase model capacity. Yet our Jumbo FFN is efficient: it processes a single token, for speed, and its parameters are shared across all layers, for memory. Crucially, our Jumbo is attention-only and non-hierarchical, like a plain ViT, so it is simple, scalable, flexible, and compatible with ViT methods new and old. Jumbo improves over ViT baselines with Registers from Nano to Large scales while maintaining speed/throughput on ImageNet-1K (0.1-13%). Jumbo also improves segmentation (1.9-3.1% on ADE20K), MAE pre-training (4.9% linear probing on ImageNet-1K), test-time adaptation (5.2% on ImageNet-C), and time series modeling. Our Jumbo models even achieve better speed-accuracy trade-offs than specialized non-ViT compute-efficient models, while maintaining plain-ViT compatibility for practicality. Code and weights are available: https://github.com/antofuller/jumbo

## Metadata
- venue: ICLR
- year: 2026
- authors: Anthony Fuller, Yousef Yassin, Daniel Kyrollos, Evan Shelhamer, James R Green
- arxiv_id: 
- openreview_id: nxcevynv08
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1887c8ded7f8497fa64fc93eb58c0ae40ae28351.pdf
- published: 2026
- keywords: efficient deep learning, computer vision, vision transformers
