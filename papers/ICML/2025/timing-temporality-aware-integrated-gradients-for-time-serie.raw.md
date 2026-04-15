---
title: "TIMING: Temporality-Aware Integrated Gradients for Time Series Explanation"
authors: ["Hyeongwon Jang", "Changhun Kim", "Eunho Yang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "qOgKMqv9T7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0954dcf01dc5530aa1bb6655b8819ca54c401844.pdf"
published: "2025"
categories: []
keywords: ["Time Series", "XAI", "Explainability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:33+09:00"
---

# TIMING: Temporality-Aware Integrated Gradients for Time Series Explanation

## Abstract
Recent explainable artificial intelligence (XAI) methods for time series primarily estimate point-wise attribution magnitudes, while overlooking the directional impact on predictions, leading to suboptimal identification of significant points. Our analysis shows that conventional Integrated Gradients (IG) effectively capture critical points with both positive and negative impacts on predictions. However, current evaluation metrics fail to assess this capability, as they inadvertently cancel out opposing feature contributions. To address this limitation, we propose novel evaluation metrics—Cumulative Prediction Difference (CPD) and Cumulative Prediction Preservation
(CPP)—to systematically assess whether attribution methods accurately identify significant positive and negative points in time series XAI. Under these metrics, conventional IG outperforms recent counterparts. However, directly applying IG to time series data may lead to suboptimal outcomes, as generated paths ignore temporal relationships and introduce out-of-distribution samples. To overcome these challenges, we introduce TIMING, which enhances IG by incorporating temporal awareness while maintaining its theoretical properties. Extensive experiments on synthetic and real-world time series benchmarks demonstrate that TIMING outperforms existing time
series XAI baselines. Our code is available at https://github.com/drumpt/TIMING.

## Metadata
- venue: ICML
- year: 2025
- authors: Hyeongwon Jang, Changhun Kim, Eunho Yang
- arxiv_id: 
- openreview_id: qOgKMqv9T7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0954dcf01dc5530aa1bb6655b8819ca54c401844.pdf
- published: 2025
- keywords: Time Series, XAI, Explainability
