---
title: "Tractable MCMC for Private Learning with Pure and Gaussian Differential Privacy"
authors: ["Yingyu Lin", "Yian Ma", "Yu-Xiang Wang", "Rachel Emily Redberg", "Zhiqi Bu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "pmweVpJ229"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/98377763ad27f9f0dab3a807c831a7d2b1e123ef.pdf"
published: "2024"
categories: []
keywords: ["Pure Differential Privacy", "Monte Carlo sampling", "Gaussian Differential Privacy", "Exponential Mechanism"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:12+09:00"
---

# Tractable MCMC for Private Learning with Pure and Gaussian Differential Privacy

## Abstract
Posterior sampling, i.e., exponential mechanism to sample from the posterior distribution, provides $\varepsilon$-pure differential privacy (DP) guarantees and does not suffer from potentially unbounded privacy breach introduced by $(\varepsilon,\delta)$-approximate DP. In practice, however, one needs to apply approximate sampling methods such as Markov chain Monte Carlo (MCMC), thus re-introducing the unappealing $\delta$-approximation error into the privacy guarantees. To bridge this gap, we propose the Approximate SAample Perturbation (abbr. ASAP) algorithm which perturbs an MCMC sample with noise proportional to its Wasserstein-infinity ($W_\infty$) distance from a reference distribution that satisfies pure DP or pure Gaussian DP (i.e., $\delta=0$). We then leverage a Metropolis-Hastings algorithm to generate the sample and prove that the algorithm converges in W$_\infty$ distance. We show that by combining our new techniques with a localization step, we obtain the first nearly linear-time algorithm that achieves the optimal rates in the DP-ERM problem with strongly convex and smooth losses.

## Metadata
- venue: ICLR
- year: 2024
- authors: Yingyu Lin, Yian Ma, Yu-Xiang Wang, Rachel Emily Redberg, Zhiqi Bu
- arxiv_id: 
- openreview_id: pmweVpJ229
- anthology_id: 
- pdf_url: https://openreview.net/pdf/98377763ad27f9f0dab3a807c831a7d2b1e123ef.pdf
- published: 2024
- keywords: Pure Differential Privacy, Monte Carlo sampling, Gaussian Differential Privacy, Exponential Mechanism
