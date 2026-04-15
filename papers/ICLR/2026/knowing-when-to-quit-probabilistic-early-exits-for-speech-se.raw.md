---
title: "Knowing When to Quit: Probabilistic Early Exits for Speech Separation Networks"
authors: ["Kenny Falkær Olsen", "Mads Østergaard", "Karl Ulbæk", "Søren Føns Nielsen", "Rasmus Malik Høegh Lindrup", "Bjørn Sand Jensen", "Morten Mørup"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "RKzBRfV6J8"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/87315121a6c91117b4bc578863efc39baf31d08a.pdf"
published: "2026"
categories: []
keywords: ["speech separation", "speech enhancement", "deep learning", "early exit", "dynamic neural networks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:41+09:00"
---

# Knowing When to Quit: Probabilistic Early Exits for Speech Separation Networks

## Abstract
In recent years, deep learning-based single-channel speech separation has improved
  considerably, in large part driven by increasingly compute- and parameter-efficient
  neural network architectures. Most such architectures are, however, designed with a
  fixed compute and parameter budget and consequently cannot scale to varying compute
  demands or resources, which limits their use in embedded and heterogeneous
  devices such as mobile phones and hearables.
  To enable such use-cases we design a neural network architecture for speech separation
  and enhancement capable of early-exit, and we propose an uncertainty-aware
  probabilistic framework to jointly model the clean speech signal and error variance
  which we use to derive probabilistic early-exit conditions in terms of desired
  signal-to-noise ratios.
  We evaluate our methods on both speech separation and enhancement tasks where we
  demonstrate that early-exit capabilities can be introduced without compromising
  reconstruction, and that when trained on variable-length audio our early-exit
  conditions are well-calibrated and lead to considerable compute savings when used to
  dynamically scale compute at test time while remaining directly interpretable.

## Metadata
- venue: ICLR
- year: 2026
- authors: Kenny Falkær Olsen, Mads Østergaard, Karl Ulbæk, Søren Føns Nielsen, Rasmus Malik Høegh Lindrup, Bjørn Sand Jensen, Morten Mørup
- arxiv_id: 
- openreview_id: RKzBRfV6J8
- anthology_id: 
- pdf_url: https://openreview.net/pdf/87315121a6c91117b4bc578863efc39baf31d08a.pdf
- published: 2026
- keywords: speech separation, speech enhancement, deep learning, early exit, dynamic neural networks
