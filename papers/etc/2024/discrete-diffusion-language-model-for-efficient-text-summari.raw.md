---
title: "Discrete Diffusion Language Model for Efficient Text Summarization"
authors: ["Do Huu Dat", "Do Duc Anh", "Anh Tuan Luu", "Wray Buntine"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2407.10998"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2407.10998v2"
published: "2024-06-25"
categories: ["cs.CL", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:12+09:00"
---

# Discrete Diffusion Language Model for Efficient Text Summarization

## Abstract
While diffusion models excel at conditional generating high-quality images, prior works in discrete diffusion models were not evaluated on conditional long-text generation. In this work, we address the limitations of prior discrete diffusion models for conditional long-text generation, particularly in long sequence-to-sequence tasks such as abstractive summarization. Despite fast decoding speeds compared to autoregressive methods, previous diffusion models failed on the abstractive summarization task due to the incompatibility between the backbone architectures and the random noising process. To overcome these challenges, we introduce a novel semantic-aware noising process that enables Transformer backbones to handle long sequences effectively. Additionally, we propose CrossMamba, an adaptation of the Mamba model to the encoder-decoder paradigm, which integrates seamlessly with the random absorbing noising process. Our approaches achieve state-of-the-art performance on three benchmark summarization datasets: Gigaword, CNN/DailyMail, and Arxiv, outperforming existing discrete diffusion models on ROUGE metrics as well as possessing much faster speed in inference compared to autoregressive models.

## Metadata
- venue: arXiv
- year: 2024
- authors: Do Huu Dat, Do Duc Anh, Anh Tuan Luu, Wray Buntine
- arxiv_id: 2407.10998
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2407.10998v2
- published: 2024-06-25
