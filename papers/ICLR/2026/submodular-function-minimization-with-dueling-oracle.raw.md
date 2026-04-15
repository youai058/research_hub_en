---
title: "Submodular Function Minimization with Dueling Oracle"
authors: ["Kaien Sho", "Shinji Ito"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BeMtzSH1d7"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/292c7ad81d0077f84ba8757f469eecb7b0f5bcaf.pdf"
published: "2026"
categories: []
keywords: ["submodular minimization", "deling oracle", "preference-based optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:12+09:00"
---

# Submodular Function Minimization with Dueling Oracle

## Abstract
We consider submodular function minimization using a *dueling oracle*, a noisy pairwise comparison oracle that provides relative feedback on function values between two queried sets.
The oracle's responses are governed by a *transfer function*, which characterizes the relationship between differences in function values and the parameters of the response distribution.
For a linear transfer function, we propose an algorithm that achieves an error rate of $O(n^{\frac{3}{2}}/\sqrt{T})$, where $n$ is the size of the ground set and $T$ denotes the number of oracle calls.
We establish a lower bound: Under the constraint that differences between queried sets are bounded by a constant, any algorithm incurs an error of at least $\Omega(n^{\frac{3}{2}}/\sqrt{T})$.
Without such a constraint, the lower bound becomes $\Omega(n/\sqrt{T})$.
These results show that our algorithm is optimal up to constant factors for constrained algorithms.
For a sigmoid transfer function, we design an algorithm with an error rate of $O(n^{\frac{7}{5}}/T^{\frac{2}{5}})$,
and establish lower bounds analogous to the linear case.

## Metadata
- venue: ICLR
- year: 2026
- authors: Kaien Sho, Shinji Ito
- arxiv_id: 
- openreview_id: BeMtzSH1d7
- anthology_id: 
- pdf_url: https://openreview.net/pdf/292c7ad81d0077f84ba8757f469eecb7b0f5bcaf.pdf
- published: 2026
- keywords: submodular minimization, deling oracle, preference-based optimization
