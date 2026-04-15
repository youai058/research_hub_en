---
title: "Graph-Triggered Rising Bandits"
authors: ["Gianmarco Genalti", "Marco Mussi", "Nicola Gatti", "Marcello Restelli", "Matteo Castiglioni", "Alberto Maria Metelli"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "bPsohGR6gD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/134ef7009b1f5beef15c604e6948ed20c9be147c.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:21+09:00"
---

# Graph-Triggered Rising Bandits

## Abstract
In this paper, we propose a novel generalization of rested and restless bandits where the evolution of the arms' expected rewards is governed by a graph defined over the arms. An edge connecting a pair of arms $(i,j)$ represents the fact that a pull of arm $i$ *triggers* the evolution of arm $j$, and vice versa. Interestingly, rested and restless bandits are both special cases of our model for some suitable (degenerate) graphs. Still, the model can represent way more general and interesting scenarios. We first tackle the problem of computing the optimal policy when no specific structure is assumed on the graph, showing that it is NP-hard. Then, we focus on a specific structure forcing the graph to be composed of a set of fully connected subgraphs (i.e., cliques), and we prove that the optimal policy can be easily computed in closed form. Then, we move to the learning problem presenting regret minimization algorithms for deterministic and stochastic cases. Our regret bounds highlight the complexity of the learning problem by incorporating instance-dependent terms that encode specific properties of the underlying graph structure. Moreover, we illustrate how the knowledge of the underlying graph is not necessary for achieving the no-regret property.

## Metadata
- venue: ICML
- year: 2024
- authors: Gianmarco Genalti, Marco Mussi, Nicola Gatti, Marcello Restelli, Matteo Castiglioni, Alberto Maria Metelli
- arxiv_id: 
- openreview_id: bPsohGR6gD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/134ef7009b1f5beef15c604e6948ed20c9be147c.pdf
- published: 2024
