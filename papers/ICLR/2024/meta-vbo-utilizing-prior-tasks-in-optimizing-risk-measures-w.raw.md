---
title: "Meta-VBO: Utilizing Prior Tasks in Optimizing Risk Measures with Gaussian Processes"
authors: ["Quoc Phong Nguyen", "Bryan Kian Hsiang Low", "Patrick Jaillet"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ElykcDu5YK"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/438a0598bfd4e1457d158d87209039d77cfd4c53.pdf"
published: "2024"
categories: []
keywords: ["meta-learning", "Bayesian optimization", "risk measure", "value-at-risk", "conditional value-at-risk"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:04+09:00"
---

# Meta-VBO: Utilizing Prior Tasks in Optimizing Risk Measures with Gaussian Processes

## Abstract
Research on optimizing the risk measure of a blackbox function using Gaussian processes, especially Bayesian optimization (BO) of risk measures, has become increasingly important due to the inevitable presence of uncontrollable variables in real-world applications. Nevertheless, existing works on BO of risk measures start the optimization from scratch for every new task without considering the results of prior tasks. In contrast, its vanilla BO counterpart has received a thorough investigation on utilizing prior tasks to speed up the current task through the body of works on meta-BO which, however, have not considered risk measures. To bridge this gap, this paper presents the first algorithm for meta-BO of risk measures (i.e., value-at-risk (VaR) and the conditional VaR), namely meta-VBO, by introducing a novel adjustment to the upper confidence bound acquisition function. Our proposed algorithm exhibits two desirable properties: (i) invariance to scaling and vertical shifting of the blackbox function and (ii) robustness to prior harmful tasks. We provide a theoretical performance guarantee for our algorithm and empirically demonstrate its performance using several synthetic function benchmarks and real-world objective functions.

## Metadata
- venue: ICLR
- year: 2024
- authors: Quoc Phong Nguyen, Bryan Kian Hsiang Low, Patrick Jaillet
- arxiv_id: 
- openreview_id: ElykcDu5YK
- anthology_id: 
- pdf_url: https://openreview.net/pdf/438a0598bfd4e1457d158d87209039d77cfd4c53.pdf
- published: 2024
- keywords: meta-learning, Bayesian optimization, risk measure, value-at-risk, conditional value-at-risk
