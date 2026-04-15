---
title: "sRGB Real Noise Modeling via Noise-Aware Sampling with Normalizing Flows"
authors: ["Dongjin Kim", "Donggoo Jung", "Sungyong Baik", "Tae Hyun Kim"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2XBBumBGeP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4e4c68a8b09ae4ef7e4d0ff1f101a225642f3723.pdf"
published: "2024"
categories: []
keywords: ["sRGB real noise modeling", "Normalizing flow", "Low-level vision"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:08+09:00"
---

# sRGB Real Noise Modeling via Noise-Aware Sampling with Normalizing Flows

## Abstract
Noise poses a widespread challenge in signal processing, particularly when it comes to denoising images. Although convolutional neural networks (CNNs) have exhibited remarkable success in this field, they are predicated upon the belief that noise follows established distributions, which restricts their practicality when dealing with real-world noise. To overcome this limitation, several efforts have been taken to collect noisy image datasets from the real world. Generative methods, employing techniques such as generative adversarial networks (GANs) and normalizing flows (NFs), have emerged as a solution for generating realistic noisy images. Recent works model noise using camera metadata, however requiring metadata even for sampling phase. In contrast, in this work, we aim to estimate the underlying camera settings, enabling us to improve noise modeling and generate diverse noise distributions. To this end, we introduce a new NF framework that allows us to both classify noise based on camera settings and generate various noisy images. Through experimental results, our model demonstrates exceptional noise quality and leads in denoising performance on benchmark datasets.

## Metadata
- venue: ICLR
- year: 2024
- authors: Dongjin Kim, Donggoo Jung, Sungyong Baik, Tae Hyun Kim
- arxiv_id: 
- openreview_id: 2XBBumBGeP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4e4c68a8b09ae4ef7e4d0ff1f101a225642f3723.pdf
- published: 2024
- keywords: sRGB real noise modeling, Normalizing flow, Low-level vision
