---
title: "Corrected Samplers for Discrete Flow Models"
authors: ["Zhengyan Wan", "Yidong Ouyang", "Liyan Xie", "Fang Fang", "Hongyuan Zha", "Guang Cheng"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.22519"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.22519v1"
published: "2026-01-30"
categories: ["stat.ML", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:36+09:00"
---

# Corrected Samplers for Discrete Flow Models

## Abstract
Discrete flow models (DFMs) have been proposed to learn the data distribution on a finite state space, offering a flexible framework as an alternative to discrete diffusion models. A line of recent work has studied samplers for discrete diffusion models, such as tau-leaping and Euler solver. However, these samplers require a large number of iterations to control discretization error, since the transition rates are frozen in time and evaluated at the initial state within each time interval. Moreover, theoretical results for these samplers often require boundedness conditions of the transition rate or they focus on a specific type of source distributions. To address those limitations, we establish non-asymptotic discretization error bounds for those samplers without any restriction on transition rates and source distributions, under the framework of discrete flow models. Furthermore, by analyzing a one-step lower bound of the Euler sampler, we propose two corrected samplers: \textit{time-corrected sampler} and \textit{location-corrected sampler}, which can reduce the discretization error of tau-leaping and Euler solver with almost no additional computational cost. We rigorously show that the location-corrected sampler has a lower iteration complexity than existing parallel samplers. We validate the effectiveness of the proposed method by demonstrating improved generation quality and reduced inference time on both simulation and text-to-image generation tasks. Code can be found in https://github.com/WanZhengyan/Corrected-Samplers-for-Discrete-Flow-Models.

## Metadata
- venue: arXiv
- year: 2026
- authors: Zhengyan Wan, Yidong Ouyang, Liyan Xie, Fang Fang, Hongyuan Zha, Guang Cheng
- arxiv_id: 2601.22519
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.22519v1
- published: 2026-01-30
