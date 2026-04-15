---
title: "CLAWS:Creativity detection for LLM-generated solutions using Attention Window of Sections"
authors: ["Keuntae Kim", "Eunhye Jeong", "Sehyeon Lee", "Seohee Yoon", "Yong Suk Choi"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "yiSoT2pHfk"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1def4784a6e1f2045d4c683ea291426ad146a305.pdf"
published: "2025"
categories: []
keywords: ["llm", "reasoning", "math", "creativity", "hallucination"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:49+09:00"
---

# CLAWS:Creativity detection for LLM-generated solutions using Attention Window of Sections

## Abstract
Recent advances in enhancing the reasoning ability of Large Language Models (LLMs) have been remarkably successful. LLMs trained with Reinforcement Learning (RL) for reasoning demonstrate strong performance in challenging tasks such as mathematics and coding, even with relatively small model sizes. However, despite these impressive improvements in task accuracy, the assessment of creativity in LLM generations has been largely overlooked in reasoning tasks, in contrast to writing tasks. The lack of research on creativity assessment in reasoning primarily stems from two challenges: (1) the difficulty of defining the range of creativity, and (2) the necessity of human evaluation in the assessment process. To address these challenges, we propose CLAWS, a novel method that defines and classifies mathematical solutions into Typical, Creative, and Hallucinated categories without human evaluation, by leveraging attention weights across prompt sections and output. CLAWS outperforms five existing white-box detection methods—Perplexity, Logit Entropy, Window Entropy, Hidden Score, and Attention Score—on five 7–8B math RL models (DeepSeek, Qwen, Mathstral, OpenMath2, and Oreal). We validate CLAWS on 4,545 math problems collected from 181 math contests (A(J)HSME, AMC, AIME). Our code is available at https://github.com/kkt94/CLAWS.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Keuntae Kim, Eunhye Jeong, Sehyeon Lee, Seohee Yoon, Yong Suk Choi
- arxiv_id: 
- openreview_id: yiSoT2pHfk
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1def4784a6e1f2045d4c683ea291426ad146a305.pdf
- published: 2025
- keywords: llm, reasoning, math, creativity, hallucination
