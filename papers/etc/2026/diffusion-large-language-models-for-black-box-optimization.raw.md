---
title: "Diffusion Large Language Models for Black-Box Optimization"
authors: ["Ye Yuan", "Can", "Chen", "Zipeng Sun", "Dinghuai Zhang", "Christopher Pal", "Xue Liu"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.14446"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.14446v1"
published: "2026-01-20"
categories: ["cs.CE", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Diffusion Large Language Models for Black-Box Optimization

## Abstract
Offline black-box optimization (BBO) aims to find optimal designs based solely on an offline dataset of designs and their labels. Such scenarios frequently arise in domains like DNA sequence design and robotics, where only a few labeled data points are available. Traditional methods typically rely on task-specific proxy or generative models, overlooking the in-context learning capabilities of pre-trained large language models (LLMs). Recent efforts have adapted autoregressive LLMs to BBO by framing task descriptions and offline datasets as natural language prompts, enabling direct design generation. However, these designs often contain bidirectional dependencies, which left-to-right models struggle to capture. In this paper, we explore diffusion LLMs for BBO, leveraging their bidirectional modeling and iterative refinement capabilities. This motivates our in-context denoising module: we condition the diffusion LLM on the task description and the offline dataset, both formatted in natural language, and prompt it to denoise masked designs into improved candidates. To guide the generation toward high-performing designs, we introduce masked diffusion tree search, which casts the denoising process as a step-wise Monte Carlo Tree Search that dynamically balances exploration and exploitation. Each node represents a partially masked design, each denoising step is an action, and candidates are evaluated via expected improvement under a Gaussian Process trained on the offline dataset. Our method, dLLM, achieves state-of-the-art results in few-shot settings on design-bench.

## Metadata
- venue: arXiv
- year: 2026
- authors: Ye Yuan, Can, Chen, Zipeng Sun, Dinghuai Zhang, Christopher Pal, Xue Liu
- arxiv_id: 2601.14446
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.14446v1
- published: 2026-01-20
