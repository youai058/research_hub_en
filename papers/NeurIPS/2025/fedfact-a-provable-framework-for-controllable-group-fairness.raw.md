---
title: "FedFACT: A Provable Framework for Controllable Group-Fairness Calibration in Federated Learning"
authors: ["Li Zhang", "Zhongxuan Han", "XiaoHua Feng", "Jiaming Zhang", "Yuyuan Li", "Chaochao Chen"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "6lCY5bLW8E"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5df5d12019dda54e36fff2ebea8a2c18a18d1413.pdf"
published: "2025"
categories: []
keywords: ["Federated Learning; Fairness; Multi-Class Classification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:35+09:00"
---

# FedFACT: A Provable Framework for Controllable Group-Fairness Calibration in Federated Learning

## Abstract
With emerging application of Federated Learning (FL) in decision-making scenarios, it is imperative to regulate model fairness to prevent disparities across sensitive groups (e.g., female, male).
Current research predominantly focuses on two concepts of group fairness within FL: *Global Fairness* (overall model disparity across all clients) and *Local Fairness* (the disparity within each client).
However, the non-decomposable, non-differentiable nature of fairness criteria pose two fundamental, unresolved challenges for fair FL: (i) *Harmonizing global and local fairness, especially in multi-class classification*; (ii) *Enabling a controllable, optimal accuracy-fairness trade-off*.
To tackle the aforementioned challenges, we propose a novel controllable federated group-fairness calibration framework, named FedFACT.
FedFACT identifies the Bayes-optimal classifiers under both global and local fairness constraints in multi-class case, yielding models with minimal performance decline while guaranteeing fairness.
To effectively realize an adjustable, optimal accuracy-fairness balance, we derive specific characterizations of the Bayes-optimal fair classifiers for reformulating fair FL as personalized cost-sensitive learning problem for in-processing, and bi-level optimization for post-processing.
Theoretically, we provide convergence and generalization guarantees for FedFACT to approach the near-optimal accuracy under given fairness levels.
Extensive experiments on multiple datasets across various data heterogeneity demonstrate that FedFACT consistently outperforms baselines in balancing accuracy and global-local fairness.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Li Zhang, Zhongxuan Han, XiaoHua Feng, Jiaming Zhang, Yuyuan Li, Chaochao Chen
- arxiv_id: 
- openreview_id: 6lCY5bLW8E
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5df5d12019dda54e36fff2ebea8a2c18a18d1413.pdf
- published: 2025
- keywords: Federated Learning; Fairness; Multi-Class Classification
