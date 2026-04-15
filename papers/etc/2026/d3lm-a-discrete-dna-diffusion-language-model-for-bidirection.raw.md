---
title: "D3LM: A Discrete DNA Diffusion Language Model for Bidirectional DNA Understanding and Generation"
authors: ["Zhao Yang", "Hengchang Liu", "Chuan Cao", "Bing Su"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.01780"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.01780v1"
published: "2026-03-02"
categories: ["cs.LG", "q-bio.GN"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# D3LM: A Discrete DNA Diffusion Language Model for Bidirectional DNA Understanding and Generation

## Abstract
Early DNA foundation models adopted BERT-style training, achieving good performance on DNA understanding tasks but lacking generative capabilities. Recent autoregressive models enable DNA generation, but employ left-to-right causal modeling that is suboptimal for DNA where regulatory relationships are inherently bidirectional. We present D3LM (\textbf{D}iscrete \textbf{D}NA \textbf{D}iffusion \textbf{L}anguage \textbf{M}odel), which unifies bidirectional representation learning and DNA generation through masked diffusion. D3LM directly adopts the Nucleotide Transformer (NT) v2 architecture but reformulates the training objective as masked diffusion in discrete DNA space, enabling both bidirectional understanding and generation capabilities within a single model. Compared to NT v2 of the same size, D3LM achieves improved performance on understanding tasks. Notably, on regulatory element generation, D3LM achieves an SFID of 10.92, closely approaching real DNA sequences (7.85) and substantially outperforming the previous best result of 29.16 from autoregressive models. Our work suggests diffusion language models as a promising paradigm for unified DNA foundation models. We further present the first systematic study of masked diffusion models in the DNA domain, investigating practical design choices such as tokenization schemes and sampling strategies, thereby providing empirical insights and a solid foundation for future research. D3LM has been released at https://huggingface.co/collections/Hengchang-Liu/d3lm.

## Metadata
- venue: arXiv
- year: 2026
- authors: Zhao Yang, Hengchang Liu, Chuan Cao, Bing Su
- arxiv_id: 2603.01780
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.01780v1
- published: 2026-03-02
