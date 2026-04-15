---
title: "Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions"
authors: ["Sachin Kumar", "Chan Young Park", "Yulia Tsvetkov"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "rkplYfqUr0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2c0276dcc674aef018e1899f39fed7767c226540.pdf"
published: "2024"
categories: []
keywords: ["zero-shot classification", "prompting", "generative classification", "label descriptions"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:06+09:00"
---

# Gen-Z: Generative Zero-Shot Text Classification with Contextualized Label Descriptions

## Abstract
Language model (LM) prompting—a popular paradigm for solving NLP tasks—has been shown to be susceptible to miscalibration and brittleness to slight prompt variations, caused by its discriminative prompting approach, i.e., predicting the label given the input. To address these issues, we propose Gen-Z—a generative prompting framework for zero-shot text classification. GEN-Z is generative, as it measures the LM likelihood of input text, conditioned on natural language descriptions of labels. The framework is multivariate, as label descriptions allow us to seamlessly integrate additional contextual information about the labels to improve task performance. On various standard classification benchmarks, with six open-source LM families, we show that zero-shot classification with simple contextualization of the data source of the evaluation set consistently outperforms both zero-shot and few-shot baselines while improving robustness to prompt variations. Further, our approach enables personalizing classification in a zero-shot manner by incorporating author, subject, or reader information in the label descriptions.

## Metadata
- venue: ICLR
- year: 2024
- authors: Sachin Kumar, Chan Young Park, Yulia Tsvetkov
- arxiv_id: 
- openreview_id: rkplYfqUr0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2c0276dcc674aef018e1899f39fed7767c226540.pdf
- published: 2024
- keywords: zero-shot classification, prompting, generative classification, label descriptions
