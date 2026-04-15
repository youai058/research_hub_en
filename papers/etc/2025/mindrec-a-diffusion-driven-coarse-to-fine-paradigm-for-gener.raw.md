---
title: "MindRec: A Diffusion-driven Coarse-to-Fine Paradigm for Generative Recommendation"
authors: ["Mengyao Gao", "Chongming Gao", "Haoyan Liu", "Qingpeng Cai", "Peng Jiang", "Jiajia Chen", "Shuai Yuan", "Xiangnan He"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2511.12597"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2511.12597v2"
published: "2025-11-16"
categories: ["cs.IR"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:06+09:00"
---

# MindRec: A Diffusion-driven Coarse-to-Fine Paradigm for Generative Recommendation

## Abstract
Recent advancements in large language model-based recommendation systems often represent items as text or semantic IDs and generate recommendations in an auto-regressive manner. However, due to the left-to-right greedy decoding strategy and the unidirectional logical flow, such methods often fail to produce globally optimal recommendations. In contrast, human reasoning does not follow a rigid left-to-right sequence. Instead, it often begins with keywords or intuitive insights, which are then refined and expanded. Inspired by this fact, we propose MindRec, a diffusion-driven coarse-to-fine generative paradigm that emulates human thought processes. Built upon a diffusion language model, MindRec departs from auto-regressive generation by leveraging a masked diffusion process to reconstruct items in a flexible, non-sequential manner. Particularly, our method first generates key tokens that reflect user preferences, and then expands them into the complete item, enabling adaptive and human-like generation. To further emulate the structured nature of human decision-making, we organize items into a hierarchical category tree. This structure guides the model to first produce the coarse-grained category and then progressively refine its selection through finer-grained subcategories before generating the specific item. To mitigate the local optimum problem inherent in greedy decoding, we design a novel beam search algorithm, Diffusion Beam Search, tailored for our mind-inspired generation paradigm. Experimental results demonstrate that MindRec yields a 9.5\% average improvement in top-1 accuracy over state-of-the-art methods, highlighting its potential to enhance recommendation performance. The implementation is available via https://github.com/Mr-Peach0301/MindRec.

## Metadata
- venue: arXiv
- year: 2025
- authors: Mengyao Gao, Chongming Gao, Haoyan Liu, Qingpeng Cai, Peng Jiang, Jiajia Chen, Shuai Yuan, Xiangnan He
- arxiv_id: 2511.12597
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2511.12597v2
- published: 2025-11-16
