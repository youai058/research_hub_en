---
title: "Diffusing DeBias: Synthetic Bias Amplification for Model Debiasing"
authors: ["Massimiliano Ciranni", "Vito Paolo Pastore", "Roberto Di Via", "Enzo Tartaglione", "Francesca Odone", "Vittorio Murino"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "66Z5tS8E45"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/28c96aa6ccd780bc52d0e4dfe4a4e6544b857406.pdf"
published: "2025"
categories: []
keywords: ["Model debiasing", "bias amplification", "diffusion models", "image classification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:37+09:00"
---

# Diffusing DeBias: Synthetic Bias Amplification for Model Debiasing

## Abstract
The effectiveness of deep learning models in classification tasks is often challenged by the quality and quantity of training data whenever they are affected by strong spurious correlations between specific attributes and target labels. This results in a form of bias affecting training data, which typically leads to unrecoverable weak generalization in prediction. This paper addresses this problem by leveraging bias amplification with generated synthetic data only: we introduce Diffusing DeBias (DDB), a novel approach acting as a plug-in for common methods of unsupervised model debiasing, exploiting the inherent bias-learning tendency of diffusion models in data generation. Specifically, our approach adopts conditional diffusion models to generate synthetic bias-aligned images, which fully replace the original training set for learning an effective bias amplifier model to be subsequently incorporated into an end-to-end and a two-step unsupervised debiasing approach. By tackling the fundamental issue of bias-conflicting training samples’ memorization in learning auxiliary models, typical of this type of technique, our proposed method outperforms the current state-of-the-art in multiple benchmark datasets, demonstrating its potential as a versatile and effective tool for tackling bias in deep learning models. Code is available at https://github.com/Malga-Vision/DiffusingDeBias

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Massimiliano Ciranni, Vito Paolo Pastore, Roberto Di Via, Enzo Tartaglione, Francesca Odone, Vittorio Murino
- arxiv_id: 
- openreview_id: 66Z5tS8E45
- anthology_id: 
- pdf_url: https://openreview.net/pdf/28c96aa6ccd780bc52d0e4dfe4a4e6544b857406.pdf
- published: 2025
- keywords: Model debiasing, bias amplification, diffusion models, image classification
