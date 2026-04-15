---
title: "Improving Text Style Transfer using Masked Diffusion Language Models with Inference-time Scaling"
authors: ["Tejomay Kishor Padole", "Suyash P Awate", "Pushpak Bhattacharyya"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2508.10995"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2508.10995v2"
published: "2025-08-14"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# Improving Text Style Transfer using Masked Diffusion Language Models with Inference-time Scaling

## Abstract
Masked diffusion language models (MDMs) have recently gained traction as a viable generative framework for natural language. This can be attributed to its scalability and ease of training compared to other diffusion model paradigms for discrete data, establishing itself as the state-of-the-art non-autoregressive generator for discrete data. Diffusion models, in general, have shown excellent ability to improve the generation quality by leveraging inference-time scaling either by increasing the number of denoising steps or by using external verifiers on top of the outputs of each step to guide the generation. In this work, we propose a verifier-based inference-time scaling method that aids in finding a better candidate generation during the denoising process of the MDM. Our experiments demonstrate the application of MDMs for standard text-style transfer tasks and establish MDMs as a better alternative to autoregressive language models. Additionally, we show that a simple soft-value-based verifier setup for MDMs using off-the-shelf pre-trained embedding models leads to significant gains in generation quality even when used on top of typical classifier-free guidance setups in the existing literature.

## Metadata
- venue: arXiv
- year: 2025
- authors: Tejomay Kishor Padole, Suyash P Awate, Pushpak Bhattacharyya
- arxiv_id: 2508.10995
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2508.10995v2
- published: 2025-08-14
