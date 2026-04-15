---
title: "Double-Step Alternating Extragradient with Increasing Timescale Separation for Finding Local Minimax Points: Provable Improvements"
authors: ["Kyuwon Kim", "Donghwan Kim"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "nUVForc3VP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7075f40d146aa11801c2b028fc04e41464c63f51.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:14+09:00"
---

# Double-Step Alternating Extragradient with Increasing Timescale Separation for Finding Local Minimax Points: Provable Improvements

## Abstract
In nonconvex-nonconcave minimax optimization, two-timescale gradient methods have shown their potential to find local minimax (optimal) points, provided that the timescale separation between the min and the max player is sufficiently large. However, existing two-timescale variants of gradient descent ascent and extragradient methods face two shortcomings, especially when we search for non-strict local minimax points that are prevalent in modern overparameterized setting. In specific, (1) these methods can be unstable at some non-strict local minimax points even with sufficiently large timescale separation, and even (2) computing a proper amount of timescale separation is infeasible in practice. To remedy these two issues, we propose to incorporate two simple but provably effective schemes, double-step alternating update and increasing timescale separation, into the two-timescale extragradient method, respectively. Under mild conditions, we show that the proposed methods converge to non-strict local minimax points that all existing two-timescale methods fail to converge.

## Metadata
- venue: ICML
- year: 2024
- authors: Kyuwon Kim, Donghwan Kim
- arxiv_id: 
- openreview_id: nUVForc3VP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7075f40d146aa11801c2b028fc04e41464c63f51.pdf
- published: 2024
