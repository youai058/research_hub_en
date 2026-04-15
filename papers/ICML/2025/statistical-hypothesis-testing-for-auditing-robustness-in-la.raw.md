---
title: "Statistical Hypothesis Testing for Auditing Robustness in Language Models"
authors: ["Paulius Rauba", "Qiyao Wei", "Mihaela van der Schaar"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ECayXPDoha"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ef3bba5904e4fcf5f631941e823b3bf8bc7b0ae8.pdf"
published: "2025"
categories: []
keywords: ["language models", "safety", "interpretability", "reliability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:08+09:00"
---

# Statistical Hypothesis Testing for Auditing Robustness in Language Models

## Abstract
Consider the problem of testing whether the outputs of a large language model (LLM) system change under an arbitrary intervention, such as an input perturbation or changing the model variant. We cannot simply compare two LLM outputs since they might differ due to the stochastic nature of the system, nor can we compare the entire output distribution due to computational intractability. While existing methods for analyzing text-based outputs exist, they focus on fundamentally different problems, such as measuring bias or fairness. To this end, we introduce distribution-based perturbation analysis, a framework that reformulates LLM perturbation analysis as a frequentist hypothesis testing problem. We construct empirical null and alternative output distributions within a low-dimensional semantic similarity space via Monte Carlo sampling, enabling tractable inference without restrictive distributional assumptions. The framework is (i) model-agnostic, (ii) supports the evaluation of arbitrary input perturbations on any black-box LLM,  (iii) yields interpretable p-values; (iv) supports multiple perturbations via controlled error rates; and (v) provides scalar effect sizes. We demonstrate the usefulness of the framework across multiple case studies, showing how we can quantify response changes, measure true/false positive rates, and evaluate alignment with reference models. Above all, we see this as a reliable frequentist hypothesis testing framework for LLM auditing.

## Metadata
- venue: ICML
- year: 2025
- authors: Paulius Rauba, Qiyao Wei, Mihaela van der Schaar
- arxiv_id: 
- openreview_id: ECayXPDoha
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ef3bba5904e4fcf5f631941e823b3bf8bc7b0ae8.pdf
- published: 2025
- keywords: language models, safety, interpretability, reliability
