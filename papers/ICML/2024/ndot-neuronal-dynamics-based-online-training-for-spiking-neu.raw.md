---
title: "NDOT: Neuronal Dynamics-based Online Training for Spiking Neural Networks"
authors: ["Haiyan Jiang", "Giulia De Masi", "Huan Xiong", "Bin Gu"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "elF0QoBSFV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cafae435342dc2085c5e27f3823aa642775a21d1.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:44+09:00"
---

# NDOT: Neuronal Dynamics-based Online Training for Spiking Neural Networks

## Abstract
Spiking Neural Networks (SNNs) are attracting great attention for their energy-efficient and fast-inference properties in neuromorphic computing. However, the efficient training of deep SNNs poses challenges in gradient calculation due to the non-differentiability of their binary spike-generating activation functions. The widely used surrogate gradient (SG) method, combined with the back-propagation through time (BPTT), has shown considerable effectiveness. Yet, BPTT's process of unfolding and back-propagating along the computation graph requires storing intermediate information at all time-steps, resulting in huge memory consumption and failing to meet online requirements. In this work, we propose Neuronal Dynamics-based Online Training (NDOT) for SNNs, which uses the neuronal dynamics-based temporal dependency/sensitivity in gradient computation. NDOT enables forward-in-time learning by decomposing the full gradient into temporal and spatial gradients. To illustrate the intuition behind NDOT, we employ the Follow-the-Regularized-Leader (FTRL) algorithm. FTRL explicitly utilizes historical information and addresses limitations in instantaneous loss. Our proposed NDOT method accurately captures temporal dependencies through neuronal dynamics, functioning similarly to FTRL's explicit utilizing historical information. Experiments on CIFAR-10, CIFAR-100, and CIFAR10-DVS demonstrate the superior performance of our NDOT method on large-scale static and neuromorphic datasets within a small number of time steps. The codes are available at https://github.com/HaiyanJiang/SNN-NDOT.

## Metadata
- venue: ICML
- year: 2024
- authors: Haiyan Jiang, Giulia De Masi, Huan Xiong, Bin Gu
- arxiv_id: 
- openreview_id: elF0QoBSFV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cafae435342dc2085c5e27f3823aa642775a21d1.pdf
- published: 2024
