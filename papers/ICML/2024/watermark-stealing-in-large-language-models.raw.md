---
title: "Watermark Stealing in Large Language Models"
authors: ["Nikola Jovanović", "Robin Staab", "Martin Vechev"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Wp054bnPq9"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6a6d4f28cf8c1db8bb6c5297a23f1714b71308d0.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:22+09:00"
---

# Watermark Stealing in Large Language Models

## Abstract
LLM watermarking has attracted attention as a promising way to detect AI-generated content, with some works suggesting that current schemes may already be fit for deployment. In this work we dispute this claim, identifying *watermark stealing* (WS) as a fundamental vulnerability of these schemes. We show that querying the API of the watermarked LLM to approximately reverse-engineer a watermark enables practical *spoofing attacks*, as hypothesized in prior work, but also greatly boosts *scrubbing* attacks, which was previously unnoticed. We are the first to propose an automated WS algorithm and use it in the first comprehensive study of spoofing and scrubbing in realistic settings. We show that for under $50 an attacker can both spoof and scrub state-of-the-art schemes previously considered safe, with average success rate of over 80\%. Our findings challenge common beliefs about LLM watermarking, stressing the need for more robust schemes. We make all our code and additional examples available at https://watermark-stealing.org.

## Metadata
- venue: ICML
- year: 2024
- authors: Nikola Jovanović, Robin Staab, Martin Vechev
- arxiv_id: 
- openreview_id: Wp054bnPq9
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6a6d4f28cf8c1db8bb6c5297a23f1714b71308d0.pdf
- published: 2024
