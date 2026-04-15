---
title: "Revisiting the Last-Iterate Convergence of Stochastic Gradient Methods"
authors: ["Zijian Liu", "Zhengyuan Zhou"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xxaEhwC1I4"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/49e36604c5405004e38defe39ca3ff6ecf070ca6.pdf"
published: "2024"
categories: []
keywords: ["Convex Optimization", "Stochastic Optimization", "Last Iterate"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:20+09:00"
---

# Revisiting the Last-Iterate Convergence of Stochastic Gradient Methods

## Abstract
In the past several years, the last-iterate convergence of the Stochastic Gradient Descent (SGD) algorithm has triggered people's interest due to its good performance in practice but lack of theoretical understanding. For Lipschitz convex functions, different works have established the optimal $O(\log(1/\delta)\log T/\sqrt{T})$ or $O(\sqrt{\log(1/\delta)/T})$ high-probability convergence rates for the final iterate, where $T$ is the time horizon and $\delta$ is the failure probability. However, to prove these bounds, all the existing works are either limited to compact domains or require almost surely bounded noises. It is natural to ask whether the last iterate of SGD can still guarantee the optimal convergence rate but without these two restrictive assumptions. Besides this important question, there are still lots of theoretical problems lacking an answer. For example, compared with the last-iterate convergence of SGD for non-smooth problems, only few results for smooth optimization have yet been developed. Additionally, the existing results are all limited to a non-composite objective and the standard Euclidean norm. It still remains unclear whether the last-iterate convergence can be provably extended to wider composite optimization and non-Euclidean norms. In this work, to address the issues mentioned above, we revisit the last-iterate convergence of stochastic gradient methods and provide the first unified way to prove the convergence rates both in expectation and in high probability to accommodate general domains, composite objectives, non-Euclidean norms, Lipschitz conditions, smoothness, and (strong) convexity simultaneously.

## Metadata
- venue: ICLR
- year: 2024
- authors: Zijian Liu, Zhengyuan Zhou
- arxiv_id: 
- openreview_id: xxaEhwC1I4
- anthology_id: 
- pdf_url: https://openreview.net/pdf/49e36604c5405004e38defe39ca3ff6ecf070ca6.pdf
- published: 2024
- keywords: Convex Optimization, Stochastic Optimization, Last Iterate
