---
title: "JudgeLM: Fine-tuned Large Language Models are Scalable Judges"
authors: ["Lianghui Zhu", "Xinggang Wang", "Xinlong Wang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xsELpEPn4A"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4c4ba67c698460cb4e4cdf26f4af0388a3b992b7.pdf"
published: "2025"
categories: []
keywords: ["LLM Judging"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:57+09:00"
---

# JudgeLM: Fine-tuned Large Language Models are Scalable Judges

## Abstract
Evaluating Large Language Models (LLMs) in open-ended scenarios is challenging because existing benchmarks and metrics can not measure them comprehensively. To address this problem, we propose to fine-tune LLMs as scalable judges (JudgeLM) to evaluate LLMs efficiently and effectively in open-ended benchmarks. We first propose a comprehensive, large-scale, high-quality dataset containing task seeds, LLMs-generated answers, and GPT-4-generated judgments for fine-tuning high-performance judges, as well as a new benchmark for evaluating the judges. We train JudgeLM at different scales from 7B, 13B, to 33B parameters, and conduct a systematic analysis of its capabilities and behaviors. We then analyze the key biases in fine-tuning LLM as a judge and consider them as position bias, knowledge bias, and format bias. To address these issues, JudgeLM introduces a bag of techniques including swap augmentation, reference support, and reference drop, which clearly enhance the judge's performance. JudgeLM obtains the state-of-the-art judge performance on both the existing PandaLM benchmark and our proposed new benchmark. Our JudgeLM is efficient and the JudgeLM-7B only needs 3 minutes to judge 5K samples with 8 A100 GPUs. JudgeLM obtains high agreement with the teacher judge, achieving an agreement exceeding 90% that even surpasses human-to-human agreement. JudgeLM also demonstrates extended capabilities in being judges of the single answer, multimodal models, multiple answers, multi-turn chat, etc.

## Metadata
- venue: ICLR
- year: 2025
- authors: Lianghui Zhu, Xinggang Wang, Xinlong Wang
- arxiv_id: 
- openreview_id: xsELpEPn4A
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4c4ba67c698460cb4e4cdf26f4af0388a3b992b7.pdf
- published: 2025
- keywords: LLM Judging
