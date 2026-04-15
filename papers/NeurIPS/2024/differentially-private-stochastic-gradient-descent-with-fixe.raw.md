---
title: "Differentially Private Stochastic Gradient Descent with Fixed-Size Minibatches: Tighter RDP Guarantees with or without Replacement"
authors: ["Jeremiah Birrell", "Mohammadreza Ebrahimi", "Rouzbeh Behnia", "Jason Pacheco"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "TJsknGasMy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e0eb51870ca3857821a9fc9f43370fa379cb36fe.pdf"
published: "2024"
categories: []
keywords: ["privacy preserving machine learning", "differential privacy", "differentially private stochastic gradient descent", "fixed-size subsampled mechanisms", "privacy amplification lemma"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:01+09:00"
---

# Differentially Private Stochastic Gradient Descent with Fixed-Size Minibatches: Tighter RDP Guarantees with or without Replacement

## Abstract
Differentially private stochastic gradient descent (DP-SGD) has been instrumental in privately training deep learning models by providing a framework to control and track the privacy loss incurred during training.  At the core of this computation lies a subsampling method that uses a privacy amplification lemma to enhance the privacy guarantees provided by the additive noise. Fixed size subsampling is appealing for its constant memory usage, unlike the variable sized minibatches in Poisson subsampling. It is also of interest in addressing class imbalance and federated learning. Current computable guarantees for fixed-size subsampling are not tight and do not consider both add/remove and replace-one adjacency relationships. We present a new and holistic Rényi differential privacy (RDP)  accountant for DP-SGD with fixed-size subsampling without replacement (FSwoR) and with replacement (FSwR). For FSwoR we consider both add/remove and replace-one adjacency, where we improve on the best current computable bound by a factor of $4$. We also show for the first time that the widely-used Poisson subsampling and FSwoR with replace-one adjacency have the same privacy to leading order in the sampling probability. Our work suggests that FSwoR is often preferable to Poisson subsampling due to constant memory usage. Our FSwR accountant includes explicit non-asymptotic upper and lower bounds and, to the  authors' knowledge, is the first such RDP analysis of fixed-size  subsampling with replacement  for DP-SGD. We analytically and empirically compare fixed size and Poisson subsampling, and show that DP-SGD gradients in a fixed-size subsampling regime exhibit lower variance in practice in addition to memory usage benefits.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Jeremiah Birrell, Mohammadreza Ebrahimi, Rouzbeh Behnia, Jason Pacheco
- arxiv_id: 
- openreview_id: TJsknGasMy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e0eb51870ca3857821a9fc9f43370fa379cb36fe.pdf
- published: 2024
- keywords: privacy preserving machine learning, differential privacy, differentially private stochastic gradient descent, fixed-size subsampled mechanisms, privacy amplification lemma
