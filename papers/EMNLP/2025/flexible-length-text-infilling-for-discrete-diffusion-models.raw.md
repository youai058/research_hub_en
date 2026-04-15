---
title: "Flexible-length Text Infilling for Discrete Diffusion Models"
authors: ["Andrew Zhang", "Anushka Sivakumar", "Chia-Wei Tang", "Chris Thomas"]
venue: "EMNLP"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: ""
anthology_id: "2025.emnlp-main.1597"
pdf_url: "https://aclanthology.org/2025.emnlp-main.1597.pdf"
published: "2025"
categories: []
keywords: []
venue_source: "anthology"
hunter_fetched: "2026-04-15T05:16:58+09:00"
---

# Flexible-length Text Infilling for Discrete Diffusion Models

## Abstract
Discrete diffusion models are a new class of text generators that offer advantages such as bidirectional context use, parallelizable generation, and flexible prompting compared to autoregressive models. However, a critical limitation of discrete diffusion models is their inability to perform flexible-length or flexible-position text infilling without access to ground-truth positional data. We introduce DDOT (Discrete Diffusion with Optimal Transport Position Coupling), the first discrete diffusion model to overcome this challenge. DDOT jointly denoises token values and token positions, employing a novel sample-level Optimal Transport (OT) coupling. This coupling preserves relative token ordering while dynamically adjusting the positions and length of infilled segments, a capability previously missing in text diffusion. Our method is orthogonal to existing discrete text diffusion methods and is compatible with various pretrained text denoisers. Extensive experiments on text infilling benchmarks such as One-Billion-Word and Yelp demonstrate that DDOT outperforms naive diffusion baselines. Furthermore, DDOT achieves performance on par with state-of-the-art non-autoregressive models and enables significant improvements in training efficiency and flexibility.

## Metadata
- venue: EMNLP
- year: 2025
- authors: Andrew Zhang, Anushka Sivakumar, Chia-Wei Tang, Chris Thomas
- arxiv_id: 
- openreview_id: 
- anthology_id: 2025.emnlp-main.1597
- pdf_url: https://aclanthology.org/2025.emnlp-main.1597.pdf
- published: 2025
