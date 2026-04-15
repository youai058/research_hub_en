---
title: "Fairness via Independence: A General Regularization Framework for Machine Learning"
authors: ["Yezi Liu", "Hanning Chen", "Wenjun Huang", "Yang Ni", "Mohsen Imani"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "sbEb0Ld6MK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3a929ce3b9a24cc34fdd96f63e4eab9a870dd5d0.pdf"
published: "2026"
categories: []
keywords: ["Bias Mitigation", "Statistical Independence", "Fairness in Machine Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:15+09:00"
---

# Fairness via Independence: A General Regularization Framework for Machine Learning

## Abstract
Fairness in machine learning has emerged as a central concern, as predictive models frequently inherit or even amplify biases present in training data. Such biases often manifest as unintended correlations between model outcomes and sensitive attributes, leading to systematic disparities across demographic groups. Existing approaches to fair learning largely fall into two directions: incorporating fairness constraints tailored to specific definitions, which limits their generalizability, or reducing the statistical dependence between predictions and sensitive attributes, which is more flexible but highly sensitive to the choice of distance measure. The latter strategy in particular raises the challenge of finding a principled and reliable measure of dependence that can perform consistently across tasks. In this work, we present a general and model-agnostic approach to address this challenge. The method is based on encouraging independence between predictions and sensitive features through an optimization framework that leverages the Cauchy–Schwarz (CS) Divergence as a principled measure of dependence. Prior studies suggest that CS Divergence provides a tighter theoretical bound compared to alternative distance measures used in earlier fairness methods, offering a stronger foundation for fairness-oriented optimization. Our framework, therefore, unifies prior efforts under a simple yet effective principle and highlights the value of carefully chosen statistical measures in fair learning. Through extensive empirical evaluation on four tabular datasets and one image dataset, we show that our approach consistently improves multiple fairness metrics while maintaining competitive accuracy.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yezi Liu, Hanning Chen, Wenjun Huang, Yang Ni, Mohsen Imani
- arxiv_id: 
- openreview_id: sbEb0Ld6MK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3a929ce3b9a24cc34fdd96f63e4eab9a870dd5d0.pdf
- published: 2026
- keywords: Bias Mitigation, Statistical Independence, Fairness in Machine Learning
