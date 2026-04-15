---
title: "On Tractable $\\Phi$-Equilibria in Non-Concave Games"
authors: ["Yang Cai", "Constantinos Costis Daskalakis", "Haipeng Luo", "Chen-Yu Wei", "Weiqiang Zheng"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "3CtTMF5zzM"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/866edf8c9d76de6dca52c84e7633872c02b45952.pdf"
published: "2024"
categories: []
keywords: ["Non-Concave Games", "$\\Phi$-Equilibrium", "$\\Phi$-Regret Minimization", "Learning in Games"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:40+09:00"
---

# On Tractable $\Phi$-Equilibria in Non-Concave Games

## Abstract
While Online Gradient Descent and other no-regret learning procedures are known to efficiently converge to a coarse correlated equilibrium in games where each agent's utility is concave in their own strategy, this is not the case when utilities are non-concave -- a common scenario in machine learning applications involving strategies parameterized by deep neural networks, or when agents' utilities are computed by neural networks, or both. Non-concave games introduce significant game-theoretic and optimization challenges: (i) Nash equilibria may not exist; (ii) local Nash equilibria, though they exist, are intractable; and (iii) mixed Nash, correlated, and coarse correlated equilibria generally have infinite support and are intractable. To sidestep these challenges, we revisit the classical solution concept of $\Phi$-equilibria introduced by Greenwald and Jafari [GJ03], which is guaranteed to exist for an arbitrary set of strategy modifications $\Phi$ even in non-concave games [SL07]. However, the tractability of $\Phi$-equilibria in such games remains elusive. In this paper, we initiate the study of tractable $\Phi$-equilibria in non-concave games and examine several natural families of strategy modifications. We show that when $\Phi$ is finite, there exists an efficient uncoupled learning algorithm that approximates the corresponding $\Phi$-equilibria. Additionally, we explore cases where $\Phi$ is infinite but consists of local modifications, showing that Online Gradient Descent can efficiently approximate $\Phi$-equilibria in non-trivial regimes.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Yang Cai, Constantinos Costis Daskalakis, Haipeng Luo, Chen-Yu Wei, Weiqiang Zheng
- arxiv_id: 
- openreview_id: 3CtTMF5zzM
- anthology_id: 
- pdf_url: https://openreview.net/pdf/866edf8c9d76de6dca52c84e7633872c02b45952.pdf
- published: 2024
- keywords: Non-Concave Games, $\Phi$-Equilibrium, $\Phi$-Regret Minimization, Learning in Games
