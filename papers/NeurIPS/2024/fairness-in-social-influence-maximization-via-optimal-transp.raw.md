---
title: "Fairness in Social Influence Maximization via Optimal Transport"
authors: ["Shubham Chowdhary", "Giulia De Pasquale", "Nicolas Lanzetti", "Ana-Andreea Stoica", "Florian Dorfler"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "axW8xvQPkF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a991c5e3897ae49ac7700dd696dc4a12d539a01d.pdf"
published: "2024"
categories: []
keywords: ["Fairness", "social influence maximization", "optimal transport"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:42+09:00"
---

# Fairness in Social Influence Maximization via Optimal Transport

## Abstract
We study fairness in social influence maximization, whereby one seeks to select
seeds that spread a given information throughout a network, ensuring balanced
outreach among different communities (e.g. demographic groups). In the literature,
fairness is often quantified in terms of the expected outreach within individual
communities. In this paper, we demonstrate that such fairness metrics can be
misleading since they overlook the stochastic nature of information diffusion
processes. When information diffusion occurs in a probabilistic manner, multiple
outreach scenarios can occur. As such, outcomes such as “In 50% of the cases, no
one in group 1 gets the information, while everyone in group 2 does, and in the
other 50%, it is the opposite”, which always results in largely unfair outcomes,
are classified as fair by a variety of fairness metrics in the literature. We tackle
this problem by designing a new fairness metric, mutual fairness, that captures
variability in outreach through optimal transport theory. We propose a new seed-
selection algorithm that optimizes both outreach and mutual fairness, and we show
its efficacy on several real datasets. We find that our algorithm increases fairness
with only a minor decrease (and at times, even an increase) in efficiency.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Shubham Chowdhary, Giulia De Pasquale, Nicolas Lanzetti, Ana-Andreea Stoica, Florian Dorfler
- arxiv_id: 
- openreview_id: axW8xvQPkF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a991c5e3897ae49ac7700dd696dc4a12d539a01d.pdf
- published: 2024
- keywords: Fairness, social influence maximization, optimal transport
