---
title: "Raptor: Scalable Train-Free Embeddings for 3D Medical Volumes Leveraging Pretrained 2D Foundation Models"
authors: ["Ulzee An", "Moonseong Jeong", "Simon Austin Lee", "Aditya Gorla", "Yuzhe Yang", "Sriram Sankararaman"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "4yHWV3B6g4"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/62c6e057794303a9a335c06eb9824ece833318f3.pdf"
published: "2025"
categories: []
keywords: ["Embedding", "Volumes", "Foundation model", "Random projection", "Compression", "MRI", "CT"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:38+09:00"
---

# Raptor: Scalable Train-Free Embeddings for 3D Medical Volumes Leveraging Pretrained 2D Foundation Models

## Abstract
Current challenges in developing foundational models for volumetric imaging data, such as magnetic resonance imaging (MRI), stem from the computational complexity of state-of-the-art architectures in high dimensions and curating sufficiently large datasets of volumes.
To address these challenges, we introduce Raptor (Random Planar Tensor Reduction), a train-free method for generating semantically rich embeddings for volumetric data. Raptor leverages a frozen 2D foundation model, pretrained on natural images, to extract visual tokens from individual cross-sections of medical volumes. These tokens are then spatially compressed using random projections, significantly reducing computational complexity while retaining rich semantic information. Extensive experiments on 10 diverse medical volume tasks verify the superior performance of Raptor over state-of-the-art methods, including those pretrained exclusively on medical volumes (+3% SuPreM, +6% MISFM, +10% Merlin, +13% VoCo, and +14% SLIViT), while entirely bypassing the need for costly training. Our results highlight Raptor's effectiveness and versatility as a foundation for advancing deep learning-based methods for medical volumes (code: github.com/sriramlab/raptor).

## Metadata
- venue: ICML
- year: 2025
- authors: Ulzee An, Moonseong Jeong, Simon Austin Lee, Aditya Gorla, Yuzhe Yang, Sriram Sankararaman
- arxiv_id: 
- openreview_id: 4yHWV3B6g4
- anthology_id: 
- pdf_url: https://openreview.net/pdf/62c6e057794303a9a335c06eb9824ece833318f3.pdf
- published: 2025
- keywords: Embedding, Volumes, Foundation model, Random projection, Compression, MRI, CT
