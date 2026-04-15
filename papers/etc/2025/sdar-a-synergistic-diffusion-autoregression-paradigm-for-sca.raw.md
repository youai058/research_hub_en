---
title: "SDAR: A Synergistic Diffusion-AutoRegression Paradigm for Scalable Sequence Generation"
authors: ["Shuang Cheng", "Yihan Bian", "Dawei Liu", "Linfeng Zhang", "Qian Yao", "Zhongbo Tian", "Wenhai Wang", "Qipeng Guo", "Kai Chen", "Biqing Qi", "Bowen Zhou"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2510.06303"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2510.06303v3"
published: "2025-10-07"
categories: ["cs.LG", "cs.AI"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:22+09:00"
---

# SDAR: A Synergistic Diffusion-AutoRegression Paradigm for Scalable Sequence Generation

## Abstract
We propose SDAR, a Synergistic Diffusion-Autoregression paradigm that unifies the training efficiency of autoregressive models with the parallel inference capability of diffusion. Instead of costly end-to-end diffusion training, SDAR performs a lightweight paradigm conversion that transforms a well-trained autoregressive (AR) model into a blockwise diffusion model through brief, data-efficient adaptation. During inference, SDAR generates sequences autoregressively across blocks for global coherence while decoding all tokens within each block in parallel via a discrete diffusion process. Extensive experiments show that AR models remain substantially more compute-efficient than masked diffusion models, providing a strong foundation for adaptation. Building on this insight, SDAR achieves efficient AR-to-diffusion conversion with minimal cost, preserving AR-level performance while enabling parallel generation. Scaling studies across dense and Mixture-of-Experts architectures confirm that SDAR scales without compromise: larger models exhibit stronger robustness to block size and decoding thresholds, yielding greater speedups without accuracy loss. Beyond efficiency, SDAR demonstrates enhanced reasoning and domain adaptability. Our 30B MoE model surpasses its AR counterpart on challenging scientific reasoning benchmarks such as GPQA and ChemBench, and gains further improvements under test-time scaling methods like majority voting and pass@k. Together, these results establish SDAR as a practical paradigm that combines the strengths of autoregression and diffusion for scalable, high-throughput reasoning.

## Metadata
- venue: arXiv
- year: 2025
- authors: Shuang Cheng, Yihan Bian, Dawei Liu, Linfeng Zhang, Qian Yao, Zhongbo Tian, Wenhai Wang, Qipeng Guo, Kai Chen, Biqing Qi, Bowen Zhou
- arxiv_id: 2510.06303
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2510.06303v3
- published: 2025-10-07
