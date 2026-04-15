---
title: "MT-Ranker: Reference-free machine translation evaluation by inter-system ranking"
authors: ["Ibraheem Muhammad Moosa", "Rui Zhang", "Wenpeng Yin"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Rry1SeSOQL"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fa181eb3a2cd5c3485b73e3829ad16f3dffa5faa.pdf"
published: "2024"
categories: []
keywords: ["Machine Translation Evaluation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:23+09:00"
---

# MT-Ranker: Reference-free machine translation evaluation by inter-system ranking

## Abstract
Traditionally, Machine Translation (MT) Evaluation has been treated as a regression problem -- producing an absolute translation-quality score. This approach has two limitations: i) the scores lack interpretability, and human annotators struggle with giving consistent scores; ii) most scoring methods are based on (reference, translation) pairs, limiting their applicability in real-world scenarios where references are absent. In practice, we often care about whether a new MT system is better or worse than some competitors. In addition, reference-free MT evaluation is increasingly practical and necessary. Unfortunately, these two practical considerations have yet to be jointly explored. In this work, we formulate the reference-free MT evaluation into a pairwise ranking problem. Given the source sentence and a pair of translations, our system predicts which translation is better. In addition to proposing this new formulation, we further show that this new paradigm can demonstrate superior correlation with human judgments by merely using indirect supervision from natural language inference and weak supervision from our synthetic data. In the context of reference-free evaluation, MT-Ranker, trained without any human annotations, achieves state-of-the-art results on the WMT Shared Metrics Task benchmarks DARR20, MQM20, and MQM21. On a more challenging benchmark, ACES, which contains fine-grained evaluation criteria such as addition, omission, and mistranslation errors, MT-Ranker marks state-of-the-art against reference-free as well as reference-based baselines.

## Metadata
- venue: ICLR
- year: 2024
- authors: Ibraheem Muhammad Moosa, Rui Zhang, Wenpeng Yin
- arxiv_id: 
- openreview_id: Rry1SeSOQL
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fa181eb3a2cd5c3485b73e3829ad16f3dffa5faa.pdf
- published: 2024
- keywords: Machine Translation Evaluation
