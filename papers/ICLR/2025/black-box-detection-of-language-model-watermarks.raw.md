---
title: "Black-Box Detection of Language Model Watermarks"
authors: ["Thibaud Gloaguen", "Nikola Jovanović", "Robin Staab", "Martin Vechev"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "E4LAVLXAHW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f663a98866d599b0943a7ee3063ce496f5b59a81.pdf"
published: "2025"
categories: []
keywords: ["llm", "watermarking"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:46+09:00"
---

# Black-Box Detection of Language Model Watermarks

## Abstract
Watermarking has emerged as a promising way to detect LLM-generated text, by augmenting LLM generations with later detectable signals. Recent work has proposed multiple families of watermarking schemes, several of which focus on preserving the LLM distribution. This distribution-preservation property is motivated by the fact that it is a tractable proxy for retaining LLM capabilities, as well as the inherently implied undetectability of the watermark by downstream users. Yet, despite much discourse around undetectability, no prior work has investigated the practical detectability of any of the current watermarking schemes in a realistic black-box setting. In this work we tackle this for the first time, developing rigorous statistical tests to detect the presence, and estimate parameters, of all three popular watermarking scheme families, using only a limited number of black-box queries. We experimentally confirm the effectiveness of our methods on a range of schemes and a diverse set of open-source models. Further, we validate the feasibility of our tests on real-world APIs. Our findings indicate that current watermarking schemes are more detectable than previously believed.

## Metadata
- venue: ICLR
- year: 2025
- authors: Thibaud Gloaguen, Nikola Jovanović, Robin Staab, Martin Vechev
- arxiv_id: 
- openreview_id: E4LAVLXAHW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f663a98866d599b0943a7ee3063ce496f5b59a81.pdf
- published: 2025
- keywords: llm, watermarking
