---
title: "Sensitivity Verification for Additive Decision Tree Ensembles"
authors: ["Arhaan Ahmad", "Tanay Vineet Tayal", "Ashutosh Gupta", "S. Akshay"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "h0vC0fm1q7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0baccd0626487637d58895c5bf4daa1f701f0d6f.pdf"
published: "2025"
categories: []
keywords: ["Robustness verification", "Sensitivity analysis", "SAT solvers", "efficient encodings", "NP-hardness", "fairness", "confidence"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:44+09:00"
---

# Sensitivity Verification for Additive Decision Tree Ensembles

## Abstract
Tree ensemble models, such as Gradient Boosted Decision Trees (GBDTs) and random forests, are widely popular models for a variety of machine learning tasks. The power of these models comes from the ensemble of decision trees, which makes analysis of such models significantly harder than for single trees. As a result, recent work has focused on developing exact and approximate techniques for questions such as robustness verification, fairness and explainability for such models of tree ensembles.

In this paper, we focus on a specific problem of feature sensitivity for additive decision tree ensembles and build a formal verification framework for a parametrized variant of it, where we also take into account the confidence of the tree ensemble in its output. We start by showing theoretical (NP-)hardness of the problem and explain how it relates to other verification problems. Next, we provide a novel encoding of the problem using pseudo-Boolean constraints. Based on this encoding, we develop a tunable algorithm to perform sensitivity analysis, which can trade off precision for running time. We implement our algorithm and study its performance on a suite of GBDT benchmarks from the literature. Our experiments show the practical utility of our approach and its improved performance compared to existing approaches.

## Metadata
- venue: ICLR
- year: 2025
- authors: Arhaan Ahmad, Tanay Vineet Tayal, Ashutosh Gupta, S. Akshay
- arxiv_id: 
- openreview_id: h0vC0fm1q7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0baccd0626487637d58895c5bf4daa1f701f0d6f.pdf
- published: 2025
- keywords: Robustness verification, Sensitivity analysis, SAT solvers, efficient encodings, NP-hardness, fairness, confidence
