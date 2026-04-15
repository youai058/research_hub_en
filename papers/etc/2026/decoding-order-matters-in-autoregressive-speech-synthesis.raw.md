---
title: "Decoding Order Matters in Autoregressive Speech Synthesis"
authors: ["Minghui Zhao", "Anton Ragni"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.08450"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.08450v1"
published: "2026-01-13"
categories: ["cs.SD", "cs.AI", "eess.AS"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Decoding Order Matters in Autoregressive Speech Synthesis

## Abstract
Autoregressive speech synthesis often adopts a left-to-right order, yet generation order is a modelling choice. We investigate decoding order through masked diffusion framework, which progressively unmasks positions and allows arbitrary decoding orders during training and inference. By interpolating between identity and random permutations, we show that randomness in decoding order affects speech quality. We further compare fixed strategies, such as \texttt{l2r} and \texttt{r2l} with adaptive ones, such as Top-$K$, finding that fixed-order decoding, including the dominating left-to-right approach, is suboptimal, while adaptive decoding yields better performance. Finally, since masked diffusion requires discrete inputs, we quantise acoustic representations and find that even 1-bit quantisation can support reasonably high-quality speech.

## Metadata
- venue: arXiv
- year: 2026
- authors: Minghui Zhao, Anton Ragni
- arxiv_id: 2601.08450
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.08450v1
- published: 2026-01-13
