---
title: "RDPM: Solve Diffusion Probabilistic Models via Recurrent Token Prediction"
authors: ["Xiaoping Wu", "Jie Hu", "Xiaoming Wei"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2412.18390"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2412.18390v2"
published: "2024-12-24"
categories: ["cs.CV", "cs.AI", "cs.LG", "cs.MM"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:09+09:00"
---

# RDPM: Solve Diffusion Probabilistic Models via Recurrent Token Prediction

## Abstract
Diffusion Probabilistic Models (DPMs) have emerged as the de facto approach for high-fidelity image synthesis, operating diffusion processes on continuous VAE latent, which significantly differ from the text generation methods employed by Large Language Models (LLMs). In this paper, we introduce a novel generative framework, the Recurrent Diffusion Probabilistic Model (RDPM), which enhances the diffusion process through a recurrent token prediction mechanism, thereby pioneering the field of Discrete Diffusion. By progressively introducing Gaussian noise into the latent representations of images and encoding them into vector-quantized tokens in a recurrent manner, RDPM facilitates a unique diffusion process on discrete-value domains. This process iteratively predicts the token codes for subsequent timesteps, transforming the initial standard Gaussian noise into the source data distribution, aligning with GPT-style models in terms of the loss function. RDPM demonstrates superior performance while benefiting from the speed advantage of requiring only a few inference steps. This model not only leverages the diffusion process to ensure high-quality generation but also converts continuous signals into a series of high-fidelity discrete tokens, thereby maintaining a unified optimization strategy with other discrete tokens, such as text. We anticipate that this work will contribute to the development of a unified model for multimodal generation, specifically by integrating continuous signal domains such as images, videos, and audio with text. We will release the code and model weights to the open-source community.

## Metadata
- venue: arXiv
- year: 2024
- authors: Xiaoping Wu, Jie Hu, Xiaoming Wei
- arxiv_id: 2412.18390
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2412.18390v2
- published: 2024-12-24
