---
title: "Time-o1: Time-Series Forecasting Needs Transformed Label Alignment"
authors: ["Hao Wang", "Licheng Pan", "Zhichao Chen", "Xu Chen", "Qingyang Dai", "Lei Wang", "Haoxuan Li", "Zhouchen Lin"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RxWILaXuhb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/53f26f93c97ec8286da63bd8230771dd1c838499.pdf"
published: "2025"
categories: []
keywords: ["Time-Series", "Label Autocorrelation", "Orthogonalization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:20+09:00"
---

# Time-o1: Time-Series Forecasting Needs Transformed Label Alignment

## Abstract
Training time-series forecasting models poses unique challenges in loss function design. Most existing approaches adopt temporal mean squared error, but this study reveals two critical limitations: (1) it ignores the presence of label autocorrelation, which biases it from the true label sequence likelihood;  (2) it involves excessive number of tasks, which complicates optimization, especially for long-term forecasting. To address these issues, we introduce Time-o1, a transform-enhanced loss function for time-series forecasting. The central idea is to transform the label sequence into decorrelated components with discriminated significance. Models are then trained to align the most significant components, thereby effectively mitigating label autocorrelation and reducing task amount. Experiments demonstrate that Time-o1 achieves state-of-the-art performance and is compatible with various forecast models. Code is available at https://github.com/Master-PLC/Time-o1.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Hao Wang, Licheng Pan, Zhichao Chen, Xu Chen, Qingyang Dai, Lei Wang, Haoxuan Li, Zhouchen Lin
- arxiv_id: 
- openreview_id: RxWILaXuhb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/53f26f93c97ec8286da63bd8230771dd1c838499.pdf
- published: 2025
- keywords: Time-Series, Label Autocorrelation, Orthogonalization
