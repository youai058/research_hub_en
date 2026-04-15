---
title: "Are Global Dependencies Necessary? Scalable Time Series Forecasting via Local Cross-Variate Modeling"
authors: ["Kun Liu", "Renjun Jia", "Ruifeng Yang", "Xirui Zeng", "Yuqi Liang", "Cen Chen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CNVL194fO5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3def1dc505bc036f10ab58e21772da735a067162.pdf"
published: "2026"
categories: []
keywords: ["Time Series Forecasting", "Time Series Analysis", "Deep Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:36+09:00"
---

# Are Global Dependencies Necessary? Scalable Time Series Forecasting via Local Cross-Variate Modeling

## Abstract
Effectively modeling cross-variate dependencies is a central, yet challenging, task in multivariate time series forecasting.
While attention-based methods have advanced the state-of-the-art by capturing global cross-variate dependencies, their quadratic complexity with respect to the number of variates severely limits their scalability. In this work, we challenge the necessity of global dependency modeling. We posit, through both theoretical analysis and empirical evidence, that modeling local cross-variate interactions is not only sufficient but also more efficient for many dense dependency systems.
Motivated by this core insight, we propose VPNet, a novel architecture that excels in both accuracy and efficiency. VPNet's design is founded on two key principles: a channelized reinterpretation of patch embeddings into a higher-level variate-patch field, and a specialized VarTCNBlock that operates upon it. Specifically, the model first employs a patch-level autoencoder to extract robust local representations. In a pivotal step, these representations are then re-conceptualized as a 2D field constructed over a "variates × patches" grid. The VarTCNBlock then applies depthwise 2D convolutions across this field to efficiently capture local spatio-temporal patterns (i.e., cross-variate and temporal dependencies simultaneously), followed by pointwise convolutions for feature mixing. This design ensures that the computational complexity scales linearly with the number of variates. Finally, variate-wise prediction heads map the refined historical patch representations to future ones, which are decoded back into the time domain. Extensive experiments demonstrate that VPNet not only achieves state-of-the-art performance across multiple benchmarks but also offers significant efficiency gains, establishing it as a superior and scalable solution for high-dimensional forecasting.

## Metadata
- venue: ICLR
- year: 2026
- authors: Kun Liu, Renjun Jia, Ruifeng Yang, Xirui Zeng, Yuqi Liang, Cen Chen
- arxiv_id: 
- openreview_id: CNVL194fO5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3def1dc505bc036f10ab58e21772da735a067162.pdf
- published: 2026
- keywords: Time Series Forecasting, Time Series Analysis, Deep Learning
