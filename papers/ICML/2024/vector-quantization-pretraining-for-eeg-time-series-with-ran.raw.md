---
title: "Vector Quantization Pretraining for EEG Time Series with Random Projection and Phase Alignment"
authors: ["Haokun GUI", "Xiucheng Li", "Xinyang Chen"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "7uwLvFvpis"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9f46a9f0dc412d0315412191b7223502e4851500.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:36+09:00"
---

# Vector Quantization Pretraining for EEG Time Series with Random Projection and Phase Alignment

## Abstract
In this paper, we propose a BERT-style self-supervised learning model, VQ-MTM (Vector Quantization Masked Time-Series Modeling), for the EEG time series data analysis. At its core, VQ-MTM comprises a theoretically grounded random-projection quantization module and a phase-aligning module guided by the Time-Phase-Shift Equivariance of Fourier Transform, the two modules can generate well-defined semantic units (akin to words in natural language) for the corrupted and periodic time series, thus offering robust and consistent learning signals for the EEG self-supervised learning. VQ-MTM also owns low model complexity and can easily adapt to large-scale datasets. We conduct experiments on five real-world datasets including two large-scale datasets to verify the efficacy of our proposed model, the experiment results show that VQ-MTM is able to consistently surpass the existing methods by large margins on both seizure detection and classification tasks. Our code is available at https://github.com/HaokunGUI/VQ_MTM.

## Metadata
- venue: ICML
- year: 2024
- authors: Haokun GUI, Xiucheng Li, Xinyang Chen
- arxiv_id: 
- openreview_id: 7uwLvFvpis
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9f46a9f0dc412d0315412191b7223502e4851500.pdf
- published: 2024
