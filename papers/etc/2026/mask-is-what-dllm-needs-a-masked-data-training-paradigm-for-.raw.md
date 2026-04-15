---
title: "Mask Is What DLLM Needs: A Masked Data Training Paradigm for Diffusion LLMs"
authors: ["Linrui Ma", "Yufei Cui", "Kai Han", "Yunhe Wang"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.15803"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.15803v1"
published: "2026-03-16"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:58+09:00"
---

# Mask Is What DLLM Needs: A Masked Data Training Paradigm for Diffusion LLMs

## Abstract
Discrete diffusion models offer global context awareness and flexible parallel generation. However, uniform random noise schedulers in standard DLLM training overlook the highly non-uniform information density inherent in real-world sequences. This wastes optimization resources on low-density structural glues while leaving high-density logical pivot points severely under-optimized. To address this, we propose an Information Density Driven Smart Noise Scheduler. By extracting information-dense hubs and applying Complementary Priority Masking, our method decouples a single training instance into mutually reinforcing reasoning and syntax samples, forcing the model to master both logical deduction and foundational sequence structure. Experiments demonstrate that our approach improves average accuracy by ~4\% across four Code and Math reasoning benchmarks, significantly outperforming uniform baselines. Mechanistic analyses further reveal that probabilistic priority masking effectively mitigates contextual collapse during block diffusion training. Overall, this density-aware strategy efficiently unlocks the reasoning potential of diffusion language models at minimal annotation cost, emerging as a promising new masked data training paradigm for Diffusion LLMs. Our processed dataset can be found at https://huggingface.co/datasets/malr07/opc-sft-stage2-dense-extracted.

## Metadata
- venue: arXiv
- year: 2026
- authors: Linrui Ma, Yufei Cui, Kai Han, Yunhe Wang
- arxiv_id: 2603.15803
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.15803v1
- published: 2026-03-16
