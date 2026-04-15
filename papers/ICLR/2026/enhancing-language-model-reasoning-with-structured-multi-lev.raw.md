---
title: "Enhancing Language Model Reasoning with Structured Multi-Level Modeling"
authors: ["Siheng Xiong", "Ali Payani", "Faramarz Fekri"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "PlkzZhqBCd"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c1aa8a110cc65a27b3895fdd66f50c70fd6b0cef.pdf"
published: "2026"
categories: []
keywords: ["Chain-of-Thought reasoning", "Direct Preference Optimization", "Process supervision", "Twisted Sequential Monte Carlo", "Large language models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:40+09:00"
---

# Enhancing Language Model Reasoning with Structured Multi-Level Modeling

## Abstract
Inference-time scaling enhances a model’s reasoning by extending its chain-of-thought (CoT). However, existing approaches typically rely on a single policy trained with outcome-reward reinforcement learning (RL), which often suffers from long-horizon plan failures where the implicit plan drifts from valid strategies, especially for small LMs with limited capacity. To address this, we propose Multi-Level Reasoning (MLR), which reformulates long-CoT generation as a two-level stochastic process. A high-level planner generates structured step descriptors specifying both the reasoning mode and the semantic subgoal. The low-level executor then produces detailed reasoning conditioned on these descriptors, forming an alternating plan--execute loop. To maintain scalability, we adopt a minimal design where the base model serves as the low-level policy and a lightweight LoRA module implements the high-level policy. For training, we observe that outcome-reward RL provides sparse and delayed feedback for long trajectories (e.g., several thousand tokens), hindering credit assignment. We therefore introduce iterative Step-DPO, a process-level preference optimization scheme that leverages Twisted Sequential Monte Carlo (TSMC) to provide scalable stepwise supervision. This yields more effective training, improved stability, and higher accuracy. Extensive experiments on challenging math, science, and logical reasoning benchmarks show that, under the same reduced data budget (10% SFT and 5% preference relative to the DeepSeek-R1 distillation setup), MLR outperforms both SFT-based distillation and strong RL/preference-optimization baselines across multiple base models and tasks. Moreover, MLR exhibits slower performance degradation on long-horizon reasoning, demonstrating stronger robustness under extended CoT generation.

## Metadata
- venue: ICLR
- year: 2026
- authors: Siheng Xiong, Ali Payani, Faramarz Fekri
- arxiv_id: 
- openreview_id: PlkzZhqBCd
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c1aa8a110cc65a27b3895fdd66f50c70fd6b0cef.pdf
- published: 2026
- keywords: Chain-of-Thought reasoning, Direct Preference Optimization, Process supervision, Twisted Sequential Monte Carlo, Large language models
