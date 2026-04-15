---
title: "ComaDICE: Offline Cooperative Multi-Agent Reinforcement Learning with Stationary Distribution Shift Regularization"
authors: ["The Viet Bui", "Thanh Hong Nguyen", "Tien Anh Mai"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "5o9JJJPPm6"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/47b6e4f77893ddc057541ed679a8725a2d346ae7.pdf"
published: "2025"
categories: []
keywords: ["Offline Reinforcement Learning", "Multi-Agent Reinforcement Learning", "Stationary Distribution Correction Estimation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:43+09:00"
---

# ComaDICE: Offline Cooperative Multi-Agent Reinforcement Learning with Stationary Distribution Shift Regularization

## Abstract
Offline reinforcement learning (RL) has garnered significant attention for its ability to learn effective policies from pre-collected datasets without the need for further environmental interactions. While promising results have been demonstrated in single-agent settings, offline multi-agent reinforcement learning (MARL) presents additional challenges due to the large joint state-action space and the complexity of multi-agent behaviors. A key issue in offline RL is the distributional shift, which arises when the target policy being optimized deviates from the behavior policy that generated the data. This problem is exacerbated in MARL due to the interdependence between agents' local policies and the expansive joint state-action space. Prior approaches have primarily addressed this challenge by incorporating regularization in the space of either Q-functions or policies. In this work, we propose a novel type of regularizer in the space of stationary distributions to address the distributional shift more effectively. Our algorithm, ComaDICE, provides a principled framework for offline cooperative MARL to correct the stationary distribution of the global policy, which is then leveraged to derive local policies for individual agents. Through extensive experiments on the offline multi-agent MuJoCo and StarCraft II benchmarks, we demonstrate that ComaDICE achieves superior performance compared to state-of-the-art offline MARL methods across nearly all tasks.

## Metadata
- venue: ICLR
- year: 2025
- authors: The Viet Bui, Thanh Hong Nguyen, Tien Anh Mai
- arxiv_id: 
- openreview_id: 5o9JJJPPm6
- anthology_id: 
- pdf_url: https://openreview.net/pdf/47b6e4f77893ddc057541ed679a8725a2d346ae7.pdf
- published: 2025
- keywords: Offline Reinforcement Learning, Multi-Agent Reinforcement Learning, Stationary Distribution Correction Estimation
