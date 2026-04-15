---
title: "Revisiting Cooperative Off-Policy Multi-Agent Reinforcement Learning"
authors: ["Yueheng Li", "Guangming Xie", "Zongqing Lu"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "JPkJAyutW0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b54da94f46d6cf880109d9d512f14e2e0c4fb912.pdf"
published: "2025"
categories: []
keywords: ["cooperative multi-agent reinforcement learning", "off-policy multi-agent reinforcement learning", "value factorization", "extrapolation error"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:35+09:00"
---

# Revisiting Cooperative Off-Policy Multi-Agent Reinforcement Learning

## Abstract
Cooperative Multi-Agent Reinforcement Learning (MARL) has become a critical tool for addressing complex real-world problems. 
However, off-policy MARL methods, which rely on joint Q-functions, face significant scalability challenges due to the exponentially growing joint action space.
In this work, we highlight a critical yet often overlooked issue: erroneous Q-target estimation, primarily caused by extrapolation error.
Our analysis reveals that this error becomes increasingly severe as the number of agents grows, leading to unique challenges in MARL due to its expansive joint action space and the decentralized execution paradigm.
To address these challenges, we propose a suite of techniques tailored for off-policy MARL, including annealed multi-step bootstrapping, averaged Q-targets, and restricted action representation. Experimental results demonstrate that these methods effectively mitigate erroneous estimations, yielding substantial performance improvements in challenging benchmarks such as SMAC, SMACv2, and Google Research Football.

## Metadata
- venue: ICML
- year: 2025
- authors: Yueheng Li, Guangming Xie, Zongqing Lu
- arxiv_id: 
- openreview_id: JPkJAyutW0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b54da94f46d6cf880109d9d512f14e2e0c4fb912.pdf
- published: 2025
- keywords: cooperative multi-agent reinforcement learning, off-policy multi-agent reinforcement learning, value factorization, extrapolation error
