---
title: "Soft Robust MDPs and Risk-Sensitive MDPs: Equivalence, Policy Gradient, and Sample Complexity"
authors: ["Runyu Zhang", "Yang Hu", "Na Li"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dEz3ge8QSo"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/317b11f5d5ce4a86be220bbd6715b66f4a55103a.pdf"
published: "2024"
categories: []
keywords: ["risk-sensitive reinforcement learning", "robust Markov Decision Processes"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:21+09:00"
---

# Soft Robust MDPs and Risk-Sensitive MDPs: Equivalence, Policy Gradient, and Sample Complexity

## Abstract
Robust Markov Decision Processes (MDPs) and risk-sensitive MDPs are both powerful tools for making decisions in the presence of uncertainties. Previous efforts have aimed to establish their connections, revealing equivalences in specific formulations. This paper introduces a new formulation for risk-sensitive MDPs, which assesses risk in a slightly different manner compared to the classical Markov risk measure [Ruszczy ́nski 2010], and establishes its equivalence with a class of soft robust MDP (RMDP) problems, including the standard RMDP as a special case. Leveraging this equivalence, we further derive the policy gradient theorem for both problems, proving gradient domination and global convergence of the exact policy gradient method under the tabular setting with direct parameterization. This forms a sharp contrast to the Markov risk measure, known to be potentially non-gradient-dominant [Huang et al. 2021]. We also propose a sample-based offline learning algorithm, namely the robust fitted-Z iteration (RFZI), for a specific soft RMDP problem with a KL-divergence regularization term (or equivalently the risk-sensitive MDP with an entropy risk measure). We showcase its streamlined
design and less stringent assumptions due to the equivalence and analyze its sample complexity.

## Metadata
- venue: ICLR
- year: 2024
- authors: Runyu Zhang, Yang Hu, Na Li
- arxiv_id: 
- openreview_id: dEz3ge8QSo
- anthology_id: 
- pdf_url: https://openreview.net/pdf/317b11f5d5ce4a86be220bbd6715b66f4a55103a.pdf
- published: 2024
- keywords: risk-sensitive reinforcement learning, robust Markov Decision Processes
