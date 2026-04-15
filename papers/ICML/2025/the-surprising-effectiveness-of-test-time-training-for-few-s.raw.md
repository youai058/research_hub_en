---
title: "The Surprising Effectiveness of Test-Time Training for Few-Shot Learning"
authors: ["Ekin Akyürek", "Mehul Damani", "Adam Zweiger", "Linlu Qiu", "Han Guo", "Jyothish Pari", "Yoon Kim", "Jacob Andreas"]
venue: "ICML"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "asgBo3FNdg"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4e00aa4323cfda1f6f1808595d6d5124eb1c4319.pdf"
published: "2025"
categories: []
keywords: ["Test-Time Training", "In-Context Learning", "Few-Shot Learning", "ARC", "BIG-Bench Hard"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:16:28+09:00"
---

# The Surprising Effectiveness of Test-Time Training for Few-Shot Learning

## Abstract
Language models (LMs) have shown impressive performance on tasks within their training distribution, but often struggle with structurally novel tasks even when given a small number of in-context task examples. We investigate the effectiveness of test-time training (TTT)—temporarily updating model parameters during inference using a loss derived from input data—as a mechanism for improving LMs' reasoning and few-shot learning capabilities. On the Abstraction and Reasoning Corpus (ARC), performing TTT with in-context examples yields up to $6\times$ higher accuracy compared to fine-tuned baselines—reaching $53.0\%$ on the public validation set with an 8B-parameter LM and $61.9\%$ when ensembled with program-synthesis methods, matching average human performance. On BIG-Bench Hard (BBH), TTT on in-context examples surpasses standard few-shot prompting in the $10$-shot setting by $7.3$ percentage points ($50.5\%$ to $57.8\%$). Our findings highlight the limitations of in-context learning for novel tasks and demonstrate the potential of test-time training to enhance language model adaptability.

## Metadata
- venue: ICML
- year: 2025
- authors: Ekin Akyürek, Mehul Damani, Adam Zweiger, Linlu Qiu, Han Guo, Jyothish Pari, Yoon Kim, Jacob Andreas
- arxiv_id: 
- openreview_id: asgBo3FNdg
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4e00aa4323cfda1f6f1808595d6d5124eb1c4319.pdf
- published: 2025
- keywords: Test-Time Training, In-Context Learning, Few-Shot Learning, ARC, BIG-Bench Hard
