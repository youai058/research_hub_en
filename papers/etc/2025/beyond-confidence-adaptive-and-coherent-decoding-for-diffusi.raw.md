---
title: "Beyond Confidence: Adaptive and Coherent Decoding for Diffusion Language Models"
authors: ["Kecheng Chen", "Ziru Liu", "Xijia Tao", "Hui Liu", "Xinyu Fu", "Suiyun Zhang", "Dandan Tu", "Lingpeng Kong", "Rui Liu", "Haoliang Li"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2512.02044"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2512.02044v1"
published: "2025-11-26"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:03+09:00"
---

# Beyond Confidence: Adaptive and Coherent Decoding for Diffusion Language Models

## Abstract
Diffusion Language Models (DLMs) have recently achieved significant success due to their any-order generation capabilities. However, existing inference methods typically rely on local, immediate-step metrics such as confidence or entropy which inherently lack a more reliable perspective. This limitation frequently leads to inconsistent sampling trajectories and suboptimal generation quality. To address this, we propose Coherent Contextual Decoding (CCD), a novel inference framework built upon two core innovations. First, CCD employs a trajectory rectification mechanism that leverages historical context to enhance sequence coherence, enabling the early rejection of suboptimal paths. We demonstrate that this mechanism is theoretically equivalent to modeling the consistency of historical steps via the conditional mutual information between context and token predictions. Building on this theoretical insight, we further address the inefficiency of conventional uniform decoding budgets. Instead of rigid allocations based on diffusion steps, we introduce an adaptive sampling strategy that dynamically adjusts the unmasking budget for each step according to our consistency metric. Consequently, our method significantly improves the quality of generation trajectories while accelerating the sampling process. Empirically, our method achieves a simultaneous enhancement in both inference speed and performance across diverse benchmarks on Dream and LLaDA, delivering up to 3.48x speedup alongside 3.91% performance improvement.

## Metadata
- venue: arXiv
- year: 2025
- authors: Kecheng Chen, Ziru Liu, Xijia Tao, Hui Liu, Xinyu Fu, Suiyun Zhang, Dandan Tu, Lingpeng Kong, Rui Liu, Haoliang Li
- arxiv_id: 2512.02044
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2512.02044v1
- published: 2025-11-26
