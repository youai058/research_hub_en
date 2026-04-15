---
title: "A Fano-Style Accuracy Upper Bound for LLM Single-Pass Reasoning in Multi-Hop QA"
authors: ["Kaiyang Wan", "Lang Gao", "Honglin Mu", "Preslav Nakov", "Yuxia Wang", "Xiuying Chen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dPAcHrG4rl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d7c1d763f425fdc3245f6145defcff54716be532.pdf"
published: "2026"
categories: []
keywords: ["large language models", "multi-hop question answering", "information-theoretic analysis", "multi-call reasoning framework"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:38+09:00"
---

# A Fano-Style Accuracy Upper Bound for LLM Single-Pass Reasoning in Multi-Hop QA

## Abstract
Multi-Hop Question Answering (MHQA) requires integrating dispersed, interdependent evidence through sequential reasoning under noise. This task is challenging for LLMs as they have a finite per-pass output capacity, beyond which the integration of task-relevant evidence proves unreliable. Consequently, the single-pass reasoning paradigm is inherently vulnerable to this capacity overflow. To formalize this bottleneck, our analysis establishes a Fano-style accuracy upper bound, defining a theoretical performance ceiling for single-pass LLMs. This bound reveals that accuracy inevitably collapses once task complexity exceeds model capacity, providing general principles for capacity-aware representation and structuring of MHQA in LLMs. Building on these principles, we introduce a proof-of-concept multi-call framework for MHQA, InfoQA. It ensures high per-step accuracy by combining capacity-aware task decomposition with active pruning of prior reasoning traces, keeping the information load within the single-pass limit. It further achieves robustness by a dependency-explicit workflow that enables precise control over the reasoning path. We construct a stringent and noise-rich benchmark to validate our theory and framework. Experimental results show that model behavior aligns with our predicted capacity curves while InfoQA achieves consistent performance improvements. We hope our work inspires more LLM multi-step reasoning methods: \faGithub  \href{https://anonymous.4open.science/r/InfoQA-55D1}{InfoQA}.

## Metadata
- venue: ICLR
- year: 2026
- authors: Kaiyang Wan, Lang Gao, Honglin Mu, Preslav Nakov, Yuxia Wang, Xiuying Chen
- arxiv_id: 
- openreview_id: dPAcHrG4rl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d7c1d763f425fdc3245f6145defcff54716be532.pdf
- published: 2026
- keywords: large language models, multi-hop question answering, information-theoretic analysis, multi-call reasoning framework
