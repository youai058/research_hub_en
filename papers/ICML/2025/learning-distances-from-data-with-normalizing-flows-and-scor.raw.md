---
title: "Learning Distances from Data with Normalizing Flows and Score Matching"
authors: ["Peter Sorrenson", "Daniel Behrend-Uriarte", "Christoph Schnoerr", "Ullrich Koethe"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "SOwcmZ91Sl"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e4567fadae26bda3198810b57741099a5a504521.pdf"
published: "2025"
categories: []
keywords: ["density-based distance", "Fermat distance", "Riemannian geometry", "representation learning", "normalizing flows", "score matching"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:07+09:00"
---

# Learning Distances from Data with Normalizing Flows and Score Matching

## Abstract
Density-based distances (DBDs) provide a principled approach to metric learning by defining distances in terms of the underlying data distribution. By employing a Riemannian metric that increases in regions of low probability density, shortest paths naturally follow the data manifold. Fermat distances, a specific type of DBD, have attractive properties, but existing estimators based on nearest neighbor graphs suffer from poor convergence due to inaccurate density estimates. Moreover, graph-based methods scale poorly to high dimensions, as the proposed geodesics are often insufficiently smooth. We address these challenges in two key ways. First, we learn densities using normalizing flows. Second, we refine geodesics through relaxation, guided by a learned score model. Additionally, we introduce a dimension-adapted Fermat distance that scales intuitively to high dimensions and improves numerical stability. Our work paves the way for the practical use of density-based distances, especially in high-dimensional spaces.

## Metadata
- venue: ICML
- year: 2025
- authors: Peter Sorrenson, Daniel Behrend-Uriarte, Christoph Schnoerr, Ullrich Koethe
- arxiv_id: 
- openreview_id: SOwcmZ91Sl
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e4567fadae26bda3198810b57741099a5a504521.pdf
- published: 2025
- keywords: density-based distance, Fermat distance, Riemannian geometry, representation learning, normalizing flows, score matching
