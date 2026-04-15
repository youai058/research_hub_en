---
title: "Contextual Bandits for Unbounded Context Distributions"
authors: ["Puning Zhao", "Rongfei Fan", "Shaowei Wang", "Li Shen", "Qixin Zhang", "ZongKe", "Tianhang Zheng"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gGY9TNVYs3"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/aa7efae8f4a0f9164b6c87caf507b40b44b39093.pdf"
published: "2025"
categories: []
keywords: ["Contextual bandits", "nonparametric statistics"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:30+09:00"
---

# Contextual Bandits for Unbounded Context Distributions

## Abstract
Nonparametric contextual bandit is an important model of sequential decision making problems. Under $\alpha$-Tsybakov margin condition, existing research has established a regret bound of $\tilde{O}\left(T^{1-\frac{\alpha+1}{d+2}}\right)$ for bounded supports. However, the optimal regret with unbounded contexts has not been analyzed. The challenge of solving contextual bandit problems with unbounded support is to achieve both exploration-exploitation tradeoff and bias-variance tradeoff simultaneously. In this paper, we solve the nonparametric contextual bandit problem with unbounded contexts. We propose two nearest neighbor methods combined with UCB exploration. The first method uses a fixed $k$. Our analysis shows that this method achieves minimax optimal regret under a weak margin condition and relatively light-tailed context distributions. The second method uses adaptive $k$. By a proper data-driven selection of $k$, this method achieves an expected regret of $\tilde{O}\left(T^{1-\frac{(\alpha+1)\beta}{\alpha+(d+2)\beta}}+T^{1-\beta}\right)$, in which $\beta$ is a parameter describing the tail strength. This bound matches the minimax lower bound up to logarithm factors, indicating that the second method is approximately optimal.

## Metadata
- venue: ICML
- year: 2025
- authors: Puning Zhao, Rongfei Fan, Shaowei Wang, Li Shen, Qixin Zhang, ZongKe, Tianhang Zheng
- arxiv_id: 
- openreview_id: gGY9TNVYs3
- anthology_id: 
- pdf_url: https://openreview.net/pdf/aa7efae8f4a0f9164b6c87caf507b40b44b39093.pdf
- published: 2025
- keywords: Contextual bandits, nonparametric statistics
