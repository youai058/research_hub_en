---
title: "On improved Conditioning Mechanisms and Pre-training Strategies for Diffusion Models"
authors: ["Tariq Berrada", "Pietro Astolfi", "Melissa Hall", "Reyhane Askari Hemmat", "Yohann Benchetrit", "Marton Havasi", "Matthew J. Muckley", "Karteek Alahari", "Adriana Romero-Soriano", "Jakob Verbeek", "Michal Drozdzal"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "B3rZZRALhk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7b83d29ed3b6ed29761de9aef2359c65fdb177c5.pdf"
published: "2024"
categories: []
keywords: ["Generative Models", "Generative Modeling", "Diffusion", "Latent diffusion", "Computer vision", "text-to-image diffusion"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:47+09:00"
---

# On improved Conditioning Mechanisms and Pre-training Strategies for Diffusion Models

## Abstract
Large-scale training of latent diffusion models (LDMs) has enabled unprecedented quality in image generation. 
However, large-scale end-to-end training of these models is computationally costly, and hence most research  focuses either on finetuning  pretrained models or experiments at smaller scales.
In this work we aim to improve the training efficiency and performance of LDMs with the goal of scaling to larger datasets and higher resolutions.
We focus our study on two points that are critical for good performance and efficient training: 
(i) the mechanisms used for  semantic level (\eg a text prompt, or class name) and low-level (crop size, random flip, \etc) conditioning of the model, and 
(ii) pre-training strategies to transfer representations learned on smaller and lower-resolution datasets to larger ones.
The main contributions of our work are the following: 
we present systematic experimental study of these points, 
we propose a novel conditioning mechanism that disentangles semantic and low-level conditioning, 
we obtain state-of-the-art performance  on CC12M for text-to-image at 512 resolution.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Tariq Berrada, Pietro Astolfi, Melissa Hall, Reyhane Askari Hemmat, Yohann Benchetrit, Marton Havasi, Matthew J. Muckley, Karteek Alahari, Adriana Romero-Soriano, Jakob Verbeek, Michal Drozdzal
- arxiv_id: 
- openreview_id: B3rZZRALhk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7b83d29ed3b6ed29761de9aef2359c65fdb177c5.pdf
- published: 2024
- keywords: Generative Models, Generative Modeling, Diffusion, Latent diffusion, Computer vision, text-to-image diffusion
