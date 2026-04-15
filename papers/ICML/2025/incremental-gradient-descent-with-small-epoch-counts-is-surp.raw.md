---
title: "Incremental Gradient Descent with Small Epoch Counts is Surprisingly Slow on Ill-Conditioned Problems"
authors: ["Yujun Kim", "Jaeyoung Cha", "Chulhee Yun"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LiXD7mpjU0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2a86f116d8a0db9d31787c984118e0d5da310bd1.pdf"
published: "2025"
categories: []
keywords: ["Permutation-based SGD", "Incremental Gradient Descent", "Lower Bound", "Convex Optimization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:18+09:00"
---

# Incremental Gradient Descent with Small Epoch Counts is Surprisingly Slow on Ill-Conditioned Problems

## Abstract
Recent theoretical results demonstrate that the convergence rates of permutation-based SGD (e.g., random reshuffling SGD) are faster than uniform-sampling SGD; however, these studies focus mainly on the large epoch regime, where the number of epochs $K$ exceeds the condition number $\kappa$. In contrast, little is known when $K$ is smaller than $\kappa$, and it is still a challenging open question whether permutation-based SGD can converge faster in this small epoch regime (Safran and Shamir, 2021). As a step toward understanding this gap, we study the naive deterministic variant, Incremental Gradient Descent (IGD), on smooth and strongly convex functions. Our lower bounds reveal that for the small epoch regime, IGD can exhibit surprisingly slow convergence even when all component functions are strongly convex. Furthermore, when some component functions are allowed to be nonconvex, we prove that the optimality gap of IGD can be significantly worse throughout the small epoch regime. Our analyses reveal that the convergence properties of permutation-based SGD in the small epoch regime may vary drastically depending on the assumptions on component functions. Lastly, we supplement the paper with tight upper and lower bounds for IGD in the large epoch regime.

## Metadata
- venue: ICML
- year: 2025
- authors: Yujun Kim, Jaeyoung Cha, Chulhee Yun
- arxiv_id: 
- openreview_id: LiXD7mpjU0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2a86f116d8a0db9d31787c984118e0d5da310bd1.pdf
- published: 2025
- keywords: Permutation-based SGD, Incremental Gradient Descent, Lower Bound, Convex Optimization
