---
title: "KLASS: KL-Guided Fast Inference in Masked Diffusion Models"
authors: ["Seo Hyun Kim", "Sunwoo Hong", "Hojung Jung", "Youngrok Park", "Se-Young Yun"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gOG9Zoyn4R"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e5d6b78c9b1c9df5c9f7d513c8e643f790928834.pdf"
published: "2025"
categories: []
keywords: ["Generative Models", "Efficient Inference Methods"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:23+09:00"
---

# KLASS: KL-Guided Fast Inference in Masked Diffusion Models

## Abstract
Masked diffusion models have demonstrated competitive results on various tasks including language generation. However, due to its iterative refinement process, the inference is often bottlenecked by slow and static sampling speed. To overcome this problem, we introduce `KL-Adaptive Stability Sampling' (KLASS), a fast yet effective sampling method that exploits token-level KL divergence to identify stable, high-confidence predictions. By unmasking multiple tokens in each iteration without any additional model training, our approach speeds up generation significantly while maintaining sample quality. On reasoning benchmarks, KLASS achieves up to $2.78\times$ wall-clock speedups while improving performance over standard greedy decoding, attaining state-of-the-art results among diffusion-based samplers. We further validate KLASS across diverse domains, including text, image, and molecular generation, showing its effectiveness as a broadly applicable sampler across different models.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Seo Hyun Kim, Sunwoo Hong, Hojung Jung, Youngrok Park, Se-Young Yun
- arxiv_id: 
- openreview_id: gOG9Zoyn4R
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e5d6b78c9b1c9df5c9f7d513c8e643f790928834.pdf
- published: 2025
- keywords: Generative Models, Efficient Inference Methods
