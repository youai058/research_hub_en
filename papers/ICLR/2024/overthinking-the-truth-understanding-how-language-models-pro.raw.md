---
title: "Overthinking the Truth: Understanding how Language Models Process False Demonstrations"
authors: ["Danny Halawi", "Jean-Stanislas Denain", "Jacob Steinhardt"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Tigr1kMDZy"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/55ea326a66e2cf61319ebe01bdea1b4ebbd8d775.pdf"
published: "2024"
categories: []
keywords: ["Mechanistic Interpretability", "AI Safety", "Interpretability", "Science of ML", "few-shot learning", "Large Language Models"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:21+09:00"
---

# Overthinking the Truth: Understanding how Language Models Process False Demonstrations

## Abstract
Modern language models can imitate complex patterns through few-shot learning, enabling them to complete challenging tasks without fine-tuning. However, imitation can also lead models to reproduce inaccuracies or harmful content if present in the context. We study harmful imitation through the lens of a model’s internal representations, and identify two related phenomena: overthinking and false induction heads. The first phenomenon, overthinking, appears when we decode predictions from intermediate layers, given correct vs. incorrect few-shot demonstrations. At early layers, both demonstrations induce similar model behavior, but the behavior diverges sharply at some “critical layer”, after which the accuracy given incorrect demonstrations progressively decreases. The second phenomenon, false induction heads, are a possible mechanistic cause of overthinking: these are heads in late layers that attend to and copy false information from previous demonstrations, and whose ablation reduces overthinking. Beyond scientific understanding, our results suggest that studying intermediate model computations could be a promising avenue for understanding and guarding against harmful model behaviors.

## Metadata
- venue: ICLR
- year: 2024
- authors: Danny Halawi, Jean-Stanislas Denain, Jacob Steinhardt
- arxiv_id: 
- openreview_id: Tigr1kMDZy
- anthology_id: 
- pdf_url: https://openreview.net/pdf/55ea326a66e2cf61319ebe01bdea1b4ebbd8d775.pdf
- published: 2024
- keywords: Mechanistic Interpretability, AI Safety, Interpretability, Science of ML, few-shot learning, Large Language Models
