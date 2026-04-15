---
title: "The Implicit Bias of Gradient Descent on Separable Multiclass Data"
authors: ["Hrithik Ravi", "Clayton Scott", "Daniel Soudry", "Yutong Wang"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JlWn80mTJi"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a98548ee7fe755a8977ce11fead8d69c849f366f.pdf"
published: "2024"
categories: []
keywords: ["gradient descent", "multiclass classification", "hard-margin SVM", "implicit bias"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:28+09:00"
---

# The Implicit Bias of Gradient Descent on Separable Multiclass Data

## Abstract
Implicit bias describes the phenomenon where optimization-based training algorithms, without explicit regularization, show a preference for simple estimators even when more complex estimators have equal objective values. Multiple works have developed the theory of implicit bias for binary classification under the assumption that the loss satisfies an *exponential tail property*. However, there is a noticeable gap in analysis for multiclass classification, with only a handful of results which themselves are restricted to the cross-entropy loss. In this work, we employ the framework of Permutation Equivariant and Relative Margin-based (PERM) losses [Wang and Scott, 2024] to introduce a multiclass extension of the exponential tail property. This class of losses includes not only cross-entropy but also other losses. Using this framework, we extend the implicit bias result of Soudry et al. [2018] to multiclass classification. Furthermore, our proof techniques closely mirror those of the binary case, thus illustrating the power of the PERM framework for bridging the binary-multiclass gap.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Hrithik Ravi, Clayton Scott, Daniel Soudry, Yutong Wang
- arxiv_id: 
- openreview_id: JlWn80mTJi
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a98548ee7fe755a8977ce11fead8d69c849f366f.pdf
- published: 2024
- keywords: gradient descent, multiclass classification, hard-margin SVM, implicit bias
