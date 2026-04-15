---
title: "Beyond Next-Token Prediction: A Performance Characterization of Diffusion versus Autoregressive Language Models"
authors: ["Minseo Kim", "Coleman Hooper", "Aditya Tomar", "Chenfeng Xu", "Mehrdad Farajtabar", "Michael W. Mahoney", "Kurt Keutzer", "Amir Gholami"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.04146"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.04146v2"
published: "2025-10-05"
categories: ["cs.LG", "cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# Beyond Next-Token Prediction: A Performance Characterization of Diffusion versus Autoregressive Language Models

## Abstract
Large Language Models (LLMs) have achieved state-of-the-art performance on a broad range of Natural Language Processing (NLP) tasks, including document processing and code generation. Autoregressive Language Models (ARMs), which generate tokens sequentially conditioned on all previous tokens, have been the predominant paradigm for LLMs. While these models have achieved high accuracy across a range of downstream tasks, they exhibit low arithmetic intensity due to the inherent sequential dependency in next-token prediction. Recently, Diffusion Language Models (DLMs) have emerged as a promising alternative architecture. DLMs generate output tokens in parallel, mitigating the limitations of sequential decoding. However, the performance implications of DLMs relative to commonly deployed ARMs are not fully understood. In this work, we present a comprehensive study of the performance characteristics of ARMs and DLMs, combining theoretical analysis with empirical profiling to characterize the trade-offs between these approaches. We show that although DLMs can achieve higher arithmetic intensity than ARMs by leveraging parallelism across token positions, they fail to scale effectively with longer contexts. We then explore block-wise decoding for DLMs, which decouples arithmetic intensity from sequence length and enables better scaling to long contexts (similar to ARMs). We also examine batched inference and find that ARMs exhibit superior throughput as they benefit more from parallelism across sequences in the batch. Finally, we highlight opportunities for accelerating DLM inference, emphasizing that reducing the number of sampling steps is key for open-source DLMs to achieve lower latency relative to ARMs.

## Metadata
- venue: arXiv
- year: 2025
- authors: Minseo Kim, Coleman Hooper, Aditya Tomar, Chenfeng Xu, Mehrdad Farajtabar, Michael W. Mahoney, Kurt Keutzer, Amir Gholami
- arxiv_id: 2510.04146
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.04146v2
- published: 2025-10-05
