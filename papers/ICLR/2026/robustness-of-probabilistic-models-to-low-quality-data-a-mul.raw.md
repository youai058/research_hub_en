---
title: "Robustness of Probabilistic Models to Low-Quality Data: A Multi-Perspective Analysis"
authors: ["Liu Peng", "Yaochu Jin"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ZFZhV7Snf4"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/498f3d627454def5bb3e2ee1a1b7ee4631ba6b04.pdf"
published: "2026"
categories: []
keywords: ["data quality; probabilistic model; multi-perspective analysis;"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:33+09:00"
---

# Robustness of Probabilistic Models to Low-Quality Data: A Multi-Perspective Analysis

## Abstract
This paper investigates a critical challenge in modern machine learning: 
how different probabilistic models withstand low-quality training data. 
Through a systematic, comparative investigation, 
we reveal a stark spectrum of robustness. 
Empirically, we find that autoregressive language models 
exhibit remarkable resilience against both token-level noise 
and structural corruption (for GPT-2, test NLL increases modestly from 
2.87 to 3.59 despite 50\% corruption). 
By sharp contrast, class-conditional diffusion models degrade catastrophically 
under identical noise levels (image-label consistency plummets by 56.81\%), 
while image classifiers show a moderate vulnerability that diminishes with dataset scale.
To explain these discrepancies, 
we analyze the results through a multi-perspective lens 
integrating information theory, PAC learning, and gradient dynamics. 
This framework identifies what informational properties drive robustness, 
why they are required for generalization, 
and how the optimization process achieves this resilience.
These analyses suggest that robustness is heavily influenced by two key principles: 
the richness of conditioning information, which constrains the learning problem, 
and the absolute information content of the training data, which allows the signal from correct information to dominate statistical noise.

## Metadata
- venue: ICLR
- year: 2026
- authors: Liu Peng, Yaochu Jin
- arxiv_id: 
- openreview_id: ZFZhV7Snf4
- anthology_id: 
- pdf_url: https://openreview.net/pdf/498f3d627454def5bb3e2ee1a1b7ee4631ba6b04.pdf
- published: 2026
- keywords: data quality; probabilistic model; multi-perspective analysis;
