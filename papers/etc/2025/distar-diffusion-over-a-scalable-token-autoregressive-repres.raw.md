---
title: "DiSTAR: Diffusion over a Scalable Token Autoregressive Representation for Speech Generation"
authors: ["Yakun Song", "Xiaobin Zhuang", "Jiawei Chen", "Zhikang Niu", "Guanrou Yang", "Chenpeng Du", "Dongya Jia", "Zhuo Chen", "Yuping Wang", "Yuxuan Wang", "Xie Chen"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.12210"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.12210v2"
published: "2025-10-14"
categories: ["eess.AS", "cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:22+09:00"
---

# DiSTAR: Diffusion over a Scalable Token Autoregressive Representation for Speech Generation

## Abstract
Recent attempts to interleave autoregressive (AR) sketchers with diffusion-based refiners over continuous speech representations have shown promise, but they remain brittle under distribution shift and offer limited levers for controllability. We introduce DISTAR, a zero-shot text-to-speech framework that operates entirely in a discrete residual vector quantization (RVQ) code space and tightly couples an AR language model with a masked diffusion model, without forced alignment or a duration predictor. Concretely, DISTAR drafts block-level RVQ tokens with an AR language model and then performs parallel masked-diffusion infilling conditioned on the draft to complete the next block, yielding long-form synthesis with blockwise parallelism while mitigating classic AR exposure bias. The discrete code space affords explicit control at inference: DISTAR produces high-quality audio under both greedy and sample-based decoding using classifier-free guidance, supports trade-offs between robustness and diversity, and enables variable bit-rate and controllable computation via RVQ layer pruning at test time. Extensive experiments and ablations demonstrate that DISTAR surpasses state-of-the-art zero-shot TTS systems in robustness, naturalness, and speaker/style consistency, while maintaining rich output diversity. Audio samples are provided on https://anonymous.4open.science/w/DiSTAR_demo.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yakun Song, Xiaobin Zhuang, Jiawei Chen, Zhikang Niu, Guanrou Yang, Chenpeng Du, Dongya Jia, Zhuo Chen, Yuping Wang, Yuxuan Wang, Xie Chen
- arxiv_id: 2510.12210
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.12210v2
- published: 2025-10-14
