---
title: "Large Language Models as Automated Aligners for  benchmarking  Vision-Language Models"
authors: ["Yuanfeng Ji", "Chongjian GE", "Weikai Kong", "Enze Xie", "Zhengying Liu", "Zhenguo Li", "Ping Luo"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "kZEXgtMNNo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fec2f0e416c0a90d47240e5522b34b70940223f4.pdf"
published: "2024"
categories: []
keywords: ["LLMs", "VLMs", "Benchmark"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:09+09:00"
---

# Large Language Models as Automated Aligners for  benchmarking  Vision-Language Models

## Abstract
With the advancements in Large Language Models (LLMs), Vision-Language Models (VLMs) have reached a new level of sophistication, showing notable competence in executing intricate cognition and reasoning tasks. However, existing evaluation benchmarks, primarily relying on rigid, hand-crafted datasets to measure task-specific performance, face significant limitations in assessing the alignment of these increasingly anthropomorphic models with human intelligence. In this work, we address the limitations via Auto-Bench, which delves into exploring LLMs as proficient aligners, measuring the alignment between VLMs and human intelligence and value through automatic data curation and assessment. Specifically, for data curation, Auto-Bench utilizes LLMs (e.g., GPT-4) to automatically generate a vast set of question-answer-reasoning triplets via prompting on visual symbolic representations (e.g., captions, object locations, instance relationships, and etc. The curated data closely matches human intent, owing to the extensive world knowledge embedded in LLMs. Through this pipeline, a total of 28.5K human-verified and 3,504K unfiltered question-answer-reasoning triplets have been curated, covering 4 primary abilities and 16 sub-abilities. We subsequently engage LLMs like GPT-3.5 to serve as judges, implementing the quantitative and qualitative automated assessments to facilitate a comprehensive evaluation of VLMs. Our validation results reveal that LLMs are proficient in both evaluation data curation and model assessment, achieving an average agreement rate of 85%. We envision Auto-Bench as a flexible, scalable, and comprehensive benchmark for evaluating the evolving sophisticated VLMs.

## Metadata
- venue: ICLR
- year: 2024
- authors: Yuanfeng Ji, Chongjian GE, Weikai Kong, Enze Xie, Zhengying Liu, Zhenguo Li, Ping Luo
- arxiv_id: 
- openreview_id: kZEXgtMNNo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fec2f0e416c0a90d47240e5522b34b70940223f4.pdf
- published: 2024
- keywords: LLMs, VLMs, Benchmark
