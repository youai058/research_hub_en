---
title: "Training-Free Safe Text Embedding Guidance for Text-to-Image Diffusion Models"
authors: ["Byeonghu Na", "Mina Kang", "Jiseok Kwak", "Minsang Park", "Jiwoo Shin", "SeJoon Jun", "Gayoung Lee", "Jin-Hwa Kim", "Il-chul Moon"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fbDHv2LQZJ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6e99289525d5ff47f76dd7f79473dbbd759b9ead.pdf"
published: "2025"
categories: []
keywords: ["diffusion model", "safe generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:41+09:00"
---

# Training-Free Safe Text Embedding Guidance for Text-to-Image Diffusion Models

## Abstract
Text-to-image models have recently made significant advances in generating realistic and semantically coherent images, driven by advanced diffusion models and large-scale web-crawled datasets. However, these datasets often contain inappropriate or biased content, raising concerns about the generation of harmful outputs when provided with malicious text prompts. We propose Safe Text embedding Guidance (STG), a training-free approach to improve the safety of diffusion models by guiding the text embeddings during sampling. STG adjusts the text embeddings based on a safety function evaluated on the expected final denoised image, allowing the model to generate safer outputs without additional training. Theoretically, we show that STG aligns the underlying model distribution with safety constraints, thereby achieving safer outputs while minimally affecting generation quality. Experiments on various safety scenarios, including nudity, violence, and artist-style removal, show that STG consistently outperforms both training-based and training-free baselines in removing unsafe content while preserving the core semantic intent of input prompts. Our code is available at https://github.com/aailab-kaist/STG.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Byeonghu Na, Mina Kang, Jiseok Kwak, Minsang Park, Jiwoo Shin, SeJoon Jun, Gayoung Lee, Jin-Hwa Kim, Il-chul Moon
- arxiv_id: 
- openreview_id: fbDHv2LQZJ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6e99289525d5ff47f76dd7f79473dbbd759b9ead.pdf
- published: 2025
- keywords: diffusion model, safe generation
