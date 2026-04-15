---
title: "Better by default: Strong pre-tuned MLPs and boosted trees on tabular data"
authors: ["David Holzmüller", "Leo Grinsztajn", "Ingo Steinwart"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3BNPUDvqMt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f3f758f8439dbffcbb999c4ec2bc5130b182dec7.pdf"
published: "2024"
categories: []
keywords: ["tabular data", "benchmark", "default parameters", "neural networks", "deep learning", "multilayer perceptron", "gradient-boosted decision trees"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:41+09:00"
---

# Better by default: Strong pre-tuned MLPs and boosted trees on tabular data

## Abstract
For classification and regression on tabular data, the dominance of gradient-boosted decision trees (GBDTs) has recently been challenged by often much slower deep learning methods with extensive hyperparameter tuning. We address this discrepancy by introducing (a) RealMLP, an improved multilayer perceptron (MLP), and (b) strong meta-tuned default parameters for GBDTs and RealMLP. We tune RealMLP and the default parameters on a meta-train benchmark with 118 datasets and compare them to hyperparameter-optimized versions on a disjoint meta-test benchmark with 90 datasets, as well as the GBDT-friendly benchmark by Grinsztajn et al. (2022). Our benchmark results on medium-to-large tabular datasets (1K--500K samples) show that RealMLP offers a favorable time-accuracy tradeoff compared to other neural baselines and is competitive with GBDTs in terms of benchmark scores. Moreover, a combination of RealMLP and GBDTs with improved default parameters can achieve excellent results without hyperparameter tuning. Finally, we demonstrate that some of RealMLP's improvements can also considerably improve the performance of TabR with default parameters.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: David Holzmüller, Leo Grinsztajn, Ingo Steinwart
- arxiv_id: 
- openreview_id: 3BNPUDvqMt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f3f758f8439dbffcbb999c4ec2bc5130b182dec7.pdf
- published: 2024
- keywords: tabular data, benchmark, default parameters, neural networks, deep learning, multilayer perceptron, gradient-boosted decision trees
