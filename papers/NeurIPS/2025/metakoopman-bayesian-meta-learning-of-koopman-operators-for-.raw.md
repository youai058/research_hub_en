---
title: "MetaKoopman: Bayesian Meta-Learning of Koopman Operators for Modeling Structured Dynamics under Distribution Shifts"
authors: ["Mahmoud Selim", "Sriharsha Bhat", "Karl Henrik Johansson"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "BJ3z1hYuKx"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/99a35cc652a2eb21468db9141b983e47dd5c4fee.pdf"
published: "2025"
categories: []
keywords: ["Meta Learning", "Koopman Theory", "Motion Planning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:43+09:00"
---

# MetaKoopman: Bayesian Meta-Learning of Koopman Operators for Modeling Structured Dynamics under Distribution Shifts

## Abstract
Modeling and forecasting nonlinear dynamics under distribution shifts is essential for robust decision-making in real-world systems. In this work, we propose **MetaKoopman**, a Bayesian meta-learning framework for modeling nonlinear dynamics through linear latent representations. MetaKoopman learns a Matrix Normal-Inverse Wishart (*MNIW*) prior over the Koopman operator, enabling closed-form Bayesian updates conditioned on recent trajectory segments. Moreover, it provides a closed-form posterior predictive distribution over future state trajectories, capturing both epistemic and aleatoric uncertainty in the learned dynamics. We evaluate MetaKoopman on a full-scale autonomous truck and trailer system across a wide range of adverse winter scenarios—including snow, ice, and mixed-friction conditions—as well as in simulated control tasks with diverse distribution shifts. MetaKoopman consistently outperforms prior approaches in multi-step prediction accuracy, uncertainty calibration and robustness to distributional shifts. Field experiments further demonstrate its effectiveness in dynamically feasible motion planning, particularly during evasive maneuvers and operation at the limits of traction. Project website: [https://mahmoud-selim.github.io/MetaKoopman/](https://mahmoud-selim.github.io/MetaKoopman/)

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Mahmoud Selim, Sriharsha Bhat, Karl Henrik Johansson
- arxiv_id: 
- openreview_id: BJ3z1hYuKx
- anthology_id: 
- pdf_url: https://openreview.net/pdf/99a35cc652a2eb21468db9141b983e47dd5c4fee.pdf
- published: 2025
- keywords: Meta Learning, Koopman Theory, Motion Planning
