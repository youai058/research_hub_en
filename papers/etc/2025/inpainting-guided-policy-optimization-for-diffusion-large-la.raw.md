---
title: "Inpainting-Guided Policy Optimization for Diffusion Large Language Models"
authors: ["Siyan Zhao", "Mengchen Liu", "Jing Huang", "Miao Liu", "Chenyu Wang", "Bo Liu", "Yuandong Tian", "Guan Pang", "Sean Bell", "Aditya Grover", "Feiyu Chen"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.10396"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.10396v1"
published: "2025-09-12"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:26+09:00"
---

# Inpainting-Guided Policy Optimization for Diffusion Large Language Models

## Abstract
Masked diffusion large language models (dLLMs) are emerging as promising alternatives to autoregressive LLMs, offering competitive performance while supporting unique generation capabilities such as inpainting. We explore how inpainting can inform RL algorithm design for dLLMs. Aligning LLMs with reinforcement learning faces an exploration challenge: sparse reward signals and sample waste when models fail to discover correct solutions. While this inefficiency affects LLMs broadly, dLLMs offer a distinctive opportunity--their inpainting ability can guide exploration. We introduce IGPO (Inpainting Guided Policy Optimization), an RL framework that strategically inserts partial ground-truth reasoning traces during online sampling. Unlike providing full solutions, inpainting steers exploration toward promising trajectory spaces while preserving self-generated reasoning, bridging supervised fine-tuning and reinforcement learning. We apply IGPO to group-based optimization methods such as GRPO, where exploration failures cause zero advantages and gradients. IGPO restores meaningful gradients while improving sample efficiency. We also propose supervised fine-tuning on synthetically rewritten concise traces that better align with dLLM generation patterns. With additional techniques including entropy-based filtering, our training recipe yields substantial gains across three mathematical benchmarks--GSM8K, Math500, and AMC--achieving new state-of-the-art results for full-attention masked dLLMs.

## Metadata
- venue: arXiv
- year: 2025
- authors: Siyan Zhao, Mengchen Liu, Jing Huang, Miao Liu, Chenyu Wang, Bo Liu, Yuandong Tian, Guan Pang, Sean Bell, Aditya Grover, Feiyu Chen
- arxiv_id: 2509.10396
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.10396v1
- published: 2025-09-12
