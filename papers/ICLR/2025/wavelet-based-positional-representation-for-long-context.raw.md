---
title: "Wavelet-based Positional Representation for Long Context"
authors: ["Yui Oka", "Taku Hasegawa", "Kyosuke Nishida", "Kuniko Saito"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OhauMUNW8T"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d5ed2fc8f4eb31801279781b07970b112229814c.pdf"
published: "2025"
categories: []
keywords: ["Positional Encoding", "Extrapolation", "Wavelet Transform", "Transformers", "RoPE", "ALiBi", "NLP"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:06+09:00"
---

# Wavelet-based Positional Representation for Long Context

## Abstract
In the realm of large-scale language models, a significant challenge arises when extrapolating sequences beyond the maximum allowable length. 
This is because the model's position embedding mechanisms are limited to positions encountered during training, thus preventing effective representation of positions in longer sequences.
We analyzed conventional position encoding methods for long contexts and found the following characteristics.
(1) When the representation dimension is regarded as the time axis, Rotary Position Embedding (RoPE) can be interpreted as a restricted wavelet transform using Haar-like wavelets. 
However, because it uses only a fixed scale parameter, it does not fully exploit the advantages of wavelet transforms, which capture the fine movements of non-stationary signals using multiple scales (window sizes). 
This limitation could explain why RoPE performs poorly in extrapolation.
(2)
Previous research as well as our own analysis indicates that Attention with Linear Biases (ALiBi) functions similarly to windowed attention, using windows of varying sizes.
However, it has limitations in capturing deep dependencies because it restricts the receptive field of the model.
From these insights, we propose a new position representation method that captures multiple scales (i.e., window sizes) by leveraging wavelet transforms without limiting the model's attention field.
Experimental results show that this new method improves the performance of the model in both short and long contexts. 
In particular, our method allows extrapolation of position information without limiting the model's attention field.

## Metadata
- venue: ICLR
- year: 2025
- authors: Yui Oka, Taku Hasegawa, Kyosuke Nishida, Kuniko Saito
- arxiv_id: 
- openreview_id: OhauMUNW8T
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d5ed2fc8f4eb31801279781b07970b112229814c.pdf
- published: 2025
- keywords: Positional Encoding, Extrapolation, Wavelet Transform, Transformers, RoPE, ALiBi, NLP
