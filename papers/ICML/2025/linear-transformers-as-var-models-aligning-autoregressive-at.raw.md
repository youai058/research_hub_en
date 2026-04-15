---
title: "Linear Transformers as VAR Models:  Aligning Autoregressive Attention Mechanisms with Autoregressive Forecasting"
authors: ["Jiecheng Lu", "Shihao Yang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "SxJUV9mnyt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f45aad098737754464b9019acbd08338eb0d6aae.pdf"
published: "2025"
categories: []
keywords: ["Linear Attention", "Transformer", "Time Series Forecasting", "Vector Autoregression"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:33+09:00"
---

# Linear Transformers as VAR Models:  Aligning Autoregressive Attention Mechanisms with Autoregressive Forecasting

## Abstract
Autoregressive attention-based time series forecasting (TSF) has drawn increasing interest, with mechanisms like linear attention often outperforming vanilla attention. However, deeper Transformer architectures frequently misalign with autoregressive objectives, obscuring the underlying VAR structure embedded within linear attention and hindering their ability to capture the data generative processes in TSF. In this work, we first show that a single linear attention layer can be interpreted as a dynamic vector autoregressive (VAR) structure. We then explain that existing multi-layer Transformers have structural mismatches with the autoregressive forecasting objective, which impair interpretability and generalization ability. To address this, we show that by rearranging the MLP, attention, and input-output flow, multi-layer linear attention can also be aligned as a VAR model. Then, we propose Structural Aligned Mixture of VAR (SAMoVAR), a linear Transformer variant that integrates interpretable dynamic VAR weights for multivariate TSF. By aligning the Transformer architecture with autoregressive objectives, SAMoVAR delivers improved performance, interpretability, and computational efficiency, comparing to SOTA TSF models.

## Metadata
- venue: ICML
- year: 2025
- authors: Jiecheng Lu, Shihao Yang
- arxiv_id: 
- openreview_id: SxJUV9mnyt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f45aad098737754464b9019acbd08338eb0d6aae.pdf
- published: 2025
- keywords: Linear Attention, Transformer, Time Series Forecasting, Vector Autoregression
