---
title: "Decomposing LLM Computation with Jets"
authors: ["Yihong Chen", "Xiangxiang Xu", "Pontus Stenetorp", "Sebastian Riedel", "Luca Franceschi"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "u6JLh0BO5h"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1673c50e0097be73d6945813a79ffe2bdb7cf10d.pdf"
published: "2026"
categories: []
keywords: ["decomposition", "transformer", "neural-symbolic", "n-grams", "interpretability", "controllability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:11+09:00"
---

# Decomposing LLM Computation with Jets

## Abstract
Large language models are becoming general knowledge engines for diverse applications. However, their computations are deeply entangled after training, resisting modularization which complicates interpretability, auditing, and long-term maintenance. We introduce Jet Expansions, a framework for expanding computational graphs using jet operators that generalize truncated Taylor series. Our method systematically decomposes language models into explicit input-to-output computational paths and complementary remainders. This functional decomposition provides a principled, knife-like operator for cutting through entanglement in LLMs, enabling scalable model inspection. We demonstrate how Jet Expansions ground and subsume the popular interpretability technique Logit Lens, reveal a (super-)exponential path structure with respect to recursive residual depth, and support several interpretability applications, including sketching a transformer language model with $n$-gram statistics extracted from its computations and indexing model toxicity levels *without* curated benchmarks.

## Metadata
- venue: ICLR
- year: 2026
- authors: Yihong Chen, Xiangxiang Xu, Pontus Stenetorp, Sebastian Riedel, Luca Franceschi
- arxiv_id: 
- openreview_id: u6JLh0BO5h
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1673c50e0097be73d6945813a79ffe2bdb7cf10d.pdf
- published: 2026
- keywords: decomposition, transformer, neural-symbolic, n-grams, interpretability, controllability
