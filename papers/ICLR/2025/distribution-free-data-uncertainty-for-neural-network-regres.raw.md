---
title: "Distribution-Free Data Uncertainty for Neural Network Regression"
authors: ["Domokos M. Kelen", "Ádám Jung", "Péter Kersch", "Andras A Benczur"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pDDODPtpx9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/763c2430cbe272fedf9975b8a70e6635341bdd56.pdf"
published: "2025"
categories: []
keywords: ["deep learning", "uncertainty quantification", "regression uncertainty", "aleatoric uncertainty", "scoring rules", "continuous ranked probability score"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:51+09:00"
---

# Distribution-Free Data Uncertainty for Neural Network Regression

## Abstract
Quantifying uncertainty is an essential part of predictive modeling, especially in the context of high-stakes decision-making. While classification output includes data uncertainty by design in the form of class probabilities, the regression task generally aims only to predict the expected value of the target variable. Probabilistic extensions often assume parametric distributions around the expected value, optimizing the likelihood over the resulting explicit densities. However, using parametric distributions can limit practical applicability, making it difficult for models to capture skewed, multi-modal, or otherwise complex distributions. In this paper, we propose optimizing a novel nondeterministic neural network regression architecture for loss functions derived from a sample-based approximation of the continuous ranked probability score (CRPS), enabling a truly distribution-free approach by learning to sample from the target's aleatoric distribution, rather than predicting explicit densities. Our approach allows the model to learn well-calibrated, arbitrary uni- and multivariate output distributions. We evaluate the method on a variety of synthetic and real-world tasks, including uni- and multivariate problems, function inverse approximation, and standard regression uncertainty benchmarks. Finally, we make all experiment code publicly available.

## Metadata
- venue: ICLR
- year: 2025
- authors: Domokos M. Kelen, Ádám Jung, Péter Kersch, Andras A Benczur
- arxiv_id: 
- openreview_id: pDDODPtpx9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/763c2430cbe272fedf9975b8a70e6635341bdd56.pdf
- published: 2025
- keywords: deep learning, uncertainty quantification, regression uncertainty, aleatoric uncertainty, scoring rules, continuous ranked probability score
