---
title: "UniCBE: An Uniformity-driven Comparing Based Evaluation Framework with Unified Multi-Objective Optimization"
authors: ["Peiwen Yuan", "Shaoxiong Feng", "Yiwei Li", "Xinglin Wang", "Yueqi Zhang", "Jiayi Shi", "Chuyi Tan", "Boyuan Pan", "Yao Hu", "Kan Li"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rpwGUtTeA5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9e7ec666dcb3ef8f90e2c4017d28c5d7fff5951a.pdf"
published: "2025"
categories: []
keywords: ["evaluation", "efficient", "scalability", "accuracy", "convergence"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:50+09:00"
---

# UniCBE: An Uniformity-driven Comparing Based Evaluation Framework with Unified Multi-Objective Optimization

## Abstract
Human preference plays a significant role in measuring large language models and guiding them to align with human values. Unfortunately, current comparing-based evaluation (CBE) methods typically focus on a single optimization objective, failing to effectively utilize scarce yet valuable preference signals. To address this, we delve into key factors that can enhance the accuracy, convergence, and scalability of CBE: suppressing sampling bias, balancing descending process of uncertainty, and mitigating updating uncertainty.
Following the derived guidelines, we propose UniCBE, a unified uniformity-driven CBE framework which simultaneously optimize these core objectives by constructing and integrating three decoupled sampling probability matrices, each designed to ensure uniformity in specific aspects. We further ablate the optimal tuple sampling and preference aggregation strategies to achieve efficient CBE.
On the AlpacaEval benchmark, UniCBE saves over 17% of evaluation budgets while achieving a Pearson correlation with ground truth exceeding 0.995, demonstrating excellent accuracy and convergence. In scenarios where new models are continuously introduced, UniCBE can even save over 50% of evaluation costs, highlighting its improved scalability.

## Metadata
- venue: ICLR
- year: 2025
- authors: Peiwen Yuan, Shaoxiong Feng, Yiwei Li, Xinglin Wang, Yueqi Zhang, Jiayi Shi, Chuyi Tan, Boyuan Pan, Yao Hu, Kan Li
- arxiv_id: 
- openreview_id: rpwGUtTeA5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9e7ec666dcb3ef8f90e2c4017d28c5d7fff5951a.pdf
- published: 2025
- keywords: evaluation, efficient, scalability, accuracy, convergence
