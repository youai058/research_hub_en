---
title: "Sample-Efficient Geometry Reconstruction from Euclidean Distances using Non-Convex Optimization"
authors: ["Ipsita Ghosh", "Abiy Tasissa", "Christian Kümmerle"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Yu7H8ZOuI2"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d774199a5e31ec68b4d93e82ba594ca2865fe985.pdf"
published: "2024"
categories: []
keywords: ["Euclidean distance geometry", "non-convex optimization", "iteratively reweighted least squares", "low-rank", "data efficiency", "convergence guarnatees", "restricted isometry property", "dual basis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:35+09:00"
---

# Sample-Efficient Geometry Reconstruction from Euclidean Distances using Non-Convex Optimization

## Abstract
The problem of finding suitable point embedding or geometric configurations given only Euclidean distance information of point pairs arises both as a core task and as a sub-problem in a variety of machine learning applications. In this paper, we aim to solve this problem given a minimal number of distance samples. 
To this end, we leverage continuous and non-convex rank minimization formulations of the problem and establish a local convergence  
guarantee for a variant of iteratively reweighted least squares (IRLS), which applies if a minimal random set of observed distances is provided.
 As a technical tool, we establish a restricted isometry property (RIP) restricted to a tangent space of the manifold of symmetric rank-$r$ matrices given random Euclidean distance  measurements, which might be of independent interest for the analysis of other non-convex approaches.  Furthermore, we assess data efficiency, scalability and generalizability of different reconstruction algorithms through numerical experiments with simulated data as well as real-world data, demonstrating the proposed algorithm's ability to identify the underlying geometry from fewer distance samples compared to the state-of-the-art.
 
 The Matlab code can be found at \href{https://github.com/ipsita-ghosh-1/EDG-IRLS}{github\_SEGRED}

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Ipsita Ghosh, Abiy Tasissa, Christian Kümmerle
- arxiv_id: 
- openreview_id: Yu7H8ZOuI2
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d774199a5e31ec68b4d93e82ba594ca2865fe985.pdf
- published: 2024
- keywords: Euclidean distance geometry, non-convex optimization, iteratively reweighted least squares, low-rank, data efficiency, convergence guarnatees, restricted isometry property, dual basis
