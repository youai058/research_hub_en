---
title: "PIPER: Primitive-Informed Preference-based Hierarchical Reinforcement Learning via Hindsight Relabeling"
authors: ["Utsav Singh", "Wesley A Suttle", "Brian M. Sadler", "Vinay P. Namboodiri", "Amrit Bedi"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "l6Hef6FVd0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/486d2e3f8b1d6cd84cc050e257c70fda5c2f6980.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:27+09:00"
---

# PIPER: Primitive-Informed Preference-based Hierarchical Reinforcement Learning via Hindsight Relabeling

## Abstract
In this work, we introduce PIPER: Primitive-Informed Preference-based Hierarchical reinforcement learning via Hindsight Relabeling, a novel approach that leverages preference-based learning to learn a reward model, and subsequently uses this reward model to relabel higher-level replay buffers. Since this reward is unaffected by lower primitive behavior, our relabeling-based approach is able to mitigate non-stationarity, which is common in existing hierarchical approaches, and demonstrates impressive performance across a range of challenging sparse-reward tasks. Since obtaining human feedback is typically impractical, we propose to replace the human-in-the-loop approach with our primitive-in-the-loop approach, which generates feedback using sparse rewards provided by the environment. Moreover, in order to prevent infeasible subgoal prediction and avoid degenerate solutions, we propose primitive-informed regularization that conditions higher-level policies to generate feasible subgoals for lower-level policies. We perform extensive experiments to show that PIPER mitigates non-stationarity in hierarchical reinforcement learning and achieves greater than 50$\\%$ success rates in challenging, sparse-reward robotic environments, where most other baselines fail to achieve any significant progress.

## Metadata
- venue: ICML
- year: 2024
- authors: Utsav Singh, Wesley A Suttle, Brian M. Sadler, Vinay P. Namboodiri, Amrit Bedi
- arxiv_id: 
- openreview_id: l6Hef6FVd0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/486d2e3f8b1d6cd84cc050e257c70fda5c2f6980.pdf
- published: 2024
