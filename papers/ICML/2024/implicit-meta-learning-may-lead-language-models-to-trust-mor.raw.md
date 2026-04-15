---
title: "Implicit meta-learning may lead language models to trust more reliable sources"
authors: ["Dmitrii Krasheninnikov", "Egor Krasheninnikov", "Bruno Kacper Mlodozeniec", "Tegan Maharaj", "David Krueger"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Fzp1DRzCIN"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/f9ff7df1c721b133862e6327f51393e368a6dd80.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:10+09:00"
---

# Implicit meta-learning may lead language models to trust more reliable sources

## Abstract
We demonstrate that large language models (LLMs) may learn indicators of document usefulness and modulate their updates accordingly. We introduce random strings ("tags") as indicators of usefulness in a synthetic fine-tuning dataset. Fine-tuning on this dataset leads to **implicit meta-learning (IML)**: in further fine-tuning, the model updates to make more use of text that is tagged as useful. We perform a thorough empirical investigation of this phenomenon, finding (among other things) that (i) it occurs in both pretrained LLMs and those trained from scratch, as well as on a vision task, and (ii) larger models and smaller batch sizes tend to give more IML. We also use probing to examine how IML changes the way models store knowledge in their parameters. Finally, we reflect on what our results might imply about the capabilities, risks, and controllability of future AI systems.

## Metadata
- venue: ICML
- year: 2024
- authors: Dmitrii Krasheninnikov, Egor Krasheninnikov, Bruno Kacper Mlodozeniec, Tegan Maharaj, David Krueger
- arxiv_id: 
- openreview_id: Fzp1DRzCIN
- anthology_id: 
- pdf_url: https://openreview.net/pdf/f9ff7df1c721b133862e6327f51393e368a6dd80.pdf
- published: 2024
