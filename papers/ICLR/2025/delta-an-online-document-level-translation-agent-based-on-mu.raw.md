---
title: "DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory"
authors: ["Yutong Wang", "Jiali Zeng", "Xuebo Liu", "Derek F. Wong", "Fandong Meng", "Jie Zhou", "Min Zhang"]
venue: "ICLR"
year: 2025
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hoYFLRNbhc"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/46c09c6621cdb1818c886adb57ebecfae7302a2d.pdf"
published: "2025"
categories: []
keywords: ["Document-Level Translation", "Large Language Models", "Autonomous Agents", "Natural Language Processing"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:15:10+09:00"
---

# DelTA: An Online Document-Level Translation Agent Based on Multi-Level Memory

## Abstract
Large language models (LLMs) have achieved reasonable quality improvements in machine translation (MT).
However, most current research on MT-LLMs still faces significant challenges in maintaining translation consistency and accuracy when processing entire documents.
In this paper, we introduce DelTA, a Document-levEL Translation Agent designed to overcome these limitations.
DelTA features a multi-level memory structure that stores information across various granularities and spans, including Proper Noun Records, Bilingual Summary, Long-Term Memory, and Short-Term Memory, which are continuously retrieved and updated by auxiliary LLM-based components.
Experimental results indicate that DelTA significantly outperforms strong baselines in terms of translation consistency and quality across four open/closed-source LLMs and two representative document translation datasets, achieving an increase in consistency scores by up to 4.58 percentage points and in COMET scores by up to 3.16 points on average.
DelTA employs a sentence-by-sentence translation strategy, ensuring no sentence omissions and offering a memory-efficient solution compared to the mainstream method.
Furthermore, DelTA improves pronoun and context-dependent translation accuracy, and the summary component of the agent also shows promise as a tool for query-based summarization tasks.
The code and data of our approach are released at https://github.com/YutongWang1216/DocMTAgent.

## Metadata
- venue: ICLR
- year: 2025
- authors: Yutong Wang, Jiali Zeng, Xuebo Liu, Derek F. Wong, Fandong Meng, Jie Zhou, Min Zhang
- arxiv_id: 
- openreview_id: hoYFLRNbhc
- anthology_id: 
- pdf_url: https://openreview.net/pdf/46c09c6621cdb1818c886adb57ebecfae7302a2d.pdf
- published: 2025
- keywords: Document-Level Translation, Large Language Models, Autonomous Agents, Natural Language Processing
