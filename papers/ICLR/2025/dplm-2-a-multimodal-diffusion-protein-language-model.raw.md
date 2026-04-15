---
title: "DPLM-2: A Multimodal Diffusion Protein Language Model"
authors: ["Xinyou Wang", "Zaixiang Zheng", "Fei YE", "Dongyu Xue", "Shujian Huang", "Quanquan Gu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5z9GjHgerY"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/13c6bc9b904922e7352e690eae7cad8a2d4526f7.pdf"
published: "2025"
categories: []
keywords: ["protein foundation model", "diffusion language model", "multimodal language model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:49+09:00"
---

# DPLM-2: A Multimodal Diffusion Protein Language Model

## Abstract
Proteins are essential macromolecules defined by their amino acid sequences, which determine their three-dimensional structures and, consequently, their functions in all living organisms. Therefore, generative protein modeling necessitates a multimodal approach to simultaneously model, understand, and generate both sequences and structures. However, existing methods typically use separate models for each modality, limiting their ability to capture the intricate relationships between sequence and structure. This results in suboptimal performance in tasks that requires joint understanding and generation of both modalities.
In this paper, we introduce DPLM-2, a multimodal protein foundation model that extends discrete diffusion protein language model (DPLM) to accommodate both sequences and structures.
To enable structural learning with the language model, 3D coordinates are converted to discrete tokens using a lookup-free quantization-based tokenizer.
By training on both experimental and high-quality synthetic structures, DPLM-2 learns the joint distribution of sequence and structure, as well as their marginals and conditionals.
We also implement an efficient warm-up strategy to exploit the connection between large-scale evolutionary data and structural inductive biases from pre-trained sequence-based protein language models.
Empirical evaluation shows that DPLM-2 can simultaneously generate highly compatible amino acid sequences and their corresponding 3D structures eliminating the need for a two-stage generation approach.
Moreover, DPLM-2 demonstrates competitive performance in various conditional generation tasks, including folding, inverse folding, and scaffolding with multimodal motif inputs.

## Metadata
- venue: ICLR
- year: 2025
- authors: Xinyou Wang, Zaixiang Zheng, Fei YE, Dongyu Xue, Shujian Huang, Quanquan Gu
- arxiv_id: 
- openreview_id: 5z9GjHgerY
- anthology_id: 
- pdf_url: https://openreview.net/pdf/13c6bc9b904922e7352e690eae7cad8a2d4526f7.pdf
- published: 2025
- keywords: protein foundation model, diffusion language model, multimodal language model
