---
title: "LUM-ViT: Learnable Under-sampling Mask Vision Transformer for Bandwidth Limited Optical Signal Acquisition"
authors: ["Lingfeng Liu", "Dong Ni", "Hangjie Yuan"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wkbeqr5XhC"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e727a272852fd9b151a8c6fee5946d926aa8f97c.pdf"
published: "2024"
categories: []
keywords: ["hyperspectral imaging", "optical modulation", "real-time detection", "vision transformer", "pre-acquisition modulation", "learnable mask", "weight binarization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:54+09:00"
---

# LUM-ViT: Learnable Under-sampling Mask Vision Transformer for Bandwidth Limited Optical Signal Acquisition

## Abstract
Bandwidth constraints during signal acquisition frequently impede real-time detection applications. Hyperspectral data is a notable example, whose vast volume compromises real-time hyperspectral detection. To tackle this hurdle, we introduce a novel approach leveraging pre-acquisition modulation to reduce the acquisition volume. This modulation process is governed by a deep learning model, utilizing prior information. Central to our approach is LUM-ViT, a Vision Transformer variant. Uniquely, LUM-ViT incorporates a learnable under-sampling mask tailored for pre-acquisition modulation. To further optimize for optical calculations, we propose a kernel-level weight binarization technique and a three-stage fine-tuning strategy. Our evaluations reveal that, by sampling a mere 10\% of the original image pixels, LUM-ViT maintains the accuracy loss within 1.8\% on the ImageNet classification task. The method sustains near-original accuracy when implemented on real-world optical hardware, demonstrating its practicality. Code will be available at [https://github.com/MaxLLF/LUM-ViT](https://github.com/MaxLLF/LUM-ViT).

## Metadata
- venue: ICLR
- year: 2024
- authors: Lingfeng Liu, Dong Ni, Hangjie Yuan
- arxiv_id: 
- openreview_id: wkbeqr5XhC
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e727a272852fd9b151a8c6fee5946d926aa8f97c.pdf
- published: 2024
- keywords: hyperspectral imaging, optical modulation, real-time detection, vision transformer, pre-acquisition modulation, learnable mask, weight binarization
