---
title: "Rethinking Code Similarity for Automated Algorithm Design with LLMs"
authors: ["Rui Zhang", "Zhichao Lu"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "HIUqeO9OOr"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b3f87bd3f037e5f575a59fba9de10d75548bf22b.pdf"
published: "2026"
categories: []
keywords: ["Algorithm Similarity", "Automated Algorithm Design", "Large Language Model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:34+09:00"
---

# Rethinking Code Similarity for Automated Algorithm Design with LLMs

## Abstract
The rise of Large Language Model-based Automated Algorithm Design (LLM-AAD) has transformed algorithm development by autonomously generating code implementations of expert-level algorithms. Unlike traditional expert-driven algorithm development, in the LLM-AAD paradigm, the algorithm's ideas are often implicitly embedded in the generated code. Therefore, assessing algorithmic similarity directly from code, distinguishing genuine algorithmic innovation from mere syntactic variation, becomes essential. While code similarity metrics exist, they fail to capture algorithmic similarity, as they focus on surface-level syntax or output equivalence rather than problem-solving behavior.

We propose BehaveSim, a novel method to measure algorithmic similarity through the lens of problem-solving trajectories (PSTrajs)—sequences of intermediate solutions produced during execution. By quantifying the alignment between PSTrajs using dynamic time warping (DTW), BehaveSim distinguishes algorithms with divergent logic despite syntactic or output-level similarities. We demonstrate its utility in two key applications: (i) Enhancing LLM-AAD: Integrating BehaveSim into existing LLM-AAD frameworks (e.g., FunSearch, EoH) promotes behavioral diversity, significantly improving performance on three AAD tasks. (ii) Algorithm analysis: BehaveSim clusters generated algorithms by behavior, enabling systematic analysis of problem-solving strategies—a crucial tool for the growing ecosystem of AI-generated algorithms. Data and code of this work are open-sourced at https://github.com/RayZhhh/behavesim.

## Metadata
- venue: ICLR
- year: 2026
- authors: Rui Zhang, Zhichao Lu
- arxiv_id: 
- openreview_id: HIUqeO9OOr
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b3f87bd3f037e5f575a59fba9de10d75548bf22b.pdf
- published: 2026
- keywords: Algorithm Similarity, Automated Algorithm Design, Large Language Model
