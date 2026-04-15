---
title: "Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse"
authors: ["Maojia Song", "Shang Hong Sim", "Rishabh Bhardwaj", "Hai Leong Chieu", "Navonil Majumder", "Soujanya Poria"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "Iyrtb9EJBp"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/29703dfd9cef0f6afde425618f603cca393e0979.pdf"
published: "2025"
categories: []
keywords: ["Large Language Models", "Trustworthiness", "Hallucinations", "Retrieval Augmented Generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:08+09:00"
---

# Measuring and Enhancing Trustworthiness of LLMs in RAG through Grounded Attributions and Learning to Refuse

## Abstract
LLMs are an integral component of retrieval-augmented generation (RAG) systems. While many studies focus on evaluating the overall quality of end-to-end RAG systems, there is a gap in understanding the appropriateness of LLMs for the RAG task. To address this, we introduce Trust-Score, a holistic metric that evaluates the trustworthiness of LLMs within the RAG framework. Our results show that various prompting methods, such as in-context learning, fail to effectively adapt LLMs to the RAG task as measured by Trust-Score. Consequently, we propose Trust-Align, a method to align LLMs for improved Trust-Score performance. 26 out of 27 models aligned using Trust-Align substantially outperform competitive baselines on ASQA, QAMPARI, and ELI5. Specifically, in LLaMA-3-8b, Trust-Align outperforms FRONT on ASQA (↑12.56), QAMPARI (↑36.04), and ELI5 (↑17.69). Trust-Align also significantly enhances models’ ability to correctly refuse and provide quality citations. We also demonstrate the effectiveness of Trust-Align across different open-weight models, including the LLaMA series (1b to 8b), Qwen-2.5 series (0.5b to 7b), and Phi3.5 (3.8b). We release our code at https://github.com/declare-lab/trust-align.

## Metadata
- venue: ICLR
- year: 2025
- authors: Maojia Song, Shang Hong Sim, Rishabh Bhardwaj, Hai Leong Chieu, Navonil Majumder, Soujanya Poria
- arxiv_id: 
- openreview_id: Iyrtb9EJBp
- anthology_id: 
- pdf_url: https://openreview.net/pdf/29703dfd9cef0f6afde425618f603cca393e0979.pdf
- published: 2025
- keywords: Large Language Models, Trustworthiness, Hallucinations, Retrieval Augmented Generation
