---
title: "The Cost of Robustness: Tighter Bounds on Parameter Complexity for Robust Memorization in ReLU Nets"
authors: ["Yujun Kim", "Chaewon Moon", "Chulhee Yun"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Jsln9ZyMl4"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/67021de451ba98cbb10a68f5660bb52fae246c0c.pdf"
published: "2025"
categories: []
keywords: ["Robust memorization", "Memorization", "Adversarial training", "Parameter Complexity"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:43+09:00"
---

# The Cost of Robustness: Tighter Bounds on Parameter Complexity for Robust Memorization in ReLU Nets

## Abstract
We study the parameter complexity of robust memorization for ReLU networks: the number of parameters required to interpolate any dataset with $\epsilon$-separation between differently labeled points, while ensuring predictions remain consistent within a $\mu$-ball around each training example. We establish upper and lower bounds on the parameter count as a function of the robustness ratio $\rho = \mu / \epsilon$. Unlike prior work, we provide a fine-grained analysis across the entire range $\rho \in (0,1)$ and obtain tighter upper and lower bounds that improve upon existing results. Our findings reveal that the parameter complexity of robust memorization matches that of non-robust memorization when $\rho$ is small, but grows with increasing $\rho$. As a special case, when the input dimension is comparable to or exceeds the dataset size, our bounds become tight (up to logarithmic factors) across the entire range of $\rho$.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Yujun Kim, Chaewon Moon, Chulhee Yun
- arxiv_id: 
- openreview_id: Jsln9ZyMl4
- anthology_id: 
- pdf_url: https://openreview.net/pdf/67021de451ba98cbb10a68f5660bb52fae246c0c.pdf
- published: 2025
- keywords: Robust memorization, Memorization, Adversarial training, Parameter Complexity
