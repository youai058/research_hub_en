---
title: "Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization"
authors: ["Junyoung Yang", "Kyungmin Kim", "Sangdon Park"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RMWcdp5IUy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/da2c879d308fd411ad20e6e6734a0afaeb265d0f.pdf"
published: "2026"
categories: []
keywords: ["Online Conformal Prediction", "Adversarial Bandit", "Semi-bandit Feedback", "Regret"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:48+09:00"
---

# Online Conformal Prediction with Adversarial Semi-bandit Feedback via Regret Minimization

## Abstract
Uncertainty quantification is crucial in safety-critical systems, where decisions must be made under uncertainty. 
In particular, we consider the problem of online uncertainty quantification, 
where data points arrive sequentially. 
Online conformal prediction is a principled online uncertainty quantification method that dynamically constructs a prediction set at each time step.
While existing methods for online conformal prediction provide long-run coverage guarantees without any distributional assumptions, they typically assume a *full feedback* setting in which the true label is always observed. 
In this paper, we propose a novel learning method for online conformal prediction with *partial feedback* from an adaptive adversary—a more challenging setup where the true label is revealed only when it lies inside the constructed prediction set.
Specifically, we formulate online conformal prediction as an adversarial bandit problem by treating each candidate prediction set as an arm. 
Building on an existing algorithm for adversarial bandits, 
our method achieves a long-run coverage guarantee by explicitly establishing its connection to the regret of the learner.
Finally, we empirically demonstrate the effectiveness of our method in both independent and identically distributed (i.i.d.) and non-i.i.d. settings, 
showing that it successfully controls the miscoverage rate while maintaining a reasonable size of the prediction set.

## Metadata
- venue: ICLR
- year: 2026
- authors: Junyoung Yang, Kyungmin Kim, Sangdon Park
- arxiv_id: 
- openreview_id: RMWcdp5IUy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/da2c879d308fd411ad20e6e6734a0afaeb265d0f.pdf
- published: 2026
- keywords: Online Conformal Prediction, Adversarial Bandit, Semi-bandit Feedback, Regret
