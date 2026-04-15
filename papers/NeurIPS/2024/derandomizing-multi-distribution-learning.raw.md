---
title: "Derandomizing Multi-Distribution Learning"
authors: ["Kasper Green Larsen", "Omar Montasser", "Nikita Zhivotovskiy"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "twYE75Mnkt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f67adbada6b20732846d792b8b89fdf428f4f20e.pdf"
published: "2024"
categories: []
keywords: ["pac learning", "multi-distribution", "derandomization", "computational efficiency", "discrepancy minimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:59+09:00"
---

# Derandomizing Multi-Distribution Learning

## Abstract
Multi-distribution or collaborative learning involves learning a single predictor that works well across multiple data distributions, using samples from each during training. Recent research on multi-distribution learning, focusing on binary loss and finite VC dimension classes, has shown near-optimal sample complexity that is achieved with oracle efficient algorithms. That is, these algorithms are computationally efficient given an efficient ERM for the class. Unlike in classical PAC learning, where the optimal sample complexity is achieved with deterministic predictors, current multi-distribution learning algorithms output randomized predictors. This raises the question: can these algorithms be derandomized to produce a deterministic predictor for multiple distributions? Through a reduction to discrepancy minimization, we show that derandomizing multi-distribution learning is computationally hard, even when ERM is computationally efficient. On the positive side, we identify a structural condition enabling an efficient black-box reduction, converting existing randomized multi-distribution predictors into deterministic ones.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Kasper Green Larsen, Omar Montasser, Nikita Zhivotovskiy
- arxiv_id: 
- openreview_id: twYE75Mnkt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f67adbada6b20732846d792b8b89fdf428f4f20e.pdf
- published: 2024
- keywords: pac learning, multi-distribution, derandomization, computational efficiency, discrepancy minimization
