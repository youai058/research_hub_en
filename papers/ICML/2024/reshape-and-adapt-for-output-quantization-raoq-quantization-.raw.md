---
title: "Reshape and Adapt for Output Quantization (RAOQ): Quantization-aware Training for In-memory Computing Systems"
authors: ["Bonan Zhang", "Chia-Yu Chen", "Naveen Verma"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fM9xTkpAdu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e2b51f7bd7794737a678b389a2d7b8183cf3bca1.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:12+09:00"
---

# Reshape and Adapt for Output Quantization (RAOQ): Quantization-aware Training for In-memory Computing Systems

## Abstract
In-memory computing (IMC) has emerged as a promising solution to address both computation and data-movement challenges, by performing computation on data in-place directly in the memory array. IMC typically relies on analog operation, which makes analog-to-digital converters (ADCs) necessary, for converting results back to the digital domain. However, ADCs maintain computational efficiency by having limited precision, leading to substantial quantization errors in compute outputs. This work proposes RAOQ (Reshape and Adapt for Output Quantization) to overcome this issue, which comprises two classes of mechanisms including: 1) mitigating ADC quantization error by adjusting the statistics of activations and weights, through an activation-shifting approach (A-shift) and a weight reshaping technique (W-reshape); 2) adapting AI models to better tolerate ADC quantization through a bit augmentation method (BitAug), complemented by the introduction of ADC-LoRA, a low-rank approximation technique, to reduce the training overhead. RAOQ demonstrates consistently high performance across different scales and domains of neural network models for computer vision and natural language processing (NLP) tasks at various bit precisions, achieving state-of-the-art results with practical IMC implementations.

## Metadata
- venue: ICML
- year: 2024
- authors: Bonan Zhang, Chia-Yu Chen, Naveen Verma
- arxiv_id: 
- openreview_id: fM9xTkpAdu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e2b51f7bd7794737a678b389a2d7b8183cf3bca1.pdf
- published: 2024
