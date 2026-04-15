---
title: "Contextual Similarity Distillation: Ensemble Uncertainties with a Single Model"
authors: ["Moritz Akiya Zanger", "Pascal R. Van der Vaart", "Wendelin Boehmer", "Matthijs T. J. Spaan"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "arms7s9dDK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2e11afbebd4af071519ffb3d09ae20640b5e3188.pdf"
published: "2026"
categories: []
keywords: ["Uncertainty Quantification", "Epistemic Uncertainty", "Reinforcement Learning", "Deep Ensembles", "Exploration", "Neural Tangent Kernel"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:45+09:00"
---

# Contextual Similarity Distillation: Ensemble Uncertainties with a Single Model

## Abstract
Uncertainty quantification is a critical aspect of reinforcement learning and deep learning, with numerous applications ranging from efficient exploration and stable offline reinforcement learning to outlier detection in medical diagnostics. The scale of modern neural networks, however, complicates the use of many theoretically well-motivated approaches such as full Bayesian inference. Approximate methods like deep ensembles can provide reliable uncertainty estimates but still remain computationally expensive. In this work, we propose contextual similarity distillation, a novel approach that explicitly estimates the variance of an ensemble of deep neural networks with a single model, without ever learning or evaluating such an ensemble in the first place. Our method builds on the predictable learning dynamics of wide neural networks, governed by the neural tangent kernel, to derive an efficient approximation of the predictive variance of an infinite ensemble. Specifically, we reinterpret the computation of ensemble variance as a supervised regression problem with kernel similarities as regression targets. The resulting model can estimate predictive variance at inference time with a single forward pass, and can make use of unlabeled target-domain data or data augmentations to refine its uncertainty estimates. We empirically validate our method across a variety of out-of-distribution detection benchmarks and sparse-reward reinforcement learning environments. We find that our single-model method performs competitively and sometimes superior to ensemble-based baselines and serves as a reliable signal for efficient exploration. These results, we believe, position contextual similarity distillation as a principled and scalable alternative for uncertainty quantification in reinforcement learning and general deep learning.

## Metadata
- venue: ICLR
- year: 2026
- authors: Moritz Akiya Zanger, Pascal R. Van der Vaart, Wendelin Boehmer, Matthijs T. J. Spaan
- arxiv_id: 
- openreview_id: arms7s9dDK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2e11afbebd4af071519ffb3d09ae20640b5e3188.pdf
- published: 2026
- keywords: Uncertainty Quantification, Epistemic Uncertainty, Reinforcement Learning, Deep Ensembles, Exploration, Neural Tangent Kernel
