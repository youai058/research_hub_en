---
title: "How many classifiers do we need?"
authors: ["Hyunsuk Kim", "Liam Hodgkinson", "Ryan Theisen", "Michael W. Mahoney"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "m5dyKArVn8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6c0cc9c39e8b9e81213e491a5cd72662641eba0d.pdf"
published: "2024"
categories: []
keywords: ["ensemble", "model aggregation", "machine learning", "computer vision"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:28+09:00"
---

# How many classifiers do we need?

## Abstract
As performance gains through scaling data and/or model size experience diminishing returns, it is becoming increasingly popular to turn to ensembling, where the predictions of multiple models are combined to improve accuracy. 
In this paper, we provide a detailed analysis of how the disagreement and the polarization (a notion we introduce and define in this paper) among classifiers relate to the performance gain achieved by aggregating individual classifiers, for majority vote strategies in classification tasks.
We address these questions in the following ways. 
(1) An upper bound for polarization is derived, and we propose what we call a neural polarization law: most interpolating neural network models are 4/3-polarized. Our empirical results not only support this conjecture but also show that polarization is nearly constant for a dataset, regardless of hyperparameters or architectures of classifiers. 
(2) The error rate of the majority vote classifier is considered under restricted entropy conditions, and we present a tight upper bound that indicates that the disagreement is linearly correlated with the error rate, and that the slope is linear in the polarization.
(3) We prove results for the asymptotic behavior of the disagreement in terms of the number of classifiers, which we show can help in predicting the performance for a larger number of classifiers from that of a smaller number. 
Our theoretical findings are supported by empirical results on several image classification tasks with various types of neural networks.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Hyunsuk Kim, Liam Hodgkinson, Ryan Theisen, Michael W. Mahoney
- arxiv_id: 
- openreview_id: m5dyKArVn8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6c0cc9c39e8b9e81213e491a5cd72662641eba0d.pdf
- published: 2024
- keywords: ensemble, model aggregation, machine learning, computer vision
