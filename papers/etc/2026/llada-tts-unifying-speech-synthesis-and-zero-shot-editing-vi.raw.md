---
title: "LLaDA-TTS: Unifying Speech Synthesis and Zero-Shot Editing via Masked Diffusion Modeling"
authors: ["Xiaoyu Fan", "Huizhi Xie", "Wei Zou", "Yunzhang Chen"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.26364"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.26364v1"
published: "2026-03-27"
categories: ["cs.SD"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:09+09:00"
---

# LLaDA-TTS: Unifying Speech Synthesis and Zero-Shot Editing via Masked Diffusion Modeling

## Abstract
Large language model (LLM)-based text-to-speech (TTS) systems achieve remarkable naturalness via autoregressive (AR) decoding, but require N sequential steps to generate N speech tokens. We present LLaDA-TTS, which replaces the AR LLM with a masked diffusion model that completes generation in a fixed number of parallel steps, decoupling inference latency from sequence length. Remarkably, using only 50 hours of fine-tuning data, we successfully transfer a pretrained AR checkpoint to the masked diffusion paradigm via bidirectional attention. At 64 steps, LLaDA-TTS achieves 0.98% CER (zh) and 1.96% WER (en) on Seed-TTS-Eval, matching the original CosyVoice 3 baseline performance while delivering a 2x LLM-stage speedup--a notable acceleration achieved despite the absence of KV cache, an optimization the AR baseline heavily relies on. Beyond acceleration, the bidirectional architecture naturally enables zero-shot speech editing--including word-level insertion, deletion, and substitution--without any additional training. Theoretically, we prove that AR-pretrained weights are near-optimal for bidirectional masked prediction under the locality property of acoustic tokens, explaining this rapid convergence. This general method modifies only the attention mask and objective, applying seamlessly to any LLM-based AR TTS system. Code and audio samples will be available at https://deft-piroshki-b652b5.netlify.app/.

## Metadata
- venue: arXiv
- year: 2026
- authors: Xiaoyu Fan, Huizhi Xie, Wei Zou, Yunzhang Chen
- arxiv_id: 2603.26364
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.26364v1
- published: 2026-03-27
