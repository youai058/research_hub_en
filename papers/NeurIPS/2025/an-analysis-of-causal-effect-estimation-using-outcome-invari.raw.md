---
title: "An Analysis of Causal Effect Estimation using Outcome Invariant Data Augmentation"
authors: ["UZAIR AKBAR", "Niki Kilbertus", "Hao Shen", "Krikamol Muandet", "Bo Dai"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "C1LVIInfZO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8114367043ade3658c5e579778d50f4103ffcb12.pdf"
published: "2025"
categories: []
keywords: ["Causal Inference", "Data Augmentation", "Instrumental Variables", "Out-of-distribution Generalization", "Causal Regularization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:31+09:00"
---

# An Analysis of Causal Effect Estimation using Outcome Invariant Data Augmentation

## Abstract
The technique of data augmentation (DA) is often used in machine learning for regularization purposes to better generalize under i.i.d. settings. In this work, we present a unifying framework with topics in causal inference to make a case for the use of DA beyond just the i.i.d. setting, but for generalization across interventions as well. Specifically, we argue that when the outcome generating mechanism is invariant to our choice of DA, then such augmentations can effectively be thought of as interventions on the treatment generating mechanism itself. This can potentially help to reduce bias in causal effect estimation arising from hidden confounders. In the presence of such unobserved confounding we typically make use of instrumental variables (IVs)—sources of treatment randomization that are conditionally independent of the outcome. However, IVs may not be as readily available as DA for many applications, which is the main motivation behind this work. By appropriately regularizing IV based estimators, we introduce the concept of *IV-like (IVL)* regression for mitigating confounding bias and improving predictive performance across interventions even when certain IV properties are relaxed. Finally, we cast parameterized DA as an IVL regression problem and show that when used in composition can simulate a worst-case application of such DA, further improving performance on causal estimation and generalization tasks beyond what simple DA may offer. This is shown both theoretically for the population case and via simulation experiments for the finite sample case using a simple linear example. We also present real data experiments to support our case.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: UZAIR AKBAR, Niki Kilbertus, Hao Shen, Krikamol Muandet, Bo Dai
- arxiv_id: 
- openreview_id: C1LVIInfZO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8114367043ade3658c5e579778d50f4103ffcb12.pdf
- published: 2025
- keywords: Causal Inference, Data Augmentation, Instrumental Variables, Out-of-distribution Generalization, Causal Regularization
