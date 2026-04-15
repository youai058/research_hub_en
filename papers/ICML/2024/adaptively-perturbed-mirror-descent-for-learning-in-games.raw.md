---
title: "Adaptively Perturbed Mirror Descent for Learning in Games"
authors: ["Kenshi Abe", "Kaito Ariu", "Mitsuki Sakamoto", "Atsushi Iwasaki"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "9U29U3cDKq"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dc6b600c606de8b03240de04186475aa8a045db7.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:33+09:00"
---

# Adaptively Perturbed Mirror Descent for Learning in Games

## Abstract
This paper proposes a payoff perturbation technique for the Mirror Descent (MD) algorithm in games where the gradient of the payoff functions is monotone in the strategy profile space, potentially containing additive noise. The optimistic family of learning algorithms, exemplified by optimistic MD, successfully achieves *last-iterate* convergence in scenarios devoid of noise, leading the dynamics to a Nash equilibrium. A recent re-emerging trend underscores the promise of the perturbation approach, where payoff functions are perturbed based on the distance from an anchoring, or *slingshot*, strategy. In response, we propose *Adaptively Perturbed MD* (APMD), which adjusts the magnitude of the perturbation by repeatedly updating the slingshot strategy at a predefined interval. This innovation empowers us to find a Nash equilibrium of the underlying game with guaranteed rates. Empirical demonstrations affirm that our algorithm exhibits significantly accelerated convergence.

## Metadata
- venue: ICML
- year: 2024
- authors: Kenshi Abe, Kaito Ariu, Mitsuki Sakamoto, Atsushi Iwasaki
- arxiv_id: 
- openreview_id: 9U29U3cDKq
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dc6b600c606de8b03240de04186475aa8a045db7.pdf
- published: 2024
