---
title: "One Prompt is not Enough: Automated Construction of a Mixture-of-Expert Prompts"
authors: ["Ruochen Wang", "Sohyun An", "Minhao Cheng", "Tianyi Zhou", "Sung Ju Hwang", "Cho-Jui Hsieh"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "edHLN40DWu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/54ff0b135e6b5630849ddfa72a66d987e7d0dff9.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:14+09:00"
---

# One Prompt is not Enough: Automated Construction of a Mixture-of-Expert Prompts

## Abstract
Large Language Models (LLMs) exhibit strong generalization capabilities to novel tasks when prompted with language instructions and in-context demos. Since this ability sensitively depends on the quality of prompts, various methods have been explored to automate the instruction design. While these methods demonstrated promising results, they also restricted the searched prompt to one instruction. Such simplification significantly limits their capacity, as a single demo-free instruction might not be able to cover the entire complex problem space of the targeted task. To alleviate this issue, we adopt the Mixture-of-Expert paradigm and divide the problem space into a set of sub-regions; Each sub-region is governed by a specialized expert, equipped with both an instruction and a set of demos. A two-phase process is developed to construct the specialized expert for each region: (1) demo assignment: Inspired by the theoretical connection between in-context learning and kernel regression, we group demos into experts based on their semantic similarity; (2) instruction assignment: A region-based joint search of an instruction per expert complements the demos assigned to it, yielding a synergistic effect. The resulting method, codenamed Mixture-of-Prompts (MoP), achieves an average win rate of 81% against prior arts across several major benchmarks.

## Metadata
- venue: ICML
- year: 2024
- authors: Ruochen Wang, Sohyun An, Minhao Cheng, Tianyi Zhou, Sung Ju Hwang, Cho-Jui Hsieh
- arxiv_id: 
- openreview_id: edHLN40DWu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/54ff0b135e6b5630849ddfa72a66d987e7d0dff9.pdf
- published: 2024
