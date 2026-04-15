---
title: "LOB-Bench: Benchmarking Generative AI for Finance - an Application to Limit Order Book Data"
authors: ["Peer Nagy", "Sascha Yves Frey", "Kang Li", "Bidipta Sarkar", "Svitlana Vyetrenko", "Stefan Zohren", "Ani Calinescu", "Jakob Nicolaus Foerster"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "CXPpYJpYXQ"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/00e284a8cc48bf5ef2dac6ecb1bd5052bdf3106c.pdf"
published: "2025"
categories: []
keywords: ["finance", "generative models", "time series", "state-space models", "benchmark"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:22+09:00"
---

# LOB-Bench: Benchmarking Generative AI for Finance - an Application to Limit Order Book Data

## Abstract
While financial data presents one of the most challenging and interesting sequence modelling tasks due to high noise, heavy tails, and strategic interactions, progress in this area has been hindered by the lack of consensus on quantitative evaluation paradigms. 
To address this, we present **LOB-Bench**, a benchmark, implemented in python, designed to evaluate the quality and realism of generative message-by-order data for limit order books (LOB) in the LOBSTER format. 
Our framework  measures distributional differences in conditional and unconditional statistics between generated and real LOB data, supporting flexible multivariate statistical evaluation. 
The benchmark also includes features commonly used LOB statistics such as spread, order book volumes, order imbalance, and message inter-arrival times, along with scores from a trained discriminator network. Lastly, LOB-Bench contains "market impact metrics", i.e. the cross-correlations and price response functions for specific events in the data. 
We benchmark generative autoregressive state-space models, a (C)GAN, as well as a parametric LOB model and find that the autoregressive GenAI approach beats traditional model classes.

## Metadata
- venue: ICML
- year: 2025
- authors: Peer Nagy, Sascha Yves Frey, Kang Li, Bidipta Sarkar, Svitlana Vyetrenko, Stefan Zohren, Ani Calinescu, Jakob Nicolaus Foerster
- arxiv_id: 
- openreview_id: CXPpYJpYXQ
- anthology_id: 
- pdf_url: https://openreview.net/pdf/00e284a8cc48bf5ef2dac6ecb1bd5052bdf3106c.pdf
- published: 2025
- keywords: finance, generative models, time series, state-space models, benchmark
