---
title: "Regression with Multi-Expert Deferral"
authors: ["Anqi Mao", "Mehryar Mohri", "Yutao Zhong"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5NTTCCO74S"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8bbe3b5d6cd9a25416cd56189ba8311bd6f2cd0d.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:35+09:00"
---

# Regression with Multi-Expert Deferral

## Abstract
Learning to defer with multiple experts is a framework where the learner can choose to defer the prediction to several experts. While this problem has received significant attention in classification contexts, it presents unique challenges in regression due to the infinite and continuous nature of the label space. In this work, we introduce a novel framework of *regression with deferral*, which involves deferring the prediction to multiple experts. We present a comprehensive analysis for both the single-stage scenario, where there is simultaneous learning of predictor and deferral functions, and the two-stage scenario, which involves a pre-trained predictor with a learned deferral function. We introduce new surrogate loss functions for both scenarios and prove that they are supported by $H$-consistency bounds. These bounds provide consistency guarantees that are stronger than Bayes consistency, as they are non-asymptotic and hypothesis set-specific. Our framework is versatile, applying to multiple experts, accommodating any bounded regression losses, addressing both instance-dependent and label-dependent costs, and supporting both single-stage and two-stage methods. Our single-stage formulation subsumes as a special case the recent *regression with abstention* (Cheng et al., 2023) framework, where only a single expert is considered, specifically for the squared loss and a label-independent cost. Minimizing our proposed loss functions directly leads to novel algorithms for regression with deferral. We report the results of extensive experiments showing the effectiveness of our proposed algorithms.

## Metadata
- venue: ICML
- year: 2024
- authors: Anqi Mao, Mehryar Mohri, Yutao Zhong
- arxiv_id: 
- openreview_id: 5NTTCCO74S
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8bbe3b5d6cd9a25416cd56189ba8311bd6f2cd0d.pdf
- published: 2024
