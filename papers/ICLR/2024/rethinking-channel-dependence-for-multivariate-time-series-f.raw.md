---
title: "Rethinking Channel Dependence for Multivariate Time Series Forecasting: Learning from Leading Indicators"
authors: ["Lifan Zhao", "Yanyan Shen"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JiTVtCUOpS"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d434e3f2213d54e8999f551b44bbc2454529e8fb.pdf"
published: "2024"
categories: []
keywords: ["Multivariate time series forecasting", "channel dependence", "lead-lag relationships", "distribution shift"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:57+09:00"
---

# Rethinking Channel Dependence for Multivariate Time Series Forecasting: Learning from Leading Indicators

## Abstract
Recently, channel-independent methods have achieved state-of-the-art performance in multivariate time series (MTS) forecasting. Despite reducing overfitting risks, these methods miss potential opportunities in utilizing channel dependence for accurate predictions. We argue that there exist locally stationary lead-lag relationships between variates, i.e., some lagged variates may follow the leading indicators within a short time period. Exploiting such channel dependence is beneficial since leading indicators offer advance information that can be used to reduce the forecasting difficulty of the lagged variates. In this paper, we propose a new method named LIFT that first efficiently estimates leading indicators and their leading steps at each time step and then judiciously allows the lagged variates to utilize the advance information from leading indicators. LIFT plays as a plugin that can be seamlessly collaborated with arbitrary time series forecasting methods. Extensive experiments on six real-world datasets demonstrate that LIFT improves the state-of-the-art methods by 5.4% in average forecasting performance. Our code is available at https://github.com/SJTU-Quant/LIFT.

## Metadata
- venue: ICLR
- year: 2024
- authors: Lifan Zhao, Yanyan Shen
- arxiv_id: 
- openreview_id: JiTVtCUOpS
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d434e3f2213d54e8999f551b44bbc2454529e8fb.pdf
- published: 2024
- keywords: Multivariate time series forecasting, channel dependence, lead-lag relationships, distribution shift
