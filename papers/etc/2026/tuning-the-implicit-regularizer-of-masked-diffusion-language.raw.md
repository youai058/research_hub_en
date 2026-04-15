---
title: "Tuning the Implicit Regularizer of Masked Diffusion Language Models: Enhancing Generalization via Insights from $k$-Parity"
authors: ["Jianhao Huang", "Baharan Mirzasoleiman"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.22450"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.22450v1"
published: "2026-01-30"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Tuning the Implicit Regularizer of Masked Diffusion Language Models: Enhancing Generalization via Insights from $k$-Parity

## Abstract
Masked Diffusion Language Models have recently emerged as a powerful generative paradigm, yet their generalization properties remain understudied compared to their auto-regressive counterparts. In this work, we investigate these properties within the setting of the $k$-parity problem (computing the XOR sum of $k$ relevant bits), where neural networks typically exhibit grokking -- a prolonged plateau of chance-level performance followed by sudden generalization. We theoretically decompose the Masked Diffusion (MD) objective into a Signal regime which drives feature learning, and a Noise regime which serves as an implicit regularizer. By training nanoGPT using MD objective on the $k$-parity problem, we demonstrate that MD objective fundamentally alters the learning landscape, enabling rapid and simultaneous generalization without experiencing grokking. Furthermore, we leverage our theoretical insights to optimize the distribution of the mask probability in the MD objective. Our method significantly improves perplexity for 50M-parameter models and achieves superior results across both pre-training from scratch and supervised fine-tuning. Specifically, we observe performance gains peaking at $8.8\%$ and $5.8\%$, respectively, on 8B-parameter models, confirming the scalability and effectiveness of our framework in large-scale masked diffusion language model regimes.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jianhao Huang, Baharan Mirzasoleiman
- arxiv_id: 2601.22450
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.22450v1
- published: 2026-01-30
