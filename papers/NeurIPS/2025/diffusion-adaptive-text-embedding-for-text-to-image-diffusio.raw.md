---
title: "Diffusion Adaptive Text Embedding for Text-to-Image Diffusion Models"
authors: ["Byeonghu Na", "Minsang Park", "Gyuwon Sim", "Donghyeok Shin", "HeeSun Bae", "Mina Kang", "Se Jung Kwon", "Wanmo Kang", "Il-chul Moon"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cHi8QxGrZH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e1ae17dc245ce2c942c3df6b2e453cf997208812.pdf"
published: "2025"
categories: []
keywords: ["Diffusion models", "text-to-image diffusion models", "text-to-image generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:39+09:00"
---

# Diffusion Adaptive Text Embedding for Text-to-Image Diffusion Models

## Abstract
Text-to-image diffusion models rely on text embeddings from a pre-trained text encoder, but these embeddings remain fixed across all diffusion timesteps, limiting their adaptability to the generative process. We propose Diffusion Adaptive Text Embedding (DATE), which dynamically updates text embeddings at each diffusion timestep based on intermediate perturbed data. We formulate an optimization problem and derive an update rule that refines the text embeddings at each sampling step to improve alignment and preference between the mean predicted image and the text. This allows DATE to dynamically adapts the text conditions to the reverse-diffused images throughout diffusion sampling without requiring additional model training. Through theoretical analysis and empirical results, we show that DATE maintains the generative capability of the model while providing superior text-image alignment over fixed text embeddings across various tasks, including multi-concept generation and text-guided image editing. Our code is available at https://github.com/aailab-kaist/DATE.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Byeonghu Na, Minsang Park, Gyuwon Sim, Donghyeok Shin, HeeSun Bae, Mina Kang, Se Jung Kwon, Wanmo Kang, Il-chul Moon
- arxiv_id: 
- openreview_id: cHi8QxGrZH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e1ae17dc245ce2c942c3df6b2e453cf997208812.pdf
- published: 2025
- keywords: Diffusion models, text-to-image diffusion models, text-to-image generation
