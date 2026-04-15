---
title: "On the $ε$-Free Inference Complexity of Absorbing Discrete Diffusion"
authors: ["Xunpeng Huang", "Yingyu Lin", "Nishant Jain", "Kaibo Wang", "Difan Zou", "Yian Ma", "Tong Zhang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.21835"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.21835v2"
published: "2025-09-26"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:44+09:00"
---

# On the $ε$-Free Inference Complexity of Absorbing Discrete Diffusion

## Abstract
Absorbing discrete diffusion has emerged as a dominant framework for discrete data generation. However, a significant disparity remains between its empirical success and theoretical understanding: existing analyses fail to demonstrate a complexity advantage over the $\mathcal{O}(d \ln(d/ε))$ baseline established for \emph{uniform} discrete diffusion. We bridge this gap by identifying a critical structural advantage: whereas uniform diffusion redundantly re-denoises valid elements, the absorbing scheme denoises each absorbing state exactly once. Leveraging this insight, we introduce \emph{Absorbing-Aware Truncated Uniformization} (AATU). We prove that AATU achieves $ε$-TV convergence with $\mathcal{O}(d \ln d)$ complexity-\emph{independent} of the error tolerance $ε$-thereby strictly outperforming existing uniform baselines. Beyond improving convergence rates, our analysis eliminates the restrictive bounded-score assumption commonly required in prior studies of uniformization-based inference. Furthermore, we extend AATU to time-invariant parameterizations, showing that it naturally adopts an imputation-type inference with a uniformly randomized denoising order. When combined with a lazy update strategy, TV convergence requires only $\mathcal{O}(d)$ discrete score evaluations. These results not only establish a rigorous foundation for absorbing discrete diffusion -- confirming its efficiency in high-accuracy generation -- but also open new avenues for analyzing diffusion-based language models under the masking paradigm.

## Metadata
- venue: arXiv
- year: 2025
- authors: Xunpeng Huang, Yingyu Lin, Nishant Jain, Kaibo Wang, Difan Zou, Yian Ma, Tong Zhang
- arxiv_id: 2509.21835
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.21835v2
- published: 2025-09-26
