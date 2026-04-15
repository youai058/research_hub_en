---
title: "Chain of Hindsight aligns Language Models with Feedback"
authors: ["Hao Liu", "Carmelo Sferrazza", "Pieter Abbeel"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "6xfe4IVcOu"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6dc18121c96221c694b6c583053368af3aa30ace.pdf"
published: "2024"
categories: []
keywords: ["Reinforcement Learning", "Reinforcement Learning from Human Feedback", "RLHF"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:58+09:00"
---

# Chain of Hindsight aligns Language Models with Feedback

## Abstract
Learning from human preferences is important for language models to match human needs and to align with human and social values. 
Prior works have achieved remarkable successes by learning from human feedback to understand and follow instructions. Nonetheless, these methods are either founded on hand-picked model generations that are favored by human annotators, rendering them inefficient in terms of data utilization and challenging to apply in general, or they depend on reinforcement learning, which often suffers from imperfect reward functions and relies on extremely challenging optimizations. In this work, we propose a novel technique, Chain of Hindsight, that is easy to optimize and can learn from any form of feedback, regardless of its polarity. Our idea is inspired by how humans learn from extensive feedback presented in the form of languages. We convert all types of feedback into sequences of sentences, which are then used to fine-tune the model, allowing us to take advantage of the language comprehension capabilities of language models.
We condition the model on a sequence of model generations paired with feedback. By doing so, the model is trained to generate outputs based on feedback, while learning to identify and correct negative attributes or errors.  Applying our method to large language models, we observed that Chain of Hindsight significantly surpasses previous methods in aligning language models with human preferences. We report significant improvements on summarization and dialogue benchmarks, with our approach markedly preferred in human evaluations.

## Metadata
- venue: ICLR
- year: 2024
- authors: Hao Liu, Carmelo Sferrazza, Pieter Abbeel
- arxiv_id: 
- openreview_id: 6xfe4IVcOu
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6dc18121c96221c694b6c583053368af3aa30ace.pdf
- published: 2024
- keywords: Reinforcement Learning, Reinforcement Learning from Human Feedback, RLHF
