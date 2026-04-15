---
title: "Coevolutionary Continuous Discrete Diffusion: Make Your Diffusion Language Model a Latent Reasoner"
authors: ["Cai Zhou", "Chenxiao Yang", "Yi Hu", "Chenyu Wang", "Chubin Zhang", "Muhan Zhang", "Lester Mackey", "Tommi Jaakkola", "Stephen Bates", "Dinghuai Zhang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.03206"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.03206v1"
published: "2025-10-03"
categories: ["cs.AI", "cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:10+09:00"
---

# Coevolutionary Continuous Discrete Diffusion: Make Your Diffusion Language Model a Latent Reasoner

## Abstract
Diffusion language models, especially masked discrete diffusion models, have achieved great success recently. While there are some theoretical and primary empirical results showing the advantages of latent reasoning with looped transformers or continuous chain-of-thoughts, continuous diffusion models typically underperform their discrete counterparts. In this paper, we argue that diffusion language models do not necessarily need to be in the discrete space. In particular, we prove that continuous diffusion models have stronger expressivity than discrete diffusions and looped transformers. We attribute the contradiction between the theoretical expressiveness and empirical performance to their practical trainability: while continuous diffusion provides intermediate supervision that looped transformers lack, they introduce additional difficulty decoding tokens into the discrete token space from the continuous representation space. We therefore propose Coevolutionary Continuous Discrete Diffusion (CCDD), which defines a joint multimodal diffusion process on the union of a continuous representation space and a discrete token space, leveraging a single model to simultaneously denoise in the joint space. By combining two modalities, CCDD is expressive with rich semantics in the latent space, as well as good trainability and sample quality with the help of explicit discrete tokens. We also propose effective architectures and advanced training/sampling techniques for CCDD, which reveals strong empirical performance in extensive language modeling experiments on real-world tasks.

## Metadata
- venue: arXiv
- year: 2025
- authors: Cai Zhou, Chenxiao Yang, Yi Hu, Chenyu Wang, Chubin Zhang, Muhan Zhang, Lester Mackey, Tommi Jaakkola, Stephen Bates, Dinghuai Zhang
- arxiv_id: 2510.03206
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.03206v1
- published: 2025-10-03
