---
title: "Attributing Culture-Conditioned Generations to Pretraining Corpora"
authors: ["Huihan Li", "Arnav Goel", "Keyu He", "Xiang Ren"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "XrsOu4KgDE"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/d4ad6ebf55597935dddd75a72863d66152715ca2.pdf"
published: "2025"
categories: []
keywords: ["culture bias", "pretraining data", "memorization", "generalization"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:09+09:00"
---

# Attributing Culture-Conditioned Generations to Pretraining Corpora

## Abstract
In open-ended generative tasks like narrative writing or dialogue, large language models often exhibit cultural biases, showing limited knowledge and generating templated outputs for less prevalent cultures. Recent works show that these biases may stem from uneven cultural representation in pretraining corpora. This work investigates how pretraining leads to biased culture-conditioned generations
by analyzing how models associate entities with cultures based on pretraining data patterns. We propose the MEMOED framework (MEMOrization from prEtraining Document) to determine whether a generation for a culture arises from memorization. Using MEMOED on culture-conditioned generations about food and clothing for 110 cultures, we find that high-frequency cultures in pretraining data yield more generations with memorized symbols, while some low-frequency cultures produce none. Additionally, the model favors generating entities with extraordinarily high frequency regardless of the conditioned culture, reflecting biases toward frequent pretraining terms irrespective of relevance. We hope that the MEMOED framework and our insights will inspire more works on attributing model performance on pretraining data.

## Metadata
- venue: ICLR
- year: 2025
- authors: Huihan Li, Arnav Goel, Keyu He, Xiang Ren
- arxiv_id: 
- openreview_id: XrsOu4KgDE
- anthology_id: 
- pdf_url: https://openreview.net/pdf/d4ad6ebf55597935dddd75a72863d66152715ca2.pdf
- published: 2025
- keywords: culture bias, pretraining data, memorization, generalization
