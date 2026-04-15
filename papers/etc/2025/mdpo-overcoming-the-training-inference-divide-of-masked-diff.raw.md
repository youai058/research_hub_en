---
title: "MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models"
authors: ["Haoyu He", "Katrin Renz", "Yong Cao", "Andreas Geiger"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2508.13148"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2508.13148v2"
published: "2025-08-18"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:29+09:00"
---

# MDPO: Overcoming the Training-Inference Divide of Masked Diffusion Language Models

## Abstract
Diffusion language models, as a promising alternative to traditional autoregressive (AR) models, enable faster generation and richer conditioning on bidirectional context. However, they suffer from a key discrepancy between training and inference: during inference, MDLMs progressively reveal the structure of the generated sequence by producing fewer and fewer masked tokens, whereas this structure is ignored in training as tokens are masked at random. Although this discrepancy between training and inference can lead to suboptimal performance, it has been largely overlooked by previous works, leaving closing this gap between the two stages an open problem. To address this, we frame the problem of learning effective denoising trajectories as a sequential decision-making problem and use the resulting framework to apply reinforcement learning. We propose a novel Masked Diffusion Policy Optimization (MDPO) to exploit the Markov property diffusion possesses and explicitly train the model under the same progressive refining schedule used at inference. MDPO matches the performance of the previous state-of-the-art (SOTA) method with 60x fewer gradient updates, while achieving average improvements of 9.6% on MATH500 and 54.2% on Countdown over SOTA when trained within the same number of weight updates. Additionally, we improve the remasking strategy of MDLMs as a plug-in inference replacement to overcome the limitation that the model cannot refine tokens flexibly. This training-free method, termed Running Confidence Remasking (RCR), consistently enhances performance and provides further improvements when used with MDPO. Our findings establish great potential for investigating the discrepancy between pre-training and inference of MDLMs. Code: https://github.com/autonomousvision/mdpo. Project Page: https://cli212.github.io/MDPO/.

## Metadata
- venue: arXiv
- year: 2025
- authors: Haoyu He, Katrin Renz, Yong Cao, Andreas Geiger
- arxiv_id: 2508.13148
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2508.13148v2
- published: 2025-08-18
