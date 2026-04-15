---
title: "Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems"
authors: ["Tian Ye", "Zicheng Xu", "Yuanzhi Li", "Zeyuan Allen-Zhu"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "zpDGwcmMV4"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f32bd8e22a2d6399f178aef058260798753fbe48.pdf"
published: "2025"
categories: []
keywords: ["pretraining", "language model", "error correction", "error detection"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:17+09:00"
---

# Physics of Language Models: Part 2.2, How to Learn From Mistakes on Grade-School Math Problems

## Abstract
Language models have demonstrated remarkable performance in solving reasoning tasks; however, even the strongest models still occasionally make reasoning mistakes. Recently, there has been active research aimed at improving reasoning accuracy, particularly by using pretrained language models to "self-correct'' their mistakes via multi-round prompting. In this paper, we follow this line of work but focus on understanding the usefulness of incorporating ``error-correction'' data directly into the pretraining stage. This data consists of erroneous solution steps immediately followed by their corrections. Using a synthetic math dataset, we show promising results: this type of pretrain data can help language models achieve higher reasoning accuracy directly (i.e., through simple auto-regression, without multi-round prompting) compared to pretraining on the same amount of error-free data. We also delve into many details, such as (1) how this approach differs from beam search, (2) how such data can be prepared, (3) whether masking is needed on the erroneous tokens, (4) the amount of error required, (5) whether such data can be deferred to the fine-tuning stage, and many others.

## Metadata
- venue: ICLR
- year: 2025
- authors: Tian Ye, Zicheng Xu, Yuanzhi Li, Zeyuan Allen-Zhu
- arxiv_id: 
- openreview_id: zpDGwcmMV4
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f32bd8e22a2d6399f178aef058260798753fbe48.pdf
- published: 2025
- keywords: pretraining, language model, error correction, error detection
