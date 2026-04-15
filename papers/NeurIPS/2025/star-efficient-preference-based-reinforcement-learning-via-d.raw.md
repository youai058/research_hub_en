---
title: "STAR: Efficient Preference-based Reinforcement Learning via Dual Regularization"
authors: ["Fengshuo Bai", "Rui Zhao", "Hongming Zhang", "Sijia Cui", "Shao Zhang", "bo xu", "Lei Han", "Ying Wen", "Yaodong Yang"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "E9EwDc45f8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/816de5e71586cb85fa0371c65e55d438930026ba.pdf"
published: "2025"
categories: []
keywords: ["preference-based RL"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:45+09:00"
---

# STAR: Efficient Preference-based Reinforcement Learning via Dual Regularization

## Abstract
Preference-based reinforcement learning (PbRL) bypasses complex reward engineering by learning from human feedback. However, due to the high cost of obtaining feedback, PbRL typically relies on a limited set of preference-labeled samples. This data scarcity introduces two key inefficiencies: (1) the reward model overfits to the limited feedback, leading to poor generalization to unseen samples, and (2) the agent exploits the learned reward model, exacerbating overestimation of action values in temporal difference (TD) learning. To address these issues, we propose STAR, an efficient PbRL method that integrates preference margin regularization and policy regularization. Preference margin regularization mitigates overfitting by introducing a bounded margin in reward optimization, preventing excessive bias toward specific feedback. Policy regularization bootstraps a conservative estimate $\widehat{Q}$ from well-supported state-action pairs in the replay memory, reducing overestimation during policy learning. Experimental results show that STAR improves feedback efficiency, achieving 34.8\% higher performance in online settings and 29.7\% in offline settings compared to state-of-the-art methods. Ablation studies confirm that STAR facilitates more robust reward and value function learning. The videos of this project are released at https://sites.google.com/view/pbrl-star.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Fengshuo Bai, Rui Zhao, Hongming Zhang, Sijia Cui, Shao Zhang, bo xu, Lei Han, Ying Wen, Yaodong Yang
- arxiv_id: 
- openreview_id: E9EwDc45f8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/816de5e71586cb85fa0371c65e55d438930026ba.pdf
- published: 2025
- keywords: preference-based RL
