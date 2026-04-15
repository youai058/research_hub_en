---
title: "Stochastic Amortization: A Unified Approach to Accelerate Feature and Data Attribution"
authors: ["Ian Connick Covert", "Chanwoo Kim", "Su-In Lee", "James Zou", "Tatsunori Hashimoto"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ZdWTN2HOie"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9d4ffdc3cd39eceb70fbae6c89c7f10944b4a18b.pdf"
published: "2024"
categories: []
keywords: ["Amortization", "feature attribution", "data valuation", "stochastic optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:31+09:00"
---

# Stochastic Amortization: A Unified Approach to Accelerate Feature and Data Attribution

## Abstract
Many tasks in explainable machine learning, such as data valuation and feature attribution, perform expensive computation for each data point and are intractable for large datasets. These methods require efficient approximations, and although amortizing the process by learning a network to directly predict the desired output is a promising solution, training such models with exact labels is often infeasible. We therefore explore training amortized models with noisy labels, and we find that this is inexpensive and surprisingly effective. Through theoretical analysis of the label noise and experiments with various models and datasets, we show that this approach tolerates high noise levels and significantly accelerates several feature attribution and data valuation methods, often yielding an order of magnitude speedup over existing approaches.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Ian Connick Covert, Chanwoo Kim, Su-In Lee, James Zou, Tatsunori Hashimoto
- arxiv_id: 
- openreview_id: ZdWTN2HOie
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9d4ffdc3cd39eceb70fbae6c89c7f10944b4a18b.pdf
- published: 2024
- keywords: Amortization, feature attribution, data valuation, stochastic optimization
