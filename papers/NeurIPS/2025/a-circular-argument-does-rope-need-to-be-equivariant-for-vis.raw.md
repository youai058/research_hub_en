---
title: "A Circular Argument: Does RoPE need to be Equivariant for Vision?"
authors: ["Chase van de Geijn", "Timo Lüddecke", "Polina Turishcheva", "Alexander S. Ecker"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "WCenI6RU9s"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/3e766f3dc7338c5007de8cf6b4dd61b28a050d7a.pdf"
published: "2025"
categories: []
keywords: ["Positional Encoding", "RoPE", "Lie algebras", "LieRE", "Vision"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:52+09:00"
---

# A Circular Argument: Does RoPE need to be Equivariant for Vision?

## Abstract
Rotary Positional Encodings (RoPE) have emerged as a highly effective technique for one-dimensional sequences in Natural Language Processing spurring recent progress towards generalizing RoPE to higher-dimensional data such as images and videos. The success of RoPE has been thought to be due to its positional equivariance, i.e. its status as a \textit{relative} positional encoding. In this paper, we mathematically show RoPE to be one of the most general solutions for equivariant positional embedding in one-dimensional data. Moreover, we show Mixed RoPE to be the analogously general solution for $M$-dimensional data, if we require commutative generators -- a property necessary for RoPE's equivariance. However, we question the necessity of equivariance. We propose Spherical RoPE, a method analogous to Mixed RoPE, but with the assumption of anti-commutative generators -- relaxing the equivariant condition. Empirically, we find Spherical RoPE to have the equivalent learning behavior as its equivariant analogues. This strongly suggests that relative positional embeddings are not as important as is commonly believed. We expect this discovery to facilitate future work in positional encodings for vision that are faster and generalize better by removing the preconception that they must be relative.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Chase van de Geijn, Timo Lüddecke, Polina Turishcheva, Alexander S. Ecker
- arxiv_id: 
- openreview_id: WCenI6RU9s
- anthology_id: 
- pdf_url: https://openreview.net/pdf/3e766f3dc7338c5007de8cf6b4dd61b28a050d7a.pdf
- published: 2025
- keywords: Positional Encoding, RoPE, Lie algebras, LieRE, Vision
