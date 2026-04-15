---
title: "Understanding Finetuning for Factual Knowledge Extraction"
authors: ["Gaurav Rohit Ghosal", "Tatsunori Hashimoto", "Aditi Raghunathan"]
venue: "ICML"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "cPsn9AcOYh"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fddda38cc4b49098d98812e825e99c7140c837eb.pdf"
published: "2024"
categories: []
keywords: []
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:24+09:00"
---

# Understanding Finetuning for Factual Knowledge Extraction

## Abstract
In this work, we study the impact of QA fine-tuning data on downstream factuality. We show that fine-tuning on lesser-known facts that are poorly stored during pretraining yields significantly worse factuality than fine-tuning on well-known facts, even when all facts are seen during pretraining. We prove this phenomenon theoretically, showing that training on lesser-known facts can lead the model to ignore subject entity names and instead output a generic plausible response even when the relevant factual knowledge is encoded in the model. On three question answering benchmarks (PopQA, Entity Questions, and MMLU) and two language models (Llama-2-7B and Mistral-7B), we find that (i) finetuning on a completely factual but lesser-known subset of the data deteriorates downstream factuality (5-10%) and (ii) finetuning on a subset of better-known examples matches or outperforms finetuning on the entire dataset. Ultimately, our results shed light on the interaction between pretrained knowledge and finetuning data and demonstrate the importance of taking into account how facts are stored in the pretrained model when fine-tuning for knowledge-intensive tasks.

## Metadata
- venue: ICML
- year: 2024
- authors: Gaurav Rohit Ghosal, Tatsunori Hashimoto, Aditi Raghunathan
- arxiv_id: 
- openreview_id: cPsn9AcOYh
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fddda38cc4b49098d98812e825e99c7140c837eb.pdf
- published: 2024
