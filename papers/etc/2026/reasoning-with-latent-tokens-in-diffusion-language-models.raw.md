---
title: "Reasoning with Latent Tokens in Diffusion Language Models"
authors: ["Andre He", "Sean Welleck", "Daniel Fried"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.03769"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.03769v1"
published: "2026-02-03"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# Reasoning with Latent Tokens in Diffusion Language Models

## Abstract
Discrete diffusion models have recently become competitive with autoregressive models for language modeling, even outperforming them on reasoning tasks requiring planning and global coherence, but they require more computation at inference time. We trace this trade-off to a key mechanism: diffusion models are trained to jointly predict a distribution over all unknown tokens, including those that will not actually be decoded in the current step. Ablating this joint prediction yields faster inference but degrades performance, revealing that accurate prediction at the decoded position relies on joint reasoning about the distribution of undecoded tokens. We interpret these as latent tokens and introduce a method for modulating their number, demonstrating empirically that this enables a smooth tradeoff between inference speed and sample quality. Furthermore, we demonstrate that latent tokens can be introduced into autoregressive models through an auxiliary multi-token prediction objective, yielding substantial improvements on the same reasoning tasks where they have traditionally struggled. Our results suggest that latent tokens, while arising naturally in diffusion, represent a general mechanism for improving performance on tasks requiring global coherence or lookahead.

## Metadata
- venue: arXiv
- year: 2026
- authors: Andre He, Sean Welleck, Daniel Fried
- arxiv_id: 2602.03769
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.03769v1
- published: 2026-02-03
