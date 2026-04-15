---
title: "Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning in Robotics"
authors: ["Dongyoung Kim", "Sumin Park", "Huiwon Jang", "Jinwoo Shin", "Jaehyung Kim", "Younggyo Seo"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "N2bLuwofZ0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/28f2bd82b713f7bb9565dbe9321b8b6fb4782dc3.pdf"
published: "2025"
categories: []
keywords: ["LLM", "Reasoning", "RL", "Robot domain"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:49+09:00"
---

# Robot-R1: Reinforcement Learning for Enhanced Embodied Reasoning in Robotics

## Abstract
Large Vision-Language Models (LVLMs) have recently shown great promise in advancing robotics by combining embodied reasoning with robot control. A common approach involves training on embodied reasoning tasks related to robot control using Supervised Fine-Tuning (SFT). However, SFT datasets are often heuristically constructed and not explicitly optimized for improving robot control. Furthermore, SFT often leads to issues such as catastrophic forgetting and reduced generalization performance. To address these limitations, we introduce Robot-R1, a novel framework that leverages reinforcement learning to enhance embodied reasoning specifically for robot control. Robot-R1 learns to predict the next keypoint state required for task completion, conditioned on the current scene image and environment metadata derived from expert demonstrations. Inspired by the DeepSeek-R1 learning approach, Robot-R1 samples reasoning-based responses and reinforces those that lead to more accurate predictions. Our experiments show that models trained with Robot-R1 outperform SFT methods on embodied reasoning tasks. Despite having only 7B parameters, Robot-R1 even surpasses GPT-4o on reasoning tasks related to low-level action control, such as spatial and movement reasoning.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Dongyoung Kim, Sumin Park, Huiwon Jang, Jinwoo Shin, Jaehyung Kim, Younggyo Seo
- arxiv_id: 
- openreview_id: N2bLuwofZ0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/28f2bd82b713f7bb9565dbe9321b8b6fb4782dc3.pdf
- published: 2025
- keywords: LLM, Reasoning, RL, Robot domain
