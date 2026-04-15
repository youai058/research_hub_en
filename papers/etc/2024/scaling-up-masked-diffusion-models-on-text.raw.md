---
title: "Scaling up Masked Diffusion Models on Text"
authors: ["Shen Nie", "Fengqi Zhu", "Chao Du", "Tianyu Pang", "Qian Liu", "Guangtao Zeng", "Min Lin", "Chongxuan Li"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2410.18514"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2410.18514v3"
published: "2024-10-24"
categories: ["cs.AI", "cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:05+09:00"
---

# Scaling up Masked Diffusion Models on Text

## Abstract
Masked diffusion models (MDMs) have shown promise in language modeling, yet their scalability and effectiveness in core language tasks, such as text generation and language understanding, remain underexplored. This paper establishes the first scaling law for MDMs, demonstrating a scaling rate comparable to autoregressive models (ARMs) and a relatively small compute gap. Motivated by their scalability, we train a family of MDMs with up to 1.1 billion (B) parameters to systematically evaluate their performance against ARMs of comparable or larger sizes. Fully leveraging the probabilistic formulation of MDMs, we propose a simple yet effective unsupervised classifier-free guidance that effectively exploits large-scale unpaired data, boosting performance for conditional inference. In language understanding, the 1.1B MDM outperforms the 1.1B TinyLlama model trained on the same data across four of eight zero-shot benchmarks. Notably, it achieves competitive math reasoning ability with the 7B Llama-2 model on the GSM8K dataset. In text generation, MDMs with 16 times more pre-training time offer a flexible trade-off against ARMs with the accelerated sampling technique KV-Cache: MDMs match ARMs in performance while being 1.4 times faster during sampling. Moreover, MDMs address challenging tasks for ARMs by effectively handling bidirectional reasoning and adapting to temporal shifts in data. Notably, a 1.1B MDM breaks the reverse curse encountered by much larger ARMs with significantly more data and computation, such as 13B Llama-2 and 175B GPT-3. Our code is available at https://github.com/ML-GSAI/SMDM.

## Metadata
- venue: arXiv
- year: 2024
- authors: Shen Nie, Fengqi Zhu, Chao Du, Tianyu Pang, Qian Liu, Guangtao Zeng, Min Lin, Chongxuan Li
- arxiv_id: 2410.18514
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2410.18514v3
- published: 2024-10-24
