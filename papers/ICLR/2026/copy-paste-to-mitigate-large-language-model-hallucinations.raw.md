---
title: "Copy-Paste to Mitigate Large Language Model Hallucinations"
authors: ["Yongchao Long", "Yingying Zhang", "Xianbin Wen", "Xian Wu", "Yuxi Zhou", "Shenda Hong"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "crKJJ4Ej60"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/8e5dd0875eac6df6aba847032240c77d9d9bea60.pdf"
published: "2026"
categories: []
keywords: ["Hallucination", "Context Learning", "Contextual Faithfulness", "Knowledge Conflict", "Model Interpretability"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:24+09:00"
---

# Copy-Paste to Mitigate Large Language Model Hallucinations

## Abstract
While Retrieval-Augmented Generation (RAG) enables large language models (LLMs) to generate contextually grounded responses, contextual faithfulness remains challenging as LLMs may not consistently trust provided context, leading to hallucinations that undermine reliability. We observe an inverse correlation between response copying degree and context-unfaithful hallucinations on RAGTruth, suggesting higher copying degrees reduce hallucinations by fostering genuine contextual belief. We propose Copy-Paste, a generation paradigm that directly embeds contextual fragments to ensure faithfulness, and instantiate it through CopyPasteLLM via two-stage high-copying preference training. We design three prompting methods to enhance copying degree, demonstrating that high-copying responses achieve superior contextual faithfulness and hallucination control. These approaches enable a fully automated pipeline that transforms generated responses into high-copying preference data for training CopyPasteLLM. On FaithEval, ConFiQA and PubMedQA, CopyPasteLLM achieves best performance in both counterfactual and original contexts, remarkably with 12.2\% to 24.5\% accuracy improvements on FaithEval over the best baseline, while requiring only 365 training samples—1/50th of baseline data. To elucidate CopyPasteLLM's effectiveness, we propose the Context-Parameter Copying Capturing algorithm. Interestingly, this reveals that CopyPasteLLM recalibrates reliance on internal parametric knowledge rather than external knowledge during generation. All codes are available at https://github.com/longyongchao/CopyPasteLLM

## Metadata
- venue: ICLR
- year: 2026
- authors: Yongchao Long, Yingying Zhang, Xianbin Wen, Xian Wu, Yuxi Zhou, Shenda Hong
- arxiv_id: 
- openreview_id: crKJJ4Ej60
- anthology_id: 
- pdf_url: https://openreview.net/pdf/8e5dd0875eac6df6aba847032240c77d9d9bea60.pdf
- published: 2026
- keywords: Hallucination, Context Learning, Contextual Faithfulness, Knowledge Conflict, Model Interpretability
