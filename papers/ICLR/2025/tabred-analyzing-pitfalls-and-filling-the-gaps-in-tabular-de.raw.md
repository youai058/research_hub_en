---
title: "TabReD: Analyzing Pitfalls and Filling the Gaps in Tabular Deep Learning Benchmarks"
authors: ["Ivan Rubachev", "Nikolay Kartashev", "Yury Gorishniy", "Artem Babenko"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "L14sqcrUC3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ad23977de2a4f6ec3e8d6837ed58d29c4ab4b55e.pdf"
published: "2025"
categories: []
keywords: ["Tabular Data", "Benchmarks", "Reality Check", "Tabular Deep Learning", "Applications"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:52+09:00"
---

# TabReD: Analyzing Pitfalls and Filling the Gaps in Tabular Deep Learning Benchmarks

## Abstract
Advances in machine learning research drive progress in real-world applications. 
To ensure this progress, it is important to understand the potential pitfalls on the way from a novel method's success on academic benchmarks to its practical deployment. In this work, we analyze existing tabular deep learning benchmarks and find two common characteristics of tabular data in typical industrial applications that are underrepresented in the datasets usually used for evaluation in the literature.
First, in real-world deployment scenarios, distribution of data often changes over time. To account for this distribution drift, time-based train/test splits should be used in evaluation. However, existing academic tabular datasets often lack timestamp metadata to enable such evaluation.
Second, a considerable portion of datasets in production settings stem from extensive data acquisition and feature engineering pipelines. This can have an impact on the absolute and relative number of predictive, uninformative, and correlated features compared to academic datasets.
In this work, we aim to understand how recent research advances in tabular deep learning transfer to these underrepresented conditions.
To this end, we introduce TabReD -- a collection of eight industry-grade tabular datasets. 
We reassess a large number of tabular ML models and techniques on TabReD. We demonstrate that evaluation on both time-based data splits and richer feature sets leads to different methods ranking, compared to evaluation on random splits and smaller number of features, which are common in academic benchmarks. Furthermore, simple MLP-like architectures and GBDT show the best results on the TabReD datasets, while other methods are less effective in the new setting.

## Metadata
- venue: ICLR
- year: 2025
- authors: Ivan Rubachev, Nikolay Kartashev, Yury Gorishniy, Artem Babenko
- arxiv_id: 
- openreview_id: L14sqcrUC3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ad23977de2a4f6ec3e8d6837ed58d29c4ab4b55e.pdf
- published: 2025
- keywords: Tabular Data, Benchmarks, Reality Check, Tabular Deep Learning, Applications
