---
title: "CLaM-TTS: Improving Neural Codec Language Model for Zero-Shot Text-to-Speech"
authors: ["Jaehyeon Kim", "Keon Lee", "Seungjun Chung", "Jaewoong Cho"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ofzeypWosV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4aa68c6552ace824647a0f32a7f3b5ff97a6cd58.pdf"
published: "2024"
categories: []
keywords: ["text-to-speech", "speech synthesis", "neural audio codec"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:09+09:00"
---

# CLaM-TTS: Improving Neural Codec Language Model for Zero-Shot Text-to-Speech

## Abstract
With the emergence of neural audio codecs, which encode multiple streams of discrete tokens from audio, large language models have recently gained attention as a promising approach for zero-shot Text-to-Speech (TTS) synthesis. Despite the ongoing rush towards scaling paradigms, audio tokenization ironically amplifies the scalability challenge, stemming from its long sequence length and the complexity of modelling the multiple sequences. To mitigate these issues, we present CLaM-TTS that employs a probabilistic residual vector quantization to (1) achieve superior compression in the token length, and (2) allow a language model to generate multiple tokens at once, thereby eliminating the need for cascaded modeling to handle the number of token streams. Our experimental results demonstrate that CLaM-TTS is better than or comparable to state-of-the-art neural codec-based TTS models regarding naturalness, intelligibility, speaker similarity, and inference speed. In addition, we examine the impact of the pretraining extent of the language models and their text tokenization strategies on performances.

## Metadata
- venue: ICLR
- year: 2024
- authors: Jaehyeon Kim, Keon Lee, Seungjun Chung, Jaewoong Cho
- arxiv_id: 
- openreview_id: ofzeypWosV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4aa68c6552ace824647a0f32a7f3b5ff97a6cd58.pdf
- published: 2024
- keywords: text-to-speech, speech synthesis, neural audio codec
