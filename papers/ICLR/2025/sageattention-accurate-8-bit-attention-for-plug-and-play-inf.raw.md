---
title: "SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration"
authors: ["Jintao Zhang", "Jia wei", "Pengle Zhang", "Jun Zhu", "Jianfei Chen"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OL44KtasKc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e452ea42598e289378880ea077b682a961e4946d.pdf"
published: "2025"
categories: []
keywords: ["Attention", "Quantization", "quantized attention", "inference acceleration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:59+09:00"
---

# SageAttention: Accurate 8-Bit Attention for Plug-and-play Inference Acceleration

## Abstract
The transformer architecture predominates across various models. As the heart of the transformer, attention has a computational complexity of $O(N^2)$, compared to $O(N)$ for linear transformations. When handling large sequence lengths, attention becomes the primary time-consuming component. Although quantization has proven to be an effective method for accelerating model inference, existing quantization methods primarily focus on optimizing the linear layer.
In response, we first analyze the feasibility of quantization in attention detailedly. Following that, we propose SageAttention, a highly efficient and accurate quantization method for attention. The OPS (operations per second) of our approach outperforms FlashAttention2 and xformers by about 2.1x and 2.7x, respectively. SageAttention also achieves superior accuracy performance over FlashAttention3. Comprehensive experiments confirm that our approach incurs almost no end-to-end metrics loss across diverse models—including those for large language processing, image generation, and video generation. The code is available at https://github.com/thu-ml/SageAttention.

## Metadata
- venue: ICLR
- year: 2025
- authors: Jintao Zhang, Jia wei, Pengle Zhang, Jun Zhu, Jianfei Chen
- arxiv_id: 
- openreview_id: OL44KtasKc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e452ea42598e289378880ea077b682a961e4946d.pdf
- published: 2025
- keywords: Attention, Quantization, quantized attention, inference acceleration
