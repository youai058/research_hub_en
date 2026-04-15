---
title: "Reducing Confounding Bias without Data Splitting for Causal Inference via Optimal Transport"
authors: ["Yuguang Yan", "Zongyu Li", "Haolin Yang", "Zeqin Yang", "Hao Zhou", "Ruichu Cai", "Zhifeng Hao"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "fd7ddFBNmP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e1ee29ce21aaad30a38978dfdae67532d71d5436.pdf"
published: "2025"
categories: []
keywords: ["Causal inference", "continuous treatment", "optimal transport"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:24+09:00"
---

# Reducing Confounding Bias without Data Splitting for Causal Inference via Optimal Transport

## Abstract
Causal inference seeks to estimate the effect given a treatment such as a medicine or the dosage of a medication. To reduce the confounding bias caused by the non-randomized treatment assignment, most existing methods reduce the shift between subpopulations receiving different treatments. However, these methods split limited training samples into smaller groups, which cuts down the number of samples in each group, while precise distribution estimation and alignment highly rely on a sufficient number of training samples. In this paper, we propose a distribution alignment paradigm without data splitting, which can be naturally applied in the settings of binary and continuous treatments. To this end, we characterize the confounding bias by considering different probability measures of the same set including all the training samples, and exploit the optimal transport theory to analyze the confounding bias and outcome estimation error. Based on this, we propose to learn balanced representations by reducing the bias between the marginal distribution and the conditional distribution of a treatment. As a result, data reduction caused by splitting is avoided, and the outcome prediction model trained on one treatment group can be generalized to the entire population. The experiments on both binary and continuous treatment settings demonstrate the effectiveness of our method.

## Metadata
- venue: ICML
- year: 2025
- authors: Yuguang Yan, Zongyu Li, Haolin Yang, Zeqin Yang, Hao Zhou, Ruichu Cai, Zhifeng Hao
- arxiv_id: 
- openreview_id: fd7ddFBNmP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e1ee29ce21aaad30a38978dfdae67532d71d5436.pdf
- published: 2025
- keywords: Causal inference, continuous treatment, optimal transport
