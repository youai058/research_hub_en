---
title: "AEQA-NAT : Adaptive End-to-end Quantization Alignment Training Framework for Non-autoregressive Machine Translation"
authors: ["Xiangyu Qu", "guojing liu", "Liang Li"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "mQE0EsrX1y"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ba900773db5e6fed473206423e2fcbc38799466a.pdf"
published: "2025"
categories: []
keywords: ["Machine Translation", "Parallel decoding", "Vector Quantization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:21+09:00"
---

# AEQA-NAT : Adaptive End-to-end Quantization Alignment Training Framework for Non-autoregressive Machine Translation

## Abstract
Non-autoregressive Transformers (NATs) have garnered significant attention due to their efficient decoding compared to autoregressive methods. However, existing conditional dependency modeling schemes based on masked language modeling introduce a *training-inference gap* in NATs. For instance, while NATs sample target words during training to enhance input, this condition cannot be met during inference, and simply annealing the sampling rate to zero during training leads to model performance degradation. We demonstrate that this *training-inference gap* prevents NATs from fully realizing their potential. To address this, we propose an adaptive end-to-end quantization alignment training framework, which introduces a semantic consistency space to adaptively align NAT training, eliminating the need for target information and thereby bridging the *training-inference gap*.Experimental results demonstrate that our method outperforms most existing fully NAT models, delivering performance on par with Autoregressive Transformer (AT) while being 17.0 times more efficient in inference.

## Metadata
- venue: ICML
- year: 2025
- authors: Xiangyu Qu, guojing liu, Liang Li
- arxiv_id: 
- openreview_id: mQE0EsrX1y
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ba900773db5e6fed473206423e2fcbc38799466a.pdf
- published: 2025
- keywords: Machine Translation, Parallel decoding, Vector Quantization
