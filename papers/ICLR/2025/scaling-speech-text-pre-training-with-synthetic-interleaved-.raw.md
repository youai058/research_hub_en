---
title: "Scaling Speech-Text Pre-training with Synthetic Interleaved Data"
authors: ["Aohan Zeng", "Zhengxiao Du", "Mingdao Liu", "Lei Zhang", "shengmin jiang", "Yuxiao Dong", "Jie Tang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3tukjsVyrE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2bfb4c69dc2ba7cb7772f86bf3c3e979bffdc20c.pdf"
published: "2025"
categories: []
keywords: ["large language models; speech language model; spoken chatbots"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:42+09:00"
---

# Scaling Speech-Text Pre-training with Synthetic Interleaved Data

## Abstract
Speech language models (SpeechLMs) accept speech input and produce speech output, allowing for more natural human-computer interaction compared to text-based large language models (LLMs).
Traditional approaches for developing SpeechLMs are constrained by the limited availability of unsupervised speech data and parallel speech-text data, which are significantly less abundant compared to text pre-training data, thereby limiting their scalability as LLMs.
We propose a novel approach to scaling speech-text pre-training by leveraging large-scale synthetic interleaved data derived from text corpora, eliminating the need for parallel speech-text datasets.
Our method efficiently constructs speech-text interleaved data by sampling text spans from existing text corpora and synthesizing corresponding speech spans using a text-to-token model, bypassing the need to generate actual speech.
We also employ a supervised speech tokenizer derived from an automatic speech recognition (ASR) model  by incorporating a vector-quantized bottleneck into the encoder. This supervised training approach results in discrete speech tokens with strong semantic preservation even at lower sampling rates (e.g. 12.5Hz), while still maintaining speech reconstruction quality.
Starting from a pre-trained language model and scaling our pre-training to 1 trillion tokens (with 600B synthetic interleaved speech-text data), we achieve state-of-the-art performance in both speech language modeling and spoken question answering, improving performance on spoken questions tasks from the previous SOTA of 13\% (Moshi) to 31\%.
We further demonstrate that by fine-tuning the pre-trained model with speech dialogue data, we can develop an end-to-end spoken chatbot that achieves competitive performance comparable to existing baselines in both conversational abilities and speech quality, even operating exclusively in the speech domain.

## Metadata
- venue: ICLR
- year: 2025
- authors: Aohan Zeng, Zhengxiao Du, Mingdao Liu, Lei Zhang, shengmin jiang, Yuxiao Dong, Jie Tang
- arxiv_id: 
- openreview_id: 3tukjsVyrE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2bfb4c69dc2ba7cb7772f86bf3c3e979bffdc20c.pdf
- published: 2025
- keywords: large language models; speech language model; spoken chatbots
