---
title: "Proportional Fairness in Non-Centroid Clustering"
authors: ["Ioannis Caragiannis", "Evi Micha", "Nisarg Shah"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Actjv6Wect"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/42edcc1cd56a6cdd04e3d38256adf046aa216acc.pdf"
published: "2024"
categories: []
keywords: ["clustering", "proportional fairness", "core", "fully justified representation", "auditing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:43+09:00"
---

# Proportional Fairness in Non-Centroid Clustering

## Abstract
We revisit the recently developed framework of proportionally fair clustering, where the goal is to provide group fairness guarantees that become stronger for groups of data points that are large and cohesive. Prior work applies this framework to centroid-based clustering, where points are partitioned into clusters, and the cost to each data point is measured by its distance to a centroid assigned to its cluster. However, real-life applications often do not require such centroids. We extend the theory of proportionally fair clustering to non-centroid clustering by considering a variety of cost functions, both metric and non-metric, for a data point to be placed in a cluster with other data points. Our results indicate that Greedy Capture, a clustering algorithm developed for centroid clustering, continues to provide strong proportional fairness guarantees for non-centroid clustering, although the guarantees are significantly different and establishing them requires novel proof ideas. We also design algorithms for auditing proportional fairness of a given clustering solution. We conduct experiments on real data which suggest that traditional clustering algorithms are highly unfair, while our algorithms achieve strong fairness guarantees with a moderate loss in common clustering objectives.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Ioannis Caragiannis, Evi Micha, Nisarg Shah
- arxiv_id: 
- openreview_id: Actjv6Wect
- anthology_id: 
- pdf_url: https://openreview.net/pdf/42edcc1cd56a6cdd04e3d38256adf046aa216acc.pdf
- published: 2024
- keywords: clustering, proportional fairness, core, fully justified representation, auditing
