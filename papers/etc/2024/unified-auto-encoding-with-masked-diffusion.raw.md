---
title: "Unified Auto-Encoding with Masked Diffusion"
authors: ["Philippe Hansen-Estruch", "Sriram Vishwanath", "Amy Zhang", "Manan Tomar"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2406.17688"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2406.17688v1"
published: "2024-06-25"
categories: ["cs.CV", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# Unified Auto-Encoding with Masked Diffusion

## Abstract
At the core of both successful generative and self-supervised representation learning models there is a reconstruction objective that incorporates some form of image corruption. Diffusion models implement this approach through a scheduled Gaussian corruption process, while masked auto-encoder models do so by masking patches of the image. Despite their different approaches, the underlying similarity in their methodologies suggests a promising avenue for an auto-encoder capable of both de-noising tasks. We propose a unified self-supervised objective, dubbed Unified Masked Diffusion (UMD), that combines patch-based and noise-based corruption techniques within a single auto-encoding framework. Specifically, UMD modifies the diffusion transformer (DiT) training process by introducing an additional noise-free, high masking representation step in the diffusion noising schedule, and utilizes a mixed masked and noised image for subsequent timesteps. By integrating features useful for diffusion modeling and for predicting masked patch tokens, UMD achieves strong performance in downstream generative and representation learning tasks, including linear probing and class-conditional generation. This is achieved without the need for heavy data augmentations, multiple views, or additional encoders. Furthermore, UMD improves over the computational efficiency of prior diffusion based methods in total training time. We release our code at https://github.com/philippe-eecs/small-vision.

## Metadata
- venue: arXiv
- year: 2024
- authors: Philippe Hansen-Estruch, Sriram Vishwanath, Amy Zhang, Manan Tomar
- arxiv_id: 2406.17688
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2406.17688v1
- published: 2024-06-25
