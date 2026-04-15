---
title: "Flow Map Language Models: One-step Language Modeling via Continuous Denoising"
authors: ["Chanhyuk Lee", "Jaehoon Yoo", "Manan Agarwal", "Sheel Shah", "Jerry Huang", "Aditi Raghunathan", "Seunghoon Hong", "Nicholas M. Boffi", "Jinwoo Kim"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.16813"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.16813v2"
published: "2026-02-18"
categories: ["cs.CL", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Flow Map Language Models: One-step Language Modeling via Continuous Denoising

## Abstract
Language models based on discrete diffusion have attracted widespread interest for their potential to provide faster generation than autoregressive models. Despite their promise, these models typically produce samples whose quality sharply degrades in the few-step regime, preventing a dramatic speedup in practice. Here, we show that language models based on continuous flows over one-hot token embeddings can outperform discrete diffusion in both quality and speed. Importantly, our continuous formulation defines a unique flow map that can be learned directly for efficient few-step inference, a structure we show is unavailable to discrete methods. In this setting, we show that both the flow and its associated flow map can be learned with simple cross-entropy objectives that respect the simplex geometry of the data, and we identify three distinct choices for flow map distillation whose performance we compare in practice. Using these insights, we build a flow language model (FLM), a continuous flow that matches state-of-the-art discrete diffusion baselines on the One Billion Words (LM1B) and OpenWebText (OWT) datasets. We then distill FLM into a flow map language model (FMLM), whose one-step generation exceeds the 8-step quality of recent few-step discrete diffusion language models. Our work challenges the widely-held hypothesis that discrete noising processes are necessary for generative modeling over discrete modalities and paves the way toward accelerated language modeling at scale. Code is available at https://github.com/david3684/flm.

## Metadata
- venue: arXiv
- year: 2026
- authors: Chanhyuk Lee, Jaehoon Yoo, Manan Agarwal, Sheel Shah, Jerry Huang, Aditi Raghunathan, Seunghoon Hong, Nicholas M. Boffi, Jinwoo Kim
- arxiv_id: 2602.16813
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.16813v2
- published: 2026-02-18
