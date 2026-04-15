---
title: "Do LLM Agents Know How to Ground,  Recover, and Assess? Evaluating Epistemic Competence in Information-Seeking Agents"
authors: ["Jiaqi Shao", "Yuxiang Lin", "Munish Prasad Lohani", "Yufeng Miao", "Bing Luo"]
venue: "ICLR"
year: 2026
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "r0L9GwlnzP"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/fb7cbf60614e44ed5b14ce027f200c418de785a7.pdf"
published: "2026"
categories: []
keywords: ["Epistemic Competence", "Evidence-Grounded Reasoning", "LLM Search Agents"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:13:18+09:00"
---

# Do LLM Agents Know How to Ground,  Recover, and Assess? Evaluating Epistemic Competence in Information-Seeking Agents

## Abstract
Recent work has explored training Large Language Model (LLM) search agents with reinforcement learning (RL) for open-domain question answering. However, most evaluations focus solely on final answer accuracy, overlooking how these agents reason with and act on external evidence.
We introduce **SeekBench**, the first process-level evaluation framework for LLM search agents that operationalize *epistemic competence* through metrics derived from an annotation schema.
We develop and validate our annotation schema using an expert-annotated dataset of 190 traces (over 1,800 steps). 
To evaluate at scale, we introduce an LLM-as-judge pipeline.
Our framework provides granular analysis of whether agents demonstrate: (1) **groundedness**, by generating reasoning steps supported by observed evidence; (2) **recovery**, by adaptively reformulating searches to recover from low-quality results; and (3) **calibration**, by correctly assessing whether current evidence is sufficient to provide an answer. 
By applying our evaluation framework to state-of-the-art search agents tuned on Qwen2.5-7B, we uncover critical behavioral gaps that answer-only metrics miss, as well as specialized skills such as Search-R1's synthesis abilities. These analyses highlight distinct epistemic competencies, offering actionable insights for the development of more capable and trustworthy agents. Code is available at
https://github.com/SHAO-Jiaqi757/SeekBench.

## Metadata
- venue: ICLR
- year: 2026
- authors: Jiaqi Shao, Yuxiang Lin, Munish Prasad Lohani, Yufeng Miao, Bing Luo
- arxiv_id: 
- openreview_id: r0L9GwlnzP
- anthology_id: 
- pdf_url: https://openreview.net/pdf/fb7cbf60614e44ed5b14ce027f200c418de785a7.pdf
- published: 2026
- keywords: Epistemic Competence, Evidence-Grounded Reasoning, LLM Search Agents
