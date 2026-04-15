---
title: "Enhancing Instruction Following of LLMs via Activation Steering with Dynamic Rejection"
authors: ["Minjae Kang", "Jaehyung Kim"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "OpuPBNcQwe"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2c6ad4fa6baab0923567a3ea3e8f6df7c26eb6a7.pdf"
published: "2026"
categories: []
keywords: ["Large Language Models", "LLM Steering", "Instruction following", "Activation engineering"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:35+09:00"
---

# Enhancing Instruction Following of LLMs via Activation Steering with Dynamic Rejection

## Abstract
Large Language Models (LLMs), despite advances in instruction tuning, often fail to follow complex user instructions. Activation steering techniques aim to mitigate this by manipulating model internals, but have a potential risk of oversteering, where excessive emphasis on the instruction degrades task accuracy and overall text quality. To address this, we introduce DIRECTER (Dynamic rejection steering), a novel steering method that dynamically modulates steering strength by scaling the KV cache without extra dataset. DIRECTER couples steering with a plausibility-guided decoding loop, which adaptively adjusts steering strength at each step by comparing the steered output distribution to the original. If the steered output is deemed implausible, steering strength is progressively weakened. This strength modulation is guided by a lightweight, one-time attention sensitivity analysis that ranks layers by their influence on model representations. Extensive evaluations show that DIRECTER significantly enhances instruction-following capabilities across diverse benchmarks, improving accuracy by up to 6.5% over baselines without the common trade-offs in generation quality or task fidelity. The proposed dynamic, plausibility-guided control during activation steering further demonstrates its potential as a general mechanism for mitigating oversteering that is compatible with existing baselines.

## Metadata
- venue: ICLR
- year: 2026
- authors: Minjae Kang, Jaehyung Kim
- arxiv_id: 
- openreview_id: OpuPBNcQwe
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2c6ad4fa6baab0923567a3ea3e8f6df7c26eb6a7.pdf
- published: 2026
- keywords: Large Language Models, LLM Steering, Instruction following, Activation engineering
