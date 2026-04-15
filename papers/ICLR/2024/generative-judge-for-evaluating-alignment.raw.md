---
title: "Generative Judge for Evaluating Alignment"
authors: ["Junlong Li", "Shichao Sun", "Weizhe Yuan", "Run-Ze Fan", "hai zhao", "Pengfei Liu"]
venue: "ICLR"
year: 2024
venue_class: "whitelist"
arxiv_id: ""
openreview_id: "gtkFw6sZGS"
anthology_id: ""
pdf_url: "https://openreview.net/pdf/7fe3087c6257d9121061bc6f3cb0571abebf9277.pdf"
published: "2024"
categories: []
keywords: ["Generative", "Evaluation", "Alignment"]
venue_source: "openreview"
hunter_fetched: "2026-04-15T05:17:47+09:00"
---

# Generative Judge for Evaluating Alignment

## Abstract
The rapid development of Large Language Models (LLMs) has substantially expanded the range of tasks they can address. In the field of Natural Language Processing (NLP), researchers have shifted their focus from conventional NLP tasks (e.g., sequence tagging and parsing) towards tasks that revolve around aligning with human needs (e.g., brainstorming and email writing). This shift in task distribution imposes new requirements on evaluating these aligned models regarding *generality* (i.e., assessing performance across diverse scenarios), *flexibility* (i.e., examining under different protocols), and *interpretability* (i.e., scrutinizing models with explanations). In this paper, we propose a generative judge with 13B parameters, **Auto-J**, designed to address these challenges. Our model is trained on user queries and LLM-generated responses under massive real-world scenarios and accommodates diverse evaluation protocols (e.g., pairwise response comparison and single-response evaluation) with well-structured natural language critiques. To demonstrate the efficacy of our approach, we construct a new testbed covering 58 different scenarios. Experimentally, **Auto-J** outperforms a series of strong competitors, including both open-source and closed-source models, by a large margin. We also provide detailed analysis and case studies to further reveal the potential of our method and make a variety of resources public at https://github.com/GAIR-NLP/auto-j.

## Metadata
- venue: ICLR
- year: 2024
- authors: Junlong Li, Shichao Sun, Weizhe Yuan, Run-Ze Fan, hai zhao, Pengfei Liu
- arxiv_id: 
- openreview_id: gtkFw6sZGS
- anthology_id: 
- pdf_url: https://openreview.net/pdf/7fe3087c6257d9121061bc6f3cb0571abebf9277.pdf
- published: 2024
- keywords: Generative, Evaluation, Alignment
