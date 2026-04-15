---
title: "The Design Space of Tri-Modal Masked Diffusion Models"
authors: ["Louis Bethune", "Victor Turrisi", "Bruno Kacper Mlodozeniec", "Pau Rodriguez Lopez", "Lokesh Boominathan", "Nikhil Bhendawade", "Amitis Shidani", "Joris Pelemans", "Theo X. Olausson", "Devon Hjelm", "Paul Dixon", "Joao Monteiro", "Pierre Ablin", "Vishnu Banna", "Arno Blaas", "Nick Henderson", "Kari Noriy", "Dan Busbridge", "Josh Susskind", "Marco Cuturi", "Irina Belousova", "Luca Zappella", "Russ Webb", "Jason Ramapuram"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.21472"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.21472v1"
published: "2026-02-25"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# The Design Space of Tri-Modal Masked Diffusion Models

## Abstract
Discrete diffusion models have emerged as strong alternatives to autoregressive language models, with recent work initializing and fine-tuning a base unimodal model for bimodal generation. Diverging from previous approaches, we introduce the first tri-modal masked diffusion model pretrained from scratch on text, image-text, and audio-text data. We systematically analyze multimodal scaling laws, modality mixing ratios, noise schedules, and batch-size effects, and we provide optimized inference sampling defaults. Our batch-size analysis yields a novel stochastic differential equation (SDE)-based reparameterization that eliminates the need for tuning the optimal batch size as reported in recent work. This reparameterization decouples the physical batch size, often chosen based on compute constraints (GPU saturation, FLOP efficiency, wall-clock time), from the logical batch size, chosen to balance gradient variance during stochastic optimization. Finally, we pretrain a preliminary 3B-parameter tri-modal model on 6.4T tokens, demonstrating the capabilities of a unified design and achieving strong results in text generation, text-to-image tasks, and text-to-speech tasks. Our work represents the largest-scale systematic open study of multimodal discrete diffusion models conducted to date, providing insights into scaling behaviors across multiple modalities.

## Metadata
- venue: arXiv
- year: 2026
- authors: Louis Bethune, Victor Turrisi, Bruno Kacper Mlodozeniec, Pau Rodriguez Lopez, Lokesh Boominathan, Nikhil Bhendawade, Amitis Shidani, Joris Pelemans, Theo X. Olausson, Devon Hjelm, Paul Dixon, Joao Monteiro, Pierre Ablin, Vishnu Banna, Arno Blaas, Nick Henderson, Kari Noriy, Dan Busbridge, Josh Susskind, Marco Cuturi, Irina Belousova, Luca Zappella, Russ Webb, Jason Ramapuram
- arxiv_id: 2602.21472
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.21472v1
- published: 2026-02-25
