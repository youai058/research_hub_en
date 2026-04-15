---
title: "Adapt Data to Model: Adaptive Transformation Optimization for Domain-shared Time Series Foundation Models"
authors: ["Yunzhong Qiu", "Zhiyao Cen", "Zhongyi Pei", "Chen Wang", "Jianmin Wang"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "uTK1SNgi1N"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a15326dd85d140d7e653f9f308c0f26059656767.pdf"
published: "2026"
categories: []
keywords: ["time series foundation models", "transformation optimization", "time series forecasting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:42+09:00"
---

# Adapt Data to Model: Adaptive Transformation Optimization for Domain-shared Time Series Foundation Models

## Abstract
Large time series models (LTMs) have emerged as powerful tools for universal forecasting, yet they often struggle with the inherent diversity and nonstationarity of real-world time series data, leading to an unsatisfactory trade-off between forecasting accuracy and generalization. Rather than continually finetuning new LTM instances for each domain, we propose a data-centric framework, time-series adaptive transformation optimization (TATO), that enables a single frozen pre-trained LTM to adapt to diverse downstream domains through an optimally configured transformation pipeline. Specifically, TATO constructs three representative types of transformations, including context slicing, scale normalization, and outlier correction, to help LTMs better align with target domain characteristics. To ensure robustness, we incorporate carefully selected time series augmentations and a two-stage ranking mechanism that filters out pipelines underperforming on specific metrics. Extensive experiments on state-of-the-art LTMs and widely used datasets demonstrate that TATO consistently and significantly improves domain-adaptive forecasting performance, achieving a maximum reduction in MSE of 65.4\% and an average reduction of 13.6\%. Moreover, TATO is highly efficient, typically completing optimization in under 2 minutes, making it practical for real-world deployment. The source code is available at https://github.com/thulab/TATO.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yunzhong Qiu, Zhiyao Cen, Zhongyi Pei, Chen Wang, Jianmin Wang
- arxiv_id: 
- openreview_id: uTK1SNgi1N
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a15326dd85d140d7e653f9f308c0f26059656767.pdf
- published: 2026
- keywords: time series foundation models, transformation optimization, time series forecasting
