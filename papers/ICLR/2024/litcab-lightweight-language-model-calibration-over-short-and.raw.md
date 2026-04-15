---
title: "LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses"
authors: ["Xin Liu", "Muhammad Khalifa", "Lu Wang"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "jH67LHVOIO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/060aede7175d70a3fe37974ccb7cb976fcfa6486.pdf"
published: "2024"
categories: []
keywords: ["calibration", "hallucination", "large language model"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:02+09:00"
---

# LitCab: Lightweight Language Model Calibration over Short- and Long-form Responses

## Abstract
A model is considered well-calibrated when its probability estimate aligns with the actual likelihood of the output being correct. Calibrating language models (LMs) is crucial, as it plays a vital role in detecting and mitigating hallucinations of LMs as well as building more trustworthy models. However, standard calibration techniques may not be suited for LM calibration. For instance, post-processing methods such as temperature scaling do not reorder the candidate generations. On the other hand, training-based methods require fine-tuning the entire model, which is impractical for LMs of large scale. We present LitCab, a lightweight calibration mechanism consisting of a single linear layer that takes the input text representation and predicts a bias term, which is then added to the LM output logits. LitCab improves model calibration by only adding < 2% of the original model parameters. For evaluation, we construct CaT, a benchmark consisting of eight text generation tasks, covering responses ranging from short phrases to paragraphs. We test LitCab with Llama2-7B, where it improves calibration across all tasks, reducing the average ECE score by as large as 30%. We further conduct a comprehensive evaluation with multiple popular open-sourced LMs from GPT and LLaMA families, yielding the following key findings: (i) Larger models within the same family exhibit better calibration on tasks with short generation tasks, but not necessarily for longer ones. (ii) GPT-family models show superior calibration compared to LLaMA, Llama2, and Vicuna models, despite having much fewer parameters. (iii) Fine-tuning pretrained model (e.g., LLaMA) with samples of limited purpose (e.g., conversations) may lead to worse calibration, highlighting the importance of fine-tuning setups for calibrating LMs.

## Metadata
- venue: ICLR
- year: 2024
- authors: Xin Liu, Muhammad Khalifa, Lu Wang
- arxiv_id: 
- openreview_id: jH67LHVOIO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/060aede7175d70a3fe37974ccb7cb976fcfa6486.pdf
- published: 2024
- keywords: calibration, hallucination, large language model
