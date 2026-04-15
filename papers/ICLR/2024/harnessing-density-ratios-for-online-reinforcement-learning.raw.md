---
title: "Harnessing Density Ratios for Online Reinforcement Learning"
authors: ["Philip Amortila", "Dylan J Foster", "Nan Jiang", "Ayush Sekhari", "Tengyang Xie"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "THJEa8adBn"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2fffb35b07edd292dea91e77c2c874abdf3e831f.pdf"
published: "2024"
categories: []
keywords: ["reinforcement learning theory", "online RL", "offline RL", "hybrid RL", "density ratio", "marginalized importance weight", "weight function", "general function approximation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:25+09:00"
---

# Harnessing Density Ratios for Online Reinforcement Learning

## Abstract
The theories of offline and online reinforcement learning, despite having evolved in parallel, have begun to show signs of the possibility for a unification, with algorithms and analysis techniques for one setting often having natural counterparts in the other. However, the notion of *density ratio modeling*, an emerging paradigm in offline RL, has been largely absent from online RL, perhaps for good reason: the very existence and boundedness of density ratios relies on access to an exploratory dataset with good coverage, but the core challenge in online RL is to collect such a dataset without having one to start.

In this work we show---perhaps surprisingly---that density ratio-based algorithms have online counterparts.  Assuming only the existence of an exploratory distribution with good coverage, a structural condition known as *coverability* (Xie et al., 2023), we give a new algorithm (GLOW) that uses density ratio realizability and value function realizability to perform sample-efficient online exploration. GLOW addresses unbounded density ratios via careful use of truncation, and combines this with optimism to guide exploration. GLOW is computationally inefficient; we complement it with a more efficient counterpart, HyGLOW, for the Hybrid RL setting (Song et al., 2023) wherein online RL is augmented with additional offline data. HyGLOW is derived as a special case of a more general meta-algorithm that provides a provable black-box reduction from hybrid RL to offline RL, which may be of independent interest.

## Metadata
- venue: ICLR
- year: 2024
- authors: Philip Amortila, Dylan J Foster, Nan Jiang, Ayush Sekhari, Tengyang Xie
- arxiv_id: 
- openreview_id: THJEa8adBn
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2fffb35b07edd292dea91e77c2c874abdf3e831f.pdf
- published: 2024
- keywords: reinforcement learning theory, online RL, offline RL, hybrid RL, density ratio, marginalized importance weight, weight function, general function approximation
