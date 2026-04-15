---
title: "DE-COP: Detecting Copyrighted Content in Language Models Training Data"
authors: ["André Vicente Duarte", "Xuandong Zhao", "Arlindo L. Oliveira", "Lei Li"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "LO4xhXmFal"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/a40eb1d7e36f157ae3073554495eafcdd50449c0.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:47+09:00"
---

# DE-COP: Detecting Copyrighted Content in Language Models Training Data

## Abstract
*How can we detect if copyrighted content was used in the training process of a language model, considering that the training data is typically undisclosed?* We are motivated by the premise that a language model is likely to identify verbatim excerpts from its training text. We propose DE-COP, a method to determine whether a piece of copyrighted content is included in training. DE-COP's core approach is to probe an LLM with multiple-choice questions, whose options include both verbatim text and their paraphrases. We construct BookTection, a benchmark with excerpts from 165 books published prior and subsequent to a model's training cutoff, along with their paraphrases. Our experiments show that DE-COP outperforms the prior best method by 8.6% in detection accuracy (AUC) on models with logits available. Moreover, DE-COP also achieves an average accuracy of 72% for detecting suspect books on fully black-box models where prior methods give approximately 0% accuracy. The code and datasets are available at https://github.com/LeiLiLab/DE-COP.

## Metadata
- venue: ICML
- year: 2024
- authors: André Vicente Duarte, Xuandong Zhao, Arlindo L. Oliveira, Lei Li
- arxiv_id: 
- openreview_id: LO4xhXmFal
- anthology_id: 
- pdf_url: https://openreview.net/pdf/a40eb1d7e36f157ae3073554495eafcdd50449c0.pdf
- published: 2024
