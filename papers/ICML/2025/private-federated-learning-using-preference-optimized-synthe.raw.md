---
title: "Private Federated Learning using Preference-Optimized Synthetic Data"
authors: ["Charlie Hou", "Mei-Yu Wang", "Yige Zhu", "Daniel Lazar", "Giulia Fanti"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ZuaU2bYzlc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b96e11fa2d46e60733e7627944e980d0739469ce.pdf"
published: "2025"
categories: []
keywords: ["Differential privacy", "large language models", "synthetic data", "federated learning", "preference optimization", "reinforcement learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:22+09:00"
---

# Private Federated Learning using Preference-Optimized Synthetic Data

## Abstract
In practical settings, differentially private federated learning (DP-FL) is the dominant method for training models from private, on-device client data. Recent work has suggested that DP-FL may be enhanced or outperformed by methods that use DP synthetic data  (Wu et al., 2024; Hou et al., 2024). The primary algorithms for generating DP synthetic data for FL applications require careful prompt engineering based on public information and/or iterative private client feedback. Our key insight is that the private client feedback collected by prior DP synthetic data methods (Hou et al., 2024; Xie et al., 2024)  can be viewed as an RL reward. Our algorithm, Policy Optimization for Private Data (POPri) harnesses client feedback using policy optimization algorithms such as Direct Preference Optimization (DPO) to fine-tune LLMs to generate high-quality DP synthetic data. To evaluate POPri, we release LargeFedBench, a new federated text benchmark for uncontaminated LLM evaluations on federated client data. POPri closes the gap in performance between the fully-private and non-private settings by up to 58%, compared to 28% for prior synthetic data methods, and 3% for state-of-the-art DP federated learning methods. The code and data are available at https://github.com/meiyuw/POPri.

## Metadata
- venue: ICML
- year: 2025
- authors: Charlie Hou, Mei-Yu Wang, Yige Zhu, Daniel Lazar, Giulia Fanti
- arxiv_id: 
- openreview_id: ZuaU2bYzlc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b96e11fa2d46e60733e7627944e980d0739469ce.pdf
- published: 2025
- keywords: Differential privacy, large language models, synthetic data, federated learning, preference optimization, reinforcement learning
