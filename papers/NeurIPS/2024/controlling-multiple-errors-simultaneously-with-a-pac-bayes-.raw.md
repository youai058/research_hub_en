---
title: "Controlling Multiple Errors Simultaneously with a PAC-Bayes Bound"
authors: ["Reuben Adams", "John Shawe-Taylor", "Benjamin Guedj"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "lwpfH9wVkO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b2a01b03d14b41742206340ab313fea1facf52fc.pdf"
published: "2024"
categories: []
keywords: ["PAC-Bayes", "Generalization", "Statistical Learning Theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:44+09:00"
---

# Controlling Multiple Errors Simultaneously with a PAC-Bayes Bound

## Abstract
Current PAC-Bayes generalisation bounds are restricted to scalar metrics of performance, such as the loss or error rate. However, one ideally wants more information-rich certificates that control the entire distribution of possible outcomes, such as the distribution of the test loss in regression, or the probabilities of different mis-classifications. We provide the first PAC-Bayes bound capable of providing such rich information by bounding the Kullback-Leibler divergence between the empirical and true probabilities of a set of $M$ error types, which can either be discretized loss values for regression, or the elements of the confusion matrix (or a partition thereof) for classification. We transform our bound into a differentiable training objective. Our bound is especially useful in cases where the severity of different mis-classifications may change over time; existing PAC-Bayes bounds can only bound a particular pre-decided weighting of the error types. In contrast our bound implicitly controls all uncountably many weightings simultaneously.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Reuben Adams, John Shawe-Taylor, Benjamin Guedj
- arxiv_id: 
- openreview_id: lwpfH9wVkO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b2a01b03d14b41742206340ab313fea1facf52fc.pdf
- published: 2024
- keywords: PAC-Bayes, Generalization, Statistical Learning Theory
