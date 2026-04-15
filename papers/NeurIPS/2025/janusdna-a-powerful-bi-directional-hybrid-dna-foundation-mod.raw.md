---
title: "JanusDNA: A Powerful Bi-directional Hybrid DNA Foundation Model"
authors: ["Qihao Duan", "Bingding Huang", "Zhenqiao Song", "Irina Lehmann", "Lei Gu", "Roland Eils", "Benjamin Wild"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9PL1DIIB7e"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e0890fe573f380ab7dfa6c28d2d868aa21121b43.pdf"
published: "2025"
categories: []
keywords: ["genomics", "foundation model", "hybrid architecture", "learning efficiency"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:29+09:00"
---

# JanusDNA: A Powerful Bi-directional Hybrid DNA Foundation Model

## Abstract
Large language models (LLMs) have revolutionized natural language processing and are increasingly applied to other sequential data types, including genetic sequences. However, adapting LLMs to genetics presents significant challenges. Capturing complex genomic interactions requires modeling long-range global dependencies within DNA sequences, where interactions often span over 10,000 base pairs, even within a single gene. This poses substantial computational demands under conventional model architectures and training paradigms. Additionally, traditional LLM training approaches are suboptimal for DNA sequences: autoregressive training, while efficient for training, only supports unidirectional sequence understanding. However, DNA is inherently bidirectional. For instance, bidirectional promoters regulate gene expression in both directions and govern approximately 11% of human gene expression. Masked language models (MLMs) enable bidirectional understanding. However, they are inefficient since only masked tokens contribute to loss calculations at each training step. To address these limitations, we introduce JanusDNA, the first bidirectional DNA foundation model built upon a novel pretraining paradigm, integrating the optimization efficiency of autoregressive modeling with the bidirectional comprehension capability of masked modeling. JanusDNA's architecture leverages a Mamba-Attention Mixture-of-Experts (MoE) design, combining the global, high-resolution context awareness of attention mechanisms with the efficient sequential representation learning capabilities of Mamba. The MoE layers further enhance the model's capacity through sparse parameter scaling, while maintaining manageable computational costs. Notably, JanusDNA can process up to 1 million base pairs at single-nucleotide resolution on a single 80GB GPU using its hybrid architecture. Extensive experiments and ablation studies demonstrate that JanusDNA achieves new state-of-the-art performance on three genomic representation benchmarks. Remarkably, JanusDNA surpasses models with 250x more activated parameters, underscoring its efficiency and effectiveness. Code available at https://anonymous.4open.science/r/JanusDNA/.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Qihao Duan, Bingding Huang, Zhenqiao Song, Irina Lehmann, Lei Gu, Roland Eils, Benjamin Wild
- arxiv_id: 
- openreview_id: 9PL1DIIB7e
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e0890fe573f380ab7dfa6c28d2d868aa21121b43.pdf
- published: 2025
- keywords: genomics, foundation model, hybrid architecture, learning efficiency
