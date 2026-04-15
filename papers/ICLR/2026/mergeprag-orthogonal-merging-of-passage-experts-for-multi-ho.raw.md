---
title: "MergePRAG: Orthogonal Merging of Passage-experts for Multi-hop Parametric RAG"
authors: ["Xuebing Liu", "Shanbao Qiao", "Roseline Nyange", "Dongwook Min", "Hyun Kim", "Seung-Hoon Na"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "FSL1J2gmJV"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/e46b5a6188fa952a06d6d3f80fec8738dea746fe.pdf"
published: "2026"
categories: []
keywords: ["Multi-hop reasoning", "Knowledge enhancement", "Retrieval-augmented generation", "Hypernetwork-based expert generation"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:20+09:00"
---

# MergePRAG: Orthogonal Merging of Passage-experts for Multi-hop Parametric RAG

## Abstract
Large language models (LLMs) can be enhanced with external knowledge through two dominant approaches: (1) **retrieval-augmented generation (RAG)**, which supplements LLMs with in-context retrieved passages, and (2) **parametric knowledge adaptation (PKA)**, which directly updates model parameters with new domain knowledge. Recently, parametric RAG (PRAG) has emerged as a promising framework, extending RAG by translating retrieved passages into parameter updates, thereby mitigating inefficiency and noise sensitivity inherent to RAG. However, existing PRAG methods remain limited to single-pass retrieval, falling short of the **multi-hop RAG** setting that requires iterative retrieval and reasoning. 
We propose **MergePRAG**(*Orthogonal Merging of Passage-experts for Multi-hop PRAG*), a novel framework that sequentially integrates retrieved passages into LLM parameters through a continual merging mechanism, which is advanced by two key proposals: (1) **orthogonal merging** using the Gram–Schmidt process to minimize conflicts between "passage experts", and (2) **critical-layer parameterization** to efficiently encode in-context passages. Experiments on multi-hop open-domain QA and reasoning-aware knowledge editing show that MergePRAG consistently outperforms both standard and state-of-the-art RAGs as well as existing parametric adaptation methods, achieving superior effectiveness and efficiency. All datasets and code will be released at https://github.com/Liu-Xuebing/MhQA_hypernetwork.

## Metadata
- venue: ICLR
- year: 2026
- authors: Xuebing Liu, Shanbao Qiao, Roseline Nyange, Dongwook Min, Hyun Kim, Seung-Hoon Na
- arxiv_id: 
- openreview_id: FSL1J2gmJV
- anthology_id: 
- pdf_url: https://openreview.net/pdf/e46b5a6188fa952a06d6d3f80fec8738dea746fe.pdf
- published: 2026
- keywords: Multi-hop reasoning, Knowledge enhancement, Retrieval-augmented generation, Hypernetwork-based expert generation
