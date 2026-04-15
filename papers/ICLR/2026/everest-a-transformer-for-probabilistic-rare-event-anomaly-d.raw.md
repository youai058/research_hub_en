---
title: "EVEREST: A Transformer for Probabilistic Rare-Event Anomaly Detection with Evidential and Tail-Aware Uncertainty"
authors: ["Antanas Žilinskas", "Robert Noel Shorten", "Jakub Marecek"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ScpCaOVGw1"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2ee1575b7bd9a29849726904cfdb8bd6f4935a29.pdf"
published: "2026"
categories: []
keywords: ["Transformer models", "Uncertainty quantification", "Evidential deep learning", "Extreme value theory", "Imbalanced classification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:14+09:00"
---

# EVEREST: A Transformer for Probabilistic Rare-Event Anomaly Detection with Evidential and Tail-Aware Uncertainty

## Abstract
Forecasting rare events in multivariate time-series data is a central challenge in machine learning, complicated by severe class imbalance, long-range dependencies, and distributional uncertainty. We introduce EVEREST, a transformer-based architecture for probabilistic rare-event forecasting that delivers calibrated predictions and tail-aware risk estimation, with auxiliary interpretability through attention-based signal attribution. EVEREST integrates four key components: (i) a learnable attention bottleneck for soft aggregation of temporal dynamics; (ii) an evidential head for estimating aleatoric and epistemic uncertainty via a Normal–Inverse–Gamma distribution; (iii) an extreme-value head that models tail risk using a Generalized Pareto Distribution; and (iv) a lightweight precursor head for early-event detection. These modules are jointly optimised with a composite loss combining focal loss, evidential negative log-likelihood, and a tail-sensitive EVT penalty, and act only at training time; deployment uses a single classification head with no inference overhead. We evaluate EVEREST on a real-world benchmark spanning a decade of space-weather data and demonstrate state-of-the-art performance, including True Skill Statistic (TSS) scores of 0.973, 0.970, and 0.966 at 24, 48, and 72-hour horizons for C-class flares. The model is compact (≈0.81M parameters), efficient to train on commodity hardware, and applicable to other high-stakes domains such as industrial monitoring, weather, and satellite diagnostics. Limitations include reliance on fixed-length inputs and exclusion of image-based modalities, motivating future extensions to streaming and multimodal forecasting.

## Metadata
- venue: ICLR
- year: 2026
- authors: Antanas Žilinskas, Robert Noel Shorten, Jakub Marecek
- arxiv_id: 
- openreview_id: ScpCaOVGw1
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2ee1575b7bd9a29849726904cfdb8bd6f4935a29.pdf
- published: 2026
- keywords: Transformer models, Uncertainty quantification, Evidential deep learning, Extreme value theory, Imbalanced classification
