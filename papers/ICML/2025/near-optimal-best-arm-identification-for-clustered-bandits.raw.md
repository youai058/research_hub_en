---
title: "Near Optimal Best Arm Identification for Clustered Bandits"
authors: ["Yash", "Avishek Ghosh", "Nikhil Karamchandani"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3Jr5Al16MS"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e96611b0083dddb092ac4baec4ef8e034b86424b.pdf"
published: "2025"
categories: []
keywords: ["Best Arm Identification", "Multi-Armed Bandits (MAB)", "Clustered Bandits", "Pure Exploration"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:14+09:00"
---

# Near Optimal Best Arm Identification for Clustered Bandits

## Abstract
This work investigates the problem of best arm identification for multi-agent multi-armed bandits. We consider $N$ agents grouped into $M$ clusters, where each cluster solves a stochastic bandit problem. The mapping between agents and bandits is \textit{a priori} unknown. Each bandit is associated with $K$ arms, and the goal is to identify the best arm for each agent under a $\delta$-probably correct ($\delta$-PC) framework, while minimizing sample complexity and communication overhead. We propose two novel algorithms: \emph{Clustering then Best Arm Identification} (\texttt{Cl-BAI}) and \emph{Best Arm Identification then Clustering} (\texttt{BAI-Cl}). \texttt{Cl-BAI} employs a two-phase approach that first clusters agents based on the bandit problems they are learning, followed by identifying the best arm for each cluster. \texttt{BAI-Cl} reverses the sequence by identifying the best arms first and then clustering agents accordingly. Both algorithms exploit the successive elimination framework to ensure computational efficiency and high accuracy. Theoretical analysis establishes $\delta$-PC guarantees for both methods, derives bounds on their sample complexity, and provides a lower bound for the problem class. Moreover, when $M$ is small (a constant), we show that the sample complexity of (a variant of) \texttt{BAI-Cl} is (order-wise) minimax optimal. Experiments on synthetic and real-world (Movie Lens, Yelp) data demonstrates the superior performance of the proposed algorithms in terms of sample and communication efficiency, particularly in settings where $M \ll N$.

## Metadata
- venue: ICML
- year: 2025
- authors: Yash, Avishek Ghosh, Nikhil Karamchandani
- arxiv_id: 
- openreview_id: 3Jr5Al16MS
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e96611b0083dddb092ac4baec4ef8e034b86424b.pdf
- published: 2025
- keywords: Best Arm Identification, Multi-Armed Bandits (MAB), Clustered Bandits, Pure Exploration
