---
title: "Robust Classification via Regression for Learning with Noisy Labels"
authors: ["Erik Englesson", "Hossein Azizpour"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "wfgZc3IMqo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dc6d5771bf99d6ea8d806a95a0283ab492a6448c.pdf"
published: "2024"
categories: []
keywords: ["label noise", "noisy labels", "robustness", "Gaussian noise", "classification", "log-ratio transform", "compositional data analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:54+09:00"
---

# Robust Classification via Regression for Learning with Noisy Labels

## Abstract
Deep neural networks and large-scale datasets have revolutionized the field of machine learning. However, these large networks are susceptible to overfitting to label noise, resulting in reduced generalization. To address this challenge, two promising approaches have emerged: i) loss reweighting, which reduces the influence of noisy examples on the training loss, and ii) label correction that replaces noisy labels with estimated true labels. These directions have been pursued separately or combined as independent methods, lacking a unified approach. In this work, we present a unified method that seamlessly combines loss reweighting and label correction to enhance robustness against label noise in classification tasks. Specifically, by leveraging ideas from compositional data analysis in statistics, we frame the problem as a regression task, where loss reweighting and label correction can naturally be achieved with a shifted Gaussian label noise model. Our unified approach achieves strong performance compared to recent baselines on several noisy labelled datasets. We believe this work is a promising step towards robust deep learning in the presence of label noise. Our code is available at: https://github.com/ErikEnglesson/SGN.

## Metadata
- venue: ICLR
- year: 2024
- authors: Erik Englesson, Hossein Azizpour
- arxiv_id: 
- openreview_id: wfgZc3IMqo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dc6d5771bf99d6ea8d806a95a0283ab492a6448c.pdf
- published: 2024
- keywords: label noise, noisy labels, robustness, Gaussian noise, classification, log-ratio transform, compositional data analysis
