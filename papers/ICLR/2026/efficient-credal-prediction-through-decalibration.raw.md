---
title: "Efficient Credal Prediction through Decalibration"
authors: ["Paul Hofman", "Timo Löhr", "Maximilian Muschalik", "Yusuf Sale", "Eyke Hüllermeier"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BqOmsYIe7M"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d5f3394ab85fca1c8661ad207c3e7267b995bdc8.pdf"
published: "2026"
categories: []
keywords: ["efficient uncertainty representation", "credal sets", "relative likelihood"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:28+09:00"
---

# Efficient Credal Prediction through Decalibration

## Abstract
A reliable representation of uncertainty is essential for the application of modern machine learning methods in safety-critical settings. In this regard, the use of credal sets (i.e., convex sets of probability distributions) has recently been proposed as a suitable approach to representing epistemic uncertainty. However, as with other approaches to epistemic uncertainty, training credal predictors is computationally complex and usually involves (re-)training an ensemble of models. The resulting computational complexity prevents their adoption for complex models such as  foundation models and multi-modal systems. To address this problem, we propose an efficient method for credal prediction that is grounded in the notion of relative likelihood and inspired by techniques for the calibration of probabilistic classifiers. For each class label, our method predicts a range of plausible probabilities in the form of an interval. To produce the lower and upper bounds of these intervals, we propose a technique that we refer to as decalibration. Extensive experiments show that our method yields credal sets with strong performance across diverse tasks, including coverage–efficiency evaluation, out-of-distribution detection, and in-context learning. Notably, we demonstrate credal prediction on models such as TabPFN and CLIP—architectures for which the construction of credal sets was previously infeasible.

## Metadata
- venue: ICLR
- year: 2026
- authors: Paul Hofman, Timo Löhr, Maximilian Muschalik, Yusuf Sale, Eyke Hüllermeier
- arxiv_id: 
- openreview_id: BqOmsYIe7M
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d5f3394ab85fca1c8661ad207c3e7267b995bdc8.pdf
- published: 2026
- keywords: efficient uncertainty representation, credal sets, relative likelihood
