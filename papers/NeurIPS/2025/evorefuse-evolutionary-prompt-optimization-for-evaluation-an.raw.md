---
title: "EVOREFUSE: Evolutionary Prompt Optimization for Evaluation and Mitigation of LLM Over-Refusal to Pseudo-Malicious Instructions"
authors: ["Xiaorui Wu", "Fei Li", "Xiaofeng Mao", "Xin Zhang", "Li Zheng", "Yuxiang Peng", "Chong Teng", "Donghong Ji", "Zhuang Li"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dbq6NZfi3c"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b17358ed78b9c539e109975756d1b8b9045b242f.pdf"
published: "2025"
categories: []
keywords: ["Prompt Optimization", "LLM Over-Refusal", "Data Synthesis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:47+09:00"
---

# EVOREFUSE: Evolutionary Prompt Optimization for Evaluation and Mitigation of LLM Over-Refusal to Pseudo-Malicious Instructions

## Abstract
Large language models (LLMs) frequently refuse to respond to pseudo-malicious instructions: semantically harmless input queries triggering unnecessary LLM refusals due to conservative safety alignment, significantly impairing user experience. Collecting such instructions is crucial for evaluating and mitigating over-refusals, but existing instruction curation methods, like manual creation or instruction rewriting, either lack scalability or fail to produce sufficiently diverse and effective refusal-inducing prompts. To address these limitations, we introduce EVOREFUSE, a prompt optimization approach that generates diverse pseudo-malicious instructions consistently eliciting confident refusals across LLMs. EVOREFUSE employs an evolutionary algorithm exploring the instruction space in more diverse directions than existing methods via mutation strategies and recombination, and iteratively evolves seed instructions to maximize evidence lower bound on LLM refusal probability. Using EVOREFUSE, we create two novel datasets: EVOREFUSE-TEST, a benchmark of 582 pseudo-malicious instructions that outperforms the next-best benchmark with 85.34% higher average refusal triggering rate across 9 LLMs without a safety-prior system prompt, 34.86% greater lexical diversity, and 40.03% improved LLM response confidence scores; and EVOREFUSE-ALIGN, which provides 3,000 pseudo-malicious instructions with responses for supervised and preference-based alignment training. With supervised fine-tuning on EVOREFUSE-ALIGN, LLAMA3.1-8B-INSTRUCT achieves up to 29.85% fewer over-refusals than models trained on the second-best alignment dataset, without compromising safety. Our analysis with EVOREFUSE-TEST reveals models trigger over-refusals by overly focusing on sensitive keywords while ignoring broader context. Our code and datasets are available at https://github.com/FishT0ucher/EVOREFUSE .

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Xiaorui Wu, Fei Li, Xiaofeng Mao, Xin Zhang, Li Zheng, Yuxiang Peng, Chong Teng, Donghong Ji, Zhuang Li
- arxiv_id: 
- openreview_id: dbq6NZfi3c
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b17358ed78b9c539e109975756d1b8b9045b242f.pdf
- published: 2025
- keywords: Prompt Optimization, LLM Over-Refusal, Data Synthesis
