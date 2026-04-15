---
title: "Metric $k$-clustering using only Weak Comparison Oracles"
authors: ["Rahul Raychaudhury", "Aryan Esmailpour", "sainyam galhotra", "Stavros Sintos"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "KmMEQOtXAy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/aaebab2927a6f105a8ce934feeb5c062393dbb44.pdf"
published: "2026"
categories: []
keywords: ["clustering", "$k$-center", "$k$-median", "$k$-means", "comparison oracles", "learned rankers", "learning-augmented algorithms"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:50+09:00"
---

# Metric $k$-clustering using only Weak Comparison Oracles

## Abstract
Clustering is a fundamental primitive in unsupervised learning. However, classical algorithms for $k$-clustering (such as $k$-median and $k$-means) assume access to exact pairwise distances, which is an unrealistic requirement in many modern applications.  We study clustering in the \emph{Rank-model (R-model)}, where access to distances is entirely replaced by a  \emph{quadruplet oracle} that provides only relative distance comparisons. In practice, such an oracle can represent learned models or human feedback, and is expected to be noisy and entail an access cost.

Given a metric space with $n$ input items, we design randomized algorithms that, using only a noisy quadruplet oracle, compute a set of $O(k \cdot \mathsf{polylog}(n))$ centers along with a mapping from the input items to the centers such that the clustering cost of the mapping is at most constant times the optimum $k$-clustering cost. Our method achieves a query complexity of $O(n\cdot k \cdot \mathsf{polylog}(n))$ for arbitrary metric spaces and improves to $O((n+k^2) \cdot \mathsf{polylog}(n))$ when the underlying metric has bounded doubling dimension. When the metric has bounded doubling dimension we can further improve the approximation from constant to $1+\varepsilon$, for any arbitrarily small constant $\varepsilon\in(0,1)$, while preserving the same asymptotic query complexity.
Our framework demonstrates how noisy, low-cost oracles, such as those derived from large language models, can be systematically integrated into scalable clustering algorithms.

## Metadata
- venue: ICLR
- year: 2026
- authors: Rahul Raychaudhury, Aryan Esmailpour, sainyam galhotra, Stavros Sintos
- arxiv_id: 
- openreview_id: KmMEQOtXAy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/aaebab2927a6f105a8ce934feeb5c062393dbb44.pdf
- published: 2026
- keywords: clustering, $k$-center, $k$-median, $k$-means, comparison oracles, learned rankers, learning-augmented algorithms
