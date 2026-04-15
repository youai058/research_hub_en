---
title: "Structure-Aware Spectral Sparsification via Uniform Edge Sampling"
authors: ["Kaiwen He", "Petros Drineas", "Rajiv Khanna"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Z4eFqgYbha"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/cfad55f4ec2404ea6fb2c334c27fc8bde3129720.pdf"
published: "2025"
categories: []
keywords: ["Spectral Clustering", "Graph Sparsification"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:23+09:00"
---

# Structure-Aware Spectral Sparsification via Uniform Edge Sampling

## Abstract
Spectral clustering is a fundamental method for graph partitioning, but its reliance on eigenvector computation limits scalability to massive graphs. Classical sparsification methods preserve spectral properties by sampling edges proportionally to their effective resistances, but require expensive preprocessing to estimate these resistances. We study whether uniform edge sampling—a simple, structure-agnostic strategy—can suffice for spectral clustering. Our main result shows that for graphs admitting a well-separated $k$-clustering, characterized by a large structure ratio $\Upsilon(k) = \lambda_{k+1} / \rho_G(k)$, uniform sampling preserves the spectral subspace used for clustering. Specifically, we prove that uniformly sampling $O(\gamma^2 n \log n / \varepsilon^2)$ edges, where $\gamma$ is the Laplacian condition number, yields a sparsifier whose top $(n-k)$-dimensional eigenspace is approximately orthogonal to the cluster indicators. This ensures that the spectral embedding remains faithful, and clustering quality is preserved. Our analysis introduces new resistance bounds for intra-cluster edges, a rank-$(n-k)$ effective resistance formulation, and a matrix Chernoff bound adapted to the dominant eigenspace. These tools allow us to bypass importance sampling entirely. Conceptually, our result connects recent coreset-based clustering theory to spectral sparsification, showing that under strong clusterability, even uniform sampling is structure-aware. This provides the first provable guarantee that uniform edge sampling suffices for structure-preserving spectral clustering.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Kaiwen He, Petros Drineas, Rajiv Khanna
- arxiv_id: 
- openreview_id: Z4eFqgYbha
- anthology_id: 
- pdf_url: https://openreview.net/pdf/cfad55f4ec2404ea6fb2c334c27fc8bde3129720.pdf
- published: 2025
- keywords: Spectral Clustering, Graph Sparsification
