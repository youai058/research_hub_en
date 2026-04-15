---
title: "OPERA: Automatic Offline Policy Evaluation with Re-weighted Aggregates of Multiple Estimators"
authors: ["Allen Nie", "Yash Chandak", "Christina J. Yuan", "Anirudhan Badrinath", "Yannis Flet-Berliac", "Emma Brunskill"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "T6LOGZBC2m"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/0a3ac0bcceb34aa4f7547d107636259e738fca17.pdf"
published: "2024"
categories: []
keywords: ["offline reinforcement learning", "off policy evaluation", "statistics", "ensemble method"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:05+09:00"
---

# OPERA: Automatic Offline Policy Evaluation with Re-weighted Aggregates of Multiple Estimators

## Abstract
Offline policy evaluation (OPE) allows us to evaluate and estimate a new sequential decision-making policy's performance by leveraging historical interaction data collected from other policies. Evaluating a new policy online without a confident estimate of its performance can lead to costly, unsafe, or hazardous outcomes, especially in education and healthcare. Several OPE estimators have been proposed in the last decade, many of which have hyperparameters and require training. Unfortunately, choosing the best OPE algorithm for each task and domain is still unclear. In this paper, we propose a new algorithm that adaptively blends a set of OPE estimators given a dataset without relying on an explicit selection using a statistical procedure. We prove that our estimator is consistent and satisfies several desirable properties for policy evaluation. Additionally, we demonstrate that when compared to alternative approaches, our estimator can be used to select higher-performing policies in healthcare and robotics. Our work contributes to improving ease of use for a general-purpose, estimator-agnostic, off-policy evaluation framework for offline RL.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Allen Nie, Yash Chandak, Christina J. Yuan, Anirudhan Badrinath, Yannis Flet-Berliac, Emma Brunskill
- arxiv_id: 
- openreview_id: T6LOGZBC2m
- anthology_id: 
- pdf_url: https://openreview.net/pdf/0a3ac0bcceb34aa4f7547d107636259e738fca17.pdf
- published: 2024
- keywords: offline reinforcement learning, off policy evaluation, statistics, ensemble method
