---
title: "Consistent Diffusion Meets Tweedie: Training Exact Ambient Diffusion Models with Noisy Data"
authors: ["Giannis Daras", "Alex Dimakis", "Constantinos Costis Daskalakis"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "PlVjIGaFdH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3b44f9525830d7e5a738d9071cecb10fe0e47422.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:25+09:00"
---

# Consistent Diffusion Meets Tweedie: Training Exact Ambient Diffusion Models with Noisy Data

## Abstract
Ambient diffusion is a recently proposed framework for training diffusion models using corrupted data. Both Ambient Diffusion and alternative SURE-based approaches for learning diffusion models from corrupted data resort to approximations which deteriorate performance. We present the first framework for training diffusion models that provably sample from the uncorrupted distribution given only noisy training data, solving an open problem in Ambient diffusion. Our key technical contribution is a method that uses a double application of Tweedie's formula and a consistency loss function that allows us to extend sampling at noise levels below the observed data noise. We also provide further evidence that diffusion models memorize from their training sets by identifying extremely corrupted images that are almost perfectly reconstructed, raising copyright and privacy concerns. Our method for training using corrupted samples can be used to mitigate this problem. We demonstrate this by fine-tuning Stable Diffusion XL to generate samples from a distribution using only noisy samples. Our framework reduces the amount of memorization of the fine-tuning dataset, while maintaining competitive performance.

## Metadata
- venue: ICML
- year: 2024
- authors: Giannis Daras, Alex Dimakis, Constantinos Costis Daskalakis
- arxiv_id: 
- openreview_id: PlVjIGaFdH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3b44f9525830d7e5a738d9071cecb10fe0e47422.pdf
- published: 2024
