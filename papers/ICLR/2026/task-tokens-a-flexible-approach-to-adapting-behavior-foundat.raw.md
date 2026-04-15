---
title: "Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models"
authors: ["Ron Vainshtein", "Zohar Rimon", "Shie Mannor", "Chen Tessler"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "6T3wJQhvc3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b60b5ad799c0ee8bb4d10ab2e738490a3ced12c4.pdf"
published: "2026"
categories: []
keywords: ["Reinforcement Learning", "Hierarchial Reinforcement Learning", "Behavior Foundation Models", "Humanoid Control"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:11+09:00"
---

# Task Tokens: A Flexible Approach to Adapting Behavior Foundation Models

## Abstract
Recent advancements in imitation learning for robotic control have led to transformer-based behavior foundation models (BFMs) that enable multi-modal, human-like control for humanoid agents. These models generate solutions when conditioned on high-level goals or prompts, for example, walking to a coordinate when conditioned on the position of the robot's pelvis. While excelling at zero-shot generation of robust behaviors, BFMs often require meticulous prompt engineering for specific tasks, potentially yielding suboptimal results. In this work, we introduce ``Task Tokens'' - a method to effectively tailor BFMs to specific tasks while preserving their flexibility. Our approach integrates naturally within the transformer architecture of BFMs. Task Tokens trains a task-specific encoder (tokenizer), with the original BFM remaining untouched. Our method reduces trainable parameters per task by up to $\times 125$ and converges up to $\times 6$ faster compared to standard baselines. In addition, by keeping the original BFM unchanged, Task Tokens enables utilizing the pre-existing encoders. This allows incorporating user-defined priors, balancing reward design and prompt engineering.
We demonstrate Task Tokens' efficacy across various tasks, including out-of-distribution scenarios, and show their compatibility with other prompting modalities. Our results suggest that Task Tokens offer a promising approach for adapting BFMs to specific control tasks while retaining their generalization capabilities.

## Metadata
- venue: ICLR
- year: 2026
- authors: Ron Vainshtein, Zohar Rimon, Shie Mannor, Chen Tessler
- arxiv_id: 
- openreview_id: 6T3wJQhvc3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b60b5ad799c0ee8bb4d10ab2e738490a3ced12c4.pdf
- published: 2026
- keywords: Reinforcement Learning, Hierarchial Reinforcement Learning, Behavior Foundation Models, Humanoid Control
