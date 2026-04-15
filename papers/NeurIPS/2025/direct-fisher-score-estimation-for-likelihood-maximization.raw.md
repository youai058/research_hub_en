---
title: "Direct Fisher Score Estimation for Likelihood Maximization"
authors: ["Sherman Khoo", "Yakun Wang", "Song Liu", "Mark Beaumont"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "2h8bFmEQwh"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/932db12010d7d344e1b4ec2a731dc50fc4d0c713.pdf"
published: "2025"
categories: []
keywords: ["Simulation-based inference", "Likelihood-free inference", "Score Matching", "Gradient-Based Optimization", "Likelihood Maximization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:41+09:00"
---

# Direct Fisher Score Estimation for Likelihood Maximization

## Abstract
We study the problem of likelihood maximization when the likelihood function is intractable but model simulations are readily available. We propose a sequential, gradient-based optimization method that directly models the Fisher score based on a local score matching technique which uses simulations from a localized region around each parameter iterate. By employing a linear parameterization for the surrogate score model, our technique admits a closed-form, least-squares solution. This approach yields a fast, flexible, and efficient approximation to the Fisher score, effectively smoothing the likelihood objective and mitigating the challenges posed by complex likelihood landscapes. We provide theoretical guarantees for our score estimator, including bounds on the bias introduced by the smoothing. Empirical results on a range of synthetic and real-world problems demonstrate the superior performance of our method compared to existing benchmarks.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Sherman Khoo, Yakun Wang, Song Liu, Mark Beaumont
- arxiv_id: 
- openreview_id: 2h8bFmEQwh
- anthology_id: 
- pdf_url: https://openreview.net/pdf/932db12010d7d344e1b4ec2a731dc50fc4d0c713.pdf
- published: 2025
- keywords: Simulation-based inference, Likelihood-free inference, Score Matching, Gradient-Based Optimization, Likelihood Maximization
