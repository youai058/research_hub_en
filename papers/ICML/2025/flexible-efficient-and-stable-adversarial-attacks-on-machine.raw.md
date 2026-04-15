---
title: "Flexible, Efficient, and Stable Adversarial Attacks on Machine Unlearning"
authors: ["Zihan Zhou", "Yang Zhou", "Zijie Zhang", "Lingjuan Lyu", "Da Yan", "Ruoming Jin", "Dejing Dou"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ba3sSfEnj1"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/1faed6882e952bbb44df8a042dd411075e8fa325.pdf"
published: "2025"
categories: []
keywords: ["Machine unlearning", "poisoning attack", "thrust vector control theory", "John's Theorem", "polyhedral approximation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:19+09:00"
---

# Flexible, Efficient, and Stable Adversarial Attacks on Machine Unlearning

## Abstract
Machine unlearning (MU) aims to remove the influence of specific data points from trained models, enhancing compliance with privacy regulations. However, the vulnerability of basic MU models to malicious unlearning requests in adversarial learning environments has been largely overlooked. Existing adversarial MU attacks suffer from three key limitations: inflexibility due to pre-defined attack targets, inefficiency in handling multiple attack requests, and instability caused by non-convex loss functions. To address these challenges, we propose a Flexible, Efficient, and Stable Attack (DDPA). First, leveraging Carathéodory's theorem, we introduce a convex polyhedral approximation to identify points in the loss landscape where convexity approximately holds, ensuring stable attack performance. Second, inspired by simplex theory and John's theorem, we develop a regular simplex detection technique that maximizes coverage over the parameter space, improving attack flexibility and efficiency. We theoretically derive the proportion of the effective parameter space occupied by the constructed simplex. We evaluate the attack success rate of our DDPA method on real datasets against state-of-the-art machine unlearning attack methods. Our source code is available at https://github.com/zzz0134/DDPA.

## Metadata
- venue: ICML
- year: 2025
- authors: Zihan Zhou, Yang Zhou, Zijie Zhang, Lingjuan Lyu, Da Yan, Ruoming Jin, Dejing Dou
- arxiv_id: 
- openreview_id: ba3sSfEnj1
- anthology_id: 
- pdf_url: https://openreview.net/pdf/1faed6882e952bbb44df8a042dd411075e8fa325.pdf
- published: 2025
- keywords: Machine unlearning, poisoning attack, thrust vector control theory, John's Theorem, polyhedral approximation
