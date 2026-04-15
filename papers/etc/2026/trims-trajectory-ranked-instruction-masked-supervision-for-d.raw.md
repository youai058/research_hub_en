---
title: "TRIMS: Trajectory-Ranked Instruction Masked Supervision for Diffusion Language Models"
authors: ["Lingjie Chen", "Ruizhong Qiu", "Yuyu Fan", "Yanjun Zhao", "Hanghang Tong"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.00666"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.00666v1"
published: "2026-04-01"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# TRIMS: Trajectory-Ranked Instruction Masked Supervision for Diffusion Language Models

## Abstract
Diffusion language models (DLMs) offer a promising path toward low-latency generation through parallel decoding, but their practical efficiency depends heavily on the decoding trajectory. In practice, this advantage often fails to fully materialize because standard training does not provide explicit supervision over token reveal order, creating a train-inference mismatch that leads to suboptimal decoding behavior. We propose Trajectory-Ranked Instruction Masked Supervision (TRIMS), a simple trajectory-guided supervised fine-tuning framework that injects trajectory supervision into standard Masked Diffusion Language Model (MDLM) training with minimal overhead. Instead of relying on costly DLM-based distillation, TRIMS uses lightweight signals from an autoregressive teacher to guide a trajectory-aware masking strategy, encouraging the model to learn more effective decoding orders. Experiments on LLaDA and Dream across math and coding benchmarks show that TRIMS significantly improves the accuracy-parallelism trade-off over both standard MDLM training and train-free acceleration baselines, while achieving competitive performance with prior distillation-based approaches at substantially lower training cost. Further analysis shows that TRIMS leads to better decoding trajectories, validating the effectiveness of trajectory-guided supervision for DLMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Lingjie Chen, Ruizhong Qiu, Yuyu Fan, Yanjun Zhao, Hanghang Tong
- arxiv_id: 2604.00666
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.00666v1
- published: 2026-04-01
