---
title: "Diffusion on language model encodings for protein sequence generation"
authors: ["Viacheslav Meshchaninov", "Pavel Strashnov", "Andrey Shevtsov", "Fedor Nikolaev", "Nikita Ivanisenko", "Olga Kardymon", "Dmitry Vetrov"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2403.03726"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2403.03726v4"
published: "2024-03-06"
categories: ["cs.LG", "cs.AI", "q-bio.BM"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:17+09:00"
---

# Diffusion on language model encodings for protein sequence generation

## Abstract
Protein sequence design has seen significant advances through discrete diffusion and autoregressive approaches, yet the potential of continuous diffusion remains underexplored. Here, we present DiMA, a latent diffusion framework that operates on protein language model representations. Through systematic exploration of architectural choices and diffusion components, we develop a robust methodology that generalizes across multiple protein encoders ranging from 8M to 3B parameters. We demonstrate that our framework achieves consistently high performance across sequence-only (ESM-2, ESMc), dual-decodable (CHEAP), and multimodal (SaProt) representations using the same architecture and training approach. We extensively evaluate existing methods alongside DiMA using multiple metrics across two protein modalities, covering quality, diversity, novelty, and distribution matching of generated proteins. DiMA consistently produces novel, high-quality and diverse protein sequences and achieves strong results compared to baselines such as autoregressive, discrete diffusion and flow matching language models. The model demonstrates versatile functionality, supporting conditional generation tasks including protein family-generation, motif scaffolding and infilling, and fold-specific sequence design. This work provides a universal continuous diffusion framework for protein sequence generation, offering both architectural insights and practical applicability across various protein design scenarios. Code is released at \href{https://github.com/MeshchaninovViacheslav/DiMA}{GitHub}.

## Metadata
- venue: arXiv
- year: 2024
- authors: Viacheslav Meshchaninov, Pavel Strashnov, Andrey Shevtsov, Fedor Nikolaev, Nikita Ivanisenko, Olga Kardymon, Dmitry Vetrov
- arxiv_id: 2403.03726
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2403.03726v4
- published: 2024-03-06
