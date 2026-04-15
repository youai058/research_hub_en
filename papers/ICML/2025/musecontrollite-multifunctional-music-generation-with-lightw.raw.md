---
title: "MuseControlLite: Multifunctional Music Generation with Lightweight Conditioners"
authors: ["Fang-Duo Tsai", "Shih-Lun Wu", "Weijaw Lee", "Sheng-Ping Yang", "Bo-Rui Chen", "Hao-Chung Cheng", "Yi-Hsuan Yang"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "VK47MdCjBH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0ad53a87c17824d24f1ff89408573a107dc4d928.pdf"
published: "2025"
categories: []
keywords: ["Sound", "Artificial Intelligence", "Machine Learning", "Audio and Speech Processing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:38+09:00"
---

# MuseControlLite: Multifunctional Music Generation with Lightweight Conditioners

## Abstract
We propose MuseControlLite, a lightweight mechanism designed to fine-tune text-to-music generation models for precise conditioning using various time-varying musical attributes and reference audio signals. The key finding is that positional embeddings, which have been seldom used by text-to-music generation models in the conditioner for text conditions, are critical when the condition of interest is a function of time. Using melody control as an example, our experiments show that simply adding rotary positional embeddings to the decoupled cross-attention layers increases control accuracy from 56.6% to 61.1%, while requiring 6.75 times fewer trainable parameters than state-of-the-art fine-tuning mechanisms, using the same pre-trained diffusion Transformer model of Stable Audio Open. We evaluate various forms of musical attribute control, audio inpainting, and audio outpainting, demonstrating improved controllability over MusicGen-Large and Stable Audio Open ControlNet at a significantly lower fine-tuning cost, with only 85M trainable parameters. Source code, model checkpoints, and demo examples are available at: https://MuseControlLite.github.io/web/

## Metadata
- venue: ICML
- year: 2025
- authors: Fang-Duo Tsai, Shih-Lun Wu, Weijaw Lee, Sheng-Ping Yang, Bo-Rui Chen, Hao-Chung Cheng, Yi-Hsuan Yang
- arxiv_id: 
- openreview_id: VK47MdCjBH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0ad53a87c17824d24f1ff89408573a107dc4d928.pdf
- published: 2025
- keywords: Sound, Artificial Intelligence, Machine Learning, Audio and Speech Processing
