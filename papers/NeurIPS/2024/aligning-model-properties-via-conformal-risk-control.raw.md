---
title: "Aligning Model Properties via Conformal Risk Control"
authors: ["William Overman", "Jacqueline Jil Vallon", "Mohsen Bayati"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9OHXQybMZB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f759372ac453f1d4d4be266a28876ff1295ddc65.pdf"
published: "2024"
categories: []
keywords: ["Alignment", "Conformal Prediction", "Conformal Risk Control", "Property Testing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:00+09:00"
---

# Aligning Model Properties via Conformal Risk Control

## Abstract
AI model alignment is crucial due to inadvertent biases in training data and the underspecified machine learning pipeline, where models with excellent test metrics may not meet end-user requirements. While post-training alignment via human feedback shows promise, these methods are often limited to generative AI settings where humans can interpret and provide feedback on model outputs. In traditional non-generative settings with numerical or categorical outputs, detecting misalignment through single-sample outputs remains challenging, and enforcing alignment during training requires repeating costly training processes.
In this paper we consider an alternative strategy. We propose interpreting model alignment through property testing, defining an aligned model $f$ as one belonging to a subset $\mathcal{P}$ of functions that exhibit specific desired behaviors. We focus on post-processing a pre-trained model $f$ to better align with $\mathcal{P}$ using conformal risk control. Specifically, we develop a general procedure for converting queries for testing a given property $\mathcal{P}$ to a collection of loss functions suitable for use in a conformal risk control algorithm. We prove a probabilistic guarantee that the resulting conformal interval around $f$ contains a function approximately satisfying $\mathcal{P}$. We exhibit applications of our methodology on a collection of supervised learning datasets for (shape-constrained) properties such as monotonicity and concavity. The general procedure is flexible and can be applied to a wide range of desired properties. Finally, we prove that pre-trained models will always require alignment techniques even as model sizes or training data increase, as long as the training data contains even small biases.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: William Overman, Jacqueline Jil Vallon, Mohsen Bayati
- arxiv_id: 
- openreview_id: 9OHXQybMZB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f759372ac453f1d4d4be266a28876ff1295ddc65.pdf
- published: 2024
- keywords: Alignment, Conformal Prediction, Conformal Risk Control, Property Testing
