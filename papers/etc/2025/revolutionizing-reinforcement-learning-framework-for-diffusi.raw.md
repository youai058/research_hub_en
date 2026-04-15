---
title: "Revolutionizing Reinforcement Learning Framework for Diffusion Large Language Models"
authors: ["Yinjie Wang", "Ling Yang", "Bowen Li", "Ye Tian", "Ke Shen", "Mengdi Wang"]
venue: "arXiv"
year: 2025
venue_class: "etc"
arxiv_id: "2509.06949"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2509.06949v1"
published: "2025-09-08"
categories: ["cs.CL"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:17:14+09:00"
---

# Revolutionizing Reinforcement Learning Framework for Diffusion Large Language Models

## Abstract
We propose TraceRL, a trajectory-aware reinforcement learning framework for diffusion language models (DLMs) that incorporates preferred inference trajectory into post-training, and is applicable across different architectures. Equipped with a diffusion-based value model that enhances training stability, we demonstrate improved reasoning performance on complex math and coding tasks. Besides, it can also be applied to adapt block-specific models to larger blocks, which improves sampling flexibility. Employing TraceRL, we derive a series of state-of-the-art diffusion language models, namely TraDo. Although smaller than 7B-scale AR models, TraDo-4B-Instruct still consistently outperforms them across complex math reasoning tasks. TraDo-8B-Instruct achieves relative accuracy improvements of 6.1% over Qwen2.5-7B-Instruct and 51.3% over Llama3.1-8B-Instruct on mathematical reasoning benchmarks. Through curriculum learning, we also derive the first long-CoT DLM, outperforming Qwen2.5-7B-Instruct on MATH500 with an 18.1% relative accuracy gain. To facilitate reproducible research and practical applications, we release a comprehensive open-source framework for building, training, and deploying diffusion LLMs across diverse architectures. The framework integrates accelerated KV-cache techniques and inference engines for both inference and reinforcement learning, and includes implementations of various supervised fine-tuning and RL methods for mathematics, coding, and general tasks. Code and Models: https://github.com/Gen-Verse/dLLM-RL

## Metadata
- venue: arXiv
- year: 2025
- authors: Yinjie Wang, Ling Yang, Bowen Li, Ye Tian, Ke Shen, Mengdi Wang
- arxiv_id: 2509.06949
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2509.06949v1
- published: 2025-09-08
