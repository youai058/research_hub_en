---
title: "Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws"
authors: ["Nikhil Sardana", "Jacob Portes", "Sasha Doubov", "Jonathan Frankle"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0bmXrtTDUu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/77e05ffe052617301d4740a04e86ccb07081d696.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:14+09:00"
---

# Beyond Chinchilla-Optimal: Accounting for Inference in Language Model Scaling Laws

## Abstract
Large language model (LLM) scaling laws are empirical formulas that estimate changes in model quality as a result of increasing parameter count and training data. However, these formulas, including the popular Deepmind Chinchilla scaling laws, neglect to include the cost of inference. We modify the Chinchilla scaling laws to calculate the optimal LLM parameter count and pre-training data size to train and deploy a model of a given quality and inference demand. We conduct our analysis both in terms of a compute budget and real-world costs and find that LLM researchers expecting reasonably large inference demand ($\sim$1B requests) should train models smaller and longer than Chinchilla-optimal. Furthermore, we train 47 models of varying sizes and parameter counts to validate our formula and find that model quality continues to improve as we scale tokens per parameter to extreme ranges (up to 10,000). Finally, we ablate the procedure used to fit the Chinchilla scaling law coefficients and find that developing scaling laws only from data collected at typical token/parameter ratios overestimates the impact of additional tokens at these extreme ranges.

## Metadata
- venue: ICML
- year: 2024
- authors: Nikhil Sardana, Jacob Portes, Sasha Doubov, Jonathan Frankle
- arxiv_id: 
- openreview_id: 0bmXrtTDUu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/77e05ffe052617301d4740a04e86ccb07081d696.pdf
- published: 2024
