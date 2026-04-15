---
title: "LADR: Locality-Aware Dynamic Rescue for Efficient Text-to-Image Generation with Diffusion Large Language Models"
authors: ["Chenglin Wang", "Yucheng Zhou", "Shawn Chen", "Tao Wang", "Kai Zhang"]
venue: "ACL"
year: 2026
venue_class: "whitelist"
arxiv_id: "2603.13450"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.13450v2"
published: "2026-03-13"
categories: ["cs.CV", "cs.CL"]
keywords: []
venue_source: "arxiv-comment"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# LADR: Locality-Aware Dynamic Rescue for Efficient Text-to-Image Generation with Diffusion Large Language Models

## Abstract
Discrete Diffusion Language Models have emerged as a compelling paradigm for unified multimodal generation, yet their deployment is hindered by high inference latency arising from iterative decoding. Existing acceleration strategies often require expensive re-training or fail to leverage the 2D spatial redundancy inherent in visual data. To address this, we propose Locality-Aware Dynamic Rescue (LADR), a training-free method that expedites inference by exploiting the spatial Markov property of images. LADR prioritizes the recovery of tokens at the ''generation frontier'', regions spatially adjacent to observed pixels, thereby maximizing information gain. Specifically, our method integrates morphological neighbor identification to locate candidate tokens, employs a risk-bounded filtering mechanism to prevent error propagation, and utilizes manifold-consistent inverse scheduling to align the diffusion trajectory with the accelerated mask density. Extensive experiments on four text-to-image generation benchmarks demonstrate that our LADR achieves an approximate 4 x speedup over standard baselines. Remarkably, it maintains or even enhances generative fidelity, particularly in spatial reasoning tasks, offering a state-of-the-art trade-off between efficiency and quality.

## Metadata
- venue: ACL
- year: 2026
- authors: Chenglin Wang, Yucheng Zhou, Shawn Chen, Tao Wang, Kai Zhang
- arxiv_id: 2603.13450
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.13450v2
- published: 2026-03-13
