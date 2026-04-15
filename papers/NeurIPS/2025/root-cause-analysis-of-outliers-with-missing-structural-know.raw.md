---
title: "Root Cause Analysis of Outliers with Missing Structural Knowledge"
authors: ["William Roy Orchard", "Nastaran Okati", "Sergio Hernan Garrido Mejia", "Patrick Blöbaum", "Dominik Janzing"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "7Nxq4RQApu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2bb8c09f4ad9d2ba0111c95a1835e90e8912aa33.pdf"
published: "2025"
categories: []
keywords: ["root cause analysis", "causality", "contribution analysis", "actual causation", "outliers", "anomalies"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:32+09:00"
---

# Root Cause Analysis of Outliers with Missing Structural Knowledge

## Abstract
The goal of Root Cause Analysis (RCA) is to explain why an anomaly occurred by identifying where the fault originated. Several recent works model the anomalous event as resulting from a change in the causal mechanism at the root cause, i.e., as a soft intervention. RCA is then the task of identifying which causal mechanism changed. In real-world applications, one often has either few or only a single sample from the post-intervention distribution: a severe limitation for most methods, which assume one knows or can estimate the distribution. However, even those that do not are statistically ill-posed due to the need to probe regression models in regions of low probability density. In this paper, we propose simple, efficient methods to overcome both difficulties in the case where there is a single root cause and the causal graph is a polytree. When one knows the causal graph, we give guarantees for a traversal algorithm that requires only marginal anomaly scores and does not depend on specifying an arbitrary anomaly score cut-off. When one does not know the causal graph, we show that the heuristic of identifying root causes as the variables with the highest marginal anomaly scores is causally justified. To this end, we prove that anomalies with small scores are unlikely to cause those with larger scores in polytrees and give upper bounds for the likelihood of causal pathways with non-monotonic anomaly scores.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: William Roy Orchard, Nastaran Okati, Sergio Hernan Garrido Mejia, Patrick Blöbaum, Dominik Janzing
- arxiv_id: 
- openreview_id: 7Nxq4RQApu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2bb8c09f4ad9d2ba0111c95a1835e90e8912aa33.pdf
- published: 2025
- keywords: root cause analysis, causality, contribution analysis, actual causation, outliers, anomalies
