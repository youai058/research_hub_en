---
title: "dLLM-ASR: A Faster Diffusion LLM-based Framework for Speech Recognition"
authors: ["Wenjie Tian", "Bingshen Mu", "Guobin Ma", "Xuelong Geng", "Zhixian Zhao", "Lei Xie"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.17902"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.17902v1"
published: "2026-01-25"
categories: ["cs.SD", "eess.AS"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# dLLM-ASR: A Faster Diffusion LLM-based Framework for Speech Recognition

## Abstract
Automatic speech recognition (ASR) systems based on large language models (LLMs) achieve superior performance by leveraging pretrained LLMs as decoders, but their token-by-token generation mechanism leads to inference latency that grows linearly with sequence length. Meanwhile, discrete diffusion large language models (dLLMs) offer a promising alternative, enabling high-quality parallel sequence generation with pretrained decoders. However, directly applying native text-oriented dLLMs to ASR leads to a fundamental mismatch between open-ended text generation and the acoustically conditioned transcription paradigm required by ASR. As a result, it introduces unnecessary difficulty and computational redundancy, such as denoising from pure noise, inflexible generation lengths, and fixed denoising steps. We propose dLLM-ASR, an efficient dLLM-based ASR framework that formulates dLLM's decoding as a prior-guided and adaptive denoising process. It leverages an ASR prior to initialize the denoising process and provide an anchor for sequence length. Building upon this prior, length-adaptive pruning dynamically removes redundant tokens, while confidence-based denoising allows converged tokens to exit the denoising loop early, enabling token-level adaptive computation. Experiments demonstrate that dLLM-ASR achieves recognition accuracy comparable to autoregressive LLM-based ASR systems and delivers a 4.44$\times$ inference speedup, establishing a practical and efficient paradigm for ASR.

## Metadata
- venue: arXiv
- year: 2026
- authors: Wenjie Tian, Bingshen Mu, Guobin Ma, Xuelong Geng, Zhixian Zhao, Lei Xie
- arxiv_id: 2601.17902
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.17902v1
- published: 2026-01-25
