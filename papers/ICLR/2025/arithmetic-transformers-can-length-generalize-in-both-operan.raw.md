---
title: "Arithmetic Transformers Can Length-Generalize in Both Operand Length and Count"
authors: ["Hanseul Cho", "Jaeyoung Cha", "Srinadh Bhojanapalli", "Chulhee Yun"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "eIgGesYKLG"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/95515937bd46f9df573749086a859cfca4290141.pdf"
published: "2025"
categories: []
keywords: ["Length Generalization", "Transformers", "Scratchpad", "Position Coupling", "Positional Encoding", "Out-of-distribution Generalization", "Arithmetic Tasks"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:14:52+09:00"
---

# Arithmetic Transformers Can Length-Generalize in Both Operand Length and Count

## Abstract
Transformers often struggle with *length generalization*, meaning they fail to generalize to sequences longer than those encountered during training. While arithmetic tasks are commonly used to study length generalization, certain tasks are considered notoriously difficult, e.g., multi-operand addition (requiring generalization over both the number of operands and their lengths) and multiplication (requiring generalization over both operand lengths). In this work, we achieve approximately 2–3× length generalization on both tasks, which is the first such achievement in arithmetic Transformers. We design task-specific scratchpads enabling the model to focus on a fixed number of tokens per each next-token prediction step, and apply multi-level versions of *Position Coupling* (Cho et al., 2024; McLeish et al., 2024) to let Transformers know the right position to attend to. On the theory side, we prove that a 1-layer Transformer using our method can solve multi-operand addition, up to operand length and operand count that are exponential in embedding dimension.

## Metadata
- venue: ICLR
- year: 2025
- authors: Hanseul Cho, Jaeyoung Cha, Srinadh Bhojanapalli, Chulhee Yun
- arxiv_id: 
- openreview_id: eIgGesYKLG
- anthology_id: 
- pdf_url: https://openreview.net/pdf/95515937bd46f9df573749086a859cfca4290141.pdf
- published: 2025
- keywords: Length Generalization, Transformers, Scratchpad, Position Coupling, Positional Encoding, Out-of-distribution Generalization, Arithmetic Tasks
