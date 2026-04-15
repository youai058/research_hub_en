---
title: "Fast Last-Iterate Convergence of Learning in Games Requires Forgetful Algorithms"
authors: ["Yang Cai", "Gabriele Farina", "Julien Grand-Clément", "Christian Kroer", "Chung-Wei Lee", "Haipeng Luo", "Weiqiang Zheng"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hK7XTpCtBi"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7909f2d264931bfec26151315181b4579da12979.pdf"
published: "2024"
categories: []
keywords: ["Last-Iterate Convergence", "Zero-Sum Games", "Optimistic Multicaptive Weights Update", "Optimistic Gradient"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:07+09:00"
---

# Fast Last-Iterate Convergence of Learning in Games Requires Forgetful Algorithms

## Abstract
Self play via online learning is one of the premier ways to solve large-scale zero-sum games, both in theory and practice. Particularly popular algorithms include optimistic multiplicative weights update (OMWU) and optimistic gradient-descent-ascent (OGDA). While both algorithms enjoy $O(1/T)$ ergodic convergence to Nash equilibrium in two-player zero-sum games, OMWU offers several advantages, including logarithmic dependence on the size of the payoff matrix and $\tilde{O}(1/T)$ convergence to coarse correlated equilibria even in general-sum games. However, in terms of last-iterate convergence in two-player zero-sum games, an increasingly popular topic in this area, OGDA guarantees that the duality gap shrinks at a rate of $(1/\sqrt{T})$, while the best existing last-iterate convergence for OMWU depends on some game-dependent constant that could be arbitrarily large. This begs the question: is this potentially slow last-iterate convergence an inherent disadvantage of OMWU, or is the current analysis too loose? Somewhat surprisingly, we show that the former is true. More generally, we prove that a broad class of algorithms that do not forget the past quickly all suffer the same issue: for any arbitrarily small $\delta>0$, there exists a $2\times 2$ matrix game such that the algorithm admits a constant duality gap even after $1/\delta$ rounds. This class of algorithms includes OMWU and other standard optimistic follow-the-regularized-leader algorithms.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Yang Cai, Gabriele Farina, Julien Grand-Clément, Christian Kroer, Chung-Wei Lee, Haipeng Luo, Weiqiang Zheng
- arxiv_id: 
- openreview_id: hK7XTpCtBi
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7909f2d264931bfec26151315181b4579da12979.pdf
- published: 2024
- keywords: Last-Iterate Convergence, Zero-Sum Games, Optimistic Multicaptive Weights Update, Optimistic Gradient
