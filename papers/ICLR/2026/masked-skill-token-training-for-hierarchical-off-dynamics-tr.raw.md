---
title: "Masked Skill Token Training for Hierarchical Off-Dynamics Transfer"
authors: ["Zeyu Feng", "Haiyan Yin", "Yew-Soon Ong", "Harold Soh"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "K4ngUOra9m"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/b71d9ffa3e6fe943193b07c51bd50dec614d185e.pdf"
published: "2026"
categories: []
keywords: ["Tranfser Learning", "Skills", "Hierarchical RL", "Embodied AI"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:15+09:00"
---

# Masked Skill Token Training for Hierarchical Off-Dynamics Transfer

## Abstract
Generalizing policies across environments with altered dynamics remains a key challenge in reinforcement learning, particularly in offline settings where direct interaction or fine-tuning is impractical. We introduce Masked Skill Token Training (MSTT), a fully offline hierarchical RL framework that enables policy transfer using observation-only demonstrations. MSTT constructs a discrete skill space via unsupervised trajectory tokenization and trains a skill-conditioned value function using masked Bellman updates, which simulate dynamics shifts by selectively disabling skills. A diffusion-based trajectory generator, paired with feasibility-based filtering, enables the agent to execute valid, temporally extended actions without requiring action labels or access to the target environment. Our results in both discrete and continuous domains demonstrate the potential of mask-guided planning for robust generalization under dynamics shifts. To our knowledge, MSTT is the first work to explore masking as a mechanism for simulating and generalizing across off-dynamics environments. It marks a promising step toward scalable, structure-aware transfer and opens avenues to explore multi-goal conditioning, and extensions to more complex, real-world scenarios.

## Metadata
- venue: ICLR
- year: 2026
- authors: Zeyu Feng, Haiyan Yin, Yew-Soon Ong, Harold Soh
- arxiv_id: 
- openreview_id: K4ngUOra9m
- anthology_id: 
- pdf_url: https://openreview.net/pdf/b71d9ffa3e6fe943193b07c51bd50dec614d185e.pdf
- published: 2026
- keywords: Tranfser Learning, Skills, Hierarchical RL, Embodied AI
