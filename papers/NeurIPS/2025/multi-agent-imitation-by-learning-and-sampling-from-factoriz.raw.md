---
title: "Multi-Agent Imitation by Learning and Sampling from Factorized Soft Q-Function"
authors: ["Yi-Chen Li", "Zhongxiang Ling", "Tao Jiang", "Fuxiang Zhang", "Pengyuan Wang", "Lei Yuan", "Zongzhang Zhang", "Yang Yu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RbkHARGCcH"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/5074f7d62c8caac24de92731041aecebc5af1224.pdf"
published: "2025"
categories: []
keywords: ["Multi-Agent Imitation Learning", "Energy-Based Models", "Inverse Reinforcement Learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:32+09:00"
---

# Multi-Agent Imitation by Learning and Sampling from Factorized Soft Q-Function

## Abstract
Learning from multi-agent expert demonstrations, known as Multi-Agent Imitation Learning (MAIL), provides a promising approach to sequential decision-making. However, existing MAIL methods including Behavior Cloning (BC) and Adversarial Imitation Learning (AIL) face significant challenges: BC suffers from the compounding error issue, while the very nature of adversarial optimization makes AIL prone to instability. In this work, we propose \textbf{M}ulti-\textbf{A}gent imitation by learning and sampling from \textbf{F}actor\textbf{I}zed \textbf{S}oft Q-function (MAFIS), a novel method that addresses these limitations for both online and offline MAIL settings. Built upon the single-agent IQ-Learn framework, MAFIS introduces the value decomposition network to factorize the imitation objective at agent level, thus enabling scalable training for multi-agent systems. Moreover, we observe that the soft Q-function implicitly defines the optimal policy as an energy-based model, from which we can sample actions via stochastic gradient Langevin dynamics. This allows us to estimate the gradient of the factorized optimization objective for continuous control tasks, avoiding the adversarial optimization between the soft Q-function and the policy required by prior work. By doing so, we obtain a tractable and \emph{non-adversarial} objective for both discrete and continuous multi-agent control. Experiments on common benchmarks including the discrete control tasks StarCraft Multi-Agent Challenge v2 (SMACv2), Gold Miner, and Multi Particle Environments (MPE), as well as the continuous control task Multi-Agent MuJoCo (MaMuJoCo), demonstrate that MAFIS achieves superior performance compared with baselines. Our code is available at https://github.com/LAMDA-RL/MAFIS.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Yi-Chen Li, Zhongxiang Ling, Tao Jiang, Fuxiang Zhang, Pengyuan Wang, Lei Yuan, Zongzhang Zhang, Yang Yu
- arxiv_id: 
- openreview_id: RbkHARGCcH
- anthology_id: 
- pdf_url: https://openreview.net/pdf/5074f7d62c8caac24de92731041aecebc5af1224.pdf
- published: 2025
- keywords: Multi-Agent Imitation Learning, Energy-Based Models, Inverse Reinforcement Learning
