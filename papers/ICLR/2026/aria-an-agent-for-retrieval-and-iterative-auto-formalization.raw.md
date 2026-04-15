---
title: "Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph"
authors: ["Hanyu Wang", "Ruohan Xie", "Yutong Wang", "Guoxiong Gao", "XintaoYu", "Bin Dong"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CPxZClPMiy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9d6d5671c4af09d0f26f9f1ac77788aadea77ff6.pdf"
published: "2026"
categories: []
keywords: ["Lean 4", "Autoformalization", "LLM", "Graph-of-Thought", "Retrieval Augmented Generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:25+09:00"
---

# Aria: an Agent for Retrieval and Iterative Auto-Formalization via Dependency Graph

## Abstract
Accurate auto-formalization of theorem statements is essential for advancing automated discovery and verification of research-level mathematics, yet remains a major bottleneck for LLMs due to hallucinations, semantic mismatches, and their inability to synthesize new definitions.
To tackle these issues, we present Aria (**A**gent for **R**etrieval and **I**terative **A**utoformalization), a system for conjecture-level formalization in Lean that emulates human expert reasoning via a two-phase Graph-of-Thought process: recursively decomposing statements into a dependency graph and then constructing formalizations from grounded concepts. To ensure semantic correctness, we introduce **AriaScorer**, a checker that retrieves definitions from Mathlib for term-level grounding, enabling rigorous and reliable verification.
We evaluate Aria on diverse benchmarks. On ProofNet, it achieves 91.6\% compilation success rate and 68.5\% final accuracy, surpassing previous methods. On FATE-X, a suite of challenging algebra problems from research literature, it outperforms the best baseline with 44.0\% vs. 24.0\% final accuracy. On a dataset of homological conjectures, Aria reaches 42.9\% final accuracy while all other models score 0\%.

## Metadata
- venue: ICLR
- year: 2026
- authors: Hanyu Wang, Ruohan Xie, Yutong Wang, Guoxiong Gao, XintaoYu, Bin Dong
- arxiv_id: 
- openreview_id: CPxZClPMiy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9d6d5671c4af09d0f26f9f1ac77788aadea77ff6.pdf
- published: 2026
- keywords: Lean 4, Autoformalization, LLM, Graph-of-Thought, Retrieval Augmented Generation
