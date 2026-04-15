---
title: "Searching for Optimal Solutions with LLMs via Bayesian Optimization"
authors: ["Dhruv Agarwal", "Manoj Ghuhan Arivazhagan", "Rajarshi Das", "Sandesh Swamy", "Sopan Khosla", "Rashmi Gangadharaiah"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "aVfDrl7xDV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/aa018399db623960bf609f226ba279993bf64c3b.pdf"
published: "2025"
categories: []
keywords: ["search", "optimization", "LLMs", "test-time steering", "bayesian optimization", "reasoning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:03+09:00"
---

# Searching for Optimal Solutions with LLMs via Bayesian Optimization

## Abstract
Scaling test-time compute to search for optimal solutions is an important step towards building generally-capable language models that can reason. Recent work, however, shows that tasks of varying complexity require distinct search strategies to solve optimally, thus making it challenging to design a one-size-fits-all approach. Prior solutions either attempt to predict task difficulty to select the optimal search strategy, often infeasible in practice, or use a static, pre-defined strategy, e.g., repeated parallel sampling or greedy sequential search, which is sub-optimal. In this work, we argue for an alternative view using the probabilistic framework of Bayesian optimization (BO), where the search strategy is adapted dynamically based on the evolving uncertainty estimates of solutions as search progresses. To this end, we introduce Bayesian-OPRO (BOPRO)––a generalization of a recent method for in-context optimization, which iteratively samples from new proposal distributions by modifying the prompt to the LLM with a subset of its previous generations selected to explore or exploit different parts of the search space. We evaluate our method on word search, molecule optimization, and a joint hypothesis+program search task using a 1-D version of the challenging Abstraction and Reasoning Corpus (1D-ARC). Our results show that BOPRO outperforms all baselines in word search (≥10 points) and molecule optimization (higher quality and 17% fewer invalid molecules), but trails a best-k prompting strategy in program search. Our analysis reveals that despite the ability to balance exploration and exploitation using BOPRO, failure is likely due to the inability of code representation models in distinguishing sequences with low edit-distances.

## Metadata
- venue: ICLR
- year: 2025
- authors: Dhruv Agarwal, Manoj Ghuhan Arivazhagan, Rajarshi Das, Sandesh Swamy, Sopan Khosla, Rashmi Gangadharaiah
- arxiv_id: 
- openreview_id: aVfDrl7xDV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/aa018399db623960bf609f226ba279993bf64c3b.pdf
- published: 2025
- keywords: search, optimization, LLMs, test-time steering, bayesian optimization, reasoning
