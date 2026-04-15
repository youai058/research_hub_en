---
title: "From Dormant to Deleted: Tamper-Resistant Unlearning Through Weight-Space Regularization"
authors: ["Shoaib Ahmed Siddiqui", "Adrian Weller", "David Krueger", "Gintare Karolina Dziugaite", "Michael Curtis Mozer", "Eleni Triantafillou"]
venue: "NeurIPS"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Zrqn7ZshXG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/be9613c2de1eedd9326b1b659054e2fabaf7892b.pdf"
published: "2025"
categories: []
keywords: ["Unlearning", "tamper-resistance", "relearning attacks", "weight-space analysis"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:32+09:00"
---

# From Dormant to Deleted: Tamper-Resistant Unlearning Through Weight-Space Regularization

## Abstract
Recent unlearning methods for LLMs are vulnerable to relearning attacks: knowledge believed-to-be-unlearned re-emerges by fine-tuning on a small set of (even seemingly-unrelated) examples. We study this phenomenon in a controlled setting for example-level unlearning in vision classifiers. We make the surprising discovery that forget-set accuracy can recover from around 50\% post-unlearning to nearly 100\% with fine-tuning on just the *retain* set---i.e., zero examples of the forget set. We observe this effect across a wide variety of unlearning methods, whereas for a model retrained from scratch excluding the forget set (gold standard), the accuracy remains at 50\%. We observe that resistance to relearning attacks can be predicted by weight-space properties, specifically, $L_2$-distance and linear mode connectivity between the original and the unlearned model. Leveraging this insight, we propose a new class of methods that achieve state-of-the-art resistance to relearning attacks.

## Metadata
- venue: NeurIPS
- year: 2025
- authors: Shoaib Ahmed Siddiqui, Adrian Weller, David Krueger, Gintare Karolina Dziugaite, Michael Curtis Mozer, Eleni Triantafillou
- arxiv_id: 
- openreview_id: Zrqn7ZshXG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/be9613c2de1eedd9326b1b659054e2fabaf7892b.pdf
- published: 2025
- keywords: Unlearning, tamper-resistance, relearning attacks, weight-space analysis
