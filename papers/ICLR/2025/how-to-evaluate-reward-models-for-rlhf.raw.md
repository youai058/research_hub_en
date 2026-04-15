---
title: "How to Evaluate Reward Models for RLHF"
authors: ["Evan Frick", "Tianle Li", "Connor Chen", "Wei-Lin Chiang", "Anastasios Nikolas Angelopoulos", "Jiantao Jiao", "Banghua Zhu", "Joseph E. Gonzalez", "Ion Stoica"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cbttLtO94Q"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/36c1a131f5c6d861080f6e1a655f78927b42578c.pdf"
published: "2025"
categories: []
keywords: ["RLHF", "RL", "Reward Model", "LLM", "Benchmark", "Dataset", "Evaluation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:58+09:00"
---

# How to Evaluate Reward Models for RLHF

## Abstract
We introduce a new benchmark for reward models that quantifies their ability to produce strong language models through RLHF (Reinforcement Learning from Human Feedback).
The gold-standard approach is to run a full RLHF training pipeline and directly probe downstream LLM performance.
However, this process is prohibitively expensive.
To address this, we build a predictive model of downstream LLM performance by evaluating the reward model on proxy tasks. 
These proxy tasks consist of a large-scale human preference and a verifiable correctness preference dataset, in which we measure 12 metrics across 12 domains.
To investigate which reward model metrics are most correlated to gold-standard RLHF outcomes, we launch an end-to-end RLHF experiment on a large-scale crowd-sourced human preference platform to view real reward model downstream performance as ground truth. 
Ultimately, we compile our data and findings into Preference Proxy Evaluations (PPE), the first reward model benchmark explicitly linked to post-RLHF real-world human preference performance, which we opensource for public use and further development at https://github.com/lmarena/PPE.

## Metadata
- venue: ICLR
- year: 2025
- authors: Evan Frick, Tianle Li, Connor Chen, Wei-Lin Chiang, Anastasios Nikolas Angelopoulos, Jiantao Jiao, Banghua Zhu, Joseph E. Gonzalez, Ion Stoica
- arxiv_id: 
- openreview_id: cbttLtO94Q
- anthology_id: 
- pdf_url: https://openreview.net/pdf/36c1a131f5c6d861080f6e1a655f78927b42578c.pdf
- published: 2025
- keywords: RLHF, RL, Reward Model, LLM, Benchmark, Dataset, Evaluation
