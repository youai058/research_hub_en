---
title: "Beyond Single Stationary Policies: Meta-Task Players as Naturally Superior Collaborators"
authors: ["Haoming Wang", "Zhaoming Tian", "Yunpeng Song", "Xiangliang Zhang", "Zhongmin Cai"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "HpN4xeDJQF"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/88f4303d3b681c32cb72a9248358fbe1b40c321c.pdf"
published: "2024"
categories: []
keywords: ["human-AI collaboration", "Bayesian policy reuse", "reinforcement learning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:07+09:00"
---

# Beyond Single Stationary Policies: Meta-Task Players as Naturally Superior Collaborators

## Abstract
In human-AI collaborative tasks, the distribution of human behavior, influenced by mental models, is non-stationary, manifesting in various levels of initiative and different collaborative strategies. A significant challenge in human-AI collaboration is determining how to collaborate effectively with humans exhibiting non-stationary dynamics. Current collaborative agents involve initially running self-play (SP) multiple times to build a policy pool, followed by training the final adaptive policy against this pool. These agents themselves are a single policy network, which is $\textbf{insufficient for handling non-stationary human dynamics}$. We discern that despite the inherent diversity in human behaviors, the $\textbf{underlying meta-tasks within specific collaborative contexts tend to be strikingly similar}$. Accordingly, we propose $\textbf{C}$ollaborative $\textbf{B}$ayesian $\textbf{P}$olicy $\textbf{R}$euse ($\textbf{CBPR}$), a novel Bayesian-based framework that $\textbf{adaptively selects optimal collaborative policies matching the current meta-task from multiple policy networks}$ instead of just selecting actions relying on a single policy network. We provide theoretical guarantees for CBPR's rapid convergence to the optimal policy once human partners alter their policies. This framework shifts from directly modeling human behavior to identifying various meta-tasks that support human decision-making and training meta-task playing (MTP) agents tailored to enhance collaboration. Our method undergoes rigorous testing in a well-recognized collaborative cooking simulator, $\textit{Overcooked}$. Both empirical results and user studies demonstrate CBPR's superior competitiveness compared to existing baselines.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Haoming Wang, Zhaoming Tian, Yunpeng Song, Xiangliang Zhang, Zhongmin Cai
- arxiv_id: 
- openreview_id: HpN4xeDJQF
- anthology_id: 
- pdf_url: https://openreview.net/pdf/88f4303d3b681c32cb72a9248358fbe1b40c321c.pdf
- published: 2024
- keywords: human-AI collaboration, Bayesian policy reuse, reinforcement learning
