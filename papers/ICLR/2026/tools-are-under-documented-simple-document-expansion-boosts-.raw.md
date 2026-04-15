---
title: "Tools are under-documented: Simple Document Expansion Boosts Tool Retrieval"
authors: ["Xuan Lu", "Haohang Huang", "Rui Meng", "Yaohui Jin", "Wenjun Zeng", "Xiaoyu Shen"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "g9D9MgG7iW"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/2e8eb5c1866281d12fcf66b03f4c1b2718fabb50.pdf"
published: "2026"
categories: []
keywords: ["tool retrieval", "information retrieval"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:45+09:00"
---

# Tools are under-documented: Simple Document Expansion Boosts Tool Retrieval

## Abstract
Large Language Models (LLMs) have recently demonstrated strong capabilities in tool use, yet progress in tool retrieval remains hindered by incomplete and heterogeneous tool documentation. To address this challenge, we introduce Tool-REX, a new benchmark and framework that systematically enriches tool documentation with structured fields to enable more effective tool retrieval,  together with two dedicated models, Tool-Embed and Tool-Rank. We design a scalable document expansion pipeline that leverages both open- and closed-source LLMs to generate, validate, and refine enriched tool profiles at low cost, producing large-scale corpora with 50k instances for 
embedding-based retrievers and 200k for rerankers. On top of this data, we develop two models specifically tailored for tool retrieval: Tool-Embed, a dense retriever, and Tool-Rank, an LLM-based reranker. Extensive experiments on ToolRet and Tool-REX demonstrate that document expansion substantially improves retrieval performance, with Tool-Embed and Tool-Rank achieving new state-of-the-art results on both benchmarks. We further analyze the contribution of individual fields to retrieval effectiveness, as well as the broader impact of document expansion on both training and evaluation. Overall, our findings highlight both the promise and limitations of LLM-driven document expansion, positioning \textsc{Tool-REX}, along with the proposed Tool-Embed and Tool-Rank, as a foundation for future research in tool retrieval.

## Metadata
- venue: ICLR
- year: 2026
- authors: Xuan Lu, Haohang Huang, Rui Meng, Yaohui Jin, Wenjun Zeng, Xiaoyu Shen
- arxiv_id: 
- openreview_id: g9D9MgG7iW
- anthology_id: 
- pdf_url: https://openreview.net/pdf/2e8eb5c1866281d12fcf66b03f4c1b2718fabb50.pdf
- published: 2026
- keywords: tool retrieval, information retrieval
