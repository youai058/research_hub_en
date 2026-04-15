---
title: "LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token"
authors: ["Shaolei Zhang", "Qingkai Fang", "Zhe Yang", "Yang Feng"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "UQJ7CDW8nb"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/efd2169a71f1800808f58038f0bf1023ce051103.pdf"
published: "2025"
categories: []
keywords: ["Large Multimodal Models", "Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:53+09:00"
---

# LLaVA-Mini: Efficient Image and Video Large Multimodal Models with One Vision Token

## Abstract
The advent of real-time large multimodal models (LMMs) like GPT-4o has sparked considerable interest in efficient LMMs. LMM frameworks typically encode visual inputs into vision tokens (continuous representations) and integrate them and textual instructions into the context of large language models (LLMs), where large-scale parameters and numerous context tokens (predominantly vision tokens) result in substantial computational overhead. Previous efforts towards efficient LMMs always focus on replacing the LLM backbone with smaller models, while neglecting the crucial issue of token quantity. In this paper, we introduce LLaVA-Mini, an efficient LMM with minimal vision tokens. To achieve a high compression ratio of vision tokens while preserving visual information, we first analyze how LMMs understand vision tokens and find that most vision tokens only play a crucial role in the early layers of LLM backbone, where they mainly fuse visual information into text tokens. Building on this finding, LLaVA-Mini introduces modality pre-fusion to fuse visual information into text tokens in advance, thereby facilitating the extreme compression of vision tokens fed to LLM backbone into one token. LLaVA-Mini is a unified large multimodal model that can support the understanding of images, high-resolution images, and videos in an efficient manner. Experiments across 11 image-based and 7 video-based benchmarks demonstrate that LLaVA-Mini outperforms LLaVA-v1.5 with just 1 vision token instead of 576. Efficiency analyses reveal that LLaVA-Mini can reduce FLOPs by 77%, deliver low-latency responses within 40 milliseconds, and process over 10,000 frames of video on the GPU hardware with 24GB of memory.

## Metadata
- venue: ICLR
- year: 2025
- authors: Shaolei Zhang, Qingkai Fang, Zhe Yang, Yang Feng
- arxiv_id: 
- openreview_id: UQJ7CDW8nb
- anthology_id: 
- pdf_url: https://openreview.net/pdf/efd2169a71f1800808f58038f0bf1023ce051103.pdf
- published: 2025
- keywords: Large Multimodal Models, Large Language Models
