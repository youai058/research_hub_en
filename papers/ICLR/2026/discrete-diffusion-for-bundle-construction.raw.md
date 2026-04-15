---
title: "Discrete Diffusion for Bundle Construction"
authors: ["Teng Tu", "Ai Li", "Yunshan Ma", "Shuo Xu", "Xiaohao Liu", "Haokai Ma", "Liang Pang", "Tat-Seng Chua"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dKyhgfe50H"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0c37e2208a1b33dcbf3cb858ea49bc67b8c2fd2a.pdf"
published: "2026"
categories: []
keywords: ["Bundle Construction", "Bundle Completion", "Recommendation System", "Discrete Diffusion Model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:39+09:00"
---

# Discrete Diffusion for Bundle Construction

## Abstract
As a central task in product bundling, bundle construction aims to select a subset of items from large item catalogs to build an entire bundle or, more practically, complete a partial bundle. Existing methods often rely on the sequential construction paradigm that predicts items one at a time, nevertheless, this paradigm is fundamentally unsuitable for the essentially unordered bundles. In contrast, non-sequential methods model a bundle as a set, but still face two dimensionality curses: the combinatorial space grows exponentially with both bundle length and catalog size. Accordingly, we identify two technical challenges: 1) how to effectively and efficiently model the higher-order intra-bundle relations with the growth of bundle length; and 2) how to learn item representations that remain discriminative while avoiding search directly over a huge item catalog.

To address these challenges, we propose DDBC, a Discrete Diffusion model for Bundle Construction. DDBC leverages a masked denoising diffusion process to build bundles non-sequentially, capturing joint dependencies among items without relying on a fixed decoding order, thereby partially alleviating the combinatorial challenge introduced by increasing bundle length. To mitigate the curse of large catalog size, we integrate residual vector quantization (RVQ), which compresses item embeddings into discrete codes drawn from a globally shared codebook, enabling more efficient search while retaining semantic granularity.  We evaluate our method on real-world bundle construction datasets of music playlist continuation and fashion outfit completion, and the experimental results show that DDBC can achieve more than 100\% relative performance improvements compared with state-of-the-art baseline methods. Ablation and model analyses further confirm the effectiveness of both the diffusion backbone and the RVQ tokenizer, with gains becoming more pronounced for longer bundles and larger catalogs. Our code is available at https://github.com/241416/DDBC.

## Metadata
- venue: ICLR
- year: 2026
- authors: Teng Tu, Ai Li, Yunshan Ma, Shuo Xu, Xiaohao Liu, Haokai Ma, Liang Pang, Tat-Seng Chua
- arxiv_id: 
- openreview_id: dKyhgfe50H
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0c37e2208a1b33dcbf3cb858ea49bc67b8c2fd2a.pdf
- published: 2026
- keywords: Bundle Construction, Bundle Completion, Recommendation System, Discrete Diffusion Model
