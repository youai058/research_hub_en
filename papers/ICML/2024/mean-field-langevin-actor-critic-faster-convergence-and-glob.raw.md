---
title: "Mean Field Langevin Actor-Critic: Faster Convergence and Global Optimality beyond Lazy Learning"
authors: ["Kakei Yamamoto", "Kazusato Oko", "Zhuoran Yang", "Taiji Suzuki"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FOJE1kRcHG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/ae191f9eda6253e50c69c2fc489fbf4c08dfda43.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:26+09:00"
---

# Mean Field Langevin Actor-Critic: Faster Convergence and Global Optimality beyond Lazy Learning

## Abstract
This work explores the feature learning capabilities of deep reinforcement learning algorithms in the pursuit of optimal policy determination. We particularly examine an over-parameterized neural actor-critic framework within the mean-field regime, where both actor and critic components undergo updates via policy gradient and temporal-difference (TD) learning, respectively. We introduce the *mean-field Langevin TD learning* (MFLTD) method, enhancing mean-field Langevin dynamics with proximal TD updates for critic policy evaluation, and assess its performance against conventional approaches through numerical analysis. Additionally, for actor policy updates, we present the *mean-field Langevin policy gradient* (MFLPG), employing policy gradient techniques augmented by Wasserstein gradient flows for parameter space exploration. Our findings demonstrate that MFLTD accurately identifies the true value function, while MFLPG ensures linear convergence of actor sequences towards the globally optimal policy, considering a Kullback-Leibler divergence regularized framework. Through both time particle and discretized analysis, we substantiate the linear convergence guarantees of our neural actor-critic algorithms, representing a notable contribution to neural reinforcement learning focusing on *global optimality* and *feature learning*, extending the existing understanding beyond the conventional scope of lazy training.

## Metadata
- venue: ICML
- year: 2024
- authors: Kakei Yamamoto, Kazusato Oko, Zhuoran Yang, Taiji Suzuki
- arxiv_id: 
- openreview_id: FOJE1kRcHG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/ae191f9eda6253e50c69c2fc489fbf4c08dfda43.pdf
- published: 2024
