---
title: "Advancing Block Diffusion Language Models for Test-Time Scaling"
authors: ["Yi Lu", "Deyang Kong", "Jianing Wang", "Linsen Guo", "Xue Wang", "Qi Guo", "Tao Gui", "Xuanjing Huang", "Wei Ye", "Shikun Zhang", "Wei Wang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.09555"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.09555v2"
published: "2026-02-10"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Advancing Block Diffusion Language Models for Test-Time Scaling

## Abstract
Recent advances in block diffusion language models have demonstrated competitive performance and strong scalability on reasoning tasks. However, existing BDLMs have limited exploration under the test-time scaling setting and face more severe decoding challenges in long Chain-of-Thought reasoning, particularly in balancing the decoding speed and effectiveness. In this work, we propose a unified framework for test-time scaling in BDLMs that introduces adaptivity in both decoding and block-wise generation. At the decoding level, we propose Bounded Adaptive Confidence Decoding (BACD), a difficulty-aware sampling strategy that dynamically adjusts denoising based on model confidence, accelerating inference while controlling error accumulation. Beyond step-wise adaptivity, we introduce Think Coarse, Critic Fine (TCCF), a test-time scaling paradigm that allocates large block sizes to exploratory reasoning and smaller block sizes to refinement, achieving an effective efficiency-effectiveness balance. To enable efficient and effective decoding with a large block size, we adopt Progressive Block Size Extension, which mitigates performance degradation when scaling block sizes. Extensive experiments show that applying BACD and TCCF to TDAR-8B yields significant improvements over strong baselines such as TraDo-8B (2.26x speedup, +11.2 points on AIME24). These results mark an important step toward unlocking the potential of BDLMs for test-time scaling in complex reasoning tasks.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yi Lu, Deyang Kong, Jianing Wang, Linsen Guo, Xue Wang, Qi Guo, Tao Gui, Xuanjing Huang, Wei Ye, Shikun Zhang, Wei Wang
- arxiv_id: 2602.09555
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.09555v2
- published: 2026-02-10
