---
title: "Discrete Diffusion Models: Novel Analysis and New Sampler Guarantees"
authors: ["Yuchen Liang", "Yingbin Liang", "Lifeng Lai", "Ness Shroff"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.16756"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.16756v2"
published: "2025-09-20"
categories: ["cs.LG", "eess.SP"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:44+09:00"
---

# Discrete Diffusion Models: Novel Analysis and New Sampler Guarantees

## Abstract
Discrete diffusion models have recently gained significant prominence in applications involving natural language and graph data. A key factor influencing their effectiveness is the efficiency of discretized samplers. Among these, $τ$-leaping samplers have become particularly popular due to their theoretical and empirical success. However, existing theoretical analyses of $τ$-leaping often rely on somewhat restrictive and difficult-to-verify regularity assumptions, and their convergence bounds contain quadratic dependence on the vocabulary size. In this work, we introduce a new analytical approach for discrete diffusion models that removes the need for such assumptions. For the standard $τ$-leaping method, we establish convergence guarantees in KL divergence that scale linearly with vocabulary size, improving upon prior results with quadratic dependence. Our approach is also more broadly applicable: it provides the first convergence guarantees for other widely used samplers, including the Euler method and Tweedie $τ$-leaping. Central to our approach is a novel technique based on differential inequalities, offering a more flexible alternative to the traditional Girsanov change-of-measure methods. This technique may also be of independent interest for the analysis of other stochastic processes.

## Metadata
- venue: arXiv
- year: 2025
- authors: Yuchen Liang, Yingbin Liang, Lifeng Lai, Ness Shroff
- arxiv_id: 2509.16756
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.16756v2
- published: 2025-09-20
