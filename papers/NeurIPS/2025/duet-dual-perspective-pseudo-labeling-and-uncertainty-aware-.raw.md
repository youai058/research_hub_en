---
title: "DUET: Dual-Perspective Pseudo Labeling and  Uncertainty-aware Exploration & Exploitation  Training for Source-Free Domain Adaptation"
authors: ["Jae Yun Lee", "Jae Hyeon Park", "Gyoomin Lee", "Bogyeong Kim", "Min Hee Cha", "Hyeok Nam", "Joo Hyeon Jeon", "Hyunse Lee", "Sung In Cho"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "0M2M2EVreG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4687bc459fcda1e4e3da1baee33cf0ca5d403438.pdf"
published: "2025"
categories: []
keywords: ["Source-Free Domain Adaptation", "Pseudo Labeling", "Uncertainty-Aware Learning", "CLIP"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:56+09:00"
---

# DUET: Dual-Perspective Pseudo Labeling and  Uncertainty-aware Exploration & Exploitation  Training for Source-Free Domain Adaptation

## Abstract
Source-free domain adaptation (SFDA) aims to adapt a pre-trained source model to an unlabeled target domain without requiring labeled source data. 
In a self supervised setting, relying on pseudo labels on target domain samples facilitates the domain adaptation performance providing strong supervision. 
However, a critical problem of this approach is the inherent instability of the pre-trained source model in the target domain, leading to unreliable pseudo labels for the target domain data. 
To tackle this, we propose a novel Dual-perspective pseudo labeling strategy that jointly leverages a task-specific perspective and a domain-invariant perspective, assigning pseudo labels only to target samples on which the target model’s predictions and CLIP’s predictions agree. 
To further enhance representation learning without introducing noisy supervision, we apply consistency training to uncertain samples.
Additionally, we introduce a Tsallis mutual information(TMI)-based vision optimization strategy guided by an Uncertainty-based adaptation index (UAI), which dynamically modulates entropy sensitivity based on the model’s adaptation uncertainty. 
The UAI-based training paradigm enables stable and adaptive domain alignment by effectively balancing exploration and exploitation processes during the optimization process. Our proposed method achieves state-of-the-art performance on domain adaptation benchmark datasets, improving adaptation accuracy by 1.6% on Office-Home, 1.4% on VisDA-C, and 2.9% on DomainNet-126, demonstrating its effectiveness in SFDA.
The code is publicly available at https://github.com/l3umblee/duet-sfda.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Jae Yun Lee, Jae Hyeon Park, Gyoomin Lee, Bogyeong Kim, Min Hee Cha, Hyeok Nam, Joo Hyeon Jeon, Hyunse Lee, Sung In Cho
- arxiv_id: 
- openreview_id: 0M2M2EVreG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4687bc459fcda1e4e3da1baee33cf0ca5d403438.pdf
- published: 2025
- keywords: Source-Free Domain Adaptation, Pseudo Labeling, Uncertainty-Aware Learning, CLIP
