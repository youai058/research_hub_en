---
title: "Nearly Optimal Algorithms for Contextual Dueling Bandits from Adversarial Feedback"
authors: ["Qiwei Di", "Jiafan He", "Quanquan Gu"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "ATNEHkXFrW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/276895f3ccd7fcf6d9b7d2d4b9847f47b321da91.pdf"
published: "2025"
categories: []
keywords: ["Dueling Bandits", "Adversarial feedback", "optimal", "uncertainty-weighted maximum likelihood estimation."]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:39+09:00"
---

# Nearly Optimal Algorithms for Contextual Dueling Bandits from Adversarial Feedback

## Abstract
Learning from human feedback plays an important role in aligning generative models, such as large language models (LLM). However, the effectiveness of this approach can be influenced by adversaries, who may intentionally provide misleading preferences to manipulate the output in an undesirable or harmful direction.
To tackle this challenge, we study a specific model within this problem domain--contextual dueling bandits with adversarial feedback, where the true preference label can be flipped by an adversary. We propose an algorithm namely robust contextual dueling bandits ($\texttt{RCDB}$), which is based on uncertainty-weighted maximum likelihood estimation.  Our algorithm achieves an $\tilde O(d\sqrt{T}/\kappa+dC/\kappa)$ regret bound, where $T$ is the number of rounds, $d$ is the dimension of the context, $\kappa$ is the lower bound of the derivative of the link function, and $  0 \le C \le T$ is the total number of adversarial feedback. 
We also prove a lower bound to show that our regret bound is nearly optimal, both in scenarios with and without ($C=0$) adversarial feedback. Our work is the first to achieve nearly minimax optimal regret for dueling bandits in the presence of adversarial preference feedback. 
Additionally, for the sigmoid link function, we develop a novel algorithm that takes into account the effect of local derivatives into maximum likelihood estimation (MLE) analysis through a refined method for estimating the link function's derivative. This method helps us to eliminate the $\kappa$ dependence in the leading term with respect to $T$, which reduces the exponential dependence on the parameter radius $B$ to a polynomial dependence. We conduct experiments to evaluate our proposed algorithm $\texttt{RCDB}$ against various types of adversarial feedback. Experimental results demonstrate its superiority over the state-of-the-art dueling bandit algorithms in the presence of adversarial feedback.

## Metadata
- venue: ICML
- year: 2025
- authors: Qiwei Di, Jiafan He, Quanquan Gu
- arxiv_id: 
- openreview_id: ATNEHkXFrW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/276895f3ccd7fcf6d9b7d2d4b9847f47b321da91.pdf
- published: 2025
- keywords: Dueling Bandits, Adversarial feedback, optimal, uncertainty-weighted maximum likelihood estimation.
