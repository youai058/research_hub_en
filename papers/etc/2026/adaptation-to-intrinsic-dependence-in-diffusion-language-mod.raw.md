---
title: "Adaptation to Intrinsic Dependence in Diffusion Language Models"
authors: ["Yunxiao Zhao", "Changxiao Cai"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2602.20126"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2602.20126v1"
published: "2026-02-23"
categories: ["cs.LG", "cs.IT", "math.ST", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:02+09:00"
---

# Adaptation to Intrinsic Dependence in Diffusion Language Models

## Abstract
Diffusion language models (DLMs) have recently emerged as a promising alternative to autoregressive (AR) approaches, enabling parallel token generation beyond a rigid left-to-right order. Despite growing empirical success, the theoretical understanding of how unmasking schedules -- which specify the order and size of unmasked tokens during sampling -- affect generation quality remains limited. In this work, we introduce a distribution-agnostic unmasking schedule for DLMs that adapts to the (unknown) dependence structure of the target data distribution, without requiring any prior knowledge or hyperparameter tuning. In contrast to prior deterministic procedures that fix unmasking sizes, our method randomizes the number of tokens revealed at each iteration. We show that, for two specific parameter choices, the sampling convergence guarantees -- measured by Kullback-Leibler (KL) divergence -- scale as $\widetilde O(\mathsf{TC}/K)$ and $\widetilde O(\mathsf{DTC}/K)$ respectively. Here, $K$ is the number of iterations, and $\mathsf{TC}$ and $\mathsf{DTC}$ are the total correlation and dual total correlation of the target distribution, capturing the intrinsic dependence structure underlying the data. Importantly, our guarantees hold in the practically relevant parallel-sampling regime $K<L$ where $L$ is the token sequence length. These results significantly improve upon prior convergence theories and yield substantial sampling acceleration for low-complexity distributions. Overall, our findings unveil the adaptivity of DLMs to intrinsic data structures and shed light on the benefit of randomized unmasking sizes in inference schedule design.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yunxiao Zhao, Changxiao Cai
- arxiv_id: 2602.20126
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2602.20126v1
- published: 2026-02-23
