---
title: "Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates"
authors: ["Kaifeng Lyu", "Haoyu Zhao", "Xinran Gu", "Dingli Yu", "Anirudh Goyal", "Sanjeev Arora"]
venue: "NeurIPS"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "xNlQjS0dtO"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/beb490ad102910ffee423d69bbff98080fde654b.pdf"
published: "2024"
categories: []
keywords: ["safety prompt", "AI alignment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:19:04+09:00"
---

# Keeping LLMs Aligned After Fine-tuning: The Crucial Role of Prompt Templates

## Abstract
Public LLMs such as the Llama 2-Chat underwent alignment training and were considered safe. Recently Qi et al. (2024) reported that even benign fine-tuning on seemingly safe datasets can give rise to unsafe behaviors in the models. The current paper is about methods and best practices to mitigate such loss of alignment. We focus on the setting where a public model is fine-tuned before serving users for specific usage, where the model should improve on the downstream task while maintaining alignment. Through extensive experiments on several chat models (Meta's Llama 2-Chat, Mistral AI's Mistral 7B Instruct v0.2, and OpenAI's GPT-3.5 Turbo), this paper uncovers that the prompt templates used during fine-tuning and inference play a crucial role in preserving safety alignment, and proposes the “Pure Tuning, Safe Testing” (PTST) strategy --- fine-tune models without a safety prompt, but include it at test time. This seemingly counterintuitive strategy incorporates an intended distribution shift to encourage alignment preservation. Fine-tuning experiments on GSM8K, ChatDoctor, and OpenOrca show that PTST significantly reduces the rise of unsafe behaviors.

## Metadata
- venue: NeurIPS
- year: 2024
- authors: Kaifeng Lyu, Haoyu Zhao, Xinran Gu, Dingli Yu, Anirudh Goyal, Sanjeev Arora
- arxiv_id: 
- openreview_id: xNlQjS0dtO
- anthology_id: 
- pdf_url: https://openreview.net/pdf/beb490ad102910ffee423d69bbff98080fde654b.pdf
- published: 2024
- keywords: safety prompt, AI alignment
