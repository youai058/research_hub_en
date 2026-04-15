---
title: "WAVE: Weighted Autoregressive Varying Gate for Time Series Forecasting"
authors: ["Jiecheng Lu", "Xu Han", "Yan Sun", "Shihao Yang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Qqn5ktBUxH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3e40cb458f184d01dcb305a2b9e82c5d85c4c399.pdf"
published: "2025"
categories: []
keywords: ["Attention", "Transformer", "Autoregressive Moving-average", "Time Series Forecasting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:36+09:00"
---

# WAVE: Weighted Autoregressive Varying Gate for Time Series Forecasting

## Abstract
We propose a Weighted Autoregressive Varying gatE (WAVE) attention mechanism equipped with both Autoregressive (AR) and Moving-average (MA) components. It can adapt to various attention mechanisms, enhancing and decoupling their ability to capture long-range and local temporal patterns in time series data. In this paper, we first demonstrate that, for the time series forecasting (TSF) task, the previously overlooked decoder-only autoregressive Transformer model can achieve results comparable to the best baselines when appropriate tokenization and training methods are applied. Moreover, inspired by the ARMA model from statistics and recent advances in linear attention, we introduce the full ARMA structure into existing autoregressive attention mechanisms. By using an indirect MA weight generation method, we incorporate the MA term while maintaining the time complexity and parameter size of the underlying efficient attention models. We further explore how indirect parameter generation can produce implicit MA weights that align with the modeling requirements for local temporal impacts. Experimental results show that WAVE attention that incorporates the ARMA structure consistently improves the performance of various AR attentions on TSF tasks, achieving state-of-the-art results.

## Metadata
- venue: ICML
- year: 2025
- authors: Jiecheng Lu, Xu Han, Yan Sun, Shihao Yang
- arxiv_id: 
- openreview_id: Qqn5ktBUxH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3e40cb458f184d01dcb305a2b9e82c5d85c4c399.pdf
- published: 2025
- keywords: Attention, Transformer, Autoregressive Moving-average, Time Series Forecasting
