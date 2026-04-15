---
title: "Emu3.5: Native Multimodal Models are World Learners"
authors: ["Yufeng Cui", "Honghao Chen", "Haoge Deng", "Xu Huang", "Xinghang Li", "Jirong Liu", "Yang Liu", "Zhuoyan Luo", "Jinsheng Wang", "Wenxuan Wang", "Yueze Wang", "Chengyuan Wang", "Fan Zhang", "Yingli Zhao", "Ting Pan", "Xianduo Li", "Zecheng Hao", "Wenxuan Ma", "Zhuo Chen", "Yulong Ao", "Tiejun Huang", "Zhongyuan Wang", "Xinlong Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.26583"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.26583v1"
published: "2025-10-30"
categories: ["cs.CV"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:37+09:00"
---

# Emu3.5: Native Multimodal Models are World Learners

## Abstract
We introduce Emu3.5, a large-scale multimodal world model that natively predicts the next state across vision and language. Emu3.5 is pre-trained end-to-end with a unified next-token prediction objective on a corpus of vision-language interleaved data containing over 10 trillion tokens, primarily derived from sequential frames and transcripts of internet videos. The model naturally accepts interleaved vision-language inputs and generates interleaved vision-language outputs. Emu3.5 is further post-trained with large-scale reinforcement learning to enhance multimodal reasoning and generation. To improve inference efficiency, we propose Discrete Diffusion Adaptation (DiDA), which converts token-by-token decoding into bidirectional parallel prediction, accelerating per-image inference by about 20x without sacrificing performance. Emu3.5 exhibits strong native multimodal capabilities, including long-horizon vision-language generation, any-to-image (X2I) generation, and complex text-rich image generation. It also exhibits generalizable world-modeling abilities, enabling spatiotemporally consistent world exploration and open-world embodied manipulation across diverse scenarios and tasks. For comparison, Emu3.5 achieves performance comparable to Gemini 2.5 Flash Image (Nano Banana) on image generation and editing tasks and demonstrates superior results on a suite of interleaved generation tasks. We open-source Emu3.5 at https://github.com/baaivision/Emu3.5 to support community research.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yufeng Cui, Honghao Chen, Haoge Deng, Xu Huang, Xinghang Li, Jirong Liu, Yang Liu, Zhuoyan Luo, Jinsheng Wang, Wenxuan Wang, Yueze Wang, Chengyuan Wang, Fan Zhang, Yingli Zhao, Ting Pan, Xianduo Li, Zecheng Hao, Wenxuan Ma, Zhuo Chen, Yulong Ao, Tiejun Huang, Zhongyuan Wang, Xinlong Wang
- arxiv_id: 2510.26583
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.26583v1
- published: 2025-10-30
