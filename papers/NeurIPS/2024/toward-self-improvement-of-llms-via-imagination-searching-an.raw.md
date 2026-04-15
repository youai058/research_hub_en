---
title: "Toward Self-Improvement of LLMs via Imagination, Searching, and Criticizing"
authors: ["Ye Tian", "Baolin Peng", "Linfeng Song", "Lifeng Jin", "Dian Yu", "Lei Han", "Haitao Mi", "Dong Yu"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "tPdJ2qHkOB"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b2c3d9c63136264c9f2fbafd2a34aa244f407bc5.pdf"
published: "2024"
categories: []
keywords: ["self-improving", "search", "large language models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:48+09:00"
---

# Toward Self-Improvement of LLMs via Imagination, Searching, and Criticizing

## Abstract
Despite the impressive capabilities of Large Language Models (LLMs) on various tasks, they still struggle with scenarios that involves complex reasoning and planning. Self-correction and self-learning emerge as viable solutions, employing strategies that allow LLMs to refine their outputs and learn from self-assessed rewards. Yet, the efficacy of LLMs in self-refining its response, particularly in complex reasoning and planning task, remains dubious. In this paper, we introduce AlphaLLM for the self-improvements of LLMs, which integrates Monte Carlo Tree Search (MCTS) with LLMs to establish a self-improving loop, thereby enhancing the capabilities of LLMs without additional annotations. Drawing inspiration from the success of AlphaGo, AlphaLLM addresses the unique challenges of combining MCTS with LLM for self-improvement, including data scarcity, the vastness search spaces of language tasks, and the subjective nature of feedback in language tasks. AlphaLLM is comprised of prompt synthesis component, an efficient MCTS approach tailored for language tasks, and a trio of critic models for precise feedback. Our experimental results in mathematical reasoning tasks demonstrate that AlphaLLM significantly enhances the performance of LLMs without additional annotations, showing the potential for self-improvement in LLMs.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Ye Tian, Baolin Peng, Linfeng Song, Lifeng Jin, Dian Yu, Lei Han, Haitao Mi, Dong Yu
- arxiv_id: 
- openreview_id: tPdJ2qHkOB
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b2c3d9c63136264c9f2fbafd2a34aa244f407bc5.pdf
- published: 2024
- keywords: self-improving, search, large language models
