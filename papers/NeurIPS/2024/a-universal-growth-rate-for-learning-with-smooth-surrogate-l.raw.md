---
title: "A Universal Growth Rate for Learning with Smooth Surrogate Losses"
authors: ["Anqi Mao", "Mehryar Mohri", "Yutao Zhong"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "itztwTAcN6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/87213f6d42eff281d1aa2875b8795d53bed81f57.pdf"
published: "2024"
categories: []
keywords: ["surrogate loss functions", "Bayes-consistency", "H-consistency bounds", "excess error bounds", "estimation error bounds", "generalization bounds", "learning theory"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:54+09:00"
---

# A Universal Growth Rate for Learning with Smooth Surrogate Losses

## Abstract
This paper presents a comprehensive analysis of the growth rate of $H$-consistency bounds (and excess error bounds) for various surrogate losses used in classification. We prove a square-root growth rate near zero for smooth margin-based surrogate losses in binary classification, providing both upper and lower bounds under mild assumptions. This result also translates to excess error bounds. Our lower bound requires weaker conditions than those in previous work for excess error bounds, and our upper bound is entirely novel. Moreover, we extend this analysis to multi-class classification with a series of novel results, demonstrating a universal square-root growth rate for smooth *comp-sum* and *constrained losses*, covering common choices for training neural networks in multi-class classification. Given this universal rate, we turn to the question of choosing among different surrogate losses. We first examine how $H$-consistency bounds vary across surrogates based on the number of classes. Next, ignoring constants and focusing on behavior near zero, we identify *minimizability gaps* as the key differentiating factor in these bounds. Thus, we thoroughly analyze these gaps, to guide surrogate loss selection, covering: comparisons across different comp-sum losses, conditions where gaps become zero, and general conditions leading to small gaps.  Additionally, we demonstrate the key role of minimizability gaps in comparing excess error bounds and $H$-consistency bounds.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Anqi Mao, Mehryar Mohri, Yutao Zhong
- arxiv_id: 
- openreview_id: itztwTAcN6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/87213f6d42eff281d1aa2875b8795d53bed81f57.pdf
- published: 2024
- keywords: surrogate loss functions, Bayes-consistency, H-consistency bounds, excess error bounds, estimation error bounds, generalization bounds, learning theory
