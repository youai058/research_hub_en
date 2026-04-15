---
title: "DUEL: Exact Likelihood for Masked Diffusion via Deterministic Unmasking"
authors: ["Gilad Turok", "Chris De Sa", "Volodymyr Kuleshov"]
venue: "arXiv"
year: 2026
venue_class: "etc"
arxiv_id: "2603.01367"
openreview_id: ""
anthology_id: ""
pdf_url: "https://arxiv.org/pdf/2603.01367v2"
published: "2026-03-02"
categories: ["cs.LG"]
keywords: []
venue_source: "arxiv-only"
hunter_fetched: "2026-04-15T05:14:13+09:00"
---

# DUEL: Exact Likelihood for Masked Diffusion via Deterministic Unmasking

## Abstract
Masked diffusion models (MDMs) generate text by iteratively selecting positions to unmask and then predicting tokens at those positions. Yet MDMs lack proper likelihood evaluation: the evidence lower bound (ELBO) is not only a loose bound on log-likelihood, but, as we show, is also computed under the training distribution rather than the test-time distribution. We resolve this within our DUEL framework, which unifies leading MDM sampling strategies that employ $\textit{deterministic}$ position selection. We prove that DUEL samplers admit $\textbf{exact likelihood computation under the test-time distribution}$ -- giving MDMs $\textit{proper}$ likelihood, and hence proper perplexity, for the first time. This proper perplexity is the natural analogue of autoregressive perplexity and lets us revisit key questions about MDMs. $\textbf{MDMs are substantially better than previously thought}$: the MDM-autoregressive perplexity gap shrinks by up to $32\%$ on in-domain data and $82\%$ on zero-shot benchmarks. DUEL enables the first principled comparison of fast,parallel samplers across compute budgets -- an analysis impossible with the ELBO and unreliable with generative perplexity -- identifying a strong default method. Finally, oracle search over position orderings reveals MDMs can far surpass autoregressive models -- achieving $36.47$ vs. $52.11$ perplexity on AG News -- demonstrating the ceiling of MDM performance has not yet been reached.

## Metadata
- venue: arXiv
- year: 2026
- authors: Gilad Turok, Chris De Sa, Volodymyr Kuleshov
- arxiv_id: 2603.01367
- openreview_id: 
- anthology_id: 
- pdf_url: https://arxiv.org/pdf/2603.01367v2
- published: 2026-03-02
