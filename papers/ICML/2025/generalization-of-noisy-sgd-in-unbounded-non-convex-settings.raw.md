---
title: "Generalization of noisy SGD in unbounded non-convex settings"
authors: ["Leello Tadesse Dadi", "Volkan Cevher"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Au9rfI6Fjd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/413a00bf75b8001f8991d8d95dd2fb6f5377f3bf.pdf"
published: "2025"
categories: []
keywords: ["Information theoretic generalization", "Langevin", "SGD", "differential privacy"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:08+09:00"
---

# Generalization of noisy SGD in unbounded non-convex settings

## Abstract
We study generalization of iterative noisy gradient schemes on smooth non-convex losses. Formally, we establish time-independent information theoretic generalization bounds for Stochastic Gradient Langevin Dynamics (SGLD) that do not diverge as the iteration count increases. Our bounds are obtained through a stability argument: we analyze the difference between two SGLD sequences ran in parallel on two datasets sampled from the same distribution. Our result only requires an isoperimetric inequality to hold, which is merely a restriction on the tails of the loss. Our work relaxes the assumptions of prior work to establish that the iterates stay within a bounded KL divergence from each other. Under an additional dissipativity assumption, we show that the stronger Renyi divergence also stays bounded by establishing a uniform log-Sobolev constant of the iterates. Without dissipativity, we sidestep the need for local log-Sobolev inequalities and instead exploit the regularizing properties of Gaussian convolution. These techniques allow us to show that strong convexity is not necessary for finite stability bounds. Our work shows that noisy SGD can have finite, iteration-independent, generalization and differential privacy bounds in unbounded non-convex settings.

## Metadata
- venue: ICML
- year: 2025
- authors: Leello Tadesse Dadi, Volkan Cevher
- arxiv_id: 
- openreview_id: Au9rfI6Fjd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/413a00bf75b8001f8991d8d95dd2fb6f5377f3bf.pdf
- published: 2025
- keywords: Information theoretic generalization, Langevin, SGD, differential privacy
