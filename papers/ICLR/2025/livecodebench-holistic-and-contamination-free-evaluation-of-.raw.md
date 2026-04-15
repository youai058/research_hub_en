---
title: "LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code"
authors: ["Naman Jain", "King Han", "Alex Gu", "Wen-Ding Li", "Fanjia Yan", "Tianjun Zhang", "Sida Wang", "Armando Solar-Lezama", "Koushik Sen", "Ion Stoica"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "chfJJYC3iL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e4619cf824fc3a958f2d274337715f6c670e7240.pdf"
published: "2025"
categories: []
keywords: ["Code LLMs; Evaluation; Contaminationl; Overfitting"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:07+09:00"
---

# LiveCodeBench: Holistic and Contamination Free Evaluation of Large Language Models for Code

## Abstract
Large Language Models (LLMs) applied to code-related applications have emerged as a prominent field, attracting significant interest from academia and industry. However, as new and improved LLMs are developed, existing evaluation benchmarks (e.g., HumanEvla, MBPP) are no longer sufficient for assessing their capabilities suffering from data contamination, overfitting, saturation, and focus on merely code generation. In this work, we propose LiveCodeBench, a comprehensive and contamination-free evaluation of LLMs for code, which collects new problems over time from contests across three competition platforms, Leetcode, Atcoder, and Codeforces. Notably, our benchmark also focuses on a broader range of code-related capabilities, such as self-repair, code execution, and test output prediction, beyond just code generation. Currently, LiveCodeBench hosts over six hundred coding problems that were published between May 2023 and Aug 2024. We evaluate over 50 LLMs on LiveCodeBench (LCB for brevity) presenting the largest evaluation study of code LLMs on competition problems. Based on the study, we present novel empirical findings on contamination, overfitting, and holistic evaluations. We demonstrate that time-segmented evaluations serve as a robust approach to evade contamination; they are successful at detecting contamination across a wide range of open and closed models including GPT-4O, Claude, Deepseek, and Codestral. Next, we highlight overfitting and saturation of traditional coding benchmarks like HumanEvla and demonstrate LCB allows more reliable evaluations. Finally, our holistic evaluation scenarios allow for measuring the different capabilities of programming agents in isolation.

## Metadata
- venue: ICLR
- year: 2025
- authors: Naman Jain, King Han, Alex Gu, Wen-Ding Li, Fanjia Yan, Tianjun Zhang, Sida Wang, Armando Solar-Lezama, Koushik Sen, Ion Stoica
- arxiv_id: 
- openreview_id: chfJJYC3iL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e4619cf824fc3a958f2d274337715f6c670e7240.pdf
- published: 2025
- keywords: Code LLMs; Evaluation; Contaminationl; Overfitting
