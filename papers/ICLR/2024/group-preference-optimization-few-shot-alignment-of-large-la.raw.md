---
title: "Group Preference Optimization: Few-Shot Alignment of Large Language Models"
authors: ["Siyan Zhao", "John Dang", "Aditya Grover"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "DpFeMH4l8Q"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e743356473984605880070de9402840ffe780599.pdf"
published: "2024"
categories: []
keywords: ["Large Language Models", "alignment", "group preference alignment", "few-shot learning", "in-context learning", "fine-tuning"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:25+09:00"
---

# Group Preference Optimization: Few-Shot Alignment of Large Language Models

## Abstract
Many applications of large language models (LLMs), ranging from chatbots to
creative writing, require nuanced subjective judgments that can differ significantly
across different groups. Existing alignment algorithms can be expensive to align
for each group, requiring prohibitive amounts of group-specific preference data
and computation for real-world use cases. We introduce Group Preference Optimization (GPO), an alignment framework that steers language models to preferences of individual groups in a few-shot manner. In GPO, we augment the base
LLM with an independent transformer module trained to predict the preferences
of a group for the LLM generations. For few-shot learning, we parameterize this
module as an in-context autoregressive transformer and train it via meta-learning
on several groups. We empirically validate the efficacy of GPO through rigorous evaluations using LLMs with varied sizes on three human opinion adaptation tasks. These tasks involve adapting to the preferences of US demographic
groups, global countries, and individual users. Our results demonstrate that GPO
not only aligns models more accurately but also requires fewer group-specific
preferences and less training and inference computing resources, outperforming
existing strategies such as in-context steering and fine-tuning methods.

## Metadata
- venue: ICLR
- year: 2024
- authors: Siyan Zhao, John Dang, Aditya Grover
- arxiv_id: 
- openreview_id: DpFeMH4l8Q
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e743356473984605880070de9402840ffe780599.pdf
- published: 2024
- keywords: Large Language Models, alignment, group preference alignment, few-shot learning, in-context learning, fine-tuning
