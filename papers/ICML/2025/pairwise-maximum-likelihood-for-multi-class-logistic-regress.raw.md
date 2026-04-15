---
title: "Pairwise Maximum Likelihood For Multi-Class Logistic Regression Model With Multiple Rare Classes"
authors: ["Xuetong Li", "Danyang Huang", "Hansheng Wang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9Kywz2fO26"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9027a284b1ce1306a800dade3bfcfe5d1627bb32.pdf"
published: "2025"
categories: []
keywords: ["Multi-class logistic regression model", "Pairwise maximum likelihood estimation", "Rare class analysis", "Car plate recognition"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:04+09:00"
---

# Pairwise Maximum Likelihood For Multi-Class Logistic Regression Model With Multiple Rare Classes

## Abstract
We study in this work the problem of multi-class logistic regression with one major class and multiple rare classes, which is motivated by a real application in TikTok live stream data. The model is inspired by the two-class logistic regression model of Wang (2020) but with surprising theoretical findings, which in turn motivate new estimation methods with excellent statistical and computational efficiency. 
Specifically, since rigorous theoretical analysis suggests that the resulting maximum likelihood estimators of different rare classes should be asymptotically independent, we consider to solve multiple pairwise two-class logistic regression problems instead of optimizing the joint log-likelihood function with computational challenge in multi-class problem, which are computationally much easier and can be conducted in a fully parallel way. To further reduce the computation cost, a subsample-based pairwise likelihood estimator is developed by down-sampling the major class. We show rigorously that the resulting estimators could be as asymptotically efficient as the global maximum likelihood estimator under appropriate regularity conditions. Extensive simulation studies are presented to support our theoretical findings and a TikTok live stream dataset is analyzed for illustration purpose.

## Metadata
- venue: ICML
- year: 2025
- authors: Xuetong Li, Danyang Huang, Hansheng Wang
- arxiv_id: 
- openreview_id: 9Kywz2fO26
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9027a284b1ce1306a800dade3bfcfe5d1627bb32.pdf
- published: 2025
- keywords: Multi-class logistic regression model, Pairwise maximum likelihood estimation, Rare class analysis, Car plate recognition
