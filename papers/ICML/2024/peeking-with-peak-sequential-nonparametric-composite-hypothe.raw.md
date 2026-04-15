---
title: "Peeking with PEAK: Sequential, Nonparametric Composite Hypothesis Tests for Means of Multiple Data Streams"
authors: ["Brian M Cho", "Kyra Gan", "Nathan Kallus"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hcASxFvmZ5"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6d96e429dec9430edd146d5975e8a2a907c90f5d.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:23+09:00"
---

# Peeking with PEAK: Sequential, Nonparametric Composite Hypothesis Tests for Means of Multiple Data Streams

## Abstract
We propose a novel nonparametric sequential test for composite hypotheses for means of multiple data streams. Our proposed method, peeking with expectation-based averaged capital (PEAK), builds upon the testing-by-betting framework and provides a non-asymptotic $\alpha$-level test across any stopping time. Our contributions are two-fold: (1) we propose a novel betting scheme and provide theoretical guarantees on type-I error control, power, and asymptotic growth rate/$e$-power in the setting of a single data stream; (2) we introduce PEAK, a generalization of this betting scheme to multiple streams, that (i) avoids using wasteful union bounds via averaging, (ii) is a test of power one under mild regularity conditions on the sampling scheme of the streams, and (iii) reduces computational overhead when applying the testing-as-betting approaches for pure-exploration bandit problems. We illustrate the practical benefits of PEAK using both synthetic and real-world HeartSteps datasets. Our experiments show that PEAK provides up to an 85% reduction in the number of samples before stopping compared to existing stopping rules for pure-exploration bandit problems, and matches the performance of state-of-the-art sequential tests while improving upon computational complexity.

## Metadata
- venue: ICML
- year: 2024
- authors: Brian M Cho, Kyra Gan, Nathan Kallus
- arxiv_id: 
- openreview_id: hcASxFvmZ5
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6d96e429dec9430edd146d5975e8a2a907c90f5d.pdf
- published: 2024
