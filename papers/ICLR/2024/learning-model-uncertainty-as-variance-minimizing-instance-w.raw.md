---
title: "Learning model uncertainty as variance-minimizing instance weights"
authors: ["Nishant Jain", "Karthikeyan Shanmugam", "Pradeep Shenoy"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bDWXhzZT40"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ebdd64cc233d279eff550647eb57b1baf57fd9eb.pdf"
published: "2024"
categories: []
keywords: ["loss reweighting", "epistemic uncertainty", "bi-level optimization", "model calibration", "bayesian neural networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:48+09:00"
---

# Learning model uncertainty as variance-minimizing instance weights

## Abstract
Predictive uncertainty--a model’s self-awareness regarding its accuracy on an input--is key for both building robust models via training interventions and for test-time applications such as selective classification. We propose a novel instance-conditional reweighting approach that captures predictive uncertainty using an auxiliary network, and unifies these train- and test-time applications. The auxiliary network is trained using a meta-objective in a bilevel optimization framework. A key contribution of our proposal is the meta-objective of minimizing dropout variance, an approximation of Bayesian predictive uncertainty, We show in controlled experiments that we effectively capture diverse specific notions of uncertainty through this meta-objective, while previous approaches only capture certain aspects. These results translate to significant gains in real-world settings–selective classification, label noise, domain adaptation, calibration–and across datasets–Imagenet, Cifar100, diabetic retinopathy, Camelyon, WILDs, Imagenet-C,-A,-R, Clothing-1.6M, etc. For Diabetic Retinopathy, we see upto 3.4\%/3.3\% accuracy & AUC gains over SOTA in selective classification. We also improve upon large-scale pretrained models such as PLEX.

## Metadata
- venue: ICLR
- year: 2024
- authors: Nishant Jain, Karthikeyan Shanmugam, Pradeep Shenoy
- arxiv_id: 
- openreview_id: bDWXhzZT40
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ebdd64cc233d279eff550647eb57b1baf57fd9eb.pdf
- published: 2024
- keywords: loss reweighting, epistemic uncertainty, bi-level optimization, model calibration, bayesian neural networks
