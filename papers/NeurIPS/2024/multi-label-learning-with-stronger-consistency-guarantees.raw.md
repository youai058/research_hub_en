---
title: "Multi-Label Learning with Stronger Consistency Guarantees"
authors: ["Anqi Mao", "Mehryar Mohri", "Yutao Zhong"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "zAuerb1KGx"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/238907b99661ce02cecd832f90a1e415af69d730.pdf"
published: "2024"
categories: []
keywords: ["multi-label learning", "consistency", "surrogate loss", "hamming loss", "learning theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:47+09:00"
---

# Multi-Label Learning with Stronger Consistency Guarantees

## Abstract
We present a detailed study of surrogate losses and algorithms for multi-label learning, supported by $H$-consistency bounds. We first show that, for the simplest form of multi-label loss (the popular Hamming loss), the well-known consistent binary relevance surrogate suffers from a sub-optimal dependency on the number of labels in terms of $H$-consistency bounds, when using smooth losses such as logistic losses. Furthermore, this loss function fails to account for label correlations. To address these drawbacks, we introduce a novel surrogate loss, *multi-label logistic loss*,  that accounts for label correlations and benefits from label-independent $H$-consistency bounds. We then broaden our analysis to cover a more extensive family of multi-label losses, including all common ones and a new extension defined based on linear-fractional functions with respect to the confusion matrix. We also extend our multi-label logistic losses to more comprehensive multi-label comp-sum losses, adapting comp-sum losses from standard classification to the multi-label learning. We prove that this family of surrogate losses benefits from $H$-consistency bounds, and thus Bayes-consistency, across any general multi-label loss. Our work thus proposes a unified surrogate loss framework benefiting from strong consistency guarantees for any multi-label loss, significantly expanding upon previous work which only established Bayes-consistency and for specific loss functions. Additionally, we adapt constrained losses from standard classification to multi-label constrained losses in a similar way, which also benefit from $H$-consistency bounds and thus Bayes-consistency for any multi-label loss. We further describe efficient gradient computation algorithms for minimizing the multi-label logistic loss.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Anqi Mao, Mehryar Mohri, Yutao Zhong
- arxiv_id: 
- openreview_id: zAuerb1KGx
- anthology_id: 
- pdf_url: https://openreview.net/pdf/238907b99661ce02cecd832f90a1e415af69d730.pdf
- published: 2024
- keywords: multi-label learning, consistency, surrogate loss, hamming loss, learning theory
