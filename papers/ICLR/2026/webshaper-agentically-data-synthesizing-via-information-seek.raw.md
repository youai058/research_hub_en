---
title: "WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization"
authors: ["Zhengwei Tao", "Jialong Wu", "Wenbiao Yin", "Pu Wu", "Junkai Zhang", "Baixuan Li", "Haiyang SHEN", "Kuan Li", "Liwen Zhang", "Xinyu Wang", "Wentao Zhang", "Yong Jiang", "Pengjun Xie", "Fei Huang", "Jingren Zhou"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "hld4TzJsnD"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/4197d854df3d43b85f8c0bf9a461189c70ad00bf.pdf"
published: "2026"
categories: []
keywords: ["agent", "information seeking", "data synthesis", "llm"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:33+09:00"
---

# WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization

## Abstract
The advent of Large Language Model (LLM)-powered agents has revolutionized artificial intelligence by enabling solutions to complex, open-ended tasks through web-based information-seeking (IS) capabilities. The scarcity of high-quality training data has limited the development of IS agents.  Existing data synthesis approaches typically adopt an information-driven paradigm that first collects information and then refines question-answer pairs through retrieval. However, this may lead to inconsistency between information structure and reasoning structure, as well as between the question and the corresponding answer. To mitigate, we propose a formalization-driven IS data synthesis framework WebShaper, which systematically formalizes IS tasks using set-theoretic constructs.
Central to the formalization is the concept of Knowledge Projections (KP), which enables precise control over reasoning structure by KP operation compositions.  During synthesis, we begin by creating seed tasks, then use a multi-step expansion process.
At each step, an agentic Expander expands the current formal question more complex through retrieval and validation tools grounded in our formalization. We train our model on the synthesized dataset. Experiment results demonstrate that WebShaper achieves state-of-the-art performance among open-sourced IS agents on competitive benchmarks.

## Metadata
- venue: ICLR
- year: 2026
- authors: Zhengwei Tao, Jialong Wu, Wenbiao Yin, Pu Wu, Junkai Zhang, Baixuan Li, Haiyang SHEN, Kuan Li, Liwen Zhang, Xinyu Wang, Wentao Zhang, Yong Jiang, Pengjun Xie, Fei Huang, Jingren Zhou
- arxiv_id: 
- openreview_id: hld4TzJsnD
- anthology_id: 
- pdf_url: https://openreview.net/pdf/4197d854df3d43b85f8c0bf9a461189c70ad00bf.pdf
- published: 2026
- keywords: agent, information seeking, data synthesis, llm
