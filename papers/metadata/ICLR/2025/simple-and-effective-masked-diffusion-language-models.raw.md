---
title: "Simple and Effective Masked Diffusion Language Models"
authors: ["Subham Sekhar Sahoo", "Marianne Arriola", "Yair Schiff", "Aaron Gokaslan", "Edgar Marroquin", "Justin T. Chiu", "Alexander Rush", "Volodymyr Kuleshov"]
venue: "ICLR"
venue_class: "whitelist"
year: 2025
published: "2024-06-18"
url: "https://openreview.net/forum?id=mPMDVk3CKj"
arxiv_id: "2406.07524"
openreview_id: "mPMDVk3CKj"
categories: ["cs.CL", "cs.LG"]
keywords: ["masked diffusion", "language model", "MDLM", "discrete diffusion"]
hunter_fetched: "2026-04-16T12:30:00+09:00"
---

# Simple and Effective Masked Diffusion Language Models

## Abstract

While diffusion models excel in continuous domains like image generation, adapting them to natural language remains challenging. In this work, we show that simple masked discrete diffusion is more performant than previously thought. We apply an effective training recipe that improves the performance of masked diffusion models and derive a simplified, Rao-Blackwellized objective that results in a significant improvement in training efficiency. Our objective has a simple form – it is a mixture of per-token cross-entropy losses. We further show how to use our objective for zero-shot evaluation on downstream tasks. Putting these insights together, by training models up to 1.1B parameters from scratch and fine-tuning pretrained models, we demonstrate that masked diffusion models can match or exceed the performance of autoregressive models of the same or larger size on language modeling and some downstream tasks. Our code is publicly available.
