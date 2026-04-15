---
title: "From Text to Talk: Audio-Language Model Needs Non-Autoregressive Joint Training"
authors: ["Tianqiao Liu", "Xueyi Li", "Hao Wang", "Haoxuan Li", "Zhichao Chen", "Weiqi Luo", "Zitao Liu"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "e3XLWHFrnr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/90f0216be212ae7d4a1422cc204c1d014cfa456b.pdf"
published: "2026"
categories: []
keywords: ["Large Multimodal Models", "Multi-token Prediction", "Non-Autoregressive Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:17+09:00"
---

# From Text to Talk: Audio-Language Model Needs Non-Autoregressive Joint Training

## Abstract
Recent advances in large language models (LLMs) have attracted significant interest in extending their capabilities to multimodal scenarios, particularly for speech-to-speech (S2S) conversational systems. However, existing multimodal models handling interleaved audio and text rely on autoregressive (AR) methods, overlooking that text depends on target-target relations whereas audio depends mainly on source-target relations. In this work, we propose Text-to-Talk (TtT), a unified audio-text framework that integrates AR text generation with non-autoregressive (NAR) audio diffusion in a single Transformer. By leveraging the any-order AR property of absorbing discrete diffusion, our approach provides a unified training objective for text and audio. To support this hybrid generation paradigm, we design a modality-aware attention mechanism that enforces causal decoding for text while allowing bidirectional modeling within audio spans, and further introduce three training strategies that reduce train-test discrepancies. During inference, TtT employs block-wise diffusion to synthesize audio in parallel while flexibly handling variable-length outputs. Comprehensive experiments on audio question answering (Audio-QA), automatic speech recognition (ASR), automated audio caption (AAC) and S2S benchmarks show that TtT consistently surpasses strong AR and NAR baselines, with additional ablation and training-strategy analyses confirming the contribution of each component.

## Metadata
- venue: ICLR
- year: 2026
- authors: Tianqiao Liu, Xueyi Li, Hao Wang, Haoxuan Li, Zhichao Chen, Weiqi Luo, Zitao Liu
- arxiv_id: 
- openreview_id: e3XLWHFrnr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/90f0216be212ae7d4a1422cc204c1d014cfa456b.pdf
- published: 2026
- keywords: Large Multimodal Models, Multi-token Prediction, Non-Autoregressive Learning
