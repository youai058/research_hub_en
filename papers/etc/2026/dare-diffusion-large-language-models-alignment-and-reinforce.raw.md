---
title: "DARE: Diffusion Large Language Models Alignment and Reinforcement Executor"
authors: ["Jingyi Yang", "Yuxian Jiang", "Xuhao Hu", "Shuang Cheng", "Biqing Qi", "Jing Shao"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2604.04215"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2604.04215v1"
published: "2026-04-05"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:13:54+09:00"
---

# DARE: Diffusion Large Language Models Alignment and Reinforcement Executor

## Abstract
Diffusion large language models (dLLMs) are emerging as a compelling alternative to dominant autoregressive models, replacing strictly sequential token generation with iterative denoising and parallel generation dynamics. However, their open-source ecosystem remains fragmented across model families and, in particular, across post-training pipelines, where reinforcement learning objectives, rollout implementations and evaluation scripts are often released as paper-specific codebases. This fragmentation slows research iteration, raises the engineering burden of reproduction, and makes fair comparison across algorithms difficult. We present \textbf{DARE} (\textbf{d}LLMs \textbf{A}lignment and \textbf{R}einforcement \textbf{E}xecutor), an open framework for post-training and evaluating dLLMs. Built on top of verl~\cite{sheng2024hybridflow} and OpenCompass~\cite{2023opencompass}, DARE unifies supervised fine-tuning, parameter-efficient fine-tuning, preference optimization, and dLLM-specific reinforcement learning under a shared execution stack for both masked and block diffusion language models. Across representative model families including LLaDA, Dream, SDAR, and LLaDA2.x, DARE provides broad algorithmic coverage, reproducible benchmark evaluation, and practical acceleration. Extensive empirical results position that DARE serves as a reusable research substrate for developing, comparing, and deploying post-training methods for current and emerging dLLMs.

## Metadata
- venue: arXiv
- year: 2026
- authors: Jingyi Yang, Yuxian Jiang, Xuhao Hu, Shuang Cheng, Biqing Qi, Jing Shao
- arxiv_id: 2604.04215
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2604.04215v1
- published: 2026-04-05
