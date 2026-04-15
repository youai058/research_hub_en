---
title: "Physics of Language Models: Part 3.2, Knowledge Manipulation"
authors: ["Zeyuan Allen-Zhu", "Yuanzhi Li"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "oDbiL9CLoS"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/6097941da7c6577acb02e468ee39ff27979fe359.pdf"
published: "2025"
categories: []
keywords: ["knowledge manipulation", "language models", "generative models", "reversal curse"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:16+09:00"
---

# Physics of Language Models: Part 3.2, Knowledge Manipulation

## Abstract
Language models can store vast factual knowledge, yet their ability to flexibly use this knowledge for downstream tasks (e.g., via instruction finetuning) remains questionable. This paper investigates four fundamental knowledge manipulation tasks: \textbf{retrieval} (e.g., "What is person A's attribute X?"), \textbf{classification} (e.g., "Is A's attribute X even or odd?"), \textbf{comparison} (e.g., "Is A greater than B in attribute X?"), and \textbf{inverse search} (e.g., "Which person's attribute X equals T?").

We show that language models excel in knowledge retrieval but struggle even in the simplest classification or comparison tasks unless Chain of Thoughts (CoTs) are employed during both training and inference. Moreover, their performance in inverse knowledge search is virtually 0\%, regardless of the prompts.
Our primary contribution is a \emph{controlled, synthetic experiment} that confirms these weaknesses are \emph{inherent} to language models: they cannot efficiently manipulate knowledge from pre-training data, even when such knowledge is perfectly stored in the models, despite adequate training and sufficient model size. Our findings also apply to modern pretrained language models such as GPT-4, thus giving rise to many Turing tests to distinguish Humans from contemporary AIs.

## Metadata
- venue: ICLR
- year: 2025
- authors: Zeyuan Allen-Zhu, Yuanzhi Li
- arxiv_id: 
- openreview_id: oDbiL9CLoS
- anthology_id: 
- pdf_url: https://openreview.net/pdf/6097941da7c6577acb02e468ee39ff27979fe359.pdf
- published: 2025
- keywords: knowledge manipulation, language models, generative models, reversal curse
