---
title: "DiffuGR: Generative Document Retrieval with Diffusion Language Models"
authors: ["Xinpeng Zhao", "Zhaochun Ren", "Yukun Zhao", "Zhenyang Li", "Mengqi Zhang", "Jun Feng", "Ran Chen", "Ying Zhou", "Zhumin Chen", "Shuaiqiang Wang", "Dawei Yin", "Xin Xin"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.08150"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.08150v6"
published: "2025-11-11"
categories: ["cs.IR"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# DiffuGR: Generative Document Retrieval with Diffusion Language Models

## Abstract
Generative retrieval (GR) reframes document retrieval as an end-to-end task of generating sequential document identifiers (DocIDs). Existing GR methods predominantly rely on left-to-right auto-regressive decoding, which suffers from two fundamental limitations: (i) a \emph{mismatch between DocID generation and natural language generation}, whereby an incorrect DocID token generated at an early step can lead to entirely erroneous retrieval; and (ii) an \emph{inability to dynamically balance the trade-off between retrieval efficiency and accuracy}, which is crucial for practical applications. To tackle these challenges, we propose generative document retrieval with diffusion language models, termed \emph{DiffuGR}. DiffuGR formulates DocID generation as a discrete diffusion process. During training, DocIDs are corrupted through a stochastic masking process, and a diffusion language model is trained to recover them under a retrieval-aware objective. For inference, DiffuGR generates DocID tokens in parallel and refines them through a controllable number of denoising steps. Unlike auto-regressive decoding, DiffuGR introduce \emph{a novel mechanism to first generate plenty of confident DocID tokens and then refine the generation through diffusion-based denoising}. Moreover, DiffuGR also offers \emph{explicit runtime control over the quality-latency tradeoff}. Extensive experiments on widely-applied retrieval benchmarks show that DiffuGR outperforms strong auto-regressive generative retrievers. Additionally, we verify that DiffuGR achieves flexible control over the quality-latency trade-off via variable denoising budgets.

## Metadata
- venue: arXiv
- year: 2025
- authors: Xinpeng Zhao, Zhaochun Ren, Yukun Zhao, Zhenyang Li, Mengqi Zhang, Jun Feng, Ran Chen, Ying Zhou, Zhumin Chen, Shuaiqiang Wang, Dawei Yin, Xin Xin
- arxiv_id: 2511.08150
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.08150v6
- published: 2025-11-11
