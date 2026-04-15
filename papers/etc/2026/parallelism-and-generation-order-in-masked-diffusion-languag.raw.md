---
title: "Parallelism and Generation Order in Masked Diffusion Language Models: Limits Today, Potential Tomorrow"
authors: ["Yangyang Zhong", "Yanmei Gu", "Zhengqing Zang", "Xiaomeng Li", "Yuqi Ding", "Xibei Jia", "Yuting Shen", "Zhenzhong Lan", "Liwang Zhu", "Weiping Liu", "Junlin Zhou", "Haisheng Liu", "Zhong Xin Yu", "Pengxin Luo", "Donglian Qi", "Yunfeng Yan", "Junbo Zhao"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2601.15593"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2601.15593v2"
published: "2026-01-22"
categories: ["cs.CL", "cs.AI", "cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:21+09:00"
---

# Parallelism and Generation Order in Masked Diffusion Language Models: Limits Today, Potential Tomorrow

## Abstract
Masked Diffusion Language Models (MDLMs) promise parallel token generation and arbitrary-order decoding, yet it remains unclear to what extent current models truly realize these capabilities. We characterize MDLM behavior along two dimensions -- parallelism strength and generation order -- using Average Finalization Parallelism (AFP) and Kendall's tau. We evaluate eight mainstream MDLMs (up to 100B parameters) on 58 benchmarks spanning knowledge, reasoning, and programming. The results show that MDLMs still lag behind comparably sized autoregressive models, mainly because parallel probabilistic modeling weakens inter-token dependencies. Meanwhile, MDLMs exhibit adaptive decoding behavior: their parallelism and generation order vary significantly with the task domain, the stage of reasoning, and whether the output is correct. On tasks that require "backward information" (e.g., Sudoku), MDLMs adopt a solution order that tends to fill easier Sudoku blanks first, highlighting their advantages. Finally, we provide theoretical motivation and design insights supporting a Generate-then-Edit paradigm, which mitigates dependency loss while retaining the efficiency of parallel decoding.

## Metadata
- venue: arXiv
- year: 2026
- authors: Yangyang Zhong, Yanmei Gu, Zhengqing Zang, Xiaomeng Li, Yuqi Ding, Xibei Jia, Yuting Shen, Zhenzhong Lan, Liwang Zhu, Weiping Liu, Junlin Zhou, Haisheng Liu, Zhong Xin Yu, Pengxin Luo, Donglian Qi, Yunfeng Yan, Junbo Zhao
- arxiv_id: 2601.15593
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2601.15593v2
- published: 2026-01-22
