---
title: "Cost-Sensitive Freeze-thaw Bayesian Optimization for Efficient Hyperparameter Tuning"
authors: ["Dong Bok Lee", "Aoxuan Silvia Zhang", "Byungjoo Kim", "Junhyeon Park", "Steven Adriaensen", "Juho Lee", "Sung Ju Hwang", "Hae Beom Lee"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ZUb4JpNoJe"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/79a85aa9bc6cde3ef5a0bb5ef4eab81a8fd3abdc.pdf"
published: "2025"
categories: []
keywords: ["Cost-Sensitive", "Bayesian Optimization", "Multi-Fidelity HPO", "PFNs", "Transfer Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:21+09:00"
---

# Cost-Sensitive Freeze-thaw Bayesian Optimization for Efficient Hyperparameter Tuning

## Abstract
In this paper, we address the problem of cost-sensitive hyperparameter optimization (HPO) built upon freeze-thaw Bayesian optimization (BO). Specifically, we assume a scenario where users want to early-stop the HPO process when the expected performance improvement is not satisfactory with respect to the additional computational cost. Motivated by this scenario, we introduce \emph{utility} in the freeze-thaw framework, a function describing the trade-off between the cost and performance that can be estimated from the user's preference data. This utility function, combined with our novel acquisition function and stopping criterion, allows us to dynamically continue training the configuration that we expect to maximally improve the utility in the future, and also automatically stop the HPO process around the maximum utility. Further, we improve the sample efficiency of existing freeze-thaw methods with transfer learning to develop a specialized surrogate model for the cost-sensitive HPO problem. We validate our algorithm on established multi-fidelity HPO benchmarks and show that it outperforms all the previous freeze-thaw BO and transfer-BO baselines we consider, while achieving a significantly better trade-off between the cost and performance.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Dong Bok Lee, Aoxuan Silvia Zhang, Byungjoo Kim, Junhyeon Park, Steven Adriaensen, Juho Lee, Sung Ju Hwang, Hae Beom Lee
- arxiv_id: 
- openreview_id: ZUb4JpNoJe
- anthology_id: 
- pdf_url: https://openreview.net/pdf/79a85aa9bc6cde3ef5a0bb5ef4eab81a8fd3abdc.pdf
- published: 2025
- keywords: Cost-Sensitive, Bayesian Optimization, Multi-Fidelity HPO, PFNs, Transfer Learning
