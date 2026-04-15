---
title: "FlowSearcher: Synthesizing Memory-Guided Agentic Workflows for Web Information Seeking"
authors: ["Keyi Xiang", "Zeyu Feng", "Zhuoyi Lin", "Yueming Lyu", "Shi Boyuan", "Yew-Soon Ong", "Ivor Tsang", "Haiyan Yin"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "34v7DVz2l0"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2ee34373f2c57c87537190d40351bf0aa0a47092.pdf"
published: "2026"
categories: []
keywords: ["Large Language Model Reasoning", "Structured Planning", "Agentic Workflow"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:31+09:00"
---

# FlowSearcher: Synthesizing Memory-Guided Agentic Workflows for Web Information Seeking

## Abstract
Web search is a cornerstone for deep research agents, enabling them to acquire and reason over knowledge beyond static corpora. Yet most existing systems rely on ReAct-style tool chains with rigid, linear workflows,  hindering their ability to adapt to diverse query types and tool-use strategies. We introduce **FlowSearcher**, a novel deep search framework that formulates web information seeking as *memory-guided agentic workflow synthesis*.  FlowSearcher decomposes a query into subgoals and synthesizes a tailored workflow graph for each subgoal, dynamically adapting the depth, ordering, and composition of tool use. Complementing this, a hierarchical memory consolidates past workflows into reusable structural experience, which is retrieved to guide both workflow orchestration and execution on new queries.  By shifting from reactive tool calls to experience-conditioned workflow design, FlowSearcher enables flexible multi-path exploration and reuse without any supervised training or RLHF.  Experiments on GAIA, BrowseComp, and GPQA show that FlowSearcher consistently matches or exceeds the performance of RLHF-trained web agents under the same model backbone. Our code is released at [github.com/XiangKeYiNTU/flowsearcher](https://github.com/XiangKeYiNTU/flowsearcher).

## Metadata
- venue: ICLR
- year: 2026
- authors: Keyi Xiang, Zeyu Feng, Zhuoyi Lin, Yueming Lyu, Shi Boyuan, Yew-Soon Ong, Ivor Tsang, Haiyan Yin
- arxiv_id: 
- openreview_id: 34v7DVz2l0
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2ee34373f2c57c87537190d40351bf0aa0a47092.pdf
- published: 2026
- keywords: Large Language Model Reasoning, Structured Planning, Agentic Workflow
