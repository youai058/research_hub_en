---
title: "Complexity- and Statistics-Guided Anomaly Detection in Time Series Foundation Models"
authors: ["Jongwon Kim", "Samuel Yoon", "Young Myoung Ko", "Yerin Kim", "Sung Il Kim", "JAEUNG TAE"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rBt9aW3Mx7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b4efb14b1c2607f019443cf7ff96fa8b2a8a6680.pdf"
published: "2026"
categories: []
keywords: ["Timeseries anomaly detection", "Timeseries foundation model", "Reconstruction based anomaly detection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:25+09:00"
---

# Complexity- and Statistics-Guided Anomaly Detection in Time Series Foundation Models

## Abstract
This paper introduces a methodology for anomaly detection in time series using Time Series Foundation Models (TFMs). While TFMs have achieved strong success in forecasting, their role in anomaly detection remains underexplored. We identify two key challenges when applying TFMs to reconstruction-based anomaly detection and propose solutions. 

The first challenge is overgeneralization, where TFMs reconstruct both normal and abnormal data with similar accuracy, masking true anomalies. We find that this effect often occurs in data with strong low-frequency components. To address it, we propose a complexity metric, $\alpha$, that reflects how difficult the data is for TFMs and design a Complexity-Aware Ensemble (CAE) that adaptively balances TFMs with a statistical model. 

The second challenge is overstationarization, caused by instance normalization layers that improve forecasting accuracy but remove essential statistical features such as mean and variance, which are critical for anomaly detection. We resolve this by reintroducing these features into the reconstruction process without retraining the TFMs. 

Experiments on 23 univariate and 17 multivariate benchmark datasets demonstrate that our method significantly outperforms both deep learning and statistical baselines. Furthermore, we show that our complexity-based metric, $\alpha$, provides a theoretical foundation for improved anomaly detection, and we briefly explore prediction-based anomaly detection using TFMs.

## Metadata
- venue: ICLR
- year: 2026
- authors: Jongwon Kim, Samuel Yoon, Young Myoung Ko, Yerin Kim, Sung Il Kim, JAEUNG TAE
- arxiv_id: 
- openreview_id: rBt9aW3Mx7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b4efb14b1c2607f019443cf7ff96fa8b2a8a6680.pdf
- published: 2026
- keywords: Timeseries anomaly detection, Timeseries foundation model, Reconstruction based anomaly detection
