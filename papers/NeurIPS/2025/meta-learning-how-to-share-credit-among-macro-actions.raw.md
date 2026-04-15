---
title: "Meta-learning how to Share Credit among Macro-Actions"
authors: ["Ionel Hosu", "Traian Rebedea", "Razvan Pascanu"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cJlgdpEFx9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4ba40009cb21873d2dc3ebe6f8174f590798398c.pdf"
published: "2025"
categories: []
keywords: ["deep reinforcement learning", "macro-actions", "exploration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:35+09:00"
---

# Meta-learning how to Share Credit among Macro-Actions

## Abstract
One proposed mechanism to improve exploration in reinforcement learning is the use of macro-actions, a form of temporal abstractions over actions.
Paradoxically though, in many scenarios the naive addition of macro-actions does not lead to better exploration, but rather the opposite. 
In this work, we argue that the difficulty stems from the trade-offs between reducing the average number of decisions per episode versus increasing the size of the action space. 
Namely, one typically treats each potential macro-action as independent and atomic, hence strictly increasing the search space and making typical exploration strategies inefficient. 
To address this problem we propose a novel regularization term that exploits the relationship between actions and macro-actions to improve the credit assignment mechanism reducing the effective dimension of the action space and therefore improving exploration. The term relies on a similarity matrix that is meta-learned jointly with learning the desired policy.
We empirically validate our strategy looking at macro-actions in Atari games, and the StreetFighter II environment. Our results show significant improvements over the Rainbow-DQN baseline in all environments. Additionally, we show that the macro-action similarity is transferable to other environments with similar dynamics.
We believe this work is a small but important step towards understanding how the similarity-imposed geometry on the action space can be exploited to improve credit assignment and exploration, therefore making learning more efficient.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Ionel Hosu, Traian Rebedea, Razvan Pascanu
- arxiv_id: 
- openreview_id: cJlgdpEFx9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4ba40009cb21873d2dc3ebe6f8174f590798398c.pdf
- published: 2025
- keywords: deep reinforcement learning, macro-actions, exploration
