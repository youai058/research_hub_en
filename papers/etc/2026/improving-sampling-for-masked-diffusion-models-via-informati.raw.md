---
title: "Improving Sampling for Masked Diffusion Models via Information Gain"
authors: ["Kaisen Yang", "Jayden Teoh", "Kaicheng Yang", "Yitong Zhang", "Alex Lamb"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.18176"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.18176v2"
published: "2026-02-20"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# Improving Sampling for Masked Diffusion Models via Information Gain

## Abstract
Masked Diffusion Models (MDMs) offer greater flexibility in decoding order than autoregressive models but require careful planning to achieve high-quality generation. Existing samplers typically adopt greedy heuristics, prioritizing positions with the highest local certainty to decode at each step. Through failure case analysis, we identify a fundamental limitation of this approach: it neglects the downstream impact of current decoding choices on subsequent steps and fails to minimize cumulative uncertainty. In particular, these methods do not fully exploit the non-causal nature of MDMs, which enables evaluating how a decoding decision reshapes token probabilities/uncertainty across all remaining masked positions. To bridge this gap, we propose the Info-Gain Sampler, a principled decoding framework that balances immediate uncertainty with information gain over future masked tokens. Extensive evaluations across diverse architectures and tasks (reasoning, coding, creative writing, and image generation) demonstrate that Info-Gain Sampler consistently outperforms existing samplers for MDMs. For instance, it achieves a 3.6% improvement in average accuracy on reasoning tasks and a 63.1% win-rate in creative writing. Notably, on reasoning tasks it reduces cumulative uncertainty from 78.4 to 48.6, outperforming the best baseline by a large margin. The code will be available at https://github.com/yks23/Information-Gain-Sampler.

## Metadata
- venue: arXiv
- year: 2026
- authors: Kaisen Yang, Jayden Teoh, Kaicheng Yang, Yitong Zhang, Alex Lamb
- arxiv_id: 2602.18176
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.18176v2
- published: 2026-02-20
