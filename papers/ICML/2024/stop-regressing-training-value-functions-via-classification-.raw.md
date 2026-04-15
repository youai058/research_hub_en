---
title: "Stop Regressing: Training Value Functions via Classification for Scalable Deep RL"
authors: ["Jesse Farebrother", "Jordi Orbay", "Quan Vuong", "Adrien Ali Taiga", "Yevgen Chebotar", "Ted Xiao", "Alex Irpan", "Sergey Levine", "Pablo Samuel Castro", "Aleksandra Faust", "Aviral Kumar", "Rishabh Agarwal"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "dVpFKfqF3R"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d7be2bfd406a29a0a8152605d8f88ab08afd5f3d.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:22+09:00"
---

# Stop Regressing: Training Value Functions via Classification for Scalable Deep RL

## Abstract
Value functions are an essential component in deep reinforcement learning (RL), that are typically trained via mean squared error regression to match bootstrapped target values. However, scaling value-based RL methods to large networks has proven challenging. This difficulty is in stark contrast to supervised learning: by leveraging a cross-entropy classification loss, supervised methods have scaled reliably to massive networks. Observing this discrepancy, in this paper, we investigate whether the scalability of deep RL can also be improved simply by using classification in place of regression for training value functions. We show that training value functions with categorical cross-entropy significantly enhances performance and scalability across various domains, including single-task RL on Atari 2600 games, multi-task RL on Atari with large-scale ResNets, robotic manipulation with Q-transformers, playing Chess without search, and a language-agent Wordle task with high-capacity Transformers, achieving *state-of-the-art results* on these domains. Through careful analysis, we show that categorical cross-entropy mitigates issues inherent to value-based RL, such as noisy targets and non-stationarity. We argue that shifting to categorical cross-entropy for training value functions can substantially improve the scalability of deep RL at little-to-no cost.

## Metadata
- venue: ICML
- year: 2024
- authors: Jesse Farebrother, Jordi Orbay, Quan Vuong, Adrien Ali Taiga, Yevgen Chebotar, Ted Xiao, Alex Irpan, Sergey Levine, Pablo Samuel Castro, Aleksandra Faust, Aviral Kumar, Rishabh Agarwal
- arxiv_id: 
- openreview_id: dVpFKfqF3R
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d7be2bfd406a29a0a8152605d8f88ab08afd5f3d.pdf
- published: 2024
