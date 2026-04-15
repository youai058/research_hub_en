---
title: "Hyper-Transforming Latent Diffusion Models"
authors: ["Ignacio Peis", "Batuhan Koyuncu", "Isabel Valera", "Jes Frellsen"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "yhgcRwJ9Dn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/345e9cdf732bb81ae28716d900d2fa1d9bcaa2d7.pdf"
published: "2025"
categories: []
keywords: ["Latent Diffusion Models", "Transformers", "INRs"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:13+09:00"
---

# Hyper-Transforming Latent Diffusion Models

## Abstract
We introduce a novel generative framework for functions by integrating Implicit Neural Representations (INRs) and Transformer-based hypernetworks into latent variable models. Unlike prior approaches that rely on MLP-based hypernetworks with scalability limitations, our method employs a Transformer-based decoder to generate INR parameters from latent variables, addressing both representation capacity and computational efficiency. Our framework extends latent diffusion models (LDMs) to INR generation by replacing standard decoders with a Transformer-based hypernetwork, which can be trained either from scratch or via hyper-transforming—a strategy that fine-tunes only the decoder while freezing the pre-trained latent space. This enables efficient adaptation of existing generative models to INR-based representations without requiring full retraining. We validate our approach across multiple modalities, demonstrating improved scalability, expressiveness, and generalization over existing INR-based generative models. Our findings establish a unified and flexible framework for learning structured function representations.

## Metadata
- venue: ICML
- year: 2025
- authors: Ignacio Peis, Batuhan Koyuncu, Isabel Valera, Jes Frellsen
- arxiv_id: 
- openreview_id: yhgcRwJ9Dn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/345e9cdf732bb81ae28716d900d2fa1d9bcaa2d7.pdf
- published: 2025
- keywords: Latent Diffusion Models, Transformers, INRs
