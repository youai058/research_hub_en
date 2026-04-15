---
title: "Gradual Domain Adaptation via Manifold-Constrained Distributionally Robust Optimization"
authors: ["seyed amir hossein saberi", "Amir Najafi", "Amin Behjati", "Ala Emrani", "Yasaman Zolfimoselo", "Mahdi Shadrooy", "Abolfazl Motahari", "Babak Khalaj"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "UTNZKl5BUc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fae24f01dcf1059f6be92c28c0cb1c9f4c64d2fa.pdf"
published: "2024"
categories: []
keywords: ["Gradual Domain Adaptation", "Distributionally Robust Optimization", "Generalization Bound", "Error Propagation Characterization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:07+09:00"
---

# Gradual Domain Adaptation via Manifold-Constrained Distributionally Robust Optimization

## Abstract
The aim of this paper is to address the challenge of gradual domain adaptation within a class of manifold-constrained data distributions. In particular, we consider a sequence of $T\ge2$ data distributions $P_1,\ldots,P_T$ undergoing a gradual shift, where each pair of consecutive measures $P_i,P_{i+1}$ are close to each other in Wasserstein distance. We have a supervised dataset of size $n$ sampled from $P_0$, while for the subsequent distributions in the sequence, only unlabeled i.i.d. samples are available. Moreover, we assume that all distributions exhibit a known favorable attribute, such as (but not limited to) having intra-class soft/hard margins. In this context, we propose a methodology rooted in Distributionally Robust Optimization (DRO) with an adaptive Wasserstein radius. We theoretically show that this method guarantees the classification error across all $P_i$s can be suitably bounded. Our bounds rely on a newly introduced {\it {compatibility}} measure, which fully characterizes the error propagation dynamics along the sequence. Specifically, for inadequately constrained distributions, the error can exponentially escalate as we progress through the gradual shifts. Conversely, for appropriately constrained distributions, the error can be demonstrated to be linear or even entirely eradicated. We have substantiated our theoretical findings through several experimental results.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: seyed amir hossein saberi, Amir Najafi, Amin Behjati, Ala Emrani, Yasaman Zolfimoselo, Mahdi Shadrooy, Abolfazl Motahari, Babak Khalaj
- arxiv_id: 
- openreview_id: UTNZKl5BUc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fae24f01dcf1059f6be92c28c0cb1c9f4c64d2fa.pdf
- published: 2024
- keywords: Gradual Domain Adaptation, Distributionally Robust Optimization, Generalization Bound, Error Propagation Characterization
