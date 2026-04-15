---
title: "Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment"
authors: ["Deokjae Lee", "Hyun Oh Song"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "l4F50jpiVH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/518ecfba9ed223f4e43c3783e924fd758b01eb9e.pdf"
published: "2025"
categories: []
keywords: ["LLM quantization", "Post-training quantization", "Mixed scheme quantization", "Data-free quantization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:24+09:00"
---

# Q-Palette: Fractional-Bit Quantizers Toward Optimal Bit Allocation for Efficient LLM Deployment

## Abstract
We study weight-only post-training quantization (PTQ), which quantizes the weights of a large language model (LLM) without retraining, using little or no calibration data. Weight-only PTQ is crucial for reducing the memory footprint and latency of LLM inference, especially in memory-bound, small-batch inference scenarios, such as personalized inference on edge devices. Despite its importance, irregular weight distributions with heavy-tailed outliers in LLMs complicate quantization, recently motivating rotation-based methods that transform weights into near-Gaussian distributions, which are more regular with fewer outliers, thereby reducing quantization error. In this work, we first derive the information-theoretically optimal bit allocation for Gaussianized weights under given bit budgets, revealing that fine-grained fractional-bit quantizers approaching the Gaussian distortion-rate bound are essential to achieve near-optimal quantization performance. To bridge this theoretical insight and practical implementation, we introduce Q-Palette, a versatile collection of fractional-bit quantizers that range from trellis-coded quantizers offering near-optimal distortion to simpler vector and scalar quantizers optimized for faster inference, all efficiently implemented with optimized CUDA kernels across various bitwidths. Furthermore, leveraging Q-Palette as a foundational component, we propose a novel mixed-scheme quantization framework, jointly optimizing quantizer choices and layer fusion decisions given resource constraints. The code is available at https://github.com/snu-mllab/Q-Palette.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Deokjae Lee, Hyun Oh Song
- arxiv_id: 
- openreview_id: l4F50jpiVH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/518ecfba9ed223f4e43c3783e924fd758b01eb9e.pdf
- published: 2025
- keywords: LLM quantization, Post-training quantization, Mixed scheme quantization, Data-free quantization
