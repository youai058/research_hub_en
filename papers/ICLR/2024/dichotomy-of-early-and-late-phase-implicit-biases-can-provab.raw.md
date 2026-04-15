---
title: "Dichotomy of Early and Late Phase Implicit Biases Can Provably Induce Grokking"
authors: ["Kaifeng Lyu", "Jikai Jin", "Zhiyuan Li", "Simon Shaolei Du", "Jason D. Lee", "Wei Hu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XsHqr9dEGH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a44b7ffbd53a80fbd4d969f2e39aa59edf5c8012.pdf"
published: "2024"
categories: []
keywords: ["grokking", "implicit bias", "margin", "kernel", "training dynamics", "generalization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:06+09:00"
---

# Dichotomy of Early and Late Phase Implicit Biases Can Provably Induce Grokking

## Abstract
Recent work by Power et al. (2022) highlighted a surprising "grokking" phenomenon in learning arithmetic tasks: a neural net first "memorizes" the training set, resulting in perfect training accuracy but near-random test accuracy, and after training for sufficiently longer, it suddenly transitions to perfect test accuracy. This paper studies the grokking phenomenon in theoretical setups and shows that it can be induced by a dichotomy of early and late phase implicit biases. Specifically, when training homogeneous neural nets with large initialization and small weight decay on both classification and regression tasks, we prove that the training process gets trapped at a solution corresponding to a kernel predictor for a long time, and then a very sharp transition to min-norm/max-margin predictors occurs, leading to a dramatic change in test accuracy.

## Metadata
- venue: ICLR
- year: 2024
- authors: Kaifeng Lyu, Jikai Jin, Zhiyuan Li, Simon Shaolei Du, Jason D. Lee, Wei Hu
- arxiv_id: 
- openreview_id: XsHqr9dEGH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a44b7ffbd53a80fbd4d969f2e39aa59edf5c8012.pdf
- published: 2024
- keywords: grokking, implicit bias, margin, kernel, training dynamics, generalization
