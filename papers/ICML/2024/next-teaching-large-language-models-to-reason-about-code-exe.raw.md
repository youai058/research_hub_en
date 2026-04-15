---
title: "NExT: Teaching Large Language Models to Reason about Code Execution"
authors: ["Ansong Ni", "Miltiadis Allamanis", "Arman Cohan", "Yinlin Deng", "Kensen Shi", "Charles Sutton", "Pengcheng Yin"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "B1W712hMBi"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a415d96356e8fc8bcc1dfd9b9d0cedbd3b815dbf.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:31+09:00"
---

# NExT: Teaching Large Language Models to Reason about Code Execution

## Abstract
A fundamental skill among human developers is the ability to understand and reason about program execution. As an example, a programmer can mentally simulate code execution in natural language to debug and repair code (aka. rubber duck debugging). However, large language models (LLMs) of code are typically trained on the surface textual form of programs, thus may lack a semantic understanding of how programs execute at run-time. To address this issue, we propose NExT, a method to teach LLMs to inspect the execution traces of programs (variable states of executed lines) and reason about their run-time behavior through chain-of-thought (CoT) rationales. Specifically, NExT uses self-training to bootstrap a synthetic training set of execution-aware rationales that lead to correct task solutions (e.g., fixed programs) without laborious manual annotation. Experiments on program repair tasks based on MBPP and HumanEval demonstrate that NExT improves the fix rate of a PaLM 2 model, by 26.1% and 10.3% absolute, respectively, with significantly improved rationale quality as verified by automated metrics and human raters. Our model can also generalize to scenarios where program traces are absent at test-time.

## Metadata
- venue: ICML
- year: 2024
- authors: Ansong Ni, Miltiadis Allamanis, Arman Cohan, Yinlin Deng, Kensen Shi, Charles Sutton, Pengcheng Yin
- arxiv_id: 
- openreview_id: B1W712hMBi
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a415d96356e8fc8bcc1dfd9b9d0cedbd3b815dbf.pdf
- published: 2024
