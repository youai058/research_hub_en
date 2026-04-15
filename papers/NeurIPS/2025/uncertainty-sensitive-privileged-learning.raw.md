---
title: "Uncertainty-Sensitive Privileged Learning"
authors: ["Fan-Ming Luo", "Lei Yuan", "Yang Yu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "00Bwl1woOJ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4d329906b712c3b27c9aa333f7ea1c9a9045d45f.pdf"
published: "2025"
categories: []
keywords: ["Imitation Gap", "Reinforcement Learning", "Privileged Learning", "Teacher-Student Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:28+09:00"
---

# Uncertainty-Sensitive Privileged Learning

## Abstract
Privileged learning efficiently tackles high-dimensional, partially observable decision-making problems by first training a privileged policy (PP) on low-dimensional privileged observations, and then deriving a deployment policy (DP) either by imitating the PP or coupling it with an observation encoder. However, since the DP relies on local and partial observations, a behavioral divergence (BD) often emerges between the DP and the PP, ultimately degrading deployment performance.  A promising strategy is to train a PP to learn the optimal behaviors attainable under the DP’s observation space by applying reward penalties in regions with large BD. However, producing these behaviors is challenging for the PP because they rely on the DP’s information-gathering progress, which is invisible to the PP. In this paper, we quantify the DP’s information-gathering progress by estimating the prediction uncertainty of privileged observations reconstructed from partial observations, and accordingly propose the framework of Uncertainty-Sensitive Privileged Learning (USPL). USPL feeds this uncertainty estimation to the PP and combines reward transformation with privileged-observation blurring, driving the PP to choose actions that actively reduce uncertainty and thus gather the necessary information. Experiments across nine tasks demonstrate that USPL significantly reduces the behavioral discrepancies, achieving superior deployment performance compared to baselines. Additional visualization results show that the DP accurately quantifies its uncertainty, and the PP effectively adapts to uncertainty variations. Code is available at https://github.com/FanmingL/USPL.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Fan-Ming Luo, Lei Yuan, Yang Yu
- arxiv_id: 
- openreview_id: 00Bwl1woOJ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4d329906b712c3b27c9aa333f7ea1c9a9045d45f.pdf
- published: 2025
- keywords: Imitation Gap, Reinforcement Learning, Privileged Learning, Teacher-Student Learning
