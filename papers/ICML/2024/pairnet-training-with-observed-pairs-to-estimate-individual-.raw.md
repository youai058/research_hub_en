---
title: "PairNet: Training with Observed Pairs to Estimate Individual Treatment Effect"
authors: ["Lokesh Nagalapatti", "Pranava Singhal", "Avishek Ghosh", "Sunita Sarawagi"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "o5SVr80Rgg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8542c0b81c30deb10c2d35fd220b4d912812d24a.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:17+09:00"
---

# PairNet: Training with Observed Pairs to Estimate Individual Treatment Effect

## Abstract
Given a dataset of individuals each described by a covariate vector, a treatment, and an observed outcome on the treatment, the goal of the individual treatment effect (ITE) estimation task is to predict outcome changes resulting from a change in treatment. A fundamental challenge is that in the observational data, a covariate’s outcome is observed only under one treatment, whereas we need to infer the difference in outcomes under two different treatments. Several existing approaches address this issue through training with inferred pseudo-outcomes, but their success relies on the quality of these pseudo-outcomes. We propose PairNet, a novel ITE estimation training strategy that minimizes losses over pairs of examples based on their factual observed outcomes. Theoretical analysis for binary treatments reveals that PairNet is a consistent estimator of ITE risk, and achieves smaller generalization error than baseline models. Empirical comparison with thirteen existing methods across eight benchmarks, covering both discrete and continuous treatments, shows that PairNet achieves significantly lower ITE error compared to the baselines. Also, it is model-agnostic and easy to implement.

## Metadata
- venue: ICML
- year: 2024
- authors: Lokesh Nagalapatti, Pranava Singhal, Avishek Ghosh, Sunita Sarawagi
- arxiv_id: 
- openreview_id: o5SVr80Rgg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8542c0b81c30deb10c2d35fd220b4d912812d24a.pdf
- published: 2024
