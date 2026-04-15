---
title: "ONLINE EPSILON NET & PIERCING SET FOR GEOMETRIC CONCEPTS"
authors: ["Sujoy Bhore", "Devdan Dey", "Satyam Singh"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nNiWRRj6r9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/c29f6d0e41ce422474bc53d299c9beaab55e491d.pdf"
published: "2025"
categories: []
keywords: ["Theoretical machine learning", "VC-dimension", "Geometric sampling"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:45+09:00"
---

# ONLINE EPSILON NET & PIERCING SET FOR GEOMETRIC CONCEPTS

## Abstract
VC-dimension (Vapnik & Chervonenkis (1971)) and $\varepsilon$-nets  (Haussler & Welzl (1987)) are key concepts in Statistical Learning Theory. Intuitively, VC-dimension is a measure of the size of a class of sets. The famous $\varepsilon$-net theorem, a fundamental result in Discrete Geometry, asserts that if the VC-dimension of a set system is bounded, then a small sample exists that intersects all sufficiently large sets.
    
    In online learning scenarios where data arrives sequentially, the VC-dimension helps to bound the complexity of the set system, and $\varepsilon$-nets ensure the selection of a small representative set. This sampling framework is crucial in various domains, including spatial data analysis, motion planning in dynamic environments, optimization of sensor networks, and feature extraction in computer vision, among others. Motivated by these applications, we study the online $\varepsilon$-net problem for geometric concepts with bounded VC-dimension. While the offline version of this problem has been extensively studied, surprisingly, there are no known theoretical results for the online version to date. We present the first deterministic online algorithm with an optimal competitive ratio for intervals in $\mathbb{R}$. Next, we give a randomized online algorithm with a near-optimal competitive ratio for axis-aligned boxes in $\mathbb{R}^d$, for $d\le 3$. Furthermore, we introduce a novel technique to analyze similar-sized objects of constant description complexity in $\mathbb{R}^d$, which may be of independent interest. 
    
    Next, we focus on the continuous version of this problem (called online piercing set), where ranges of the set system are geometric concepts in $\mathbb{R}^d$ arriving in an online manner, but the universe is the entire ambient space, and the objective is to choose a small sample that intersects all the ranges. Although online piercing set is a very well-studied problem in the literature, to our surprise, very few works have addressed generic geometric concepts without any assumption about the sizes. We advance this field by proposing asymptotically optimal competitive deterministic algorithms for boxes and ellipsoids in $\mathbb{R}^d$, for any $d\in\mathbb{N}$.

## Metadata
- venue: ICLR
- year: 2025
- authors: Sujoy Bhore, Devdan Dey, Satyam Singh
- arxiv_id: 
- openreview_id: nNiWRRj6r9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/c29f6d0e41ce422474bc53d299c9beaab55e491d.pdf
- published: 2025
- keywords: Theoretical machine learning, VC-dimension, Geometric sampling
