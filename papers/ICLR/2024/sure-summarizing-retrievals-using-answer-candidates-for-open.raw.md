---
title: "SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs"
authors: ["Jaehyung Kim", "Jaehyun Nam", "Sangwoo Mo", "Jongjin Park", "Sang-Woo Lee", "Minjoon Seo", "Jung-Woo Ha", "Jinwoo Shin"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "w4DW6qkRmt"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/9192639fe8e3dbb64d5431c85984894b9e1b089d.pdf"
published: "2024"
categories: []
keywords: ["question answering", "large language model", "retrieval"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:18:00+09:00"
---

# SuRe: Summarizing Retrievals using Answer Candidates for Open-domain QA of LLMs

## Abstract
Large language models (LLMs) have made significant advancements in various natural language processing tasks, including question answering (QA) tasks. While incorporating new information with the retrieval of relevant passages is a promising way to improve QA with LLMs, the existing methods often require additional fine-tuning which becomes infeasible with recent LLMs. Augmenting retrieved passages via prompting has the potential to address this limitation, but this direction has been limitedly explored. To this end, we design a simple yet effective framework to enhance open-domain QA (ODQA) with LLMs, based on the summarized retrieval (SuRe). SuRe helps LLMs predict more accurate answers for a given question, which are well-supported by the summarized retrieval that could be viewed as an explicit rationale extracted from the retrieved passages. Specifically, SuRe first constructs summaries of the retrieved passages for each of the multiple answer candidates. Then, SuRe confirms the most plausible answer from the candidate set by evaluating the validity and ranking of the generated summaries. Experimental results on diverse ODQA benchmarks demonstrate the superiority of SuRe, with improvements of up to 4.6\% in exact match (EM) and 4.0\% in F1 score over standard prompting approaches. SuRe also can be integrated with a broad range of retrieval methods and LLMs. Finally, the generated summaries from SuRe show additional advantages to measure the importance of retrieved passages and serve as more preferred rationales by models and humans.

## Metadata
- venue: ICLR
- year: 2024
- authors: Jaehyung Kim, Jaehyun Nam, Sangwoo Mo, Jongjin Park, Sang-Woo Lee, Minjoon Seo, Jung-Woo Ha, Jinwoo Shin
- arxiv_id: 
- openreview_id: w4DW6qkRmt
- anthology_id: 
- pdf_url: https://openreview.net/pdf/9192639fe8e3dbb64d5431c85984894b9e1b089d.pdf
- published: 2024
- keywords: question answering, large language model, retrieval
