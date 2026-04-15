---
title: "GAFormer: Enhancing Timeseries Transformers Through Group-Aware Embeddings"
authors: ["Jingyun Xiao", "Ran Liu", "Eva L Dyer"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "c56TWtYp0W"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c6fe3e477e52b832a4b26eaa7a2d211c301b44b7.pdf"
published: "2024"
categories: []
keywords: ["Time-series", "Transformer", "Spatiotemporal"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:19+09:00"
---

# GAFormer: Enhancing Timeseries Transformers Through Group-Aware Embeddings

## Abstract
Analyzing multivariate time series is important in many domains. However, it has been difficult to learn robust and generalizable representations within multivariate datasets due to complex inter-channel relationships and dynamic shifts. In this paper, we introduce a novel approach for learning spatiotemporal structure and using it to improve the application of transformers to timeseries datasets. Our framework learns a set of group tokens, and builds an instance-specific group embedding (GE) layer that assigns input tokens to a small number of group tokens to incorporate  structure into learning. We then introduce a novel architecture, Group-Aware transFormer (GAFormer), which incorporates both spatial and temporal group embeddings to achieve state-of-the-art performance on a number of time-series classification and regression tasks. In evaluations on a number of diverse timeseries datasets, we show that GE on its own can provide a nice enhancement to a number of backbones, and that by coupling spatial and temporal group embeddings, the GAFormer can outperform the existing baselines. Finally, we show how our approach discerns latent structures in data even without information about the spatial ordering of channels, and yields a more interpretable decomposition of spatial and temporal structure underlying complex multivariate datasets.

## Metadata
- venue: ICLR
- year: 2024
- authors: Jingyun Xiao, Ran Liu, Eva L Dyer
- arxiv_id: 
- openreview_id: c56TWtYp0W
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c6fe3e477e52b832a4b26eaa7a2d211c301b44b7.pdf
- published: 2024
- keywords: Time-series, Transformer, Spatiotemporal
