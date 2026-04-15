---
title: "DiffuSpeech: Silent Thought, Spoken Answer via Unified Speech-Text Diffusion"
authors: ["Yuxuan Lou", "Ziming Wu", "Yaochen Wang", "Yong Liu", "Yingxuan Ren", "Fuming Lai", "Shaobing Lian", "Jie Tang", "Yang You"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.22889"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.22889v1"
published: "2026-01-30"
categories: ["cs.CL", "cs.AI", "cs.LG", "cs.SD"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# DiffuSpeech: Silent Thought, Spoken Answer via Unified Speech-Text Diffusion

## Abstract
Current speech language models generate responses directly without explicit reasoning, leading to errors that cannot be corrected once audio is produced. We introduce \textbf{``Silent Thought, Spoken Answer''} -- a paradigm where speech LLMs generate internal text reasoning alongside spoken responses, with thinking traces informing speech quality. To realize this, we present \method{}, the first diffusion-based speech-text language model supporting both understanding and generation, unifying discrete text and tokenized speech under a single masked diffusion framework. Unlike autoregressive approaches, \method{} jointly generates reasoning traces and speech tokens through iterative denoising, with modality-specific masking schedules. We also construct \dataset{}, the first speech QA dataset with paired text reasoning traces, containing 26K samples totaling 319 hours. Experiments show \method{} achieves state-of-the-art speech-to-speech QA accuracy, outperforming the best baseline by up to 9 points, while attaining the best TTS quality among generative models (6.2\% WER) and preserving language understanding (66.2\% MMLU). Ablations confirm that both the diffusion architecture and thinking traces contribute to these gains.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yuxuan Lou, Ziming Wu, Yaochen Wang, Yong Liu, Yingxuan Ren, Fuming Lai, Shaobing Lian, Jie Tang, Yang You
- arxiv_id: 2601.22889
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.22889v1
- published: 2026-01-30
