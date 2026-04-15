---
title: "Iterative Missing Data Imputation with Model Form Adaptation and Non-Missing Feature Supervision"
authors: ["Hao Wang", "zhengnan li", "Zhichao Chen", "Xu Chen", "Shuting He", "Guangyi Liu", "Haoxuan Li", "Zhouchen Lin"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "L84DdFuvwV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ca2ef74afad7fdd8948577cd965847125da04110.pdf"
published: "2025"
categories: []
keywords: ["missing data imputation", "missing data completion", "missing value imputation", "kernel", "ridge regression", "non-missing feature"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:30+09:00"
---

# Iterative Missing Data Imputation with Model Form Adaptation and Non-Missing Feature Supervision

## Abstract
Iterative imputation is a prevalent method for missing data imputation, where each feature is imputed iteratively by treating it as a target variable estimated from all other features. However, iterative imputation method suffers from two principal limitations: 
(1) it imposes a single parametric model form to impute all features, neglecting the potential for optimal models to vary among features, which risks model misspecification; and
(2) it assumes every feature contains missing values, overlooking the potential presence of non-missing features, termed as oracle features, which are informative for imputation. 
To address these limitations, we propose kernel point imputation (KPI), a bi-level optimization framework for iterative missing data imputation. 
At the inner level, KPI adaptively learns the optimal model form for each feature within a reproducing kernel Hilbert space, addressing limitation (1). At the outer level, KPI utilizes oracle features as supervisory signals to iteratively refine the imputations, addressing limitation (2). 
Experiments demonstrate that KPI outperforms competitive imputation methods. Code is available at https://github.com/FMLYD/kpi.git.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Hao Wang, zhengnan li, Zhichao Chen, Xu Chen, Shuting He, Guangyi Liu, Haoxuan Li, Zhouchen Lin
- arxiv_id: 
- openreview_id: L84DdFuvwV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ca2ef74afad7fdd8948577cd965847125da04110.pdf
- published: 2025
- keywords: missing data imputation, missing data completion, missing value imputation, kernel, ridge regression, non-missing feature
