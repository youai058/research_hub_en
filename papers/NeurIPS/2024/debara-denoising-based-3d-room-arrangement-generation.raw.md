---
title: "DeBaRA: Denoising-Based 3D Room Arrangement Generation"
authors: ["Léopold Maillard", "Nicolas Sereyjol-Garros", "Tom Durand", "Maks Ovsjanikov"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rajRJ6WKj2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8e9f6d8fd7649487d5a585513a50e2992ffc16e7.pdf"
published: "2024"
categories: []
keywords: ["Indoor 3D Scene Synthesis", "Layout Generation", "Score-based Generative Models", "Diffusion Models", "Conditional Generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:04+09:00"
---

# DeBaRA: Denoising-Based 3D Room Arrangement Generation

## Abstract
Generating realistic and diverse layouts of furnished indoor 3D scenes unlocks multiple interactive applications impacting a wide range of industries. The inherent complexity of object interactions, the limited amount of available data and the requirement to fulfill spatial constraints all make generative modeling for 3D scene synthesis and arrangement challenging. Current methods address these challenges autoregressively or by using off-the-shelf diffusion objectives by simultaneously predicting all attributes without 3D reasoning considerations. In this paper, we introduce DeBaRA, a score-based model specifically tailored for precise, controllable and flexible arrangement generation in a bounded environment. We argue that the most critical component of a scene synthesis system is to accurately establish the size and position of various objects within a restricted area. Based on this insight, we propose a lightweight conditional score-based model designed with 3D spatial awareness at its core. We demonstrate that by focusing on spatial attributes of objects, a single trained DeBaRA model can be leveraged at test time to perform several downstream applications such as scene synthesis, completion and re-arrangement. Further, we introduce a novel Self Score Evaluation procedure so it can be optimally employed alongside external LLM models. We evaluate our approach through extensive experiments and demonstrate significant improvement upon state-of-the-art approaches in a range of scenarios.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Léopold Maillard, Nicolas Sereyjol-Garros, Tom Durand, Maks Ovsjanikov
- arxiv_id: 
- openreview_id: rajRJ6WKj2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8e9f6d8fd7649487d5a585513a50e2992ffc16e7.pdf
- published: 2024
- keywords: Indoor 3D Scene Synthesis, Layout Generation, Score-based Generative Models, Diffusion Models, Conditional Generation
