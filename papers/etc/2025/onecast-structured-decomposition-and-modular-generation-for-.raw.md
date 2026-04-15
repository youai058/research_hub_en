---
title: "OneCast: Structured Decomposition and Modular Generation for Cross-Domain Time Series Forecasting"
authors: ["Tingyue Pan", "Mingyue Cheng", "Shilong Zhang", "Zhiding Liu", "Xiaoyu Tao", "Yucong Luo", "Jintao Zhang", "Qi Liu"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.24028"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.24028v2"
published: "2025-10-28"
categories: ["cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# OneCast: Structured Decomposition and Modular Generation for Cross-Domain Time Series Forecasting

## Abstract
Cross-domain time series forecasting is a valuable task in various web applications. Despite its rapid advancement, achieving effective generalization across heterogeneous time series data remains a significant challenge. Existing methods have made progress by extending single-domain models, yet often fall short when facing domain-specific trend shifts and inconsistent periodic patterns. We argue that a key limitation lies in treating temporal series as undifferentiated sequence, without explicitly decoupling their inherent structural components. To address this, we propose OneCast, a structured and modular forecasting framework that decomposes time series into seasonal and trend components, each modeled through tailored generative pathways. Specifically, the seasonal component is captured by a lightweight projection module that reconstructs periodic patterns via interpretable basis functions. In parallel, the trend component is encoded into discrete tokens at segment level via a semantic-aware tokenizer, and subsequently inferred through a masked discrete diffusion mechanism. The outputs from both branches are combined to produce a final forecast that captures seasonal patterns while tracking domain-specific trends. Extensive experiments across eight domains demonstrate that OneCast mostly outperforms state-of-the-art baselines.

## Metadata
- venue: arXiv
- year: 2025
- authors: Tingyue Pan, Mingyue Cheng, Shilong Zhang, Zhiding Liu, Xiaoyu Tao, Yucong Luo, Jintao Zhang, Qi Liu
- arxiv_id: 2510.24028
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.24028v2
- published: 2025-10-28
