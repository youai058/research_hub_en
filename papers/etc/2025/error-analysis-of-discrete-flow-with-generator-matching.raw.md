---
title: "Error Analysis of Discrete Flow with Generator Matching"
authors: ["Zhengyan Wan", "Yidong Ouyang", "Qiang Yao", "Liyan Xie", "Fang Fang", "Hongyuan Zha", "Guang Cheng"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.21906"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.21906v2"
published: "2025-09-26"
categories: ["math.ST", "cs.LG", "stat.ML"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:44+09:00"
---

# Error Analysis of Discrete Flow with Generator Matching

## Abstract
Discrete flow models offer a powerful framework for learning distributions over discrete state spaces and have demonstrated superior performance compared to the discrete diffusion models. However, their convergence properties and error analysis remain largely unexplored. In this work, we develop a unified framework grounded in stochastic calculus theory to systematically investigate the theoretical properties of discrete flow models. Specifically, by leveraging a Girsanov-type theorem for the path measures of two continuous-time Markov chains (CTMCs), we present a comprehensive error analysis that accounts for both transition rate estimation error and early stopping error. In fact, the estimation error of transition rates has received little attention in existing works. Unlike discrete diffusion models, discrete flow incurs no initialization error caused by truncating the time horizon in the noising process. Building on generator matching and uniformization, we establish non-asymptotic error bounds for distribution estimation without the boundedness condition on oracle transition rates. Furthermore, we derive a faster rate of total variation convergence for the estimated distribution with the boundedness condition, yielding a nearly optimal rate in terms of sample size. Our results provide the first error analysis for discrete flow models. We also investigate model performance under different settings based on simulation results.

## Metadata
- venue: arXiv
- year: 2025
- authors: Zhengyan Wan, Yidong Ouyang, Qiang Yao, Liyan Xie, Fang Fang, Hongyuan Zha, Guang Cheng
- arxiv_id: 2509.21906
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.21906v2
- published: 2025-09-26
