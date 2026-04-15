---
title: "Minimizing False-Positive Attributions in Explanations of Non-Linear Models"
authors: ["Anders Gjølbye", "Stefan Haufe", "Lars Kai Hansen"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ORrCEtiiVX"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/15dd0fc797f0eb17afb3ae18adac0bb3d3139863.pdf"
published: "2025"
categories: []
keywords: ["Explainable AI", "Interpretability", "Suppressor Variables", "Non-Linear Problems", "Machine Learning", "EEG"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:40+09:00"
---

# Minimizing False-Positive Attributions in Explanations of Non-Linear Models

## Abstract
Suppressor variables can influence model predictions without being dependent on the target outcome, and they pose a significant challenge for Explainable AI (XAI) methods. These variables may cause false-positive feature attributions, undermining the utility of explanations. Although effective remedies exist for linear models, their extension to non-linear models and instance-based explanations has remained limited. We introduce PatternLocal, a novel XAI technique that addresses this gap. PatternLocal begins with a locally linear surrogate, e.g., LIME, KernelSHAP, or gradient-based methods, and transforms the resulting discriminative model weights into a generative representation, thereby suppressing the influence of suppressor variables while preserving local fidelity. In extensive hyperparameter optimization on the XAI-TRIS benchmark, PatternLocal consistently outperformed other XAI methods and reduced false-positive attributions when explaining non-linear tasks, thereby enabling more reliable and actionable insights. We further evaluate PatternLocal on an EEG motor imagery dataset, demonstrating physiologically plausible explanations.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Anders Gjølbye, Stefan Haufe, Lars Kai Hansen
- arxiv_id: 
- openreview_id: ORrCEtiiVX
- anthology_id: 
- pdf_url: https://openreview.net/pdf/15dd0fc797f0eb17afb3ae18adac0bb3d3139863.pdf
- published: 2025
- keywords: Explainable AI, Interpretability, Suppressor Variables, Non-Linear Problems, Machine Learning, EEG
