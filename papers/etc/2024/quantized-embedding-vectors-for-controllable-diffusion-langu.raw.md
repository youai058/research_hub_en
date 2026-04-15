---
title: "Quantized Embedding Vectors for Controllable Diffusion Language Models"
authors: ["Cheng Kang", "Xinye Chen", "Yong Hu", "Daniel Novak"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2402.10107"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2402.10107v1"
published: "2024-02-15"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:02+09:00"
---

# Quantized Embedding Vectors for Controllable Diffusion Language Models

## Abstract
Improving the controllability, portability, and inference speed of diffusion language models (DLMs) is a key challenge in natural language generation. While recent research has shown significant success in complex text generation with language models, the memory and computational power are still very demanding and fall short of expectations, which naturally results in low portability and instability for the models. To mitigate these issues, numerous well-established methods were proposed for neural network quantization. To further enhance their portability of independent deployment as well as improve their stability evaluated by language perplexity, we propose a novel approach called the Quantized Embedding Controllable Diffusion Language Model (QE-CDLM). QE-CDLM builds upon the recent successful controllable DLMs by remodeling the task-specific embedding space via quantization. This leads to a gradient-based controller for the generation tasks, and more stable intermediate latent variables are obtained, which naturally brings in an accelerated convergence as well as better controllability. Additionally, the adaption fine-tuning method is employed to reduce tunable weights. Experimental results on five challenging fine-grained control tasks demonstrate that QE-CDLM compares favorably to existing methods in terms of quality and feasibility, achieving better perplexity and lightweight fine-tuning.

## Metadata
- venue: arXiv
- year: 2024
- authors: Cheng Kang, Xinye Chen, Yong Hu, Daniel Novak
- arxiv_id: 2402.10107
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2402.10107v1
- published: 2024-02-15
