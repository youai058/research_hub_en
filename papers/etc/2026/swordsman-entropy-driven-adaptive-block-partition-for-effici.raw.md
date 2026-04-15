---
title: "Swordsman: Entropy-Driven Adaptive Block Partition for Efficient Diffusion Language Models"
authors: ["Yu Zhang", "Xinchen Li", "Jialei Zhou", "Hongnan Ma", "Zhongwei Wan", "Yiwei Shi", "Duoqian Miao", "Qi Zhang", "Longbing Cao"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.04399"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.04399v1"
published: "2026-02-04"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:05+09:00"
---

# Swordsman: Entropy-Driven Adaptive Block Partition for Efficient Diffusion Language Models

## Abstract
Block-wise decoding effectively improves the inference speed and quality in diffusion language models (DLMs) by combining inter-block sequential denoising and intra-block parallel unmasking. However, existing block-wise decoding methods typically partition blocks in a rigid and fixed manner, which inevitably fragments complete semantic or syntactic constituents, leading to suboptimal performance. Inspired by the entropy reduction hypothesis (ERH), we recognize that constituent boundaries offer greater opportunities for uncertainty reduction, which motivates us to employ entropy analysis for identifying constituent boundaries. Therefore, we propose Swordsman, an entropy-driven adaptive block-wise decoding framework for DLMs. Swordsman adaptively partitions blocks by identifying entropy shifts between adjacent tokens to better align with semantic or syntactic constituent boundaries. In addition, Swordsman dynamically adjusts unmasking thresholds conditioned on the real-time unmasking status within a block, further improving both efficiency and stability. As a training-free framework, supported by KV Cache, Swordsman demonstrates state-of-the-art performance across extensive evaluations.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yu Zhang, Xinchen Li, Jialei Zhou, Hongnan Ma, Zhongwei Wan, Yiwei Shi, Duoqian Miao, Qi Zhang, Longbing Cao
- arxiv_id: 2602.04399
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.04399v1
- published: 2026-02-04
