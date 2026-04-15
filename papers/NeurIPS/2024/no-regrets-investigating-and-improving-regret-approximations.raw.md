---
title: "No Regrets: Investigating and Improving Regret Approximations for Curriculum Discovery"
authors: ["Alexander Rutherford", "Michael Beukman", "Timon Willi", "Bruno Lacerda", "Nick Hawes", "Jakob Nicolaus Foerster"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "iEeiZlTbts"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/450f8065819bc0d3298b71c62f255c51668b3b69.pdf"
published: "2024"
categories: []
keywords: ["MARL", "UED", "Robotics"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:28+09:00"
---

# No Regrets: Investigating and Improving Regret Approximations for Curriculum Discovery

## Abstract
What data or environments to use for training to improve downstream performance is a longstanding and very topical question in reinforcement learning. 
In particular, Unsupervised Environment Design (UED) methods have gained recent attention as their adaptive curricula promise to enable agents to be robust to in- and out-of-distribution tasks.
This work investigates how existing UED methods select training environments, focusing on task prioritisation metrics.
Surprisingly, despite methods aiming to maximise regret in theory, the practical approximations do not correlate with regret but with success rate.
As a result, a significant portion of an agent's experience comes from environments it has already mastered, offering little to no contribution toward enhancing its abilities. Put differently, current methods fail to predict intuitive measures of *learnability*. Specifically, they are unable to consistently identify those scenarios that the agent can sometimes solve, but not always.
Based on our analysis, we develop a method that directly trains on scenarios with high learnability. This simple and intuitive approach outperforms existing UED methods in several binary-outcome environments, including the standard domain of Minigrid and a novel setting closely inspired by a real-world robotics problem. 
We further introduce a new adversarial evaluation procedure for directly measuring robustness, closely mirroring the conditional value at risk (CVaR).
We open-source all our code and present visualisations of final policies here: https://github.com/amacrutherford/sampling-for-learnability.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Alexander Rutherford, Michael Beukman, Timon Willi, Bruno Lacerda, Nick Hawes, Jakob Nicolaus Foerster
- arxiv_id: 
- openreview_id: iEeiZlTbts
- anthology_id: 
- pdf_url: https://openreview.net/pdf/450f8065819bc0d3298b71c62f255c51668b3b69.pdf
- published: 2024
- keywords: MARL, UED, Robotics
