---
title: "Progressive Refinement Regulation for Accelerating Diffusion Language Model Decoding"
authors: ["Lipeng Wan", "Jianhui Gu", "Junjie Ma", "Jianguo Huang", "Shiguang Sun", "Siyuan Li", "Xuguang Lan"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.04514"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.04514v1"
published: "2026-03-04"
categories: ["cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# Progressive Refinement Regulation for Accelerating Diffusion Language Model Decoding

## Abstract
Diffusion language models generate text through iterative denoising under a uniform refinement rule applied to all tokens. However, tokens stabilize at different rates in practice, leading to substantial redundant refinement and motivating refinement control over the denoising process. Existing approaches typically assess refinement necessity from instantaneous, step-level signals under a fixed decoding process. In contrast, whether a token has converged is defined by how its prediction changes along its future refinement trajectory. Moreover, changing the refinement rule reshapes future refinement trajectories, which in turn determine how refinement rules should be formulated, making refinement control inherently dynamic. We propose \emph{Progressive Refinement Regulation} (PRR), a progressive, trajectory-grounded refinement control framework that derives a token-level notion of empirical convergence progress from full decoding rollouts. Based on this signal, PRR learns a lightweight token-wise controller to regulate refinement via temperature-based distribution shaping under a progressive self-evolving training scheme. Experiments show that PRR substantially accelerates diffusion language model decoding while preserving generation quality.

## Metadata
- venue: arXiv
- year: 2026
- authors: Lipeng Wan, Jianhui Gu, Junjie Ma, Jianguo Huang, Shiguang Sun, Siyuan Li, Xuguang Lan
- arxiv_id: 2603.04514
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.04514v1
- published: 2026-03-04
