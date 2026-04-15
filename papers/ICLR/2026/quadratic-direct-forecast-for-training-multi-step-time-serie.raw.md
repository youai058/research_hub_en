---
title: "Quadratic Direct Forecast for Training Multi-Step Time-Series Forecast Models"
authors: ["Eric Wang", "Licheng Pan", "Yuan Lu", "Zi Ciu Chan", "Tianqiao Liu", "Shuting He", "Zhixuan Chu", "Qingsong Wen", "Haoxuan Li", "Zhouchen Lin"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "vpO8n9AqEG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1987c914e2236b7b61b5561103abff145b5a1222.pdf"
published: "2026"
categories: []
keywords: ["Time-series", "time-series forecast"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:12+09:00"
---

# Quadratic Direct Forecast for Training Multi-Step Time-Series Forecast Models

## Abstract
The design of training objective is central to training time-series forecasting models. Existing training objectives such as mean squared error mostly treat each future step as an independent, equally weighted task, which we found leading to the following two issues: (1) overlook the *label autocorrelation effect* among future steps, leading to biased training objective; (2) fail to set *heterogeneous task weights* for different forecasting tasks corresponding to varying future steps, limiting the forecasting performance. To fill this gap, we propose a novel quadratic-form weighted training objective, addressing both of the issues simultaneously. Specifically, the off-diagonal elements of the weighting matrix account for the label autocorrelation effect, whereas the non-uniform diagonals are expected to match the most preferable weights of the forecasting tasks with varying future steps. To achieve this, we propose a Quadratic Direct Forecast (QDF) learning algorithm, which trains the forecast model using the adaptively updated quadratic-form weighting matrix. Experiments show that our QDF effectively improves performance of various forecast models, achieving state-of-the-art results. Code is available at https://anonymous.4open.science/r/QDF-8937.

## Metadata
- venue: ICLR
- year: 2026
- authors: Eric Wang, Licheng Pan, Yuan Lu, Zi Ciu Chan, Tianqiao Liu, Shuting He, Zhixuan Chu, Qingsong Wen, Haoxuan Li, Zhouchen Lin
- arxiv_id: 
- openreview_id: vpO8n9AqEG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1987c914e2236b7b61b5561103abff145b5a1222.pdf
- published: 2026
- keywords: Time-series, time-series forecast
