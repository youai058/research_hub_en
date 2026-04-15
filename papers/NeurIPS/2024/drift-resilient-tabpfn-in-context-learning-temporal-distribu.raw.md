---
title: "Drift-Resilient TabPFN: In-Context Learning Temporal Distribution Shifts on Tabular Data"
authors: ["Kai Helli", "David Schnurr", "Noah Hollmann", "Samuel Müller", "Frank Hutter"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "p3tSEFMwpG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b3a5a1ac99a58bf02a2ed186dff50e980bba1c89.pdf"
published: "2024"
categories: []
keywords: ["Temporal Distribution Shifts", "In-Context Learning", "Bayesian Inference", "Prior-Data Fitted Networks", "Temporal Domain Generalization", "Structural Causal Models", "TabPFN", "Tabular Data Modeling", "Out-Of-Distribution Generalization", "Domain Generalization", "Meta-Learning", "Concept Drift"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:57+09:00"
---

# Drift-Resilient TabPFN: In-Context Learning Temporal Distribution Shifts on Tabular Data

## Abstract
While most ML models expect independent and identically distributed data, this assumption is often violated in real-world scenarios due to distribution shifts, resulting in the degradation of machine learning model performance. Until now, no tabular method has consistently outperformed classical supervised learning, which ignores these shifts. To address temporal distribution shifts, we present Drift-Resilient TabPFN, a fresh approach based on In-Context Learning with a Prior-Data Fitted Network that learns the learning algorithm itself: it accepts the entire training dataset as input and makes predictions on the test set in a single forward pass. Specifically, it learns to approximate Bayesian inference on synthetic datasets drawn from a prior that specifies the model's inductive bias. This prior is based on structural causal models (SCM), which gradually shift over time. To model shifts of these causal models, we use a secondary SCM, that specifies changes in the primary model parameters. The resulting Drift-Resilient TabPFN can be applied to unseen data, runs in seconds on small to moderately sized datasets and needs no hyperparameter tuning. Comprehensive evaluations across 18 synthetic and real-world datasets demonstrate large performance improvements over a wide range of baselines, such as XGB, CatBoost, TabPFN, and applicable methods featured in the Wild-Time benchmark. Compared to the strongest baselines, it improves accuracy from 0.688 to 0.744 and ROC AUC from 0.786 to 0.832 while maintaining stronger calibration. This approach could serve as significant groundwork for further research on out-of-distribution prediction.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Kai Helli, David Schnurr, Noah Hollmann, Samuel Müller, Frank Hutter
- arxiv_id: 
- openreview_id: p3tSEFMwpG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b3a5a1ac99a58bf02a2ed186dff50e980bba1c89.pdf
- published: 2024
- keywords: Temporal Distribution Shifts, In-Context Learning, Bayesian Inference, Prior-Data Fitted Networks, Temporal Domain Generalization, Structural Causal Models, TabPFN, Tabular Data Modeling, Out-Of-Distribution Generalization, Domain Generalization, Meta-Learning, Concept Drift
