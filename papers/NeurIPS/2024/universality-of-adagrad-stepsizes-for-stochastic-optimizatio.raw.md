---
title: "Universality of AdaGrad Stepsizes for Stochastic Optimization: Inexact Oracle, Acceleration and Variance Reduction"
authors: ["Anton Rodomanov", "Xiaowen Jiang", "Sebastian U Stich"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rniiAVjHi5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/dd912aeb19dbd3162f55e416834322f2e59ce066.pdf"
published: "2024"
categories: []
keywords: ["convex optimization", "stochastic optimization", "adaptive methods", "universal algorithms", "acceleration", "variance reduction", "AdaGrad", "SVRG", "weakly smooth functions", "Hölder condition", "inexact oracle", "complexity estimates"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:43+09:00"
---

# Universality of AdaGrad Stepsizes for Stochastic Optimization: Inexact Oracle, Acceleration and Variance Reduction

## Abstract
We present adaptive gradient methods (both basic and accelerated) for solving
convex composite optimization problems in which the main part is approximately
smooth (a.k.a. $(\delta, L)$-smooth) and can be accessed only via a
(potentially biased) stochastic gradient oracle.
This setting covers many interesting examples including Hölder smooth problems
and various inexact computations of the stochastic gradient.
Our methods use AdaGrad stepsizes and are adaptive in the sense that they do
not require knowing any problem-dependent constants except an estimate of the
diameter of the feasible set but nevertheless achieve the best possible
convergence rates as if they knew the corresponding constants.
We demonstrate that AdaGrad stepsizes work in a variety of situations
by proving, in a unified manner, three types of new results.
First, we establish efficiency guarantees for our methods in the classical
setting where the oracle's variance is uniformly bounded.
We then show that, under more refined assumptions on the variance,
the same methods without any modifications enjoy implicit variance
reduction properties allowing us to express their complexity estimates in
terms of the variance only at the minimizer.
Finally, we show how to incorporate explicit SVRG-type variance reduction into
our methods and obtain even faster algorithms.
In all three cases, we present both basic and accelerated algorithms
achieving state-of-the-art complexity bounds.
As a direct corollary of our results, we obtain universal stochastic gradient
methods for Hölder smooth problems which can be used in all situations.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Anton Rodomanov, Xiaowen Jiang, Sebastian U Stich
- arxiv_id: 
- openreview_id: rniiAVjHi5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/dd912aeb19dbd3162f55e416834322f2e59ce066.pdf
- published: 2024
- keywords: convex optimization, stochastic optimization, adaptive methods, universal algorithms, acceleration, variance reduction, AdaGrad, SVRG, weakly smooth functions, Hölder condition, inexact oracle, complexity estimates
