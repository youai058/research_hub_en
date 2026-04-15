---
title: "Confronting Reward Model Overoptimization with Constrained RLHF"
authors: ["Ted Moskovitz", "Aaditya K Singh", "DJ Strouse", "Tuomas Sandholm", "Ruslan Salakhutdinov", "Anca Dragan", "Stephen Marcus McAleer"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gkfUvn0fLU"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9110e24405b3d1c469f8710d548cf6e5b7867692.pdf"
published: "2024"
categories: []
keywords: ["rlhf", "overoptimization", "constrained RL"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:19+09:00"
---

# Confronting Reward Model Overoptimization with Constrained RLHF

## Abstract
Large language models are typically aligned with human preferences by optimizing reward models (RMs) fitted to human feedback. However, human preferences are multi-faceted, and it is increasingly common to derive reward from a composition of simpler reward models which each capture a different aspect of language quality. This itself presents a challenge, as it is difficult to appropriately weight these component RMs when combining them. Compounding this difficulty, because any RM is only a proxy for human evaluation, this process is vulnerable to *overoptimization*, wherein past a certain point, accumulating higher reward is associated with worse human ratings. In this paper, we perform the first study on overoptimization in composite RMs, showing that correlation between component RMs has a significant effect on the locations of these points. We then introduce an approach to solve this issue using constrained reinforcement learning as a means of preventing the agent from exceeding each RM's threshold of usefulness. Our method addresses the problem of weighting component RMs by learning dynamic weights, naturally given by the Lagrange multipliers. As a result, each RM stays within the range at which it is an effective proxy, improving evaluation performance. Finally, we introduce an adaptive method using gradient-free optimization to identify and optimize towards these points during a single run.

## Metadata
- venue: ICLR
- year: 2024
- authors: Ted Moskovitz, Aaditya K Singh, DJ Strouse, Tuomas Sandholm, Ruslan Salakhutdinov, Anca Dragan, Stephen Marcus McAleer
- arxiv_id: 
- openreview_id: gkfUvn0fLU
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9110e24405b3d1c469f8710d548cf6e5b7867692.pdf
- published: 2024
- keywords: rlhf, overoptimization, constrained RL
