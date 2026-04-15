---
title: "Discrete Modeling via Boundary Conditional Diffusion Processes"
authors: ["Yuxuan Gu", "Xiaocheng Feng", "Lei Huang", "Yingsheng Wu", "Zekun Zhou", "Weihong Zhong", "Kun Zhu", "Bing Qin"]
venue: "arXiv"
year: 2024
venue_class: "etc"
arxiv_id: "2410.22380"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2410.22380v1"
published: "2024-10-29"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:20:02+09:00"
---

# Discrete Modeling via Boundary Conditional Diffusion Processes

## Abstract
We present an novel framework for efficiently and effectively extending the powerful continuous diffusion processes to discrete modeling. Previous approaches have suffered from the discrepancy between discrete data and continuous modeling. Our study reveals that the absence of guidance from discrete boundaries in learning probability contours is one of the main reasons. To address this issue, we propose a two-step forward process that first estimates the boundary as a prior distribution and then rescales the forward trajectory to construct a boundary conditional diffusion model. The reverse process is proportionally adjusted to guarantee that the learned contours yield more precise discrete data. Experimental results indicate that our approach achieves strong performance in both language modeling and discrete image generation tasks. In language modeling, our approach surpasses previous state-of-the-art continuous diffusion language models in three translation tasks and a summarization task, while also demonstrating competitive performance compared to auto-regressive transformers. Moreover, our method achieves comparable results to continuous diffusion models when using discrete ordinal pixels and establishes a new state-of-the-art for categorical image generation on the Cifar-10 dataset.

## Metadata
- venue: arXiv
- year: 2024
- authors: Yuxuan Gu, Xiaocheng Feng, Lei Huang, Yingsheng Wu, Zekun Zhou, Weihong Zhong, Kun Zhu, Bing Qin
- arxiv_id: 2410.22380
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2410.22380v1
- published: 2024-10-29
